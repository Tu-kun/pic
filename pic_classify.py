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
    try:
        create_date = re.search(r'（\d{4}\d{2}\d{2}|\d{4}.{d}}', title)
        year = create_date.group(0)[:4]  # 获取年份
        month = create_date.group(0)[4:6]
        day = create_date.group(0)[6:8]
        print(year, month, day)
    except Exception:
        print("读取失败")
        return None, None, None
    # print(year.group(0))
    return year, month, day


def get_time(title):
    print(title)
    words = pseg.cut(title, use_paddle=True)  # paddle模式
    time = []
    year, month, day = '', '', ''

    try:
        time = re.search(r'(\d{4}-\d{1,2}-\d{1,2})|(\d{4}年\d{1,2}月\d{1,2})', title).group()  #匹配2016年11月18日和2020-4-5
        year = re.search(r'\d{4}', time).group()
        month = re.search(r'\d{1,2}', time[4:]).group()
        day = re.search(r'\d{1,2}', time[-3:]).group()
    except Exception:
        for word, flag in words:
            if flag == 'm':
                print(word, end='   ')
                if len(word) == 8:  #日期格式为20160312的
                    year = word[:4]
                    month = word[4:6]
                    day = word[6:8]
                elif str(word).startswith('20'):
                    year = word[:4]

    time = year, month, day
    print(time)
    return time


def get_name(title):
    words = pseg.cut(repr(title), use_paddle=True)  # paddle模式
    name = []
    for word, flag in words:
        if flag == 'nr' and len(word) > 1:
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
            line = line.replace(' ', '')   #去除空格
            number = line[-12::].strip('\n')  # 图片编号
            title_list = line[:-18:].split('\\')  # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
            tag_1 = title_list[2]  # 一级标签，作品来源
            year, month, day = get_time(r''+line[:-18:])  # 获取年月日

            name = get_name(''.join(title_list))  # 作者
            # print(title_list)
            pic[number] = [tag_1, year, month, day, name]
            # print(line)
        print(pic)
    return pic


def write(path, pic):
    with open(path, 'w') as f:
        for item in pic.items():
            f.write(str(item) + '\n')


if __name__ == '__main__':
    Path = os.getcwd() + os.sep + 'data'
    listDirs = os.path.join(Path, 'renommelog.txt')
    result = os.path.join(Path, 'result.txt')

    pic = read(listDirs)
    write(result, pic)
