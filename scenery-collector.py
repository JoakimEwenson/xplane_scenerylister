import os
import time
from os import path

# Output and backup file names
scenery_file = 'scenery_packs.ini'
backup_file = scenery_file + '.' + str(int(time.time()))
scenery_count = 0

# Set up default values to be printed at the top of the file
# If you have scenery libraries not found in the Custom Scenery-folder, add them below the empty '', line
default_list = [
    'I',
    '1000 Version',
    'SCENERY',
    '',
    # Add your extra libraries here using 'full directory path', format, example below
    #'SCENERY_PACK D:\Steam\steamapps\common\X-Plane 11\Resources\plugins\SAM\lib\SAM_Seasons/',
]

""" This function collects a list of folder names and iterates through them to create a new scenery_packs.ini file """
def new_scenery_packs():
    global scenery_count
    # Set up empty array for holding the folder names
    scenery_list = []
    try:
        for name in os.listdir("."):
            if os.path.isfile(name):
                continue
            scenery_list.append(name)
            scenery_count = len(scenery_list)
    except:
        print('Failed to fetch folder names.')

    # Iterate over the default and scenery folder lists and write results to new file
    try:
        with open(scenery_file, "w") as text_file:
            for line in default_list:
                print(line, file=text_file)
            for line in scenery_list:
                print(f'SCENERY_PACK Custom Scenery/{line}', file=text_file)
    except:
        print(f'Failed to build new {scenery_file} file.')

# Run the function if file is opened stand alone using 'python scenery-collector.py'
if __name__ == '__main__':
    # Check if scenery_packs.ini exists and if so, rename old version for backup before building a new version
    if path.exists(scenery_file):
        try:
            os.rename(scenery_file,backup_file)
            print(f'Old filed renamed {backup_file}')
        except:
            print('Failed to rename old file')
        
        try:
            new_scenery_packs()
            print(f'New {scenery_file} created with {scenery_count} entries.')
        except:
            print(f'Failed to build new {scenery_file} file.')
    else:
        try:
            new_scenery_packs()
        except:
            print('Failed to run build function.')
