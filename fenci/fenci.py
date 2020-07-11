"""
李晓尹  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  美丽乡村  顺义马坡镇南卷村  村委会  供图  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  4  .  j
李晓尹  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  美丽乡村  顺义马坡镇南卷村  村委会  供图  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  5  .  j
李晓尹  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  美丽乡村  顺义马坡镇南卷村  村委会  供图  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  6  .  j
李晓尹  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  美丽乡村  顺义马坡镇南卷村  村委会  供图  李晓尹  -  中国  -  2016  年  11  月  18  日  -  美丽乡村  顺义马坡镇南卷村  7  .  j
李晓尹  李晓尹  -  中国  -  2016  年  1  月  14  日  -  王府井  猴年造型  李晓尹  -  中国  -  2016  年  1  月  14  日  -  王府井  猴年造型  10  .  j
李晓尹  李晓尹  -  中国  -  2016  年  1  月  14  日  -  王府井  猴年造型  李晓尹  -  中国  -  2016  年  1  月  14  日  -  左安门  角楼  复建  .  j
李晓尹  李晓尹  -  中国  -  2016  年  1  月  14  日  -  王府井  猴年造型  李晓尹  -  中国  -  2016  年  1  月  14  日  -  左安门  角楼  复建  1  .  j
李晓尹  李晓尹  -  中国  -  2016  年  1  月  14  日  -  王府井  猴年造型  李晓尹  -  中国  -  2016  年  1  月  14  日  -  游客  在  王府井  猴子  造型  前  合影留念  .  j
"""
import math
import os
import re
import time

import jieba
import jieba.analyse
import jieba.posseg as pseg
import sys

def get_monthAndDay(title):
    """
    在年份和日期中存在间隔时调用，如2012年xxxx，4月12日，5.15,只有月份信息的情况
    :param title: 照片标题字符串
    :return: 返回月份和日期
    """
    month, day = None, None
    try:
        time = re.search(r'\d{1,2}月\d{1,2}', title).group()
        month = re.search(r'\d{1,2}', time).group()
        day = re.search(r'\d{1,2}', time[2:]).group()
        print('二次读取月份和日期；{}  {}'.format(month, day))
    except Exception:
        pass
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
        time = re.search(r'(20\d{2}-\d{1,2}-\d{1,2})|(20\d{2}年\d{1,2}月\d{1,2}|(20\d{2}\d{1,2}\d{1,2}))',
                         title).group()  # 匹配2016年11月18日和2020-4-5,2017.3.18
        print('时间：{}'.format(time))
        year = re.search(r'20\d{2}', time).group()
        month = re.search(r'\d{1,2}', time[4:]).group()
        day = re.search(r'\d{1,2}', time[-2:]).group()
    except Exception:
        pass

    # 此处处理只有年份的数据，只有年份时上面的匹配规则是无法生效的
    if year is None:
        try:
            year = re.search(r'20\d{2}', title).group()
        except Exception:
            pass

    time = year, month, day
    return time


def load_dic():
    pass
    # 添加自定义词典
    # jieba.load_userdict("dic2.txt")
    # jieba.load_userdict("词库/行政地区.txt")
    # jieba.load_userdict("词库/中国风景名胜.txt")
    # jieba.load_userdict("词库/政府机关团体机构大全.txt")


def get_name(title):
    """
    获取摄影师的名字
    :param title: 图片标题字符串
    :return: 返回作者名  目前只能获取中文名
    """
    load_dic()
    words = pseg.cut(repr(title), use_paddle=True)  # paddle模式
    name = []
    for word, flag in words:
        if flag == 'nr' and len(word) > 1:
            name.append(word)

    name = list(set(name))
    print('所有的摄影师:{}'.format(name))
    result_name = ''
    #由于修改匹配规则后对于‘2016年’算法会认为这是一个人名，故需要过滤掉
    for i in name:
        try:
            re.search(r'\d', i).group()
        except Exception:
            result_name = i
    print('摄影师:{}'.format(result_name))
    # 仅返回第一个人作为作者
    # if name:
    #     return name[0]
    return result_name


