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

import jieba
import jieba.analyse

import jieba.posseg as pseg

# words = pseg.cut(r"Z:\yuexun\2016图编外拍\李晓尹\李晓尹-中国-2016年8月26日-月讯爱国主义教育\李晓尹-中国-2016年8月26日-月讯爱国主义教育1.jpg ")     #jieba默认模式
jieba.load_userdict("dic.txt")

def get_name(title):
    """
    获取作者名
    :param title: 图片标题
    :return: 返回作者名  目前只能获取中文名
    """
    # 添加自定义词典
    jieba.load_userdict("dic.txt")
    words = pseg.cut(title)
    name = []
    for word, flag in words:
        if flag == 'nr' and len(word) > 1:
            print("word:{}  flag:{}".format(word, flag))
            name.append(word)

    name = list(set(name))
    print("name:{}".format(name))
    return name


def get_keyWord(title, name):
    """
    获取关键字
    :param title: 图片标题
    :param name: 将作者姓名传入，作为停用词词表
    :return: 返回关键字列表
    """
    #添加自定义词典
    jieba.load_userdict("dic.txt")
    keyword_list = []
    print(title)

    keywords_top = jieba.analyse.extract_tags(title, topK=15)  # 关键词前3位，返回值为列表
    print('关键词top 15： {}'.format(keywords_top))
    for word in keywords_top:
        if word not in name and not word.isnumeric(): #去除人名和日期
            keyword_list.append(word)
    print("keyword_list:{}".format(keyword_list))  #['美丽乡村', '顺义马坡镇南卷村', '2016', '11', '18', 'yuexun2016', '供图', '编外', '村委会', '中国']


    keyword_list = " ".join(keyword_list)  #
    print("keyword_list1:{}".format(keyword_list))
    keywords_list = re.sub(r'[\d]+', '', keyword_list).split(' ')
    print("keyword_list2:{}".format(keywords_list))
    result = []
    for i in keywords_list:  #去除值为空的元素
        if len(i) != 0:
            result.append(i)

    print("keyword_list3:{}".format(result))
    # tag = re.findall(r'\D+', keyword_list)[0].split('/')  # 过滤掉数字信息   此处应修改为先过滤再赵关键字
    return keywords_list

# def get_keyword(title):
#     words = jieba.cut(title)
#     print('  '.join(words))
#     keywords1 = jieba.analyse.extract_tags(title)
#     print('关键词提取： ' + "/".join(keywords1))
#     keywords_top = jieba.analyse.extract_tags(title, topK=5)
#     keywords_top = "/".join(keywords_top)
#     s = re.findall(r'\D+', keywords_top)
#     print(s[0].split('/'))
#     print('关键词top3： ' + keywords_top)  # 有时不确定提取多少关键词，可利用总词的百分比
#     print('总词数{}'.format(len(list(jieba.cut(title)))))
#     print("*" * 30)
#     return None


def read(path):
    pic = {}
    with open(listDirs, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.replace(' ', '').replace('-', '')  # 去除空格
            # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
            title_list = line[:-18:].split('\\')
            name = get_name(''.join(title_list))  # 作者
            # keyWords = get_keyWord(''.join(title_list), name)
            keyWords = get_keyWord(''.join(title_list[3:]), name)  # 从2级目录开始，0级为z，一级为照片来源
            print('开始'+'*'*40)
            print(name)
            print(keyWords)
            print('结束'+'*' * 40)
        # print(pic)
    return


if __name__ == '__main__':
    Path = os.getcwd()
    Project_path = os.path.dirname(Path)

    listDirs = Project_path + os.sep + 'data' + os.sep + 'renommelog.txt'
    result = os.path.join(Path, 'result.txt')

    read(listDirs)
