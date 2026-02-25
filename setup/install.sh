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
    
    # Remove script de ativação se existir
    local activate_script="$PROJECT_DIR/activate.sh"
    if [[ -f "$activate_script" ]]; then
        rm -f "$activate_script"
        log_success "Script de ativação removido"
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





# Verifica e instala dependências do sistema
check_system_deps() {
    log_info "Verificando dependências do sistema..."
    
    local missing_deps=()
    local apt_packages=()
    
    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
        apt_packages+=("python3")
    fi
    
    if ! command -v pip3 &> /dev/null; then
        missing_deps+=("pip3")
        apt_packages+=("python3-pip")
    fi
    
    # Verifica python3-venv
    if ! python3 -c "import venv" &> /dev/null 2>&1; then
        apt_packages+=("python3-venv")
    fi
    
    if [[ ${#apt_packages[@]} -gt 0 ]]; then
        log_warning "Dependências faltando: ${missing_deps[*]}"
        log_info "Instalando automaticamente..."
        sudo apt update
        sudo apt install -y ${apt_packages[*]}
        log_success "Dependências do sistema instaladas"
    else
        log_success "Dependências do sistema OK"
    fi
}

# Parse do requirements.txt personalizado
parse_requirements() {
    local section=""
    APT_PACKAGES=()
    PIP_PACKAGES=()
    
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Remove espaços em branco e comentários
        line=$(echo "$line" | sed 's/#.*//' | xargs)
        
        [[ -z "$line" ]] && continue
        
        if [[ "$line" == "apt:" ]]; then
            section="apt"
            continue
        elif [[ "$line" == "pip:" ]]; then
            section="pip"
            continue
        fi
        
        # Remove o hífen inicial
        package=$(echo "$line" | sed 's/^-//')
        
        if [[ "$section" == "apt" ]]; then
            APT_PACKAGES+=("$package")
        elif [[ "$section" == "pip" ]]; then
            PIP_PACKAGES+=("$package")
        fi
    done < "$SCRIPT_DIR/requirements.txt"
}

# Instala pacotes apt
install_apt_packages() {
    if [[ ${#APT_PACKAGES[@]} -eq 0 ]]; then
        log_warning "Nenhum pacote apt para instalar"
        return
    fi
    
    log_info "Instalando pacotes apt: ${APT_PACKAGES[*]}"
    
    # Mapeia nomes para pacotes apt reais
    declare -A APT_MAP=(
        ["matplotlib"]="python3-matplotlib"
        ["netcdf4"]="python3-netcdf4"
        ["cartopy"]="python3-cartopy"
        ["pyorbital"]=""  # Não disponível via apt
        ["hdf4"]="libhdf4-dev"
        ["gdal"]="gdal-bin libgdal-dev python3-gdal"
        ["libnetcdf-dev"]="libnetcdf-dev"
        ["libhdf5-dev"]="libhdf5-dev"
    )
    
    local apt_to_install=()
    
    for pkg in "${APT_PACKAGES[@]}"; do
        if [[ -n "${APT_MAP[$pkg]}" ]]; then
            apt_to_install+=("${APT_MAP[$pkg]}")
        else
            log_warning "Pacote '$pkg' não mapeado para apt, será instalado via pip"
        fi
    done
    
    if [[ ${#apt_to_install[@]} -gt 0 ]]; then
        log_info "Executando: sudo apt install ${apt_to_install[*]}"
        sudo apt update
        sudo apt install -y ${apt_to_install[*]}
        log_success "Pacotes apt instalados"
    fi
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
    log_info "Instalando pacotes pip..."
    source "$VENV_DIR/bin/activate"
    PIP_CMD="pip"
    # Atualiza pip
    $PIP_CMD install --upgrade pip
    
    # Pacotes essenciais do TerraCast
    local core_packages=(
        "numpy"
        "matplotlib"
        "cartopy"
        "netCDF4"
        "h5py"
        "pyorbital"
        "GDAL"
        "pyresample"
        "satpy"
        "pyyaml"
        "watchdog"
    )
    
    # Adiciona pacotes do requirements.txt
    for pkg in "${PIP_PACKAGES[@]}"; do
        core_packages+=("$pkg")
    done
    
    # Remove duplicatas
    local unique_packages=($(printf "%s\n" "${core_packages[@]}" | sort -u))
    
    log_info "Instalando: ${unique_packages[*]}"
    
    for pkg in "${unique_packages[@]}"; do
        log_info "Instalando $pkg..."
        # GDAL precisa ser instalado com a versão do sistema
        if [[ "${pkg^^}" == "GDAL" ]]; then
            local gdal_version
            gdal_version=$(gdal-config --version 2>/dev/null)
            if [[ -n "$gdal_version" ]]; then
                if $PIP_CMD install "GDAL==$gdal_version"; then
                    log_success "GDAL $gdal_version instalado"
                else
                    log_warning "Falha ao instalar GDAL - verifique se libgdal-dev está instalado"
                fi
            else
                log_warning "gdal-config não encontrado - instale libgdal-dev primeiro"
            fi
        elif $PIP_CMD install "$pkg" 2>/dev/null; then
            log_success "$pkg instalado"
        else
            log_warning "Falha ao instalar $pkg - pode precisar de instalação manual"
        fi
    done
    
    log_success "Pacotes pip instalados"
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
    sudo sed -i "s|%USER%|$USER|g" "$dest_file"
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
    printf "${BLUE}         TerraCast - Script de Instalação v0.2              ${NC}\n"
    printf "${BLUE}============================================================${NC}\n\n"
    
    log_info "Diretório do projeto: $PROJECT_DIR"
    log_info "Ambiente virtual: $VENV_DIR"
    
    # Passo 1: Verificar sistema
    check_system_deps
    
    # Passo 2: Parse requirements
    log_info "Lendo requirements.txt..."
    parse_requirements
    log_success "Encontrados ${#APT_PACKAGES[@]} pacotes apt e ${#PIP_PACKAGES[@]} pacotes pip"
    
    # Passo 3: Instalar dependências apt
    install_apt_packages
    
    # Passo 4: Criar ambiente virtual
    create_venv
    
    # Passo 5: Instalar pacotes pip
    install_pip_packages
    
    # Passo 7: Daemon (opcional)
    if [[ $DAEMON -eq 1 ]]; then
        setup_daemon
    fi
    
    printf "\n${GREEN}============================================================${NC}\n"
    printf "${GREEN}         Instalação concluída com sucesso!                  ${NC}\n"
    printf "${GREEN}============================================================${NC}\n\n"
    
    log_info "Para usar o TerraCast:"
    echo "  1. Ative o ambiente: source $PROJECT_DIR/activate.sh"
    echo "  2. Execute: python terracast.py"
    echo ""
    
    if [[ $DAEMON -eq 1 ]]; then
        log_info "Ou use o serviço systemd:"
        echo "  sudo systemctl start terracast"
        echo "  sudo systemctl status terracast"
    fi
    

}

# Executa
main
