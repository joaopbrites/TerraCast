#!/usr/bin/python3
#######################################################################################################
# LICENSE
# Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
# General Public License as published by the Free Software Foundation, either version 3 of the License, 
# or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
# Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see http://www.gnu.org/licenses/.
#######################################################################################################
__author__ = "Diego Souza"
__copyright__ = "Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL"
__credits__ = ["Diego Souza"]
__license__ = "GPL"
__version__ = "2.5.0"
__maintainer__ = "Diego Souza"
__email__ = "diego.souza@inpe.br"
__status__ = "Production"
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

import os, sys   # Miscellaneous operating system interfaces
from pathlib import   Path            # Nova biblioteca para lidar com caminhos 
import yaml                           # Para ler o arquivo de configuração
from logs import setup_logger         # Aplicação de logging
import logging
import products as PC
from utils import audit



def main():
    config_file = Path(__file__).resolve().parent / "terracast.yml"
    # Carrega arquivo de configurações
    try:
        with open(config_file, 'r') as arqConfig:
            CONFIG = yaml.safe_load(arqConfig)
    except FileNotFoundError:
        print("Erro: O arquivo de configuração não foi encontrado.")
        print("Finalizando Programa")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        print("Finalizando Programa")
        sys.exit(1)
    CONFIG['src_dir'] = Path(__file__).resolve().parent
    
    
    # Configura o log com o nível estipulado no arquivo
    log = setup_logger(int(CONFIG["logging_level"])) 
    log.debug(f"Diretorio do projeto {CONFIG['src_dir']}")
    log.debug(f"Arquivo {config_file} carregado com sucesso")


    # Váriaveis de debug
    #SINGLE_PRODUCT_NAME = 'g16_band01_fdk'
    SINGLE_PRODUCT_NAME = None # for debug: process only this product

    CONFIG['output'] = CONFIG['output'] + '/Output/'
    if (Path(CONFIG['output']).exists()):
        log.debug(f'Diretório de destino já existia e se encontra em: {CONFIG['output']}')
    else:
        Path(CONFIG['output']).mkdir(parents=True, exist_ok=True)
        log.debug(f'Diretório de destino não existia e foi criado em: {CONFIG['output']}')


    # Carrega a lista de arquivos suportados
    product_list, number_of_prods = audit(PC.products(CONFIG), SINGLE_PRODUCT_NAME)

    # faz a contagem de produtos ativos e configura o modo de debug
    
    
    log.debug(f'{number_of_prods} products to be generated.')

    if SINGLE_PRODUCT_NAME != None:
        log.debug("Modo debug ativo")
        log.debug(f'Will process only "{SINGLE_PRODUCT_NAME}"')

    for product in product_list:
        if product['enabled']:
            PC.process_product(CONFIG, product)

   
    
if __name__ == "__main__":
    main()


