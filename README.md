# TerraCast

**Descrição:** TerraCast é uma ferramenta que converte dados de satélite divulgadas via GEONETCast-Americas em imagens para fácil visualização.

TerraCast é um fork de [SHOWCast](https://github.com/diegormsouza/showcast).

## Estrutura do Projeto

```TerraCast/
├── terracast.py                  # Entry point principal
├── showcast.yml                  # Configuração
├── setup/                        # Arquivos de instalação
│   ├── install.sh                # Script pra instalação e remoção do programa
│   ├── terracast.service.exemple # Arquivo de exemplo para copiar para a pasta systemd
│   └── requirements.txt
├── utils/                        # Bibliotecas compartilhadas
├── plugins/                      # Funcionalidades standalone
├── products/                     # Configuração de produtos
├── scripts/                      # Scripts de processamento
├── logs/                         # Sistema de logging
├── assets/                       # Recursos visuais
│   ├── colortables/
│   ├── legends/
│   ├── logos/
│   └── shapefiles/
└── tests/
```

## Instalação

### Instalação Simples

``` #Dentro do diretorio raiz rode

    cd setup/
    bash install.sh

```

O arquivo install.sh também permite parametro como:
    -d, --daemon    #Instala o serviço systemd
    -p, --path      #Diretório para o ambiente virtual
    -h, --help      #Mostra esta mensagem de ajuda

## Uso

```bash
source .Vemv_terracast/bin/activate
python terracast.py
```
