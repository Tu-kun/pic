import jieba

jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
strs=[r"Z:\yuexun\2016图编外拍\桑浥\20160428手绘京城-北海-胡同-开幕式\大\100EOS1D\20160428手绘京城-北海-胡同-开幕式-桑浥 (361).JPG",
      r"Z:\yuexun\2017年外拍\闫珅\文博会911—JPG\闫珅—文博会911—JPG (862).jpg",
      r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG"]
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
    print("Paddle Mode: " + '/'.join(list(seg_list)))

seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(r"Z:\yuexun\2018图编外拍 2\修雨辰-811张\2018年12月27日 辽金城垣博物馆\修雨辰-2018年12月27日 辽金城垣博物馆-9729.JPG")  # 搜索引擎模式
print(", ".join(seg_list))