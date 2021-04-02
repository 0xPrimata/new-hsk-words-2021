import pandas as pd
import pypinyin

trans1 = open('trans1.txt', encoding="utf8").read().split('\n')
trans2 = open('trans2.txt', encoding="utf8").read().split('\n')
trans3 = open('trans3.txt', encoding="utf8").read().split('\n')
trans4 = open('trans4.txt', encoding="utf8").read().split('\n')
trans5 = open('trans5.txt', encoding="utf8").read().split('\n')
trans6 = open('trans6.txt', encoding="utf8").read().split('\n')
trans = [trans1, trans2, trans3, trans4, trans5, trans6]
def pinyinit(file):
    text = []
    for combo in file:
        print(combo)
        a = combo.split(',')
        list = pypinyin.pinyin(a[0])
        pinyin = ''
        for i in list:
            pinyin += "".join(i)
        print(pinyin)
        b=combo+","+pinyin
        text.append(b)
    return text

# for i in range(0, 6):
#     file = pinyinit(trans[i])
#     with open(f'pinyin{i+1}.txt', 'w',encoding='utf8') as f:
#         for item in file:
#             f.write("\n%s" % item)
file = pinyinit(trans[4])
with open(f'pinyin{5}.txt', 'w',encoding='utf8') as f:
    for item in file:
        f.write("\n%s" % item)