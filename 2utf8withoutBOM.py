import re
import os
import chardet


def convert_to_utf8_nobom(file):
    BOM = '\ufeff'
    # get file encoding type
    def get_encoding_type(file):
        with open(file, 'rb') as f:
            rawdata = f.read()
        return chardet.detect(rawdata)['encoding']

    from_codec = get_encoding_type(file)
    print(file + " 文件编码格式：" + from_codec)
    if (from_codec == "utf-8"):
        print(file + " 已为 UTF-8 格式")
        return True
    elif(from_codec == "UTF-8-SIG"):
        print(file + " 文件含有 BOM 头，开始去除")
        with open(file, 'r', encoding="UTF-8-SIG") as f1, open(file+".tmp", 'w', encoding="UTF-8") as f2:
            #text = f1.read()
            #if text.startswith(BOM):
            #    text = text[1:]
            #    text = text.rstrip()
            #f2.write(text)
            for line in f1:
                if line.startswith(BOM):
                    line = line[1:]
                line = line.rstrip() + '\n'
                f2.write(line)
    else:
        print("跳过")
        return False
    
    os.remove(file)
    os.rename(file+".tmp", file)
    
    from_codec = get_encoding_type(file)
    if (from_codec == "utf-8"):
        print(file + " 已去除 BOM 头")
        return True
    elif(from_codec == "UTF-8-SIG"):
        print(file + " BOM 头去除失败")
        return False
    else:
        print("非 UTF-8 编码，请检查文件")
        return False
    

currentFolder = os.listdir(os.getcwd())
for item in currentFolder:
    if(os.path.isdir(item)):
        continue
    #print(os.path.basename(__file__))
    if(item == os.path.basename(__file__)):
        continue
    if(".py" in item):
        continue
    if(re.match(r'.*\.csv$', item) is not None):
        convert_to_utf8_nobom(item)
        