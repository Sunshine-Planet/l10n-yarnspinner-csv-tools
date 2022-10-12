import os
import re
import csv

def csv2yarntxt(yarn_file):
    csv_file = yarn_file.split(".")[0] + ".yarn.csv"
    
    MOGYARNTXTFOLDER = "output/modYarnTxt"
    mod_yarn_txt_path = MOGYARNTXTFOLDER + '/'
    
    
    if not os.path.exists(mod_yarn_txt_path):
        os.makedirs(mod_yarn_txt_path)
    
    def check_yarntag():
        global dict1
        
        
        yarn_tag_set = set()
        with open(yarn_file, 'r', encoding="UTF-8") as yarnFile:
            for line in yarnFile:
                if("#line:" in line):
                    line = line.rstrip()
                    yarn_tag = re.search(r'line:.*$', line).group()
                    yarn_tag_set.add(yarn_tag)
        #print(yarn_tag_set)
        if not yarn_tag_set:
            print(yarn_file + "文件无须替换键值!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return False
        
        with open(csv_file, 'r', encoding="UTF-8") as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            dict1 = {row[0]: row[-1] for row in csv_reader}
            #print(dict1)
        
        csv_key_set = set(dict1.keys())
        
        set_add = csv_key_set | yarn_tag_set
        set_common = csv_key_set & yarn_tag_set
        if(set_add == set_common):
            return True
        else:
            return False
        
    if not check_yarntag():
        print(csv_file + " 文件键值不匹配，请检查")
        return
    else:
        print(csv_file + " 文件键值匹配，开始替换")


    with open(yarn_file, 'r', encoding="UTF-8") as yarnFile, open(mod_yarn_txt_path + yarn_file, 'w', encoding="UTF-8") as modYarnFile:
        for line in yarnFile:
            line_is_marched = False
            if("#line:" in line):
                line_is_marched = True
                #line = line.rstrip()
                yarn_tag = re.search(r'line:.*$', line).group()
                #print(yarn_tag)
            if(line_is_marched):
                line = dict1[yarn_tag] + ' ' + "#" + yarn_tag + '\n'
                #print(line)
                modYarnFile.write(line)
                line_is_marched = False
                continue
            #print(line)
            modYarnFile.write(line)



currentFolder = os.listdir(os.getcwd())
for item in currentFolder:
    if(os.path.isdir(item)):
        continue
    #print(os.path.basename(__file__))
    if(item == os.path.basename(__file__)):
        continue
    if(".py" in item):
        continue
    if(' ' in item):
        continue
    if(re.match(r'.*\.yarn\.txt$', item) is not None):
        print("找到 YarnTxt 格式后缀文件：" + item + " 开始查找匹配 .csv 文件")
        csv2yarntxt(item)