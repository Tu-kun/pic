import os
import re
import jieba
import jieba.posseg as pseg

jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持

def get_year(title):
    """
    获取拍摄时间
    :param title: 照片标题
    :return: 返回日期
    """
    year = re.search(r'\d{4}', repr(title))
    month = re.search(r'')
    # print(year.group(0))
    return year.group(0)


def get_name(title):
    words = pseg.cut(repr(title), use_paddle=True)  # paddle模式
    name = []
    for word, flag in words:
        if flag == 'nr':
            name.append(word)

    name = list(set(name))
    print(name)
    return name

def read(path):
    """
    读取照片标题集合的文件，进行处理
    :param path: 图片标题集合文件
    :return: 返回图片编号和图片标签的字典
    """
    pic = {}
    with open(listDirs, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            number =  line[-12::].strip('\n')  #图片编号
            title_list  = line[:-18:].split('\\')   #将有效信息分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
            tag_1 = title_list[2]  #一级标签，作品来源
            year = get_year(title_list)  #年份
            name = get_name(line)  #作者
            # print(title_list)
            pic[number] = [tag_1, year, name]
            # print(line)
        print(pic)
    return pic

def write(path, pic):
    with open(path, 'w') as f:
        for item in pic.items():
            f.write(str(item)+'\n')

if __name__ == '__main__':
    Path = os.getcwd()
    listDirs = os.path.join(Path, 'renommelog.txt')
    result = os.path.join(Path, 'result.txt')

    pic = read(listDirs)
    write(result, pic)
# 客户teamViewer ID 1233273192