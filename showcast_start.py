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
import sched, time                    # Scheduler library
import os, sys   # Miscellaneous operating system interfaces
from pathlib import   Path
from os.path import dirname, abspath  # Return a normalized absolutized version of the pathname path 
import datetime                       # Basic date and time types   
import yaml                           # Para ler o arquivo de configuração
from Logs import setup_logger
import logging
import ProductsConfig as PC

# SHOWCast process number
#showcast_process = sys.argv[1]
#if VERBOSE:
#    print("SHOWCast process number: ", showcast_process)

# Python environment (Script parent dir + python env)
#osystem = platform.system()
#if osystem == "Windows":
#    python_env = showcast_dir + '/Miniconda3/envs/showcast/' 
#else:
#    python_env = showcast_dir + '/Miniconda3/envs/showcast/bin/' 
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# QT Plugin path
#os.environ['QT_PLUGIN_PATH'] = python_env + "Library/plugins/"

# Interval in seconds
#seconds = 1

# Call the function for the first time without the interval
#print("\n------------- Calling Monitor Script --------------")
#script = python_env + 'python ' + showcast_dir + '/Scripts/showcast_config.py' + ' ' + python_env + ' ' + ingest_dir + ' ' + showcast_process + ' ' + vis_dir
#script = 'python ' + showcast_dir + '/Scripts/showcast_config.py' + ' ' + python_env + ' ' + ingest_dir + ' ' + showcast_process + ' ' + vis_dir
#if VERBOSE:
#    print("Will run: ", script)



def main():
    setup_logger()
    log = logging.getLogger(f"processment.{__name__}")
    #--------------------------------------------------------------------------------------------------
    # Configuration default values --------------------------------------------------------------------
    # If you want to change, do not change here. Change at 'showcast.yml'.
    
    VERBOSE = True
    ingest_dir:Path = Path('dados/')
    vis_dir:Path = Path('output/')
    #SINGLE_PRODUCT_NAME = 'g16_band01_fdk'
    SINGLE_PRODUCT_NAME = None # for debug: process only this product
    # Read configuration from file --------------------------------------------------------------------
    print("\nSHOWCast started.")
    with open('showcast.yml', 'r') as arqConfig:
        CONFIG:dict = yaml.safe_load(arqConfig)
    CONFIG['srcDir'] = Path.cwd()
    
    if VERBOSE:
        print('Configuration:')
        for item in CONFIG:
            print('    ', item, ': ', CONFIG[item], sep='')

    # Create list of products to process
    
    
    productList:list[dict] = PC.products(CONFIG)
    numberOfProds:int = 0
    singleProduct:dict = None
    for product in productList:
        if product['enabled']:
            numberOfProds += 1
        if SINGLE_PRODUCT_NAME and product['name'] != SINGLE_PRODUCT_NAME:
            product['enabled'] = False
        if product['name'] == SINGLE_PRODUCT_NAME:
            singleProduct = product
    print(numberOfProds, 'products to be generated.')
    if SINGLE_PRODUCT_NAME:
        log.debug("Modo debug ativo")
        print('Will process only "', singleProduct['name'], '".', sep='')
    for product in productList:
        if product['enabled']:
            PC.process_product(CONFIG, product)

    #os.system(script)
    #print("------------- Monitor Script Executed -------------")
    #print("Waiting for next call. The interval is", seconds, "seconds.")
    #------------------------------------------------------------------------------------------------------
    sys.exit()
    
if __name__ == "__main__":
    main()
#------------------------------------------------------------------------------------------------------	
# Scheduler function
"""s = sched.scheduler(time.time, time.sleep)

def call_monitor(sc): 
    print("\n")
    print("------------- Calling Monitor Script --------------")
    script = python_env + 'python ' + showcast_dir + '/Scripts/showcast_config.py' + ' ' + python_env + ' ' + ingest_dir + ' ' + showcast_process + ' ' + vis_dir
    os.system(script)
    print("------------- Monitor Script Executed -------------")
    print("Waiting for next call. The interval is", seconds, "seconds.")	
    s.enter(seconds, 1, call_monitor, (sc,))
    # Keep calling the monitor
    
# Call the monitor
s.enter(seconds, 1, call_monitor, (s,))
s.run()
"""
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

