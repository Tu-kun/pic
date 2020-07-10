import os
import re
import jieba.posseg as pseg
import jieba


def read(path, result, dic_path):
    jieba.load_userdict(dic_path)
    names = []
    foreign_names = []
    with open(listDirs, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            try:
                name = re.search(r'\b[\u4E00-\u9FA5]+([·|•|･][\u4E00-\u9FA5]+)+', line).group()
                print(name)
                names.append(name)
                # file_write.write(name + '\n')
            except AttributeError:
                pass
            try:
                foreign_name = re.search((r'[A-Z][a-z]+(\s[A-Z][a-z]+)+'), line).group()
                foreign_names.append(foreign_name)
            except AttributeError:
                pass

    names = list(set(names))  #去重
    foreign_names = list(set(foreign_names))
    with open(result, 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write(' nr\n')
        for name in foreign_names:
            f.write(name)
            f.write(' nr\n')


if __name__ == '__main__':
    Path = os.getcwd()
    Project_path = os.path.dirname(Path)

    dic_path = Project_path + os.sep + 'fenci' + os.sep + 'dic.txt'
    listDirs = Project_path + os.sep + 'data' + os.sep + 'renommelog.txt'
    print(listDirs)
    result = os.path.join(Path, 'name.txt')

    read(listDirs, result, dic_path)
# 客户teamViewer ID 1233273192