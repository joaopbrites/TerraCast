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
import datetime                       # Basic Date and Time types
import pathlib                        # Object-oriented filesystem paths
import glob                           # Unix style pathname pattern expansion
import os                             # Miscellaneous operating system interfaces
from pathlib import Path
from os.path import dirname, abspath
import subprocess                     # Subprocess management (replaces os.system)
import sys                            # System-specific parameters and functions
import logging

#######################################################################################################
# FILE PROCESSING AND LOG FUNCTION
#######################################################################################################




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
    # Logger for this module (error/info logging)
    logger = logging.getLogger(f'processment.{__name__}')
    logger.info("Process product inicializado")
    terracast_dir = CONFIG['src_dir']


    # Counter to track how many products have been processed
    prod_count = 0

    # ------------------------------------------------------------------
    # 1. Build the list of candidate files (gnc_files)
    # ------------------------------------------------------------------
    gnc_files = []

    input_pattern = product['input'] + product['filename pattern']
    input_file_names = sorted(glob.glob(input_pattern))

    # Fixed-name files that need modification-time suffix
    FIXED_NAME_FILES = {
        'gfs.sam.t00z.f120', 'gfs.sam.t12z.f120',
        'gfs.crb.t00z.f120', 'gfs.crb.t12z.f120',
        'd6.gif', 'crb3_east.gif',
    }

    for filename in input_file_names:
        if product['filename pattern'] in FIXED_NAME_FILES:
            mtime = datetime.datetime.fromtimestamp(
                pathlib.Path(filename).stat().st_mtime
            ).strftime('%Y%m%d%H%M%S')
            gnc_files.append(os.path.normpath(filename + product['config'] + '_c' + mtime))
        else:
            gnc_files.append(os.path.normpath(filename + product['config']))

    if not gnc_files:
        logger.warning(f"No files found for product '{product['name']}' with pattern: {input_pattern}")
        return

    # Keep only the most recent N files
    gnc_files = gnc_files[-product['max files']:]

    # ------------------------------------------------------------------
    # 2. Read the processed-files log (gnc log)
    # ------------------------------------------------------------------
    gnc_log_path = terracast_dir / 'logs' / 'files' / f"gnc_log_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
    gnc_log_path_legacy = terracast_dir / 'Logs' / f"gnc_log_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"

    # Create the log file if it doesn't exist
    gnc_log_path.parent.mkdir(parents=True, exist_ok=True)
    gnc_log_path.touch(exist_ok=True)

    gnc_log_path_legacy.parent.mkdir(parents=True, exist_ok=True)
    gnc_log_path_legacy.touch(exist_ok=True)

    # Read already-processed file names
    with open(gnc_log_path) as f:
        processed_files = [line.strip() for line in f.readlines()]
    with open(gnc_log_path_legacy) as f:
        processed_files = [line.strip() for line in f.readlines()]
    # ------------------------------------------------------------------
    # 3. Process each new file via subprocess
    # ------------------------------------------------------------------
    script_path = terracast_dir / 'scripts' / product['script']
    extent = product.get('extent', [0.0, 0.0, 0.0, 0.0])
    interval = product.get('interval', '')

    for data_file_name in gnc_files:
        if data_file_name in processed_files:
            continue

        print(f'Processing the following file: {data_file_name}\n')
        print(f'Script used: {script_path}\n')

        prod_count += 1

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
            CONFIG['output'],           # argv[8]: vis_dir
            interval,                   # argv[9]: interval
        ]

        print('Command used:\n', ' '.join(command))
        print('\n--- Script execution started ---\n')

        try:
            # Execute script with real-time output (no capture_output)
            # stdout/stderr will be shown directly in the terminal
            result = subprocess.run(
                command,
                check=True,             # Raise on non-zero exit code
                timeout=600,            # 10 min timeout (adjust as needed)
            )

            print('\n--- Script execution completed successfully ---\n')
            logger.info(f'Successfully processed: {data_file_name}')

        except subprocess.TimeoutExpired:
            logger.error(f'Timeout processing {data_file_name}')
            print(f'\nERROR: Script timeout after 600 seconds\n')

        except subprocess.CalledProcessError as e:
            logger.error(f'Script error for {data_file_name} (exit code {e.returncode})')
            print(f'\nERROR: Script returned non-zero exit code: {e.returncode}\n')

        except Exception as e:
            logger.error(f'Unexpected error processing {data_file_name}: {e}')
            print(f'\nERROR: {e}\n')

        print()
