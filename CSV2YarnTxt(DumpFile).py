import os
import re
import csv

def csv2yarntxt(yarn_file, out_yarn_txt_path):
    csv_file = yarn_file.split(".")[0] + ".yarn.csv"
    
    def check_yarntag():
        global dict1
        
        yarn_tag_set = set()
        with open(yarn_file, 'r', encoding="UTF-8") as yarnFile:
            for line in yarnFile:
                if("#line:" in line):
                    line = line.rstrip()
                    yarn_tag = re.search(r'line:.*$', line).group()
                    yarn_tag_set.add(yarn_tag)
        if not yarn_tag_set:
            #print(yarn_file + " 文件无须替换键值, 跳过")
            return None
        #print(yarn_tag_set)
        
        with open(rootPath + '/' + modCSVPath + csv_file, 'r', encoding="UTF-8") as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            dict1 = {row[0]: row[-1] for row in csv_reader}
        
        csv_key_set = set(dict1.keys())
        
        set_add = csv_key_set | yarn_tag_set
        set_common = csv_key_set & yarn_tag_set
        if(set_add == set_common):
            return True
        else:
            return False
        
    if (check_yarntag() == False):
        print(csv_file + " 文件键值不匹配，请检查!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return
    if check_yarntag() is None:
        print(yarn_file + " 文件无须替换键值, 跳过")
        return
    print(csv_file + " 文件键值匹配，开始替换")


    with open(yarn_file, 'r', encoding="UTF-8") as yarnFile, open(out_yarn_txt_path + yarn_file, 'w', encoding="UTF-8") as modYarnFile:
        for line in yarnFile:
            line_is_marched = False
            if("#line:" in line):
                line_is_marched = True
                line = line.rstrip()
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

#csv2yarntxt("AngusConstellations.yarn.txt")



INUAFFOLDER = "Unity_Assets_Files"
OUTUAFFOLDER = "output/Unity_Assets_Files"
MODCSVFOLDER = "output/modCSV"



modCSVPath = MODCSVFOLDER + '/'
inUAFPath = INUAFFOLDER + '/'
outUAFPath = OUTUAFFOLDER + '/'
rootPath = os.getcwd()

os.chdir(INUAFFOLDER)
inUAFFolder = os.listdir(os.getcwd())
for assetItem in inUAFFolder:
    if not os.path.isdir(assetItem):
        continue
    os.chdir(assetItem)
    print("当前文件夹：" + assetItem)
    

    
    
    
    assetFolder = os.listdir(os.getcwd())
    for TxtItem  in assetFolder:
        if(".yarn.txt" not in TxtItem):
            continue
        
        if not os.path.exists(rootPath + '/' + outUAFPath + assetItem):
            os.makedirs(rootPath + '/' + outUAFPath + assetItem)
            #print("找到 Yarn Txt，创建对应输出目录")
        out_yarn_txt_path = rootPath + '/' + outUAFPath + assetItem + '/'
        csv2yarntxt(TxtItem, out_yarn_txt_path)
        #print(TxtItem)
        #shutil.move(csvFile, vanillaOutPath + csvFile)
        
    os.chdir(rootPath + '/' + inUAFPath)

