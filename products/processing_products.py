
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
# If not, see http:/www.gnu.org/licenses/.
#######################################################################################################

# Modificado por João Pedro OCT/2025, uma alternativa ao config.py

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

# Required Libraries
import datetime # Basic Date and Time types
import pathlib  # Object-oriented filesystem paths # Get the file modification time
import glob                           # Unix style pathname pattern expansion
import os    
from pathlib import Path# Miscellaneous operating system interfaces  
from os.path import dirname, abspath                                                
import datetime                       # Basic Date and Time types
import importlib                      # To load specific scripts by variable value
import logging

#######################################################################################################
# FILE PROCESSING AND LOG FUNCTION
#######################################################################################################

showcast_dir = Path.cwd()
print('showcast_dir:', showcast_dir)



#def ProcessProduct(prod_dir, identifier, config, script, min_lon, min_lat, max_lon, max_lat, resolution, output, vis_dir, interval):
def process_product(CONFIG, product):
    log = logging.getLogger(f"processment.{__name__}")
    log.info(f'Processing {product['name']}')
    # Create the list that will store the file names
    gnc_files = []

    # Add to the list the files in the dir that matches the identifier
    #print('Input directory:', product['input'])
    inputFileNames = sorted(glob.glob(product['input'] + product['filename pattern']))
    #print("Files available:", inputFileNames)
    for filename in inputFileNames:
        # If the file has a fixed name:
        if (product['filename pattern'] ==  'gfs.sam.t00z.f120') or (product['filename pattern'] ==  'gfs.sam.t12z.f120') \
            or (product['filename pattern'] ==  'gfs.crb.t00z.f120') or (product['filename pattern'] ==  'gfs.crb.t12z.f120') \
            or (product['filename pattern'] == 'd6.gif') or (product['filename pattern'] == 'crb3_east.gif'):
            mtime = datetime.datetime.fromtimestamp(pathlib.Path(filename).stat().st_mtime).strftime('%Y%m%d%H%M%S')
            gnc_files.append(os.path.normpath(filename + product['config']+ '_c' + mtime))
        else: # If the files have unique names
            gnc_files.append(os.path.normpath(filename + product['config']))

        #print("\n")
        #print("PRODDIR: ", prod_dir+identifier)
        #print("PRODNAM: ", filename + config + '_' + mtime)
        #print("\n")

    if len(gnc_files) < 1:
        print('ERRO: nenhum arquivo encontrado')
    # Keep on the list only the max number of files
    gnc_files = gnc_files[-product['max files']:]
    #print("GNC files:\n", gnc_files)

    # If the gnc log file doesn't exist yet, create one
    file = open(showcast_dir / ('logs/files/gnc_log_' + str(datetime.datetime.now())[0:10] + '.txt'), 'a')
    file.close()

    # Put all file names on the gnc log in a list
    log = []
    with open(showcast_dir / ('logs/files/gnc_log_' + str(datetime.datetime.now())[0:10] + '.txt')) as f:
        log = f.readlines()

    # Remove the line feeds
    log = [x.strip() for x in log]

    # Compare the gnc file list with the log
    # Loop through all the files
    for dataFileName in gnc_files:
    # If a file is not on the log, process it
        if dataFileName not in log:
            
            print(f'Processing the following file: {dataFileName}\n')
            product['dataFileName'] = dataFileName
            script = 'scripts/' + product['script']
            print(f'Script used: {script}\n')
            global prod_count
            prod_count += 1
            scriptName = 'scripts/' + product['script']
            print(f"script name: {scriptName}")
            workModule = importlib.import_module('scripts.'+(product['script'].rsplit('.',1)[0]))
            print(f'will run: {workModule}')
            workModule.run(CONFIG, product)
            # command = (script + ' "' + dataFileName + '" '
                # + ' '.join(str(x) for x in product['extent']) + ' ' #"min_lon min_lat max_lon max_lat"
                # + str(product['resolution']) + ' '
                # + CONFIG['output'] + ' '
                # + CONFIG['output'] + ' ' #vis_dir
                # + interval)
            #print('Command used:\n', command)
            #os.system(command)
            print('\n')

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# ~ print("\n")
# ~ print("############## SHOWCAST MONITOR STARTED ##############")
# ~ print("Started at:", datetime.datetime.now())
# ~ print("\n")

# Create a counter to identify how many products have been processed in the run
prod_count = 0

# Identifier for channel composites init
config = ''

# Extent init
extent = [0.0, 0.0, 0.0, 0.0]

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
