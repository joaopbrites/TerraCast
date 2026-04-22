#!/bin/bash

# Script de instalação do TerraCast
# Versão 0.2

set -e  # Sai em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Diretório do script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Verifica se está no diretório correto
if [[ ! -f "$SCRIPT_DIR/requirements.txt" ]]; then
    printf "${RED}Erro: Por favor rode esse script dentro do diretório setup${NC}\n" >&2
    exit 1
fi

# Garante que vá rodar em shell próprio (não com source)
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    printf "${RED}Por favor rode usando 'bash' ou 'sh', não '.' ou 'source'${NC}\n" >&2
    return 1
fi

# Variáveis padrão
DAEMON=0
VENV_DIR="$PROJECT_DIR/.Venv_terracast"

USAGE="
${BLUE}Script de Instalação do TerraCast${NC}
============================================================

Uso: $0 [opções]

Opções:
    -d, --daemon    Instala o serviço systemd
    -p, --path      Diretório para o ambiente virtual
    -h, --help      Mostra esta mensagem de ajuda

Exemplos:
    $0                    # Instalação padrão com venv
    $0 -d                 # Instala + configura daemon
    $0 -p /opt/terracast  # Ambiente em diretório específico
    $0 -r                 # Desinstala (remove venv e daemon)
============================================================
"
# Funções auxiliares
log_info() {
    printf "${BLUE}[INFO]${NC} %s\n" "$1"
}

log_success() {
    printf "${GREEN}[OK]${NC} %s\n" "$1"
}

log_warning() {
    printf "${YELLOW}[AVISO]${NC} %s\n" "$1"
}

log_error() {
    printf "${RED}[ERRO]${NC} %s\n" "$1" >&2
}

# Desinstala o TerraCast (remove venv e daemon)
uninstall() {
    printf "\n${RED}============================================================${NC}\n"
    printf "${RED}         TerraCast - Desinstalação                          ${NC}\n"
    printf "${RED}============================================================${NC}\n\n"
    
    read -p "Tem certeza que deseja desinstalar o TerraCast? [s/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        log_info "Desinstalação cancelada"
        exit 0
    fi
    
    # Remove serviço systemd
    local service_file="/etc/systemd/system/terracast.service"
    if [[ -f "$service_file" ]]; then
        log_info "Removendo serviço systemd..."
        sudo systemctl stop terracast.service 2>/dev/null || true
        sudo systemctl disable terracast.service 2>/dev/null || true
        sudo rm -f "$service_file"
        sudo systemctl daemon-reload
        log_success "Serviço systemd removido"
    else
        log_info "Serviço systemd não encontrado"
    fi
    
    # Remove ambiente virtual
    if [[ -d "$VENV_DIR" ]]; then
        log_info "Removendo ambiente virtual: $VENV_DIR"
        rm -rf "$VENV_DIR"
        log_success "Ambiente virtual removido"
    else
        log_info "Ambiente virtual não encontrado em $VENV_DIR"
    fi

    
    printf "\n${GREEN}============================================================${NC}\n"
    printf "${GREEN}         TerraCast desinstalado com sucesso!                ${NC}\n"
    printf "${GREEN}============================================================${NC}\n\n"
    
    exit 0
}
# Parsing de argumentos
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            printf "%s\n" "$USAGE"
            exit 0
            ;;
        -d|--daemon)
            DAEMON=1
            shift
            ;;
        -p|--path)
            VENV_DIR="$2"
            shift 2
            ;;
        -r|--remove)
            uninstall
            ;;
        *)
            printf "${RED}Erro: opção desconhecida '%s'${NC}\n" "$1"
            printf "%s\n" "$USAGE"
            exit 1
            ;;
    esac
done


