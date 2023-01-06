import re
import os
import shutil
import time
import csv


def yarntxt2csv(yarn_file):
    csv_file = yarn_file.split(".")[0] + ".yarn.csv.vanilla"
    with open(yarn_file, 'r', encoding="UTF-8") as yarnFile:
        line_list = []
        for line in yarnFile:
            if("#line:" in line):
                line = line.rstrip()
                #print(line)
                yarn_tag = re.search(r'#line:.*$', line).group()
                yarn_tag_withouthead = re.sub(r'^#line:', "", yarn_tag)
                vanilla_line = re.sub(yarn_tag, "", line)
                vanilla_line = vanilla_line.rstrip()
                #print(yarn_tag)
                #print(vanilla_line)
                line_list.append(["line:" + yarn_tag_withouthead, vanilla_line])
                
                #csv_writer = csv.writer(csvFile)
                #csv_writer.writerows(['line:' + yarn_tag_withouthead, vanilla_line])
    if not line_list:
        print(yarn_file + " 无需替换!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return False
        
    with open(csv_file, 'w', encoding="UTF-8", newline='') as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerows(line_list)
        print(yarn_file + " 导出完成")
    return True


UAFFOLDER = "Unity_Assets_Files"
rootPath = os.getcwd()
vanillaOutPath = rootPath + '/' + "output/vanillaCSV" + '/'
if not os.path.exists("output/vanillaCSV"):
    os.makedirs("output/vanillaCSV")

if not os.path.exists(UAFFOLDER):
    print("请把 UnityEX 导出的 Unity_Assets_Files 文件夹移动到本目录下")
    time.sleep(3)
    exit()
else:
    os.chdir(UAFFOLDER)
    UAFFolder = os.listdir(os.getcwd())
    

for assetItem in UAFFolder:
    if not os.path.isdir(assetItem):
        continue
    os.chdir(assetItem)
    assetFolder = os.listdir(os.getcwd())
    for TxtItem  in assetFolder:
        if(".yarn.txt" not in TxtItem):
            continue
        #print(TxtItem)
        if not yarntxt2csv(TxtItem):
            continue
        
        csvFile = TxtItem.split('.')[0] + '.'+ TxtItem.split('.')[1] + ".csv.vanilla"
        shutil.move(csvFile, vanillaOutPath + csvFile)
        
    os.chdir(rootPath + '/' + UAFFOLDER)