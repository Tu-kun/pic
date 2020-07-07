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

import jieba
import jieba.analyse

import jieba.posseg as pseg

# words = pseg.cut(r"Z:\yuexun\2016图编外拍\李晓尹\李晓尹-中国-2016年8月26日-月讯爱国主义教育\李晓尹-中国-2016年8月26日-月讯爱国主义教育1.jpg ")     #jieba默认模式
jieba.load_userdict("dic.txt")


def get_name(title):
    words = jieba.cut(title)
    print('  '.join(words))
    keywords1 = jieba.analyse.extract_tags(title)
    print('关键词提取： ' + "/".join(keywords1))
    keywords_top = jieba.analyse.extract_tags(title, topK=3, withWeight=False)
    print('关键词topk： ' + "/".join(keywords_top))  # 有时不确定提取多少关键词，可利用总词的百分比
    print('总词数{}'.format(len(list(jieba.cut(title)))))
    total = len(list(jieba.cut(title)))
    get_cnt = math.ceil(total * 0.1)  # 向上取整
    print('从%d 中取出%d 个词' % (total, get_cnt))
    keywords_top1 = jieba.analyse.extract_tags(title, topK=get_cnt)
    print('关键词topk： ' + "/".join(keywords_top1))
    print("*" * 30)
    return None


def read(path):
    pic = {}
    with open(listDirs, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.replace(' ', '')  # 去除空格
            # 将图片标题分割为列表，如['Z:', 'yuexun', '2018图编外拍 2', '炫彩世界收图-3124张', '周世杰-20181025炫彩世界开幕式', 'DSCF4066.JPG']
            title_list = line[:-18:].split('\\')
            name = get_name(''.join(title_list[3:]))  # 作者

        # print(pic)
    return


if __name__ == '__main__':
    Path = os.getcwd()
    Project_path = os.path.dirname(Path)

    listDirs = Project_path + os.sep + 'data' + os.sep + 'renommelog.txt'
    result = os.path.join(Path, 'result.txt')

    read(listDirs)