# Instala pacotes apt
install_apt_packages() {
    local apt_file="$SCRIPT_DIR/packages_apt.txt"
    local apt_to_install=()
    local failed_packages=()

    if [[ ! -f "$apt_file" ]]; then
        log_error "Arquivo não encontrado: $apt_file"
        return 1
    fi

    # Lê o arquivo linha por linha, ignorando comentários e linhas vazias
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Remove comentários e espaços
        line=$(echo "$line" | sed 's/#.*//' | xargs)
        [[ -z "$line" ]] && continue
        apt_to_install+=("$line")
    done < "$apt_file"

    if [[ ${#apt_to_install[@]} -eq 0 ]]; then
        log_warning "Nenhum pacote apt encontrado em packages_apt.txt"
        return 0
    fi

    log_info "Atualizando repositórios..."
    sudo apt update

    log_info "Instalando ${#apt_to_install[@]} pacotes apt..."
    for pkg in "${apt_to_install[@]}"; do
        log_info "Instalando: $pkg"
        if ! sudo apt install -y "$pkg" 2>/dev/null; then
            log_error "Falha ao instalar: $pkg"
            failed_packages+=("$pkg")
        fi
    done

    if [[ ${#failed_packages[@]} -gt 0 ]]; then
        log_error "Pacotes que falharam: ${failed_packages[*]}"
        return 1
    fi

    log_success "Todos os pacotes apt instalados com sucesso"
}

# Cria ambiente virtual
create_venv() {
    create_python_venv

}

create_python_venv() {
    log_info "Criando ambiente virtual em: $VENV_DIR"
    
    if [[ -d "$VENV_DIR" ]]; then
        log_warning "Ambiente virtual já existe em $VENV_DIR"
        read -p "Deseja sobrescrever? [s/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Ss]$ ]]; then
            log_info "Usando ambiente existente"
            return
        fi
        rm -rf "$VENV_DIR"
    fi
    
    python3 -m venv "$VENV_DIR"
    log_success "Ambiente virtual criado"
}


# Instala pacotes pip
install_pip_packages() {
    local req_file="$SCRIPT_DIR/requirements.txt"
    local sanitized_req
    local req_install_file
    local line
    local normalized
    local tmp_file
    local pip_output_file
    local missing_line
    local missing_pkg
    local retry_count=0
    local max_retries=20
    local skipped_count=0
    local kept_count=0

    if [[ ! -f "$req_file" ]]; then
        log_error "Arquivo não encontrado: $req_file"
        return 1
    fi

    log_info "Ativando ambiente virtual..."
    source "$VENV_DIR/bin/activate"

    log_info "Atualizando pip..."
    pip install --upgrade pip

    # Sanitiza requirements congelado em distro Debian para formato instalável via pip.
    # Mantém o arquivo original intacto e só filtra/normaliza em arquivo temporário.
    sanitized_req="$(mktemp)"
    while IFS= read -r line || [[ -n "$line" ]]; do
        line="$(echo "$line" | sed 's/#.*//' | xargs)"
        [[ -z "$line" ]] && continue

        case "$line" in
            apt-listchanges==*|python-apt==*|python-debian==*|python-debianbts==*|Brlapi==*|cupshelpers==*|dbus-python==*|h5py._debian_h5py_serial==*|legacy-cgi==*|louis==*|PyGObject==*|pycups==*|pysmbc==*|reportbug==*|xdg==*)
                skipped_count=$((skipped_count + 1))
                log_warning "Ignorando pacote não-PyPI no requirements: $line"
                continue
                ;;
        esac

        normalized="$(echo "$line" | sed -E 's/\+dfsg[0-9]*//g; s/\+ds[0-9]*//g')"
        echo "$normalized" >> "$sanitized_req"
        kept_count=$((kept_count + 1))
    done < "$req_file"

    log_info "Requirements sanitizado: $kept_count pacotes válidos, $skipped_count ignorados"

    log_info "Instalando pacotes do requirements.txt..."
    req_install_file="$sanitized_req"
    while true; do
        local pip_status
        pip_output_file="$(mktemp)"
        pip install -r "$req_install_file" 2>&1 | tee "$pip_output_file"
        pip_status=${PIPESTATUS[0]}
        if [[ $pip_status -eq 0 ]]; then
            rm -f "$pip_output_file"
            break
        fi

        missing_line="$(grep -E 'No matching distribution found for [A-Za-z0-9_.-]+==' "$pip_output_file" | tail -n 1 || true)"
        if [[ -z "$missing_line" ]]; then
            log_error "Falha ao instalar pacotes pip"
            rm -f "$pip_output_file" "$sanitized_req"
            deactivate
            return 1
        fi

        missing_pkg="$(echo "$missing_line" | sed -E 's/.*for ([A-Za-z0-9_.-]+)==.*/\1/')"
        if [[ -z "$missing_pkg" ]]; then
            log_error "Não foi possível identificar pacote com versão incompatível"
            rm -f "$pip_output_file" "$sanitized_req"
            deactivate
            return 1
        fi

        retry_count=$((retry_count + 1))
        if [[ $retry_count -gt $max_retries ]]; then
            log_error "Limite de tentativas atingido ao ajustar versões incompatíveis ($max_retries)"
            rm -f "$pip_output_file" "$sanitized_req"
            deactivate
            return 1
        fi

        log_warning "Versão fixada indisponível para '$missing_pkg'. Tentando versão compatível sem pin exato..."
        tmp_file="$(mktemp)"
        awk -v pkg="$missing_pkg" '{ if ($0 ~ ("^" pkg "==")) $0=pkg; print }' "$req_install_file" > "$tmp_file"
        mv "$tmp_file" "$req_install_file"
        rm -f "$pip_output_file"
    done

    rm -f "$sanitized_req"

    # Garante bindings Python do GDAL no venv para import de osgeo.
    if ! command -v gdal-config >/dev/null 2>&1; then
        log_error "gdal-config não encontrado. Verifique se libgdal-dev e gdal-bin estão instalados."
        deactivate
        return 1
    fi

    local gdal_version
    gdal_version="$(gdal-config --version)"
    log_info "Instalando bindings Python do GDAL no venv (GDAL==$gdal_version)..."
    if ! pip install "GDAL==$gdal_version"; then
        log_error "Falha ao instalar GDAL==$gdal_version no ambiente virtual"
        deactivate
        return 1
    fi

    log_info "Instalando bindings Python do systemd no venv..."
    if ! pip install systemd-python; then
        log_error "Falha ao instalar systemd-python no ambiente virtual"
        deactivate
        return 1
    fi

    log_info "Instalando o projeto via pyproject (pip install -e .)..."
    if ! pip install -e "$PROJECT_DIR"; then
        log_error "Falha ao instalar o projeto em modo editável"
        deactivate
        return 1
    fi

    log_info "Validando integridade de dependências (pip check)..."
    if ! pip check; then
        log_error "pip check encontrou dependências quebradas"
        deactivate
        return 1
    fi

    log_info "Executando teste rápido de imports críticos..."
    if ! python - <<'PY'
mods = [
    "numpy", "pandas", "scipy", "matplotlib", "netCDF4", "h5py",
    "pyproj", "shapely", "geopandas", "cartopy", "rasterio", "fiona",
    "pygrib", "pyhdf", "pyorbital", "pyresample", "satpy", "pyspectral",
    "yaml", "PIL", "affine", "folium", "osgeo", "systemd"
]

missing = []
for mod in mods:
    try:
        __import__(mod)
    except Exception as exc:
        missing.append((mod, str(exc).splitlines()[0]))

if missing:
    print("Imports críticos com falha:")
    for name, err in missing:
        print(f"- {name}: {err}")
    raise SystemExit(1)

print("Imports críticos OK")
PY
    then
        log_error "Falha no teste de imports críticos"
        deactivate
        return 1
    fi

    log_success "Pacotes pip instalados com sucesso"
    deactivate
}

# Configura daemon systemd
setup_daemon() {
    log_info "Configurando serviço systemd..."
    
    local source_file="$SCRIPT_DIR/terracast.service.exemple"
    local dest_file="/etc/systemd/system/terracast.service"
    
    if [[ ! -f "$source_file" ]]; then
        log_error "Arquivo de serviço não encontrado: $source_file"
        return 1
    fi
    
    # Copia o arquivo de serviço
    sudo cp "$source_file" "$dest_file"
    
    # Substitui placeholders no arquivo de serviço
    sudo sed -i "s|%PROJECT_DIR%|$PROJECT_DIR|g" "$dest_file"
    sudo sed -i "s|%VENV_DIR%|$VENV_DIR|g" "$dest_file"
    
    # Recarrega systemd e habilita o serviço
    sudo systemctl daemon-reload
    sudo systemctl enable terracast.service
    
    log_success "Serviço systemd configurado: $dest_file"
    log_info "Use: sudo systemctl start terracast"
}



# Main
main() {
    printf "\n${BLUE}============================================================${NC}\n"
    printf "${BLUE}         TerraCast - Script de Instalação v0.3              ${NC}\n"
    printf "${BLUE}============================================================${NC}\n\n"
    
    log_info "Diretório do projeto: $PROJECT_DIR"
    log_info "Ambiente virtual: $VENV_DIR"
    
    # Passo 1: Instalar dependências apt
    log_info "Instalando dependências do sistema..."
    if ! install_apt_packages; then
        log_error "Falha na instalação de pacotes apt. Verifique os erros acima."
        exit 1
    fi
    
    # Passo 2: Criar ambiente virtual
    create_venv
    
    # Passo 3: Instalar pacotes pip
    if ! install_pip_packages; then
        log_error "Falha na instalação de pacotes pip. Verifique os erros acima."
        exit 1
    fi
    
    # Passo 4: Daemon (opcional)
    if [[ $DAEMON -eq 1 ]]; then
        setup_daemon
    fi
    
    printf "\n${GREEN}============================================================${NC}\n"
    printf "${GREEN}         Instalação concluída com sucesso!                  ${NC}\n"
    printf "${GREEN}============================================================${NC}\n\n"
    
    log_info "Para usar o TerraCast:"
    echo "  1. Ative o ambiente: source $VENV_DIR/bin/activate"
    echo "  2. Execute: python $PROJECT_DIR/terracast.py"
    echo ""
    
    if [[ $DAEMON -eq 1 ]]; then
        log_info "Ou use o serviço systemd:"
        echo "  sudo systemctl start terracast"
        echo "  sudo systemctl status terracast"
    fi
}

# Executa
main
