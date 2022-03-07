def changefiles():
    filecontent = []
    with open("yq_in.txt","r") as f:    #打开文件yq_in.txt
        data = f.readlines()    #读取文件中的每行数据
        # print(data)
        for fline in data:  #循环读取文件中的每行数据
            filecontent.append(fline.split())   #将每行数据分割后再存入filecontent中
        # print(filecontent)
    with open("yq_out.txt","w") as f:  #写入文件yq_out.txt
        i = False   #i -->  按题目要求省份之间有空格存在，第一个省份前无空格
        province = ""
        for fline in filecontent:
            if fline[0] != province:    #如果读到的省份数据和之前的数据不同
                if i:   #如果i不为False --》 证明不是第一个出现的省份
                    f.write("\n")   #打印出空行
                i = True
                f.write(fline[0]+'\n')  #打印出新的省份
                province = fline[0]   #更新省份
                f.write(fline[1]+'\t'+fline[2]+'\n')    #打印出与省份相连接的城市与数量
            elif fline[2] != '0':    #排除所属的城市未有疫情出现，即人数为0的情况
                f.write(fline[1] + '\t' + fline[2] + '\n')
        f.write('\n')
        f.close()

if __name__ == '__main__':
    changefiles()



