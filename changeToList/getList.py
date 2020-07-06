import os

def read(path, result):
    with open(listDirs, 'r', encoding='utf-8') as file:
        with open(result, 'w', encoding='utf-8') as file_write:
            for line in file.readlines():
                tag_list = []  # 图片对应的标签列表

                title_list  = line[:-18:].split('\\')   #将有效信息分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
                file_write.write(str(title_list))
                file_write.write('\n')
                print(title_list)


if __name__ == '__main__':
    Path = os.getcwd()
    listDirs = os.path.join(Path, '../renommelog.txt')
    print(listDirs)
    result = os.path.join(Path, 'list.txt')

    read(listDirs, result)
# 客户teamViewer ID 1233273192