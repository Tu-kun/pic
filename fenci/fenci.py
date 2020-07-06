# # -*- coding: utf-8 -*-
# import jieba
# import jieba.posseg as pseg
# import datetime
# import sys
#
#
# # 词性标注，nr为人名
# def getFirstName(messageContent):
#     words = pseg.cut(messageContent)
#     for word, flag in words:
#         if flag == 'nr' and len(word) > 1:  # 单字姓名去掉
#             return word
#     return False
#
#
# def getAllName(messageContent):
#     words = pseg.cut(messageContent)
#     names = []
#     for word, flag in words:
#         print('%s,%s' % (word, flag))
#         if flag == 'nr':  # 人名词性为nr
#             names.append(word)
#     return names
#
#
# # 修改停用词集合中所有词性为名词，大部分为名词
# def alterWordTagToX(list):
#     for x in list:
#         jieba.add_word(x, tag='n')
#
#
# def LoadStopWord(StopWordFileName):
#     StopWord_file = open(StopWordFileName, 'r', encoding='utf-8')
#     StopWordList = []
#
#     for line in StopWord_file.readlines():
#         StopWordList.append(line.strip('\n'))
#
#     set(StopWordList)
#     StopWord_file.close()
#     alterWordTagToX(StopWordList)
#
#
# def main():
#     # 加载停用词词典文件
#     LoadStopWord('stopword.txt')
#
#     input_file_name = sys.argv[1]
#     output_file_name = 'name_' + input_file_name
#     print(input_file_name)
#     print(output_file_name)
#     begin = datetime.datetime.now()
#     # 单机并行分词
#     jieba.enable_parallel(8)
#     input_file = open(input_file_name, 'r', encoding='utf-8')
#     output_file = open(output_file_name, 'w')
#
#     for line in input_file:
#         temp = line.split('\t')
#         if len(temp) != 4:
#             continue
#         name = getFirstName(temp[1])
#
#         if name != False:
#             # print(name)姓名作为一行中的一个字段，其他为你需要的字段
#             time = str(temp[3]).strip('\n')
#             output_file.write(temp[0] + ',' + name + ',' + '\n')
#         else:
#             continue
#
#     end = datetime.datetime.now()
#     print((end - begin).seconds)
#
#     # 单元测试代码
#     names = getAllName('我老公宝贝叫王宁,尊敬的王大力,CCHHKK旗舰店,尊敬的铁路客服人员李天，冯达辉')
#     print(names)
#     print(getFirstName('尊敬的铁路客服人员李天'))
#     output_file.close()
#     input_file.close()
#
#
# if __name__ == '__main__':
#     main()


import jieba
import jieba.posseg as pseg
# words = pseg.cut(r"Z:\yuexun\2016图编外拍\李晓尹\李晓尹-中国-2016年8月26日-月讯爱国主义教育\李晓尹-中国-2016年8月26日-月讯爱国主义教育1.jpg ")     #jieba默认模式
jieba.enable_paddle()   #启动paddle模式。 0.40版之后开始支持，早期版本不支持
words = pseg.cut(r"Z:\yuexun\2016图编外拍\李晓尹\李晓尹-中国-2016年8月26日-月讯爱国主义教育\李晓尹-中国-2016年8月26日-月讯爱国主义教育1.jpg ", use_paddle=True) #paddle模式
name = []
for word, flag in words:
    # print('%s %s' % (word, flag))
    if flag == 'nr':
        name.append(word)
        # print(word)

name = list(set(name))
print(name)