#######################################################################################################
4# LICENSE
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

# Modificado por João Pedro, OCT/2025, uma alternativa ao showcast_config.py

__author__ = "Diego Souza"
__copyright__ = "Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL"
__credits__ = ["Diego Souza"]
__license__ = "GPL"
__version__ = "2.5.0"
__maintainer__ = "Diego Souza"
__email__ = "diego.souza@inpe.br"
__status__ = "Production"


# Scrip responsável apenas por montar descrições 

def products(CONFIG) -> list:
    output_dir = CONFIG['output']

    resultado = []
    p = {}
    p['name'] = 'g16_band01_fdk'
    p['enabled'] = True # GOES-16 L2 CMI - Band 01 - FULL DISK
    p['cicle'] = 1                                                      # Process cicle for this product (TODOS TEM O VALOR 1 !?)
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'            # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                           # Unique string on the file name
    p['max files'] = 1                                                    # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                 # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                   # Processing interval
    p['config'] = ''                                                      # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder (TODOS TEM O MESMO VALOR!)
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band01_sec' # GOES-16 L2 CMI - Band 01 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band02_fdk' # GOES-16 L2 CMI - Band 02 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    # Modifiquei aqui porque o nome do diretório mudou de Band02 para Band02-0.5km
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band02_sec' # GOES-16 L2 CMI - Band 02 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band03_fdk' # GOES-16 L2 CMI - Band 03 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band03/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band03_sec' # GOES-16 L2 CMI - Band 03 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band03/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band04_fdk' # GOES-16 L2 CMI - Band 04 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band04/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C04_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band04_sec' # GOES-16 L2 CMI - Band 04 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band04/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C04_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band05_fdk' # GOES-16 L2 CMI - Band 05 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band05_sec' # GOES-16 L2 CMI - Band 05 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band06_fdk' # GOES-16 L2 CMI - Band 06 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band06/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band06_sec' # GOES-16 L2 CMI - Band 06 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band06/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band07_fdk' # GOES-16 L2 CMI - Band 07 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band07_sec' # GOES-16 L2 CMI - Band 07 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band08_fdk' # GOES-16 L2 CMI - Band 08 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band08_sec' # GOES-16 L2 CMI - Band 08 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band09_fdk' # GOES-16 L2 CMI - Band 09 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band09_sec' # GOES-16 L2 CMI - Band 09 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band10_fdk' # GOES-16 L2 CMI - Band 10 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band10_sec' # GOES-16 L2 CMI - Band 10 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band11_fdk' # GOES-16 L2 CMI - Band 11 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band11/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C11_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band11_sec' # GOES-16 L2 CMI - Band 11 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band11/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C11_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band12_fdk' # GOES-16 L2 CMI - Band 12 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band12/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C12_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band12_sec' # GOES-16 L2 CMI - Band 12 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band12/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C12_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band13_fdk' # GOES-16 L2 CMI - Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band13_sec' # GOES-16 L2 CMI - Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band14_fdk' # GOES-16 L2 CMI - Band 14 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band14/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C14_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band14_sec' # GOES-16 L2 CMI - Band 14 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band14/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C14_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band15_fdk' # GOES-16 L2 CMI - Band 15 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band15_sec' # GOES-16 L2 CMI - Band 15 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band16_fdk' # GOES-16 L2 CMI - Band 16 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band16/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C16_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_band16_sec' # GOES-16 L2 CMI - Band 16 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band16/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C16_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-16 - ABI INDIVIDUAL L1B [RADIANCES] BANDS (FROM THE CLOUD - NEED TO ACTIVATE THE CLOUD MODULE!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb01_fdk' # GOES-16 L1b RadF - Band 01 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band01/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb01_sec' # GOES-16 L1b RadF - Band 01 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band01/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb02_fdk' # GOES-16 L1b RadF - Band 02 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band02-0.5km/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 0.5 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb02_sec' # GOES-16 L1b RadF - Band 02 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band02-0.5km/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 0.5 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb03_fdk' # GOES-16 L1b RadF - Band 03 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band03/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb03_sec' # GOES-16 L1b RadF - Band 03 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band03/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb04_fdk' # GOES-16 L1b RadF - Band 04 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band04/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C04_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb04_sec' # GOES-16 L1b RadF - Band 04 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band04/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C04_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb05_fdk' # GOES-16 L1b RadF - Band 05 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band05/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb05_sec' # GOES-16 L1b RadF - Band 05 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band05/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb06_fdk' # GOES-16 L1b RadF - Band 06 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band06/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb06_sec' # GOES-16 L1b RadF - Band 06 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band06/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb07_fdk' # GOES-16 L1b RadF - Band 07 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band07/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb07_sec' # GOES-16 L1b RadF - Band 07 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band07/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb08_fdk' # GOES-16 L1b RadF - Band 08 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band08/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb08_sec' # GOES-16 L1b RadF - Band 08 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band08/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb09_fdk' # GOES-16 L1b RadF - Band 09 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band09/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb09_sec' # GOES-16 L1b RadF - Band 09 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band09/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb10_fdk' # GOES-16 L1b RadF - Band 10 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band10/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb10_sec' # GOES-16 L1b RadF - Band 10 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band10/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb11_fdk' # GOES-16 L1b RadF - Band 11 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band11/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C11_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb11_sec' # GOES-16 L1b RadF - Band 11 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band11/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C11_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb12_fdk' # GOES-16 L1b RadF - Band 12 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band12/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C12_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb12_sec' # GOES-16 L1b RadF - Band 12 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band12/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C12_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb13_fdk' # GOES-16 L1b RadF - Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band13/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb13_sec' # GOES-16 L1b RadF - Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band13/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb14_fdk' # GOES-16 L1b RadF - Band 14 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band14/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C14_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb14_sec' # GOES-16 L1b RadF - Band 14 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band14/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C14_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb15_fdk' # GOES-16 L1b RadF - Band 15 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band15/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb15_sec' # GOES-16 L1b RadF - Band 15 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band15/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb16_fdk' # GOES-16 L1b RadF - Band 16 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band16/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C16_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_rad_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_radb16_sec' # GOES-16 L1b RadF - Band 16 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-RadF-Imagery/Band16/'              # Folder where the data is found
    p['filename pattern'] = '*L1b-RadF-M*C16_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_rad_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#######################################################################################################
