# TerraCast

**Descrição:** TerraCast é uma ferramenta que converte dados de satélite divulgadas via GEONETCast-Americas em imagens para fácil visualização.

TerraCast é um fork de [SHOWCast](https://github.com/diegormsouza/showcast).

## Estrutura do Projeto

```
TerraCast/
├── terracast.py          # Entry point principal
├── showcast.yml          # Configuração
├── setup/                # Arquivos de instalação
│   ├── apt-packages.txt
│   ├── debian-packages.txt
│   └── requirements.txt
├── utils/                # Bibliotecas compartilhadas
├── plugins/              # Funcionalidades standalone
├── products/             # Configuração de produtos
├── scripts/              # Scripts de processamento
├── logs/                 # Sistema de logging
├── assets/               # Recursos visuais
│   ├── colortables/
│   ├── legends/
│   ├── logos/
│   └── shapefiles/
└── tests/
```

## Instalação

### Dependências do sistema

Instale as bibliotecas necessárias do sistema (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y $(cat setup/apt-packages.txt)
```

Para outras distribuições Linux, consulte `setup/apt-packages.txt` e instale os equivalentes usando o gerenciador de pacotes apropriado.

### Dependências Python

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv --system-site-packages venv
source venv/bin/activate
```

2. Instale os pacotes Python:

```bash
pip install --upgrade pip
pip install -r setup/requirements.txt
```

### Verificação

Para verificar se todas as dependências foram instaladas corretamente:

```bash
python -c "import matplotlib, netCDF4, cartopy, pyorbital, pyhdf; print('✅ Dependências instaladas com sucesso')"
```

## Uso

```bash
source venv/bin/activate
python terracast.py
```