def get_keyWords(title, name):
    """
    获取关键字
    :param title: 图片标题
    :param name: 将作者姓名传入，作为停用词词表
    :return: 返回关键字列表
    """
    # 添加自定义词典
    load_dic()
    print('开始关键词的提取：{}'.format(title))
    jieba.analyse.set_stop_words('stop-words.txt')
    keyword_list = []
    rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']
    keywords_top = jieba.analyse.extract_tags(title, topK=10, allowPOS=rule)  # 关键词前10位，返回值为列表,allowPOD过滤指定词性的词
    # print('关键词top 15： {}'.format(keywords_top))
    for word in keywords_top:
        if word not in name and word.isalpha():  # 去除人名和日期
            keyword_list.append(word)
    print('关键字：{}'.format(keyword_list))

    return keyword_list

def get_keyWords_byCut(title, name):
    """
    获取关键字
    :param title: 图片标题
    :param name: 将作者姓名传入，作为停用词词表
    :return: 返回关键字列表
    """
    import jieba.posseg as pseg
    # 添加自定义词典
    load_dic()
    # jieba.analyse.set_stop_words('stop-words.txt')
    keyword_list = []
    loc = []
    names = []

    rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']
    # keywords_top = jieba.analyse.extract_tags(title, topK=10, allowPOS=rule)  # 关键词前10位，返回值为列表,allowPOD过滤指定词性的词
    keywords_top = pseg.cut(title, use_paddle=True)
    #去重
    keywords_top = list(set(keywords_top))

    for word, flag in keywords_top:
        if flag in rule and len(word) > 1:

            if word not in name and word.isalpha():  # 去除人名和日期
                keyword_list.append(word)
            # print(" word:{}  flag: {} ".format(word, flag))
            if flag == 'ns':
                loc.append(word)

    print("该照片拍摄于：{}".format(loc))
    # print("cut出的摄影师：｛｝".format(names))
    print('通过cut获取的关键字：{}'.format(keyword_list))

    return loc, keyword_list


def main(listDirs, result):
    """
    读取照片标题集合的文件，进行处理
    :param listDirs: 图片标题集合文件
    :param result: 输出文件
    :return:
    """
    time_none_number = 0
    with open(listDirs, 'r', encoding='utf-8') as file:
        with open(result, 'w', encoding='utf-8') as f:
            for line in file.readlines():
                pic = {}
                # 去除空格和连接符
                line = line.replace(' ', '').replace('-', '')
                number = line[-13::].strip('\n')  # 图片编号
                # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
                title_list = line[:-18:].split('\\')
                tag_1 = title_list[2]  # 一级标签，作品来源

                year, month, day = get_time(r'' + line[:-18:].replace('.', '-'))  # 获取年月日
                if month is None:  # 处理只有月份和日期的情况
                    month, day = get_monthAndDay(r'' + line[:-18:])
                # 考虑日期格式读取错误导致月份大于12（通常为连续读取两个年份如20102012），同时统计月份为空的数据
                if month is None or int(month) > 12:
                    month = None
                    day = None
                    time_none_number += 1

                print('提取出的年月日：{}  {}  {}'.format(year, month, day))
                name = get_name(''.join(title_list))  # 作者
                # 从2级目录开始，0级为z，1级为yuexun，2级为照片来源 Z:\yuexun\摄影师投稿作品\2019年\魏建国-2018.12月北京月讯杂志社289张（2017-2018年拍
                # keyWords = get_keyWords(''.join(title_list[3:]), name)  # 关键字
                loc, keyWords = get_keyWords_byCut(''.join(title_list[3:]), name)

                pic[number] = [tag_1, year, month, day, name, loc, keyWords]
                for key, value in pic.items():
                    f.write('{}\t'.format(key))
                    for i in value:
                        f.write('{}\t'.format(i))
                    f.write('\n')
                print('-' * 100)
            print('时间出现空缺的照片数量：{}/35691'.format(time_none_number))


if __name__ == '__main__':

    start_time = time.time()
    old = sys.stdout  # 将当前系统输出储存到一个临时变量中
    f = open('output.txt', 'w', encoding='utf-8')

    sys.stdout = f  # 输出重定向到文件

    Path = os.getcwd()
    listDirs = os.path.join(Path, 'renommelog.txt')
    result = os.path.join(Path, 'result.txt')
    main(listDirs, result)

    sys.stdout = old  # 还原原系统输出
    f.close()
    end_time = time.time()

    run_time = round(end_time - start_time, 5)
    print('运行时间为：{}'.format(run_time))

