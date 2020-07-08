import os
import re
import jieba
import jieba.analyse
import jieba.posseg as pseg


def get_monthAndDay(title):
    """
    获取拍摄时间
    :param title: 照片标题
    :return: 返回日期
    """
    month, day  = None, None
    try:
        create_date = re.search(r'\d{1,2}月\d{1,2}日', title)
        month = create_date.group(0)[0:2]
        day = create_date.group(0)[3:5]
        print(month, day)
    except Exception:
        print("读取失败")
        return None, None
    # print(year.group(0))
    return month, day


def get_time(title):
    """
    获取图片的拍摄时间
    :param title: 图片标题
    :return: 返回year,month,day
    """
    print(title)
    words = pseg.cut(title, use_paddle=True)  # paddle模式
    time = []
    year, month, day = None, None, None

    try:
        time = re.search(r'(\d{4}-\d{1,2}-\d{1,2})|(\d{4}年\d{1,2}月\d{1,2}|())', title).group()  # 匹配2016年11月18日和2020-4-5,2017.3.18
        year = re.search(r'\d{4}', time).group()
        month = re.search(r'\d{1,2}', time[4:]).group()
        day = re.search(r'\d{1,2}', time[-3:]).group()
    except Exception:
        for word, flag in words:
            if flag == 'm':
                print(word, end='   ')
                # 日期格式为20160312的,之所以不用正则是因为存在其他的数字字符串，如电话号码或其他编号之类的，避免匹配错误
                if len(word) == 8:
                    year = word[:4]
                    month = word[4:6]
                    day = word[6:8]
                elif str(word).startswith('20'):
                    year = word[:4]

    time = year, month, day
    print(time)
    return time


def get_name(title):
    """
    获取作者名
    :param title: 图片标题
    :return: 返回作者名  目前只能获取中文名
    """
    # 添加自定义词典
    jieba.load_userdict("fenci/dic.txt")
    words = pseg.cut(repr(title), use_paddle=True)  # paddle模式
    name = []
    for word, flag in words:
        if flag == 'nr' and len(word) > 1:
            name.append(word)

    name = list(set(name))
    print(name)
    #仅返回第一个人作为作者
    if name:
        return name[0]
    return name


def get_keyWord(title, name):
    """
    获取关键字
    :param title: 图片标题
    :param name: 将作者姓名传入，作为停用词词表
    :return: 返回关键字列表
    """
    #添加自定义词典
    print(title)
    jieba.load_userdict("fenci/dic.txt")
    keyword_list = []
    # jieba.enable_parallel(4)  # 开启并行分词模式，参数为并行进程数
    keywords_top = jieba.analyse.extract_tags(title, topK=10)  # 关键词前10位，返回值为列表
    print('关键词top 15： {}'.format(keywords_top))
    for word in keywords_top:
        if word not in name and word.isalpha(): #去除人名和日期
            keyword_list.append(word)
    print('关键字：{}'.format(keyword_list))

    #根据词性过滤有效信息
    rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']
    words = pseg.cut(repr(keyword_list), use_paddle=True)  # paddle模式
    result_key = []  # 最终返回信息
    for word, flag in words:
        if flag in rule:
            print(" word:{}  flag: {} ".format(flag, word))
            result_key.append(word)
    print('过滤后关键字：{}'.format(result_key))
    return result_key


def main(listDirs, result):
    """
    读取照片标题集合的文件，进行处理
    :param listDirs: 图片标题集合文件
    :param result: 输出文件
    :return:
    """

    with open(listDirs, 'r', encoding='utf-8') as file:
        with open(result, 'w') as f:
            for line in file.readlines():
                pic = {}
                # 去除空格和连接符
                line1 = line.replace(' ', '').replace('-', '')
                number = line1[-13::].strip('\n')  # 图片编号
                # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
                title_list = line1[:-18:].split('\\')
                tag_1 = title_list[2]  # 一级标签，作品来源

                year, month, day = get_time(r'' + line[:-18:].replace('.', '-'))  # 获取年月日
                if month is None: #处理只有月份和日期的情况
                    month, day = get_monthAndDay(r'' + line[:-18:])

                name = get_name(''.join(title_list))  # 作者
                # 从2级目录开始，0级为z，1级为yuexun，2级为照片来源 Z:\yuexun\摄影师投稿作品\2019年\魏建国-2018.12月北京月讯杂志社289张（2017-2018年拍
                keyWords = get_keyWord(''.join(title_list[3:]), name)   #关键字
                pic[number] = [tag_1, year, month, day, name, keyWords]
                for key, value in pic.items():
                    f.write('{}\t'.format(key))
                    for i in value:
                        f.write('{}\t'.format(i))
                    f.write('\n')
                # print(line)
            print(pic)


if __name__ == '__main__':
    Path = os.getcwd() + os.sep + 'data'
    listDirs = os.path.join(Path, 'renommelog.txt')
    result = os.path.join(Path, 'result.txt')

    main(listDirs, result)
