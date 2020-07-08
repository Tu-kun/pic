#1. 数据预处理
>提取地名、拍摄时间  

>事件  
>摄影师  

**一级标签**  
>['2016图编外拍', '2016外国摄影师拍北京-最终发回文件', '2017希腊摄影师拍北京-最终发回成片', '2017年外拍', '2018一带一路摄影师拍北京-最终发回成片', '2018图编外拍', '2018外拍', '航拍挑图', '航拍（改）-常旭', '2014年外国摄影师拍北京-643张', '2015年外国摄影师拍北京-1479张', '2018图编外拍 2', '2019图编外拍', '友协', '摄影师投稿作品']  
>一级标签共：15种

##1.1 提取时间  
>日期格式过于分散，无法找到统一的提取规则，只能大方向匹配能够提取的，然后对有的图片的时间进行单独标注  
>主要包括的的格式有：2012年6月3日，2012年06月03日，2012-2-12，2012-12-21，2013年6月，20120102，  
>采用了以下几种方式处理：  
> - 正则表达式匹配，匹配年月日格式和以‘-’连接的格式
> - 将标题切分后，统计指定字符长度的元素，如20120202这种八位的数字，然后提取具体数字  
>


##1.2 提取人名信息  
使用jieba分词，首先创建自定义的词典，很多标题中含有大量的重复性名词，可以添加之词典中，且方便进行词频的统计
通过关键词提取获取每个标题中的关键字，并获取关键词排序

    jieba.analyse.extract_tags(title, topK=3)
    ******************************
    桑浥  20160409  平谷  桃花节  挑  [  Originals  ]  桑浥  20160409  -  ISY  _  2178  .  j
    关键词提取： 桑浥/20160409/桃花节/Originals/ISY/2178/平谷
    关键词top3： 桑浥/20160409/桃花节
    总词数16
    从16 中取出2 个词
    关键词topk： 桑浥/20160409
    ******************************


2020年7月7日结果：

    ('0013341.jpg', ['2017年外拍', '2017', '4', '4', ['陈硕']])
    ('0006870.JPG', ['2016外国摄影师拍北京-最终发回文件', '2016', '05', '30', ['霍姆兹']])
    ('0013342.jpg', ['2018一带一路摄影师拍北京-最终发回成片', '2018', '5', '10', ['斯坦科', '立陶宛']])
    ('0013343.jpg', ['2018一带一路摄影师拍北京-最终发回成片', '2018', '5', '10', ['斯坦科', '立陶宛']])
    ('0013344.jpg', ['2018一带一路摄影师拍北京-最终发回成片', '2018', '5', '10', ['斯坦科', '立陶宛']])
    ('0013345.jpg', ['2018一带一路摄影师拍北京-最终发回成片', '2018', '5', '10', ['斯坦科', '立陶宛']])  
    
##1.3 提取关键词
通过jieba所实现的基于IT-IDF算法的函数进行关键字的提取，注意对关键字中作者名和时间信息的过滤，最后通过词性过滤的方法去除无效信息，保留关键信息
```python
    keyword_list = []
    keywords_top = jieba.analyse.extract_tags(title, topK=10)  # 关键词前10位，返回值为列表
    print('关键词top 10： {}'.format(keywords_top))
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
```
7月8号结果  

    00000001.jpg	2016图编外拍	2016	11	18	['李晓尹']	['美丽乡村', '顺义马坡镇南卷村', '村委会', '中国']	
    00000010.jpg	2016图编外拍	2016	1	14	['李晓尹']	['左安门', '猴年造型', '角楼', '王府井', '中国']	
    00000011.jpg	2016图编外拍	2016	1	14	['李晓尹']	['王府井', '猴年造型', '合影留念', '猴子', '游客', '造型', '中国']		
    00000044.jpg	2016图编外拍	2016	1	1	['李晓尹']	['外国摄影师巡展五彩城', '中国']	
    00000072.jpg	2016图编外拍	2016	7	12	['李晓尹']	['画火车王忠良', '境外', '中国']	
    00000079.jpg	2016图编外拍	2016	7	16	['李晓尹', '惠民']	['科教', '香山', '中关村', '刺猬']
    00004942.JPG	2016图编外拍	2016	04	28	[]	['桑浥', '手绘', '开幕式', '北海', '胡同', '京城']
    00014887.JPG	2018外拍	2018	None	None	['常旭']	['艺术展', '荆山', '南方']
    00016947.JPG	航拍（改）常旭	2016	10	11	['任晓峰', '常旭', '马文晓']	['司马台长城'