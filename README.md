# TerraCast

**Descrição:** TerraCast é uma ferramenta que converte dados de satélite divulgados via GEONETCast-Americas em imagens para fácil visualização.

TerraCast é um fork de [SHOWCast](https://github.com/diegormsouza/showcast).

> **Estado atual — Migração Gradual**
>
> O projeto está em transição da estrutura original do SHOWCast para uma organização modular própria.
> A branch `make-it-work` representa o estado mais funcional até o momento:
> os scripts legados continuam operando com caminhos hardcoded enquanto o refactor acontece de forma incremental.

---

## Estrutura do Projeto

```
TerraCast/
├── terracast.py                          # Entry point principal
├── terracast.yml                         # Configuração (renomeado de showcast.yml)
├── pyproject.toml                        # Permite 'pip install -e .' para imports do pacote
├── setup.py                              # Suporte ao install editável
├── setup/                                # Arquivos de instalação
│   ├── install.sh                        # Script de instalação e remoção
│   ├── terracast.service.exemple         # Exemplo de unit systemd
│   └── requirements.txt
├── utils/                                # Bibliotecas compartilhadas
│   └── processed_products_controller.py  # Controlador centralizado de produtos processados
├── plugins/                              # Funcionalidades standalone
├── products/                             # Módulo de produtos
│   ├── product_processor.py              # Processador de produtos (substitui processing_products.py)
│   └── products_list.py
├── scripts/                              # Scripts de processamento por produto
├── logs/                                 # Sistema de logging
├── Colortables/                          # Tabelas de cor (raiz — caminhos legados)
├── Legends/                              # Legendas (raiz — caminhos legados)
├── Logos/                                # Logos (raiz — caminhos legados)
├── Shapefiles/                           # Shapefiles (raiz — caminhos legados)
├── assets/                               # Destino futuro dos recursos visuais
│   ├── colortables/
│   ├── legends/
│   ├── logos/
│   └── shapefiles/
├── _legacy/                              # Código antigo mantido para referência
├── Logs/                                 # Logs de execução em runtime
└── tests/
```

> **Nota sobre assets:** Os diretórios `Colortables/`, `Legends/`, `Logos/` e `Shapefiles/` existem
> na raiz do projeto como estratégia transitória — os scripts legados referenciam esses caminhos
> de forma hardcoded. A migração para `assets/` será feita gradualmente.

---

## Instalação

### Pré-requisitos

```bash
# Dependências de sistema necessárias para GDAL
sudo apt install libgdal-dev gdal-bin
```

### Instalação via script

```bash
# Dentro do diretório raiz
cd setup/
bash install.sh
```

Parâmetros disponíveis do `install.sh`:

| Flag | Descrição |
|------|-----------|
| `-d`, `--daemon` | Instala o serviço systemd |
| `-p`, `--path` | Diretório para o ambiente virtual |
| `-h`, `--help` | Exibe a mensagem de ajuda |

### Instalação manual (modo editável)

```bash
python -m venv .venv_terracast
source .venv_terracast/bin/activate
pip install -e .
pip install -r setup/requirements.txt
```

O `pip install -e .` garante que os imports de pacotes internos (`utils.*`, `plugins.*`, `products.*`) resolvam corretamente sem alterar cada script individualmente.

---

## Uso

```bash
source .venv_terracast/bin/activate
python terracast.py
```
