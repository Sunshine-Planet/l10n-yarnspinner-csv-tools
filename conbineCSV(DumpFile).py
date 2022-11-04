import os
import csv
import re

def conbine_csv(csv_file):
    vanilla_csv = csv_file + ".vanilla"
    
    def check_vanilla_file(vanilla_csv):
        vanilla_folder =  os.listdir(vanilla_out_path)
        vanilla_regex = re.compile(r'^' + vanilla_csv + '$')
        for item in vanilla_folder:
            if(os.path.isdir(item)):
                continue
            #print(os.path.basename(__file__))
            if(item == os.path.basename(__file__)):
                continue
            if(".py" in item):
                continue
            if(' ' in item):
                continue
            if (re.search(vanilla_regex, item) is not None):
                print("找到匹配 .csv.vanilla 文件, 开始替换")
                return True
        print("未找到匹配 .csv.vanilla 文件")
        return False

    if not check_vanilla_file(vanilla_csv):
        print("请检查" + vanilla_csv + "是否存在")
        return
    
    out_path = "output/modCSV/"
    out_file = vanilla_csv.split('.')[0] + '.'+ vanilla_csv.split('.')[1] + ".csv"
    if not os.path.exists("output/modCSV"):
        os.makedirs("output/modCSV")

    with open(vanilla_out_path + vanilla_csv, 'r', encoding="UTF-8") as vanillaCSVFile:
        csv_reader = csv.reader(vanillaCSVFile, delimiter=',', quotechar='"')
        dict1 = {row[0]: row[1] for row in csv_reader}
    with open(csv_path + csv_file, 'r', encoding="UTF-8") as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        dict2 = {row[0]: row[-1] for row in csv_reader}
    #print(dict1.keys())
    #print(dict1)
    #print(dict2)
    def check_yarntag(dict1, dict2):
        set_add = set(dict1.keys()) | set(dict2.keys())
        set_common = set(dict1.keys()) & set(dict2.keys())
        if(set_add == set_common):
            return True
        else:
            return False
    if not check_yarntag(dict1, dict2):
        print(csv_file + " 文件键值不匹配，请检查!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return
    else:
        print(csv_file + " 文件键值匹配，开始替换")
    
    #keys = set(dict1.keys())
    #print(keys)
    with open(out_path + out_file, 'w', encoding="UTF-8", newline='') as modcsvFile:
        csv_writer = csv.writer(modcsvFile)
        csv_writer.writerows([[key, dict1[key], dict2[key]] for key in dict1.keys()])

rootPath = os.getcwd()
#print(rootPath)
CSVFOLDER = "utf8"
vanilla_out_path = "output/vanillaCSV/"
csv_path = CSVFOLDER + '/'
os.chdir(CSVFOLDER)
os.system("python " + rootPath + '/' + "2utf8withoutBOM.py")
os.chdir(rootPath)

csvFolder = os.listdir(CSVFOLDER)
for item in csvFolder:
    if(os.path.isdir(item)):
        continue
    #print(os.path.basename(__file__))
    if(item == os.path.basename(__file__)):
        continue
    if(".py" in item):
        continue
    if(' ' in item):
        continue
    if(re.match(r'.*\.csv$', item) is not None):
        print("找到 CSV 格式后缀文件：" + item + " 开始查找匹配 .csv.vanilla 文件")
        conbine_csv(item)
    
