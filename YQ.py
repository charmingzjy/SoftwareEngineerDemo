from pypinyin import lazy_pinyin
import os
class YQ_Prov(object):
    def __init__(self, prov:str, total_count:int, cities:list):
        self.prov = prov
        self.total_count = total_count
        self.cities = cities

    def _py(self, string):
        return ''.join(lazy_pinyin(string))

    def sort(self):  # sort cities
        n = len(self.cities)
        temp = None
        for i in range(0, n):
            for j in range(i, n):
                if (self.cities[i][1] < self.cities[j][1]) or \
                   (self.cities[i][1] == self.cities[j][1] and \
                    self._py(self.cities[i][0]) > self._py(self.cities[j][0])):
                    temp = self.cities[i]
                    self.cities[i] = self.cities[j]
                    self.cities[j] = temp
                    

    def print(self):
        print(f'{self.prov}\t{self.total_count}')
        for city_information in self.cities:
            city, num = city_information[0], city_information[1]
            print(f'{city}\t{num}')
        print()


class YQ_Data(object):
    def __init__(self, input_file):
        self.provs = []

        if os.path.isfile(input_file):  # if input_file exist:
            dic = {}
            with open(input_file, 'r') as f:
                for line in f.readlines():
                    lis = line.split()
                    province, city, num = lis[0], lis[1], int(lis[2])
                    if num != 0:
                        if province not in dic:
                            dic[province] = []
                            dic[province].append([city, num])
                        else:
                            dic[province].append([city, num])
        
            prov_count_dic = {}
            for prov in dic.keys():
                total_count = 0
                for item in dic[prov]:
                    num = item[1]
                    total_count += num
                prov_count_dic[prov] = total_count
        
            for prov in dic.keys():
                yq_prov = YQ_Prov(prov=prov,
                                  total_count=prov_count_dic[prov],
                                  cities=dic[prov])
                self.provs.append(yq_prov)

        else:  # input_file not exist:
            print('INPUT FILE not exist!')
            pass


    def _py(self, string):
        return ''.join(lazy_pinyin(string))

    def sort(self):  # sort YQ_Provs
        n = len(self.provs)
        temp = None
        for i in range(0, n):
            for j in range(i, n):
                if (self.provs[i].total_count < self.provs[j].total_count) or \
                   (self.provs[i].total_count == self.provs[j].total_count and \
                    self._py(self.provs[i].prov) > self._py(self.provs[j].prov)):
                    temp = self.provs[i]
                    self.provs[i] = self.provs[j]
                    self.provs[j] = temp

    def get_data(self, prov=None):
        if not prov:
            return None
        else:
            for item in self.provs:
                if item.prov == prov:
                    return item
                    break
            print('PROVINCE not found!')  # prov not found
            return None

    def print(self, sorted=True, specified_prov=None):
        if not specified_prov:
            if sorted: self.sort()
            for item in self.provs:
                if sorted:
                    item.sort()
            
            for prov_data in self.provs:
                print(f'{prov_data.prov}\t{prov_data.total_count}')
                for city_information in prov_data.cities:
                    city, num = city_information[0], city_information[1]
                    print(f'{city}\t{num}')
                print()
        
        else:
            prov_data = self.get_data(prov=specified_prov)
            if sorted:
                prov_data.sort()
            print(f'{prov_data.prov}\t{prov_data.total_count}')
            for city_information in prov_data.cities:
                city, num = city_information[0], city_information[1]
                print(f'{city}\t{num}')
            print()
