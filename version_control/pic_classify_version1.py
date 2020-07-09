import os
import re
import jieba
import jieba.analyse
import jieba.posseg as pseg


def get_monthAndDay(title):
    """
    在年份和日期中存在间隔时调用，如2012年xxxx，4月12日和5.15
    :param title: 照片标题字符串
    :return: 返回月份和日期
    """
    month, day  = None, None
    try:
        # create_date = re.search(r'\d{1,2}月\d{1,2}日', title)
        # month = create_date.group(0)[0:2]
        # day = create_date.group(0)[-2:]
        #修改后
        time = re.search(r'\d{1,2}月\d{1,2}', title).group()
        month = re.search(r'\d{1,2}', time).group()
        day = re.search(r'\d{1,2}', time[2:]).group()
        print('二次读取月份和日期；{}  {}'.format(month, day))
    except Exception:
        pass
    # print(year.group(0))
    try:
        time = re.search(r'\d{1,2}月', title).group()
        month = re.search(r'\d{1,2}', time).group()
    except Exception:
        print("时间读取失败")
    return month, day


def get_time(title):
    """
    获取图片的拍摄时间
    :param title: 图片标题
    :return: 返回year,month,day
    """
    print('开始进行时间提取：{}'.format(title))
    words = pseg.cut(title, use_paddle=True)  # paddle模式
    time = []
    year, month, day = None, None, None

    try:
        #方案1
        time = re.search(r'(20\d{2}-\d{1,2}-\d{1,2})|(20\d{2}年\d{1,2}月\d{1,2}|(20\d{2}\d{1,2}\d{1,2}))', title).group()  # 匹配2016年11月18日和2020-4-5,2017.3.18
        #此处有问题，直接按位置提取是不行的
        print('时间：{}'.format(time))
        year = re.search(r'20\d{2}', time).group()
        month = re.search(r'\d{1,2}', time[4:]).group()
        day = re.search(r'\d{1,2}', time[-2:]).group()
    except Exception:
        pass

    if year is None:
        try:
            year = re.search(r'20\d{2}', title).group()
        except Exception:
            pass

    time = year, month, day
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
    print('摄影师:{}'.format(name))
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
    print('开始关键词的提取：{}'.format(title))
    jieba.load_userdict("fenci/dic.txt")
    keyword_list = []
    # jieba.enable_parallel(4)  # 开启并行分词模式，参数为并行进程数
    keywords_top = jieba.analyse.extract_tags(title, topK=10)  # 关键词前10位，返回值为列表
    # print('关键词top 15： {}'.format(keywords_top))
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
            # print(" word:{}  flag: {} ".format(flag, word))
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
    time_none_number = 0
    with open(listDirs, 'r', encoding='utf-8') as file:
        with open(result, 'w') as f:
            for line in file.readlines():
                pic = {}
                # 去除空格和连接符
                line = line.replace(' ', '').replace('-', '')
                number = line[-13::].strip('\n')  # 图片编号
                # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
                title_list = line[:-18:].split('\\')
                tag_1 = title_list[2]  # 一级标签，作品来源

                year, month, day = get_time(r'' + line[:-18:].replace('.', '-'))  # 获取年月日
                if month is None: #处理只有月份和日期的情况
                    month, day = get_monthAndDay(r'' + line[:-18:])
                # 考虑日期格式读取错误导致月份大于12（通常为连续读取两个年份如20102012），同时统计月份为空的数据
                if month is None or int(month) > 12:
                    month = None
                    day = None
                    time_none_number += 1

                print('提取出的年月日：{}  {}  {}'.format(year, month, day))
                name = get_name(''.join(title_list))  # 作者
                # 从2级目录开始，0级为z，1级为yuexun，2级为照片来源 Z:\yuexun\摄影师投稿作品\2019年\魏建国-2018.12月北京月讯杂志社289张（2017-2018年拍
                keyWords = get_keyWord(''.join(title_list[3:]), name)   #关键字
                pic[number] = [tag_1, year, month, day, name, keyWords]
                for key, value in pic.items():
                    f.write('{}\t'.format(key))
                    for i in value:
                        f.write('{}\t'.format(i))
                    f.write('\n')
                print('-'*100)
            print('时间出现空缺的照片数量：{}/35691'.format(time_none_number))


if __name__ == '__main__':
    import sys

    old = sys.stdout  # 将当前系统输出储存到一个临时变量中
    f = open('result2.txt', 'w', encoding='utf-8')

    sys.stdout = f  # 输出重定向到文件

    Path = os.getcwd() + os.sep + 'data'
    listDirs = os.path.join(Path, 'renommelog.txt')
    result = os.path.join(Path, 'result.txt')
    main(listDirs, result)

    sys.stdout = old  # 还原原系统输出
    f.close()