import os
# import re
# #
# # title = r'2010年05月05日'
# # time = re.search(r'(\d{4}-\d{1,2}-\d{1,2})|(\d{4}年\d{1,2}月\d{1,2}日)', title).group()
# # # if time is None:
# # #     time = re.search(r'(\d{4}年\d{2}月\d{2}日)', title)  #匹配2016年11月18日和2020-4-5
# # print(time)
# # year = re.search(r'\d{4}', time).group()
# # month = re.search(r'\d{1,2}', time[4:]).group()
# # day = re.search(r'\d{1,2}', time[-3:]).group()
# # print(day)
# # # month = time.group()[5:7]
# # # day = time.group()[9:10]
# #
# # # print(year, month, day)

# pic = {'1233.jpg':['2016外国摄影师拍北京-最终发回文件', '2016', '05', '30', ['胡里奥', '潘托哈']]}
# with open('test.txt', 'w') as f:
#     for item in pic.items():
#         f.write(str(item) + '\n')
# for key, value in pic.items():
#     print(key, end='  ')
#     for i in value:
#         print(i, end='  ')

# with open("fenci/dic.txt", 'r', encoding='utf-8') as f:
#     print(f.read())

# f=open('a.txt','w')
# import sys
# old=sys.stdout #将当前系统输出储存到一个临时变量中
# sys.stdout=f  #输出重定向到文件
# print('Hello weird') #测试一个打印输出
# sys.stdout=old #还原原系统输出
# f.close()
# # print(open('a.txt','r').read())
import time
start_time = time.time()
print('hhhhh')
time.sleep(3)
end_time = time.time()
run_time = round(end_time-start_time, 5)
print('运行时间为：{}'.format(run_time))