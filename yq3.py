import os
import sys


# PARAMETERS
INPUT_DIR = None
OUTPUT_DIR = None
PROV = None

if len(sys.argv) < 2:  # len < 2, input_dir not specified
    sys.exit('ERROR: INPUT_DIR not specified.')
if len(sys.argv) < 3:  # len < 3, output_dir not specified    
    print('WARNING: OUTPUT_DIR not specified.\n')
    INPUT_DIR = sys.argv[1]
elif len(sys.argv) == 3:  # len == 3, PROV not specified
    INPUT_DIR, OUTPUT_DIR = sys.argv[1], sys.argv[2]
elif len(sys.argv) == 4:  # PROV specified
    INPUT_DIR, OUTPUT_DIR, PROV = sys.argv[1], sys.argv[2], sys.argv[3]


# OUTPUT TO CONSOLE AND LOG (IF OUTPUT_DIR SPECIFIED)
class Logger(object):
    def __init__(self):
        log_dir = OUTPUT_DIR
        self.terminal = sys.stdout
        self.log = open(log_dir, 'w')
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
if OUTPUT_DIR is not None:  # OUTPUT_DIR specified
    sys.stdout = Logger()


# MAIN FUNCTION
dic = {}
# dic = {
#     '浙江省': [ ['温州', 504], ['台州': 146], ..., ['湖州', 10] ], 
#     '江西省': [ ['九江', 118], ['南昌', 229], ..., ['赣江新区', 1] ], 
#     ..., 
#     '贵州省': [ ['遵义', 32], ['贵阳', 36], ..., ['黔西南州', 4] ]
# }
with open(INPUT_DIR, 'r') as f:
    for line in f.readlines():
        lis = line.split()
        province, city, num = lis[0], lis[1], int(lis[2])
        if num != 0:  # exclude num=0
            if province not in dic:
                dic[province] = []
                dic[province].append([city, num])
            else:
                dic[province].append([city, num])


# OUTPUT
if PROV is None:  # PROV not specified in parameters
    for prov in dic.keys():
        print(prov)
        for item in dic[prov]:
            city, num = item[0], item[1]
            print(f'{city}\t{num}')
        print()
else:  # PROV specified
    print(PROV)
    for item in dic[PROV]:
        city, num = item[0], item[1]
        print(f'{city}\t{num}')
    print()
