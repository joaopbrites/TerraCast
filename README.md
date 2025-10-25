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


## Recomendações para nomeação de commits
1. **Use hífen (-) para separar palavras** na descrição
   - ✅ `feat: adicionar-processamento-goes-18`
   - ❌ `feat: adiciona_processamento_goes_18`
   - ❌ `feat: adiciona processamento goes 18`

2. **Descrição em minúsculas** (exceto nomes próprios ou siglas)
   - ✅ `fix: corrige-ler-arquivo-netCDF`
   - ❌ `Fix: Corrige Leitura Arquivo NetCDF`

3. **Use infinitivo verbal**
   - ✅ `feat: adicionar-suporte-goes-18`
   - ❌ `feat: adicionado-suporte-goes-18`
   - ❌ `feat: adicionando-suporte-goes-18`