# GOES-16 RGB COMPOSITES
#######################################################################################################
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_24hrgb_fdk' # GOES-16 24h Microphysics RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_24H'                                                    # Configuration string
    p['script'] = 'g16_24hrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_24hrgb_sec' # GOES-16 24h Microphysics RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_24S'                                                    # Configuration string
    p['script'] = 'g16_24hrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_armrgb_fdk' # GOES-16 Airmass RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_ARM'                                                    # Configuration string
    p['script'] = 'g16_armrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_armrgb_sec' # GOES-16 Airmass RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_ARS'                                                    # Configuration string
    p['script'] = 'g16_armrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ashrgb_fdk' # GOES-16 Ash RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_ASH'                                                    # Configuration string
    p['script'] = 'g16_ashrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ashrgb_sec' # GOES-16 Ash RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_ASS'                                                    # Configuration string
    p['script'] = 'g16_ashrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_clprgb_fdk' # GOES-16 Cloud Phase RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_CLP'                                                    # Configuration string
    p['script'] = 'g16_clprgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_clprgb_sec' # GOES-16 Cloud Phase RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_CLS'                                                    # Configuration string
    p['script'] = 'g16_clprgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dccrgb_fdk' # GOES-16 Day Cloud Convection RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DCC'                                                    # Configuration string
    p['script'] = 'g16_dccrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dccrgb_sec' # GOES-16 Day Cloud Convection RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DCS'                                                    # Configuration string
    p['script'] = 'g16_dccrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dcprgb_fdk' # GOES-16 Day Cloud Phase RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DCP'                                                    # Configuration string
    p['script'] = 'g16_dcprgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dcprgb_sec' # GOES-16 Day Cloud Phase RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DCS'                                                    # Configuration string
    p['script'] = 'g16_dcprgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_conrgb_fdk' # GOES-16 Convection RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_CON'                                                    # Configuration string
    p['script'] = 'g16_conrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_conrgb_sec' # GOES-16 Convection RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band08/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C08_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_COS'                                                    # Configuration string
    p['script'] = 'g16_conrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dlcrgb_fdk' # GOES-16 Day Land Cloud RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DLC'                                                        # Configuration string
    p['script'] = 'g16_dlcrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dlcrgb_sec' # GOES-16 Day Land Cloud RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band05/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C05_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DLS'                                                    # Configuration string
    p['script'] = 'g16_dlcrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dlfrgb_fdk' # GOES-16 Day Land Cloud RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band06/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DFR'                                                        # Configuration string
    p['script'] = 'g16_dlfrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dlfrgb_sec' # GOES-16 Day Land Cloud RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band06/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C06_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DFS'                                                    # Configuration string
    p['script'] = 'g16_dlfrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dmprgb_fdk' # GOES-16 Day Microphysics RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DMP'                                                    # Configuration string
    p['script'] = 'g16_dmprgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dmprgb_sec' # GOES-16 Day Microphysics RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DMS'                                                    # Configuration string
    p['script'] = 'g16_dmprgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsfrgb_fdk' # GOES-16 Day Snow Fog RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band03/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DSF'                                                    # Configuration string
    p['script'] = 'g16_dsfrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsfrgb_sec' # GOES-16 Day Snow Fog RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band03/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C03_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DSS'                                                    # Configuration string
    p['script'] = 'g16_dsfrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dwvrgb_fdk' # GOES-16 Differential Water Vapor RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DWV'                                                    # Configuration string
    p['script'] = 'g16_dwvrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dwvrgb_sec' # GOES-16 Differential Water Vapor RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DWS'                                                    # Configuration string
    p['script'] = 'g16_dwvrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dstrgb_fdk' # GOES-16 Dust RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DST'                                                    # Configuration string
    p['script'] = 'g16_dstrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dstrgb_sec' # GOES-16 Dust RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_DSS'                                                    # Configuration string
    p['script'] = 'g16_dstrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_fcorgb_fdk' # GOES-16 False Color RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCO'                                                    # Configuration string
    p['script'] = 'g16_fcorgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_fcorgb_sec' # GOES-16 False Color RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCS'                                                    # Configuration string
    p['script'] = 'g16_fcorgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ftprgb_fdk' # GOES-16 Fire Temperature RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FTP'                                                    # Configuration string
    p['script'] = 'g16_ftprgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ftprgb_sec' # GOES-16 Fire Temperature RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band07/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C07_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FTS'                                                    # Configuration string
    p['script'] = 'g16_ftprgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ntcrgb_fdk' # GOES-16 Natural True Color RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_NTC'                                                    # Configuration string
    p['script'] = 'g16_ntcrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ntcrgb_sec' # GOES-16 Natural True Color RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_NTS'                                                    # Configuration string
    p['script'] = 'g16_ntcrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_nmprgb_fdk' # GOES-16 Day Cloud Phase RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_NMP'                                                    # Configuration string
    p['script'] = 'g16_nmprgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_nmprgb_sec' # GOES-16 Day Cloud Phase RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band15/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C15_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_NMS'                                                    # Configuration string
    p['script'] = 'g16_nmprgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_swvrgb_fdk' # GOES-16 Simple Water Vapor RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SVV'                                                    # Configuration string
    p['script'] = 'g16_swvrgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_swvrgb_sec' # GOES-16 Simple Water Vapor RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band10/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C10_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SVS'                                                    # Configuration string
    p['script'] = 'g16_swvrgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_so2rgb_fdk' # GOES-16 SO2 RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SO2'                                                    # Configuration string
    p['script'] = 'g16_so2rgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_so2rgb_sec' # GOES-16 SO2 RGB - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SOS'                                                    # Configuration string
    p['script'] = 'g16_so2rgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_trurgb_fdk' # GOES-16 True Color RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_TRU'                                                    # Configuration string
    p['script'] = 'g16_trurgb_fdk.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_trurgb_sec' # GOES-16 True Color RGB - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band01/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C01_G16*.nc'                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 1 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_TRS'                                                    # Configuration string
    p['script'] = 'g16_trurgb_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-16 BASELINE PRODUCTS (FROM GEONETCAST-AMERICAS AND / OR CLOUD)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldhgt_fdk' # GOES-16 L2 ACHAF - Cloud Top Height - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACHAF/'           # Folder where the data is found
    p['filename pattern'] = '*ACHAF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldhgt_sec' # GOES-16 L2 ACHAF - Cloud Top Height - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACHAF/'           # Folder where the data is found
    p['filename pattern'] = '*ACHAF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldtmp_fdk' # GOES-16 L2 ACHTF - Cloud Top Temperature - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACHTF/'           # Folder where the data is found
    p['filename pattern'] = '*ACHTF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldtmp_sec' # GOES-16 L2 ACHTF - Cloud Top Temperature - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACHTF/'           # Folder where the data is found
    p['filename pattern'] = '*ACHTF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 2 km                                      # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldmsk_fdk' # GOES-16 L2 ACMF - Clear Sky Masks - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACMF/'            # Folder where the data is found
    p['filename pattern'] = '*ACMF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldmsk_sec' # GOES-16 L2 ACMF - Clear Sky Masks - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACMF/'            # Folder where the data is found
    p['filename pattern'] = '*ACMF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 2 km                                      # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpha_fdk' # GOES-16 L2 ACTPF - Cloud Top Phase - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACTPF/'           # Folder where the data is found
    p['filename pattern'] = '*ACTPF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpha_sec' # GOES-16 L2 ACTPF - Cloud Top Phase - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ACTPF/'           # Folder where the data is found
    p['filename pattern'] = '*ACTPF*.nc'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_aerdet_fdk' # GOES-16 L2 ADPF - Aerosol Detection - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ADPF/'            # Folder where the data is found
    p['filename pattern'] = '*ADPF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_adpf_fdk.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_aerdet_sec' # GOES-16 L2 ADPF - Aerosol Detection - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/ADPF/'            # Folder where the data is found
    p['filename pattern'] = '*ADPF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_adpf_sec.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_aeropt_fdk' # GOES-16 L2 AODF - Aerosol Optical Depth - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/AODF/'            # Folder where the data is found
    p['filename pattern'] = '*AODF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_aeropt_sec' # GOES-16 L2 AODF - Aerosol Optical Depth - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/AODF/'            # Folder where the data is found
    p['filename pattern'] = '*AODF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldopt_fdk' # GOES-16 L2 CODF - Cloud Optical Depth - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CODF/'            # Folder where the data is found
    p['filename pattern'] = '*CODF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 4 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldopt_sec' # GOES-16 L2 CODF - Cloud Optical Depth - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CODF/'            # Folder where the data is found
    p['filename pattern'] = '*CODF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4  # Max Res.: 4 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpas_fdk' # GOES-16 L2 CPSF - Cloud Particle Size - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CPSF/'            # Folder where the data is found
    p['filename pattern'] = '*CPSF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpas_sec' # GOES-16 L2 CODF - Cloud Optical Depth - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CPSF/'            # Folder where the data is found
    p['filename pattern'] = '*CPSF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpre_fdk' # GOES-16 L2 CTPF - Cloud Top Pressure - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CTPF/'            # Folder where the data is found
    p['filename pattern'] = '*CTPF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_cldpre_sec' # GOES-16 L2 CTPF - Cloud Top Pressure - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/CTPF/'            # Folder where the data is found
    p['filename pattern'] = '*CTPF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dmwf14_fdk' # GOES-16 L2 DMWF-C14 - Derived Motion Winds Band 14 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DMWF-C14/'        # Folder where the data is found
    p['filename pattern'] = '*DMWF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_CLD'                                                    # Configuration string
    p['script'] = 'g16_dmw_clouds_fdk.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dmwf14_sec' # GOES-16 L2 DMWF-C14 - Derived Motion Winds Band 14 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DMWF-C14/'        # Folder where the data is found
    p['filename pattern'] = '*DMWF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_CLS'                                                    # Configuration string
    p['script'] = 'g16_dmw_clouds_sec.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsifpr_fdk' # GOES-16 L2 DSIF - Derived Stability Index - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DSIF/'            # Folder where the data is found
    p['filename pattern'] = '*DSIF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_dsif_fdk.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsifpr_sec' # GGOES-16 L2 DSIF - Derived Stability Index - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DSIF/'            # Folder where the data is found
    p['filename pattern'] = '*DSIF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_dsif_sec.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsradi_fdk' # GOES-16 L2 DSRF - Downward Shortwave Radiation - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DSRF/'            # Folder where the data is found
    p['filename pattern'] = '*DSRF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 25 km (but you may select higher res plots)# Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_rad_fdk.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_dsradi_sec' # GOES-16 L2 DSRF - Downward Shortwave Radiation - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/DSRF/'            # Folder where the data is found
    p['filename pattern'] = '*DSRF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 25 km (but you may select higher res plots)# Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_rad_sec.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_firmsk_fdk' # GOES-16 L2 FDCF - Fire-Hot Spot Characterization - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/FDCF/'            # Folder where the data is found
    p['filename pattern'] = '*FDCF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_fdfc_fdk.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_firmsk_sec' # GOES-16 L2 FDCF - Fire-Hot Spot Characterization - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/FDCF/'            # Folder where the data is found
    p['filename pattern'] = '*FDCF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_fdfc_sec.py'       # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_snowco_fdk' # GOES-16 L2 FSCF - Snow Cover - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/FSCF/'            # Folder where the data is found
    p['filename pattern'] = '*FSCF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_snowco_sec' # GOES-16 L2 FSCF - Snow Cover - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/FSCF/'            # Folder where the data is found
    p['filename pattern'] = '*FSCF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_lstskn_fdk' # GOES-16 L2 LSTF - Land Surface (Skin) Temperature - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/LSTF/'            # Folder where the data is found
    p['filename pattern'] = '*LST*.nc'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  10  # Max Res.: 2 km                                      # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_lstskn_sec' # GOES-16 L2 LSTF - Land Surface (Skin) Temperature - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/LSTF/'            # Folder where the data is found
    p['filename pattern'] = '*LST*.nc'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 2 km                                      # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_rrqpef_fdk' # GOES-16 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/RRQPEF/'          # Folder where the data is found
    p['filename pattern'] = '*RRQPEF*.nc'                                             # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_rrqpef_sec' # GOES-16 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/RRQPEF/'          # Folder where the data is found
    p['filename pattern'] = '*RRQPEF*.nc'                                             # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_rsradi_fdk' # GOES-16 L2 RSRF - Reflected Shortwave Radiation - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/RSRF/'            # Folder where the data is found
    p['filename pattern'] = '*RSRF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2 # Max Res.: 25 km (but you may select higher res plots) # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_rad_fdk.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_rsradi_sec' # GOES-16 L2 RSRF - Reflected Shortwave Radiation - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/RSRF/'            # Folder where the data is found
    p['filename pattern'] = '*RSRF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2 # Max Res.: 25 km (but you may select higher res plots) # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_rad_sec.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_sstskn_fdk' # GOES-16 L2 SSTF - Sea Surface (Skin) Temperature - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/SSTF/'            # Folder where the data is found
    p['filename pattern'] = '*SSTF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_sstskn_sec' # GOES-16 L2 SSTF - Sea Surface (Skin) Temperature - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/SSTF/'            # Folder where the data is found
    p['filename pattern'] = '*SSTF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_totpwa_fdk' # GOES-16 L2 TPWF - Total Precipitable Water - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/TPWF/'            # Folder where the data is found
    p['filename pattern'] = '*TPWF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_baseline_fdk.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_totpwa_sec' # GOES-16 L2 TPWF - Total Precipitable Water - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-Level-2-Products/TPWF/'            # Folder where the data is found
    p['filename pattern'] = '*TPWF*.nc'                                               # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-105.0, -60.0, -15.0, 20.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                     # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_baseline_sec.py'   # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-16 - BANDS COMPOSITES / MULTISPECTRAL IMAGERY
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_fcolor_fdk' # GOES-16 False Color - Band 02 and Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCO'                                                    # Configuration string
    p['script'] = 'g1X_false_color_fdk.py'# Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_fcolor_sec' # GOES-16 False Color - Band 02 and Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCS'                                                    # Configuration string
    p['script'] = 'g1X_false_color_sec.py'# Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ircl13_fdk' # GOES-16 IR Clouds - Band 13 with Blue Marble - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_IRC'                                                    # Configuration string
    p['script'] = 'g1X_ir_clouds_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_ircl13_sec' # GOES-16 IR Clouds - Band 13 with Blue Marble - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_IRS'                                                    # Configuration string
    p['script'] = 'g1X_ir_clouds_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_irce13_fdk' # GOES-16 IR Clouds Enhanced - Band 13 [enhanced] with Blue Marble - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                                # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'                      # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                        # Unique string on the file name
    p['max files'] = 1                                                                # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                              # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                              # Processing interval
    p['config'] = '_IRE'                                                           # Configuration string
    p['script'] = 'g1X_ir_clouds_enhance_fdk.py' # Script to activate
    p['output'] = output_dir                                      # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_irce13_sec' # GOES-16 IR Clouds Enhanced - Band 13 [enhanced] with Blue Marble - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                                # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'                      # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                        # Unique string on the file name
    p['max files'] = 1                                                                # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                                     # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                              # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                              # Processing interval
    p['config'] = '_IES'                                                           # Configuration string
    p['script'] = 'g1X_ir_clouds_enhance_sec.py' # Script to activate
    p['output'] = output_dir                                      # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_swdiff_fdk' # GOES-16 Split Window Difference - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SWD'                                                    # Configuration string
    p['script'] = 'g1X_swd_fdk.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_swdiff_sec' # GOES-16 Split Window Difference - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SWS'                                                    # Configuration string
    p['script'] = 'g1X_swd_sec.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_salpro_sec' # GOES-16 Saharan Air Layer Tracking Product - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G16*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-100.0, 0.0, -13.0, 40.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00'                                                      # Processing interval
    p['config'] = '_SAS'                                                    # Configuration string
    p['script'] = 'g1X_sal_sec.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-16 GLM (GEOSTATIONARY LIGHTNING MAPPER) - SUGGESTION: PUT IN A DEDICATED PROCESS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glm20s_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (20s) - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 10                                                        # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_glm_20s_fdk.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glm20s_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (20s) - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 10                                                        # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_glm_20s_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glir20_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (20s) + GOES-16 Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 10                                                        # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_IRF'                                                    # Configuration string
    p['script'] = 'g16_glm_ir_20s_fdk.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glir20_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (20s) + GOES-16 Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 10                                                        # Max number of historical files to be processed
    p['extent'] = [-58.0, -30.0, -43.0, -15.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_IRS'                                                    # Configuration string
    p['script'] = 'g16_glm_ir_20s_sec.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmtra_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Tracking) + GOES-16 Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 30                                                        # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_TRA'                                                    # Configuration string
    p['script'] = 'g16_glm_tra_fdk.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmtra_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Tracking) + GOES-16 Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 30                                                        # Max number of historical files to be processed
    p['extent'] = [-58.0, -30.0, -43.0, -15.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_TRS'                                                    # Configuration string
    p['script'] = 'g16_glm_tra_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmden_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Density) + GOES-16 Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 60                                                        # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_DEN'                                                    # Configuration string
    p['script'] = 'g16_glm_den_fdk.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmden_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Density) + GOES-16 Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 60                                                        # Max number of historical files to be processed
    p['extent'] = [-55.0, -25.0, -40.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_DES'                                                    # Configuration string
    p['script'] = 'g16_glm_den_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmhea_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Heatmap) + GOES-16 Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 60                                                        # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_HEA'                                                    # Configuration string
    p['script'] = 'g16_glm_hea_fdk.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmhea_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (Heatmap) + GOES-16 Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'OR_GLM*.nc'                                              # Unique string on the file name
    p['max files'] = 60                                                        # Max number of historical files to be processed
    p['extent'] = [-55.0, -25.0, -40.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_HES'                                                    # Configuration string
    p['script'] = 'g16_glm_hea_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmirc_fdk' # GOES-16 L2 GLM - Geostationary Lightning Mapper (5 min density) - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'GLM_*.nc'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g16_glm_clouds_fdk.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g16_glmirc_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (5 min density) - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-R-GLM-Products/'                      # Folder where the data is found
    p['filename pattern'] = 'GLM_*.nc'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g16_glm_clouds_sec.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-16 and GOES-17 Mosaic
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g1X_b13mos_sec' # GOES-16 L2 GLM - Geostationary Lightning Mapper (5 min density) - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120.0, 0.0, -75.0, 45.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_MOS'                                                    # Configuration string
    p['script'] = 'g1X_b13_mosaic_sec.py' # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-17 - ABI INDIVIDUAL BANDS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band02_fdk' # GOES-17 L2 CMI - Band 02 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band02_sec' # GOES-17 L2 CMI - Band 02 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120.0, 0.0, -75.0, 45.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band09_fdk' # GOES-17 L2 CMI - Band 09 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band09_sec' # GOES-17 L2 CMI - Band 09 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band09/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C09_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120.0, 0.0, -75.0, 45.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band13_fdk' # GOES-17 L2 CMI - Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'g1X_bands_fdk.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_band13_sec' # GOES-17 L2 CMI - Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120.0, 0.0, -75.0, 45.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1                                                         # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'g1X_bands_sec.py'      # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GOES-17 - BANDS COMPOSITES / MULTISPECTRAL IMAGERY
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_fcolor_fdk' # GOES-17 False Color - Band 02 and Band 13 - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCO'                                                    # Configuration string
    p['script'] = 'g1X_false_color_fdk.py'# Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_fcolor_sec' # GOES-17 False Color - Band 02 and Band 13 - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band02-0.5km/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C02_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_FCS'                                                    # Configuration string
    p['script'] = 'g1X_false_color_sec.py'# Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_ircl13_fdk' # GOES-17 IR Clouds - Band 13 with Blue Marble - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_IRC'                                                    # Configuration string
    p['script'] = 'g1X_ir_clouds_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_ircl13_sec' # GOES-17 IR Clouds - Band 13 with Blue Marble - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'               # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                 # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                       # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                       # Processing interval
    p['config'] = '_IRS'                                                    # Configuration string
    p['script'] = 'g1X_ir_clouds_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_irce13_fdk' # GOES-17 IR Clouds Enhanced - Band 13 [enhanced] with Blue Marble - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                                # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'                      # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                        # Unique string on the file name
    p['max files'] = 1                                                                # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 2 km                                              # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                              # Processing interval
    p['config'] = '_IRE'                                                           # Configuration string
    p['script'] = 'g1X_ir_clouds_enhance_fdk.py' # Script to activate
    p['output'] = output_dir                                      # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'g17_irce13_sec' # GOES-17 IR Clouds Enhanced - Band 13 [enhanced] with Blue Marble - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                                # Process cicle for this product
    p['input'] = CONFIG['input'] + 'GOES-S-CMI-Imagery/Band13/'                      # Folder where the data is found
    p['filename pattern'] = '*L2-CMIPF-M*C13_G17*.nc'                                        # Unique string on the file name
    p['max files'] = 1                                                                # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                                     # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  2  # Max Res.: 2 km                                              # Final plot resolution
    p['interval'] = '00,10,20,30,40,50'                                              # Processing interval
    p['config'] = '_IES'                                                           # Configuration string
    p['script'] = 'g1X_ir_clouds_enhance_sec.py' # Script to activate
    p['output'] = output_dir                                      # Output folder
    resultado.append(p)

#######################################################################################################
# METEOSAT PRODUCTS (YOU MAY SELECT WHICH MSG SUBPRODUCT YOU WANT TO PROCESS INSIDE THE PYTHON SCRIPT!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'msg_produc_fdk' # METEOSAT - 0 Degree (IMAGERY AND RGB'S) - FULL DISK
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MSG-0degree/IMG-3h/'                      # Folder where the data is found
    p['filename pattern'] = '*-EPI______-*'                                           # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  8  # Max Res.: 3 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'msg_bands_rgb_fdk.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'msg_produc_sec' # METEOSAT - 0 Degree (IMAGERY AND RGB'S) - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MSG-0degree/IMG-3h/'                      # Folder where the data is found
    p['filename pattern'] = '*-EPI______-*'                                           # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-63.0, -35.0, -35.0, -10.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  3  # Max Res.: 3 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_SEC'                                                    # Configuration string
    p['script'] = 'msg_bands_rgb_sec.py'  # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GCOM-W1 IMAGERY AND PRODUCTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_imager_sec' # GCOM-W1 - IMAGERY
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-IMAGERY/'                  # Folder where the data is found
    p['filename pattern'] = 'AMSR2-MBT*'                                                # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-156.0, -60.0, 6.00, 60.0]                                 # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_soilmo_sec' # GCOM-W1 - SOIL MOISTURE and LAND COVER
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-SOILMOISTURE/'             # Folder where the data is found
    p['filename pattern'] = 'AMSR2-SOIL*'                                               # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-156.0, -60.0, 6.00, 60.0]                                 # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                  # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_oceanp_sec' # GCOM-W1 - CLW, SST, TPW, WSPD
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-OCEAN/'                    # Folder where the data is found
    p['filename pattern'] = 'AMSR2-OCEAN*'                                              # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-156.00, -65.00, 6.00, 65.00]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_precip_sec' # GCOM-W1 - RAIN RATE, CONVECTIVE PREC, PROBABILITY
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-PRECIPITATION/'            # Folder where the data is found
    p['filename pattern'] = 'AMSR2-PRECIP*'                                             # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_icepro_sec' # GCOM-W1 - SEA ICE NH
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-SEAICE/'                   # Folder where the data is found
    p['filename pattern'] = 'AMSR2-SEAICE-NH*'                                          # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_icepro_sec' # GCOM-W1 - SEA ICE SH
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-SEAICE/'                   # Folder where the data is found
    p['filename pattern'] = 'AMSR2-SEAICE-SH*'                                          # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                                # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gcm_snowpr_sec' # GCOM-W1 - SNOW COVER, SNOW DEPTH, SWE
    p['enabled'] = True
    p['cicle'] = 1                                                           # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/G-SNOW/'                     # Folder where the data is found
    p['filename pattern'] = 'AMSR2-SNOW*'                                               # Unique string on the file name
    p['max files'] = 3                                                           # Max number of historical files to be processed
    p['extent'] = [-156.00, 0.00, -45.00, 75.00]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10  # Max Res.: 10 km                                       # Final plot resolution
    p['interval'] = ''                                                          # Processing interval
    p['config'] = ''                                                          # Configuration string
    p['script'] = 'gcm_imagery_products.py' # Script to activate
    p['output'] = output_dir                                 # Output folder
    resultado.append(p)

#######################################################################################################
# HOURLY GLOBAL BLENDED PRODUCTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_btpwpr_sec' # Hourly Global Blended Total Precipitable Water
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/BTPW/'                     # Folder where the data is found
    p['filename pattern'] = 'BHP-TPW*'                                                # Unique string on the file name
    p['max files'] = 3                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -71.0, 180.0, 71.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8  # Max Res.: 16 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_btpw_v2.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_bpctpr_sec' # Hourly Global Blended Total Precipitable Water Anomaly
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/BTPW/'                     # Folder where the data is found
    p['filename pattern'] = 'BHP-PCT*'                                                # Unique string on the file name
    p['max files'] = 3                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -71.0, 180.0, 71.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8  # Max Res.: 16 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_btpw_v2.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_rainpr_sec' # Hourly Global Rain Rate
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/BTPW/'                     # Folder where the data is found
    p['filename pattern'] = 'BHP-RR*'                                                 # Unique string on the file name
    p['max files'] = 3                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -71.0, 180.0, 71.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8  # Max Res.: 16 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_btpw_v2.py'        # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# FLOOD MAPPING PRODUCTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'fld_abihly_sec' # GOES-16 ABI Hourly Composite
    p['enabled'] = True
    p['cicle'] = 1                                                                    # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIMSS/Flood-ABI/'                                    # Folder where the data is found
    p['filename pattern'] = '*part004*'                                                          # Unique string on the file name
    p['max files'] = 3                                                                    # Max number of historical files to be processed
    p['extent'] = [-52.0, -5.0, -47.0, 0.0] # Recommended using a max of 5 x 5 degree  # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1  # Max Res.: 1 km                                                  # Final plot resolution
    p['interval'] = ''                                                                   # Processing interval
    p['config'] = ''                                                                   # Configuration string
    p['script'] = 'flood_mapping.py'                 # Script to activate
    p['output'] = output_dir                                          # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'fld_joinva_sec' # Joint VIIRS / ABI flood product (daily)
    p['enabled'] = True
    p['cicle'] = 1                                                                    # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIMSS/Flood-Joint/'                                  # Folder where the data is found
    p['filename pattern'] = '*part041*'                                                          # Unique string on the file name
    p['max files'] = 3                                                                    # Max number of historical files to be processed
    p['extent'] = [-52.0, -5.0, -47.0, 0.0] # Recommended using a max of 5 x 5 degree  # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  0.375 # Max Res.: 0.375 km                                           # Final plot resolution
    p['interval'] = ''                                                                   # Processing interval
    p['config'] = ''                                                                   # Configuration string
    p['script'] = 'flood_mapping.py'                 # Script to activate
    p['output'] = output_dir                                          # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'fld_vrs5da_sec' # Suomi-NPP and NOAA-20 VIIRS 5-day Composite (daily)
    p['enabled'] = True
    p['cicle'] = 1                                                                    # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIMSS/Flood-Composite/'                              # Folder where the data is found
    p['filename pattern'] = '*part041*'                                                          # Unique string on the file name
    p['max files'] = 3                                                                    # Max number of historical files to be processed
    p['extent'] = [-52.0, -5.0, -47.0, 0.0] # Recommended using a max of 5 x 5 degree  # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  0.375 # Max Res.: 0.375 km                                           # Final plot resolution
    p['interval'] = ''                                                                   # Processing interval
    p['config'] = ''                                                                   # Configuration string
    p['script'] = 'flood_mapping.py'                 # Script to activate
    p['output'] = output_dir                                          # Output folder
    resultado.append(p)

#######################################################################################################
# METOP GLOBAL SST
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mtp_glbsst_sec' # METOP - Global Sea Surface Temperature
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MTOP-GLBSST*'                                           # Unique string on the file name
    p['max files'] = 5                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -70.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  16 # Max Res.: 6 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'mtp_gblsst_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# SEA ICE PRODUCTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_sitype_sec' # Sea Ice Type (Northern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_NH_TYPEn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_sitype_sec' # Sea Ice Type (Southern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_SH_TYPEn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_siedge_sec' # Sea Ice Edge (Northern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_NH_EDGEn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_siedge_sec' # Sea Ice Edge (Southern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_SH_EDGEn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'dms_siconc_sec' # DMSP SSMIS Sea Ice Concentration (Northern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_NH_CONCn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'dms_siconc_sec' # DMSP SSMIS Sea Ice Concentration (Southern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*MULT-GL_SH_CONCn*.gz'                                   # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'dms_siemis_sec' # DMSP AMSU / SSMIS Sea Ice Emissivity (Northern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*DMSP-GL_NH_EMIS*.gz'                                    # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'dms_siemis_sec' # DMSP AMSU / SSMIS Sea Ice Emissivity (Southern Hemisphere)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'EUMETSAT/'                                 # Folder where the data is found
    p['filename pattern'] = '*DMSP-GL_SH_EMIS*.gz'                                    # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -80.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  10 # Max Res.: 10 km                                      # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'ice.py'                # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# NUCAPS SOUNDINGS - SUGGESTION: PUT IN A DEDICATED PROCESS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'n20_nucaps_sec' # NUCAPS SOUNDINGS
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/NUCAPS/'                   # Folder where the data is found
    p['filename pattern'] = 'NUCAPS-EDR*'                                             # Unique string on the file name
    p['max files'] = 300                                                       # Max number of historical files to be processed
    p['extent'] = [-54.0, -28.0, -43.0, -18.0]                              # Recommended using a max of 5 x 5 degree  # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  1 # Max Res.: 1 km                                        # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'nucaps.py'             # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# MULTIMISSION FIRE / HOT SPOTS (INPE SHAPEFILES)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_firein_sec' # MULTIMISSION FIRE / HOTSPOTS - INPE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'INPE/'                                     # Folder where the data is found
    p['filename pattern'] = 'INPE_MVF_*.gz'                                           # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'mul_fires.py'          # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# BLENDED TOAST - DAILY TOTAL OZONE
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_tstngl_sec' # TOAST - SNPP OMPS & NOAA-20 CrIS DAILY TOTAL OZONE - GLOBAL
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/TOAST/'                    # Folder where the data is found
    p['filename pattern'] = '*j01_CRIN_j01_OMPS*'                                     # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_tstngl_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_tstnnh_sec' # TOAST - SNPP OMPS & NOAA-20 CrIS DAILY TOTAL OZONE - NORTHERN HEMISPHERE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/TOAST/'                    # Folder where the data is found
    p['filename pattern'] = '*j01_CRIN_j01_OMPS*'                                     # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_NHP'                                                    # Configuration string
    p['script'] = 'jps_tstnnh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_tstnsh_sec' # TOAST - SNPP OMPS & NOAA-20 CrIS DAILY TOTAL OZONE - SOUTHERN HEMISPHERE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/TOAST/'                    # Folder where the data is found
    p['filename pattern'] = '*j01_CRIN_j01_OMPS*'                                     # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -90.0, 180.0, 90.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8                                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_SHP'                                                    # Configuration string
    p['script'] = 'jps_tstnsh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GFS MODEL 0.5 DEGREE - SOUTH AMERICA - 00Z RUN (SET AS TRUE ONLY SAM OR ONLY CRB!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_2mtems_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - 2 M TEMPERATURE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_001'                                                    # Configuration string
    p['script'] = 'gfs_2mtemp_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_accprs_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - ACCUMULATED PRECIPITACION
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_002'                                                    # Configuration string
    p['script'] = 'gfs_accpre_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_prtmss_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PRESSION REDUCED TO MEAN SEA LEVEL
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_003'                                                    # Configuration string
    p['script'] = 'gfs_prtmsl_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gdinds_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - GALVEZ DAVISON INDEX
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_004'                                                    # Configuration string
    p['script'] = 'gfs_gdindx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gh500s_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - RELATIVE VORTICITY AND GEOPOTENTIAL HEIGHT 500 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_005'                                                    # Configuration string
    p['script'] = 'gfs_ghv500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_psgwrs_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PSML + GEOP. DIF. (1000-850 hPa) + WINDS (925 hPa) + MEAN RH (1000~400 hPa)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_006'                                                    # Configuration string
    p['script'] = 'gfs_psgwrh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcaps_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PRECIPITABLE WATER & CAPE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_007'                                                    # Configuration string
    p['script'] = 'gfs_pwcape_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_sphcls_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - SPECIFIC HUMIDITY > 70% @ 800, 500 & 300 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_008'                                                    # Configuration string
    p['script'] = 'gfs_sphcld_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws200s_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 200 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_009'                                                    # Configuration string
    p['script'] = 'gfs_wsd200_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws500s_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 500 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_010'                                                    # Configuration string
    p['script'] = 'gfs_wsd500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws700s_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 700 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_011'                                                    # Configuration string
    p['script'] = 'gfs_wsd700_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws850s_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 850 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_012'                                                    # Configuration string
    p['script'] = 'gfs_wsd850_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcpts_00z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PSML / WIND 10 m / CLOUDS / PREC / THICKNESS (500-1000 hPa)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_013'                                                    # Configuration string
    p['script'] = 'gfs_pwcpth_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GFS MODEL 0.5 DEGREE - SOUTH AMERICA - 12Z RUN (SET AS TRUE ONLY SAM OR ONLY CRB!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_2mtems_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - 2 M TEMPERATURE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_001'                                                    # Configuration string
    p['script'] = 'gfs_2mtemp_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_accprs_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - ACCUMULATED PRECIPITACION
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_002'                                                    # Configuration string
    p['script'] = 'gfs_accpre_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_prtmss_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PRESSION REDUCED TO MEAN SEA LEVEL
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_003'                                                    # Configuration string
    p['script'] = 'gfs_prtmsl_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gdinds_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - GALVEZ DAVISON INDEX
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_004'                                                    # Configuration string
    p['script'] = 'gfs_gdindx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gh500s_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - RELATIVE VORTICITY AND GEOPOTENTIAL HEIGHT 500 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_005'                                                    # Configuration string
    p['script'] = 'gfs_ghv500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_psgwrs_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PSML + GEOP. DIF. (1000-850 hPa) + WINDS (925 hPa) + MEAN RH (1000~400 hPa)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_006'                                                    # Configuration string
    p['script'] = 'gfs_psgwrh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcaps_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PRECIPITABLE WATER & CAPE
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_007'                                                    # Configuration string
    p['script'] = 'gfs_pwcape_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_sphcls_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - SPECIFIC HUMIDITY > 70% @ 800, 500 & 300 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_008'                                                    # Configuration string
    p['script'] = 'gfs_sphcld_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws200s_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 200 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_009'                                                    # Configuration string
    p['script'] = 'gfs_wsd200_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws500s_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 500 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_010'                                                    # Configuration string
    p['script'] = 'gfs_wsd500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws700s_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 700 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_011'                                                    # Configuration string
    p['script'] = 'gfs_wsd700_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws850s_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - WIND SPEED AND DIRECTION - 850 hPa
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_012'                                                    # Configuration string
    p['script'] = 'gfs_wsd850_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcpts_12z' # GFS MODEL 0.5 DEGREE - SOUTH AMERICA - PSML / WIND 10 m / CLOUDS / PREC / THICKNESS (500-1000 hPa)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.sam.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_013'                                                    # Configuration string
    p['script'] = 'gfs_pwcpth_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)

#######################################################################################################
# GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - 00Z RUN (SET AS TRUE ONLY SAM OR ONLY CRB!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_2mtemc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - 2 M TEMPERATURE
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_001'                                                    # Configuration string
    p['script'] = 'gfs_2mtemp_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_accprc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - ACCUMULATED PRECIPITACION
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_002'                                                    # Configuration string
    p['script'] = 'gfs_accpre_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_prtmsc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PRESSION REDUCED TO MEAN SEA LEVEL
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_003'                                                    # Configuration string
    p['script'] = 'gfs_prtmsl_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gdindc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - GALVEZ DAVISON INDEX
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_004'                                                    # Configuration string
    p['script'] = 'gfs_gdindx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gh500c_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - RELATIVE VORTICITY AND GEOPOTENTIAL HEIGHT 500 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_005'                                                    # Configuration string
    p['script'] = 'gfs_ghv500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_psgwrc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PSML + GEOP. DIF. (1000-850 hPa) + WINDS (925 hPa) + MEAN RH (1000~400 hPa)
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_006'                                                    # Configuration string
    p['script'] = 'gfs_psgwrh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcapc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PRECIPITABLE WATER & CAPE
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_007'                                                    # Configuration string
    p['script'] = 'gfs_pwcape_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_sphclc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - SPECIFIC HUMIDITY > 70% @ 800, 500 & 300 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_008'                                                    # Configuration string
    p['script'] = 'gfs_sphcld_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws200c_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 200 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_009'                                                    # Configuration string
    p['script'] = 'gfs_wsd200_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws500c_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 500 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_010'                                                    # Configuration string
    p['script'] = 'gfs_wsd500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws700c_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 700 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_011'                                                    # Configuration string
    p['script'] = 'gfs_wsd700_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws850c_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 850 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_012'                                                    # Configuration string
    p['script'] = 'gfs_wsd850_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcptc_00z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PSML / WIND 10 m / CLOUDS / PREC / THICKNESS (500-1000 hPa)
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t00z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_013'                                                    # Configuration string
    p['script'] = 'gfs_pwcpth_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - 12Z RUN (SET AS TRUE ONLY SAM OR ONLY CRB!)
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_2mtemc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - 2 M TEMPERATURE
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_001'                                                    # Configuration string
    p['script'] = 'gfs_2mtemp_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_accprc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - ACCUMULATED PRECIPITACION
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_002'                                                    # Configuration string
    p['script'] = 'gfs_accpre_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_prtmsc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PRESSION REDUCED TO MEAN SEA LEVEL
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_003'                                                    # Configuration string
    p['script'] = 'gfs_prtmsl_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gdindc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - GALVEZ DAVISON INDEX
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_004'                                                    # Configuration string
    p['script'] = 'gfs_gdindx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_gh500c_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - RELATIVE VORTICITY AND GEOPOTENTIAL HEIGHT 500 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_005'                                                    # Configuration string
    p['script'] = 'gfs_ghv500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_psgwrc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PSML + GEOP. DIF. (1000-850 hPa) + WINDS (925 hPa) + MEAN RH (1000~400 hPa)
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_006'                                                    # Configuration string
    p['script'] = 'gfs_psgwrh_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcapc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PRECIPITABLE WATER & CAPE
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_007'                                                    # Configuration string
    p['script'] = 'gfs_pwcape_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_sphclc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - SPECIFIC HUMIDITY > 70% @ 800, 500 & 300 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_008'                                                    # Configuration string
    p['script'] = 'gfs_sphcld_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws200c_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 200 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_009'                                                    # Configuration string
    p['script'] = 'gfs_wsd200_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws500c_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 500 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_010'                                                    # Configuration string
    p['script'] = 'gfs_wsd500_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws700c_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 700 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_011'                                                    # Configuration string
    p['script'] = 'gfs_wsd700_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_ws850c_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - WIND SPEED AND DIRECTION - 850 hPa
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-119.0, -1.0, -42.0, 37.0]# Max:[-119.0,-1.0,-42.0,37.0] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_012'                                                    # Configuration string
    p['script'] = 'gfs_wsd850_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'gfs_pwcptc_12z' # GFS MODEL 0.5 DEGREE - CENTRAL AMERICA + CARIBBEAN - PSML / WIND 10 m / CLOUDS / PREC / THICKNESS (500-1000 hPa)
    p['enabled'] = False
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'MARN-El Salvador/'                         # Folder where the data is found
    p['filename pattern'] = 'gfs.crb.t12z.f120'                                       # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-88.0, -60.0, -30.0, 8.00]# Max:[-88.0,-60.0,-30.0,8.00] # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_013'                                                    # Configuration string
    p['script'] = 'gfs_pwcpth_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# FORECAST CHARTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'idk_samqpf_sec' # QUANTITATIVE PRECIP. FORECASTS FOR DAYS 1-6 (SOUTH AMERICA)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'RANET/'                                    # Folder where the data is found
    p['filename pattern'] = 'd6.gif'                                                  # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'idk_idkqpf_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'idk_crbqpf_sec' # QUANTITATIVE PRECIP. FORECASTS FOR DAYS 1-6 (CENTRAL AMERICA AND CARIBBEAN)
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'RANET/'                                    # Folder where the data is found
    p['filename pattern'] = 'crb3_east.gif'                                           # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'idk_idkqpf_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# ISCS - INTERNATIONAL SERVICES AND COMMUNICATION SYSTEMS - SUGGESTION: PUT IN A DEDICATED PROCESS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_atrodn_sec' # ISCS-ANLZ-CLIMATE - NORTH ATLANTIC AREA
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-ANLZ-CLIMATE/'                        # Folder where the data is found
    p['filename pattern'] = '*T_AXNT*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_atrodn_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_atrode_sec' # ISCS-ANLZ-CLIMATE - EASTERN PACIFIC AREA
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-ANLZ-CLIMATE/'                        # Folder where the data is found
    p['filename pattern'] = '*T_AXPZ*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_atrode_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_ssynop_sec' # ISCS-SURFACE - SYNOP
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-SURFACE/'                             # Folder where the data is found
    p['filename pattern'] = '*T_SMBO*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_ssynop_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_sbuoys_sec' # ISCS-SURFACE - DRIFTING BUOYS
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-SURFACE/'                             # Folder where the data is found
    p['filename pattern'] = '*T_SSVX*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_sbuoys_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_smetar_sec' # ISCS-SURFACE - METAR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-SURFACE/'                             # Folder where the data is found
    p['filename pattern'] = '*T_SAAG*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_smetar_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_sspeci_sec' # ISCS-SURFACE - SPECI
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-SURFACE/'                             # Folder where the data is found
    p['filename pattern'] = '*T_SPBZ*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_sspeci_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_ftafms_sec' # ISCS-FCAST - TAF
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-FCAST/'                               # Folder where the data is found
    p['filename pattern'] = '*T_FCAJ*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_ftafms_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_wsigme_sec' # ISCS-WARN - SIGMETS
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-WARN/'                                # Folder where the data is found
    p['filename pattern'] = '*T_WSAG*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                         # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_wsigme_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_wairme_sec' # ISCS-WARN - AIRMETS
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-WARN/'                                # Folder where the data is found
    p['filename pattern'] = '*T_WABZ*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_wairme_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_fvolca_sec' # ISCS-FCAST - VOLCANIC ASH
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-FCAST/'                               # Folder where the data is found
    p['filename pattern'] = '*T_FVAG*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_fvolca_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_wtsuna_sec' # ISCS-WARN - TSUNAMI
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-WARN/'                                # Folder where the data is found
    p['filename pattern'] = '*T_WE*'                                                  # Unique string on the file name
    p['max files'] = 10                                                        # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_wtsuna_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'ics_wvolca_sec' # ISCS-WARN - VOLCANIC ASH
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'ISCS-WARN/'                                # Folder where the data is found
    p['filename pattern'] = '*T_WVEQ*'                                                # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['resolution'] =  0 # Max Res.: N/A                                         # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'isc_wvolca_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# ALWP - ADVECTED LAYERED PRECIPITABLE WATER
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_alpw01_sec' # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (Sfc - 850 mb)
    p['enabled'] = True
    p['cicle'] = 1                                                             # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIRA/'                                         # Folder where the data is found
    p['filename pattern'] = '*ADVECT_COMPOSITE*'                                          # Unique string on the file name
    p['max files'] = 1                                                             # Max number of historical files to be processed
    p['extent'] = [-85.0, -55.0, -24.9, 12.6]# Max:[-180.0,-71.0,180.0,71.0]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8 # Max Res.: N/A                                             # Final plot resolution
    p['interval'] = ''                                                            # Processing interval
    p['config'] = '_850'                                                        # Configuration string
    p['script'] = 'jps_alpwat_single_sec.py'  # Script to activate
    p['output'] = output_dir                                   # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_alpw02_sec' # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (850 - 700 mb)
    p['enabled'] = True
    p['cicle'] = 1                                                             # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIRA/'                                         # Folder where the data is found
    p['filename pattern'] = '*ADVECT_COMPOSITE*'                                          # Unique string on the file name
    p['max files'] = 1                                                             # Max number of historical files to be processed
    p['extent'] = [-85.0, -55.0, -24.9, 12.6]# Max:[-180.0,-71.0,180.0,71.0]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8 # Max Res.: N/A                                             # Final plot resolution
    p['interval'] = ''                                                            # Processing interval
    p['config'] = '_700'                                                        # Configuration string
    p['script'] = 'jps_alpwat_single_sec.py'  # Script to activate
    p['output'] = output_dir                                   # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_alpw03_sec' # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (700 - 500 mb)
    p['enabled'] = True
    p['cicle'] = 1                                                             # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIRA/'                                         # Folder where the data is found
    p['filename pattern'] = '*ADVECT_COMPOSITE*'                                          # Unique string on the file name
    p['max files'] = 1                                                             # Max number of historical files to be processed
    p['extent'] = [-85.0, -55.0, -24.9, 12.6]# Max:[-180.0,-71.0,180.0,71.0]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8 # Max Res.: N/A                                             # Final plot resolution
    p['interval'] = ''                                                            # Processing interval
    p['config'] = '_500'                                                        # Configuration string
    p['script'] = 'jps_alpwat_single_sec.py'  # Script to activate
    p['output'] = output_dir                                   # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_alpw04_sec' # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (500 - 300 mb)
    p['enabled'] = True
    p['cicle'] = 1                                                             # Process cicle for this product
    p['input'] = CONFIG['input'] + 'CIRA/'                                         # Folder where the data is found
    p['filename pattern'] = '*ADVECT_COMPOSITE*'                                          # Unique string on the file name
    p['max files'] = 1                                                             # Max number of historical files to be processed
    p['extent'] = [-85.0, -55.0, -24.9, 12.6]# Max:[-180.0,-71.0,180.0,71.0]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  8 # Max Res.: N/A                                             # Final plot resolution
    p['interval'] = ''                                                            # Processing interval
    p['config'] = '_300'                                                        # Configuration string
    p['script'] = 'jps_alpwat_single_sec.py'  # Script to activate
    p['output'] = output_dir                                   # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# SST - NOAA CORAL REEF WATCH DAILY 5km
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_sstcor_sec' # SST - NOAA CORAL REEF WATCH DAILY 5km - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'NOAA-NESDIS/'                              # Folder where the data is found
    p['filename pattern'] = 'coraltemp*'                                              # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -70.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  16 # Max Res.: 5 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'sst_coralre_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# SST ANOMALY - NOAA CORAL REEF WATCH DAILY 5km
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_sstano_sec' # SST ANOMALY - NOAA CORAL REEF WATCH DAILY 5km - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'NOAA-NESDIS/'                              # Folder where the data is found
    p['filename pattern'] = 'ct5km_ssta*'                                             # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -70.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  16 # Max Res.: 5 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'sst_anomaly_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# 7-DAY SST TREND - NOAA CORAL REEF WATCH DAILY 5km
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'mul_ssttre_sec' # 7-DAY SST TREND - NOAA CORAL REEF WATCH DAILY 5km - USER SECTOR
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'NOAA-NESDIS/'                              # Folder where the data is found
    p['filename pattern'] = 'ct5km_sst-trend-7d*'                                     # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-180.0, -70.0, 180.0, 80.0]                              # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  16 # Max Res.: 5 km                                       # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'sst_7dtrend_sec.py'    # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# NOAA-20 - CHLOROPHYLL-A CONCENTRATION
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgvy_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION VY
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*VY*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120.0, 0.0, -60.0, 44.0]# Max:[-120.0, 0.0, -60.0, 44.0]# [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgwy_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION WY
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*WY*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-60.0, 0.0, 0.0, 44.0]# Max:[-60.0, 0.0, 0.0, 44.0]      # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgvx_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION VX
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*VX*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120, -44.0, -60.0, 0.0]# Max:[-120.0, -44.0, -60.0, 0.0]# [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgwx_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION WX
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*WX*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-60.0, -44.0, -0.0, 0.0]# Max:[-60.0, -44.0, -0.0, 0.0]  # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgvw_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION VW
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*VW*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-120, -89.0, -60.0, -44.0]# Max:[-120, -8.09, -60.0, -44]# [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ocrgwu_sec' # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION WU
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/OC/'                       # Folder where the data is found
    p['filename pattern'] = 'VR1VCW_*WU*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-60.0, -89.0, 0.0, -44.0]# Max:[-60.0, -89.0, 0.0, -44.0]# [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 0.750 km                                    # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_oceanc_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------

