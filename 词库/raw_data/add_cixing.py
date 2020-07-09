import sys

new_fileName = sys.argv[1].rsplit('.')[0] + '_new.txt'
f = open(new_fileName, 'w', encoding='utf-8')
old = sys.stdout
sys.stdout = f
with open(sys.argv[1], 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        old_str = line.strip('\n')
        new_str = old_str + ' '+ sys.argv[2]
        print(new_str)

sys.stdout = f
f.close()
