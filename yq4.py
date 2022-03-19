import os
import sys
from pypinyin import lazy_pinyin


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


# RETURN PINYIN
def pinyin(string):
    return ''.join(lazy_pinyin(string))


# SORT FUNCTION
# lis: list of lists
#      e.g.: lis = [ ['prov1', 100], ['prov2', 120], ..., ['prov_n', 40] ]
#        or: lis = [ ['city1', 20], ['city2', 40], ..., ['city_n', 43] ]
# FIRST SORT BY item[1] (number)
# IF item[1] EQUAL THEN SORT BY item[0] (prov/city name)
def mysort(lis):  # BUBBLE SORT
    n = len(lis)
    temp = None
    for i in range(0, n):
        for j in range(i, n):
            # 后一项的值大于前一项，则交换（按值降序排列），或：
            # 两项的值相同，看省份（或城市）的名字，
            # 后一项小于前一项，则交换（按名称升序排列）
            if (lis[i][1] < lis[j][1]) or \
               (lis[i][1] == lis[j][1] and \
                pinyin(lis[i][0]) > pinyin(lis[j][0])):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    return lis


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

prov_count = []
# prov_count = [ ['浙江省', 1205], ['江西省', 934], ..., ['贵州省', 146] ]
for prov in dic.keys():
    total_count = 0
    for item in dic[prov]:
        num = item[1]  # city = item[0], num = item[1]
        total_count += num
    prov_count.append([prov, total_count])


# OUTPUT
if PROV is None:  # PROV not specified in parameters
    sorted_prov_count = mysort(prov_count)
    for item in sorted_prov_count:
        prov, total = item[0], item[1]
        print(f'{prov}\t{total}')

        sorted_cities = mysort(dic[prov])
        for city_information in sorted_cities:
            city, num = city_information[0], city_information[1]
            print(f'{city}\t{num}')
        print()
else:  # PROV specified
    total = None
    for item in prov_count:
        if item[0] == PROV:
            total = item[1]  # get the total number of PROV
            break
    print(f'{PROV}\t{total}')

    sorted_cities = mysort(dic[PROV])
    for city_information in sorted_cities:
        city, num = city_information[0], city_information[1]
        print(f'{city}\t{num}')
    print()
