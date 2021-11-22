import re

FILENAME = '/home/hduser/Development/data/CARPATGRID_TA/PredtandfilaGrid.dat'
TARGET_FILENAME = 'grid.csv'

with open(TARGET_FILENAME, 'w') as target_file:
    with open(FILENAME) as file:
        for line in file:
            data_line = re.sub(' +', ' ', line).strip()
            data_line = re.sub(' ', ';', data_line)
            target_file.write(data_line + '\n')