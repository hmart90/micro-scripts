import re

FILENAME = '/home/marthalasz/Development/data/CARPATGRID_TA/CARPATGRID_TA_Y.ser'
TARGET_FILENAME = 'output.txt'

with open(TARGET_FILENAME, 'w') as target_file:
    target_file.write('year;id;value\n')

i = 0
with open(FILENAME) as file:
    for line in file:
        if i == 0:
            header = re.sub(' +', ' ', line)
            header = re.sub('\n', '', header).strip().split(" ")
        else:
            data_line = re.sub(' +', ' ', line)
            data_line = re.sub('\n', '', data_line).strip().split(" ")
            year = data_line[0]
            data_list = data_line[1:]
            with open(TARGET_FILENAME, 'a') as target_file:
                for n in range(0, len(data_list)):
                    target_file.write(year + ';' + header[n] + ';' + data_list[n] + '\n')
        i = i + 1
