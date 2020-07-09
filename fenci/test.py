import jieba
import jieba.posseg as pseg
import jieba.analyse
# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=[r"Z:\yuexun\2016图编外拍\桑浥\20160428手绘京城-北海-胡同-开幕式\大\100EOS1D\20160428手绘京城-北海-胡同-开幕式-桑浥 (361).JPG",
#       r"Z:\yuexun\2017年外拍\闫珅\文博会911—JPG\闫珅—文博会911—JPG (862).jpg",
#       r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG"]
# for str in strs:
#     seg_list = jieba.cut(str, use_paddle=True) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))
#
# seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG")  # 搜索引擎模式
# print(", ".join(seg_list))
jieba.load_userdict('dic.txt')
seg_list = jieba.cut(r"李晓尹李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村美丽乡村顺义马坡镇南卷村村委会供图李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村1",)  # 搜索引擎模式
print("默认：{}".format(' '.join(seg_list)))

seg_list = jieba.cut(r"李晓尹李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村美丽乡村顺义马坡镇南卷村村委会供图李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村1", HMM=True)  # 搜索引擎模式
print("开启了HMM：{}".format(' '.join(seg_list)))

title = "李晓尹李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村美丽乡村顺义马坡镇南卷村村委会供图李晓尹中国2016年11月18日美丽乡村顺义马坡镇南卷村1"
title2 = '李晓尹李晓尹中国2016年1月14日王府井猴年造型李晓尹第六届中国2016年1月14日左安门角楼复建'
title3 = ['桑浥', '电影节', '第六届', '签约']
print("cut模式")
words = pseg.cut(repr(title2), use_paddle=True)  # paddle模式
name = []
rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']
print('未过滤前')
for word, flag in words:
    print(" word:{}  flag: {} ".format(flag, word))
print('*'*50)
words = pseg.cut(repr(title2), use_paddle=True)  # paddle模式
print('过滤后')
for word, flag in words:
    if flag in rule:
        print(" word:{}  flag: {} ".format(flag, word))

name = []
rule = ['ns', 'nt', 'nz', 'f', 'i', 'l', 'j', 'vn', 'n', 'Ng', 'nr', 'z']

print("关键字模式")
words = jieba.analyse.extract_tags(repr(title2), allowPOS=rule)
for word in words:
    print(" word:{}".format(word))
print('*'*50)

print("关键字模式未过滤")
words = jieba.analyse.extract_tags(repr(title2))  # paddle模式
for word in words:
    print(" word:{}".format(word))
print('*'*50)