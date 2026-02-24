# TerraCast

**Descrição:** TerraCast é uma ferramenta que converte dados de satélite divulgadas via GEONETCast-Americas em páginas HTML com imagens para fácil visualização.

TerraCast é um fork de [SHOWCast](https://github.com/diegormsouza/showcast).


## Instalação

### Dependências do sistema

Instale as bibliotecas necessárias do sistema (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y $(cat apt-packages.txt)
```

Para outras distribuições Linux, consulte `apt-packages.txt` e instale os equivalentes usando o gerenciador de pacotes apropriado.

### Dependências Python

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instale os pacotes Python:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Verificação

Para verificar se todas as dependências foram instaladas corretamente:

```bash
python -c "import matplotlib, netCDF4, cartopy, pyorbital, pyhdf; print('✅ Dependências instaladas com sucesso')"
```