#######################################################################################################
# JPSS - VIIRS VEGETATION PRODUCTS
#######################################################################################################

#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_gblgvf_sec' # JPSS - GREEN VEGETATION FRACTION - GLOBAL - 4km
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/VEGETATION/'               # Folder where the data is found
    p['filename pattern'] = 'GVF-WKL-GLB*.nc'                                         # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-150.0, -60.0, -20.0, 70.0]# Max:[-180, -80, 180, 80]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 4 km                                        # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = ''                                                        # Configuration string
    p['script'] = 'jps_gblgvf_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ndvita_sec' # JPSS - NORMALIZED DIFFERENCE VEGETATION INDEX AT TOP OF ATMOSPHERE (TOA) - GLOBAL - 4km
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/VEGETATION/'               # Folder where the data is found
    p['filename pattern'] = 'VI-WKL-GLB*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-150.0, -60.0, -20.0, 70.0]# Max:[-180, -80, 180, 80]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 4 km                                        # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_NDA'                                                    # Configuration string
    p['script'] = 'jps_vegidx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_ndvitc_sec' # JPSS - NORMALIZED DIFFERENCE VEGETATION INDEX AT TOP OF CANOPY (TOC) - GLOBAL - 4km
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/VEGETATION/'               # Folder where the data is found
    p['filename pattern'] = 'VI-WKL-GLB*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-150.0, -60.0, -20.0, 70.0]# Max:[-180, -80, 180, 80]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 4 km                                        # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_NDC'                                                    # Configuration string
    p['script'] = 'jps_vegidx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    p = {}
    p['name'] = 'jps_evitoc_sec' # JPSS - ENHANCED VEGETATION INDEX AT TOP OF CANOPY (TOC) - GLOBAL - 4km
    p['enabled'] = True
    p['cicle'] = 1                                                         # Process cicle for this product
    p['input'] = CONFIG['input'] + 'JPSS/PRODUCTS/VEGETATION/'               # Folder where the data is found
    p['filename pattern'] = 'VI-WKL-GLB*.nc'                                          # Unique string on the file name
    p['max files'] = 1                                                         # Max number of historical files to be processed
    p['extent'] = [-150.0, -60.0, -20.0, 70.0]# Max:[-180, -80, 180, 80]    # [min_lon, min_lat, max_lon, max_lat]
    p['resolution'] =  4 # Max Res.: 4 km                                        # Final plot resolution
    p['interval'] = ''                                                        # Processing interval
    p['config'] = '_EVC'                                                    # Configuration string
    p['script'] = 'jps_vegidx_sec.py'     # Script to activate
    p['output'] = output_dir                               # Output folder
    resultado.append(p)
#------------------------------------------------------------------------------------------------------
    return resultado # Fim da função Produtos

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
