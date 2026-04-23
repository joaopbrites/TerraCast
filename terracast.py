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
import glob   
from utils import ControllerProducts
import datetime  
import importlib



   



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
    log = setup_logger(int(CONFIG["logging_level"]), CONFIG.get("log_journal", True))
    log.debug(f"Diretorio do projeto {CONFIG['src_dir']}")
    log.debug(f"Arquivo {config_file} carregado com sucesso")


    # Váriaveis de debug
    SINGLE_PRODUCT_NAME = 'g16_band01_fdk'
    #SINGLE_PRODUCT_NAME = None # for debug: process only this product

    CONFIG['output'] = CONFIG['output'] + '/Output/'
    if (Path(CONFIG['output']).exists()):
        log.debug(f'Diretório de destino já existia e se encontra em: {CONFIG['output']}')
    else:
        Path(CONFIG['output']).mkdir(parents=True, exist_ok=True)
        log.debug(f'Diretório de destino não existia e foi criado em: {CONFIG['output']}')


    # Carrega a lista de produtos suportados
    product_list = PC.products(CONFIG)

    # Filtro opcional para debug: processa apenas um produto pelo nome
    if SINGLE_PRODUCT_NAME is not None:
        for product in product_list:
            product['enabled'] = (product['name'] == SINGLE_PRODUCT_NAME)

    number_of_prods = sum(1 for product in product_list if product.get('enabled'))

    # faz a contagem de produtos ativos e configura o modo de debug
    
    
    log.debug(f'{number_of_prods} products to be generated.')

    if SINGLE_PRODUCT_NAME != None:
        log.debug("Modo debug ativo")
        log.debug(f'Will process only "{SINGLE_PRODUCT_NAME}"')

    for product in product_list:
        if product['enabled']:
            process_product(CONFIG, product)



def process_product(CONFIG, product):
    """
    Process a single product by:
    1. Scanning the input directory for matching files
    2. Checking which files haven't been processed yet (via gnc log)
    3. Executing the corresponding script via subprocess for each new file

    Parameters are passed to the script via command line arguments,
    following the same order as the legacy showcast_config_old.py:
        argv[1] = dataFileName
        argv[2] = min_lon
        argv[3] = min_lat
        argv[4] = max_lon
        argv[5] = max_lat
        argv[6] = resolution
        argv[7] = output dir
        argv[8] = vis_dir
        argv[9] = interval
    """
    #inicalização log
    logger = logging.getLogger(f'processment.{__name__}')
    logger.debug("Process product inicializado")
    terracast_dir = CONFIG['src_dir']

    controller_products = ControllerProducts()

    # ------------------------------------------------------------------
    # 1. Build the list of candidate files (gnc_files)
    # ------------------------------------------------------------------
    gnc_files = []

    # Entra no diretorio do produto a ser processado e ordena 
    input_pattern = product['input'] + product['filename pattern']
    input_file_names = sorted(glob.glob(input_pattern))

    # Fixed-name files that need modification-time suffix
    FIXED_NAME_FILES = {
        'gfs.sam.t00z.f120', 'gfs.sam.t12z.f120',
        'gfs.crb.t00z.f120', 'gfs.crb.t12z.f120',
        'd6.gif', 'crb3_east.gif',
    }

    for filename in input_file_names:
        # Esses arquivos são sobrescritos periodicamente com o mesmo nome-base.
        # Adicionamos `_c<mtime>` para manter uma chave única no log de processados.
        # Esta regra depende do `filename pattern` (fontes de nome fixo)
        if product['filename pattern'] in FIXED_NAME_FILES:
            mtime = datetime.datetime.fromtimestamp(
                Path(filename).stat().st_mtime
            ).strftime('%Y%m%d%H%M%S')
            gnc_files.append(os.path.normpath(filename + product['config'] + '_c' + mtime))
        else:
            gnc_files.append(os.path.normpath(filename + product['config']))

    # se não ouver arquivos para processar marca como falahado e retorna
    if not gnc_files:
        data_file_name = f"{input_pattern}{product['name']}"
        logger.warning(
            f"No files found for product",
            extra={
                "status": "failed",
                "exception": f"with pattern: {input_pattern}",
                "script": product['script'],
                "product": product['name'],
                "input_file": data_file_name,
                "event_time": datetime.datetime.now().isoformat(timespec="seconds"),
            },
        )
        controller_products.mark_failed(data_file_name, f"No files found for product")
        return

    # Keep only the most recent N files
    gnc_files = gnc_files[-product['max files']:]

    # ------------------------------------------------------------------
    # 3. Process each new file via subprocess
    # ------------------------------------------------------------------
    script_path = terracast_dir / 'scripts' / product['script']
    extent = product.get('extent', [0.0, 0.0, 0.0, 0.0])
    interval = product.get('interval', '')
    child_env = os.environ.copy()
    project_path = str(terracast_dir)
    current_pythonpath = child_env.get("PYTHONPATH", "")

    if current_pythonpath:
        pythonpath_entries = current_pythonpath.split(os.pathsep)
        if project_path not in pythonpath_entries:
            child_env["PYTHONPATH"] = project_path + os.pathsep + current_pythonpath
    else:
        child_env["PYTHONPATH"] = project_path


    for data_file_name in gnc_files:
        if controller_products.is_processed(data_file_name):
            continue

        # Build the command — same parameter order as the legacy system
        command = [
            sys.executable,             # Python interpreter
            str(script_path),           # Script to run
            data_file_name,             # argv[1]: file path
            str(extent[0]),             # argv[2]: min_lon
            str(extent[1]),             # argv[3]: min_lat
            str(extent[2]),             # argv[4]: max_lon
            str(extent[3]),             # argv[5]: max_lat
            str(product['resolution']), # argv[6]: resolution
            CONFIG['output'],           # argv[7]: output dir
            CONFIG['output_vis'],           # argv[8]: vis_dir
            interval,                   # argv[9]: interval
        ]

        logger.info(
            "Starting product processing",
            extra={
                "status": "running",
                "exception": "",
                "script": product['script'],
                "product": product['name'],
                "input_file": data_file_name,
                "event_time": datetime.datetime.now().isoformat(timespec="seconds"),
            },
        )

        try:

            workModule = importlib.import_module('scripts.' + (product['script'].rsplit('.', 1)[0]))
            print('will run:', workModule)

            # Preserve the base product definition and attach per-file context.
            runtime_product = dict(product)
            runtime_product['dataFileName'] = data_file_name
            workModule.run(CONFIG, runtime_product)

            controller_products.mark_processed(data_file_name)
            logger.info(
                "Product processed successfully",
                extra={
                    "status": "success",
                    "exception": "",
                    "script": product['script'],
                    "product": product['name'],
                    "input_file": data_file_name,
                    "event_time": datetime.datetime.now().isoformat(timespec="seconds"),
                },
            )
            
        except Exception as e:
            error_message = f"ERROR: {e}"
            logger.error(
                error_message,
                extra={
                    "status": "failed",
                    "exception": type(e).__name__,
                    "script": product['script'],
                    "product": product['name'],
                    "input_file": data_file_name,
                    "event_time": datetime.datetime.now().isoformat(timespec="seconds"),
                },
            )
            controller_products.mark_failed(data_file_name, error_message)

if __name__ == "__main__":
    main()
