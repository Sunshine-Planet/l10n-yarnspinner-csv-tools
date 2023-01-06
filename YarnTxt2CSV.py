import re
import os
import csv

def yarntxt2csv(yarn_file):
    csv_file = yarn_file.split(".")[0] + ".yarn.csv.vanilla"
    #with open(yarn_file, 'r', encoding="UTF-8") as yarnFile, open(csv_file, 'w', encoding="UTF-8") as csvFile:
    
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
                #print(vanilla_line)
                line_list.append(["line:" + yarn_tag_withouthead, vanilla_line])
                #print(line_list)
                
    if not line_list:
        print(yarn_file + " 无需替换!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return False
    
    with open(csv_file, 'w', encoding="UTF-8", newline='') as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerows(line_list)
    return True

currentFolder = os.listdir(os.getcwd())
for item in currentFolder:
    if(os.path.isdir(item)):
        continue
    #print(os.path.basename(__file__))
    if(item == os.path.basename(__file__)):
        continue
    if(".py" in item):
        continue
    if(".yarn.txt" in item):
        print("找到 Yarn Txt 格式后缀文件：" + item)
        yarntxt2csv(item)