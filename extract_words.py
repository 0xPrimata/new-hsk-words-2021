import re
import zhon.hanzi

#extract
def e(old, new):
    vocab = []
    for word in new:
        if word not in old:
            vocab.append(word)
    return vocab
def clean(band):
    new = []
    for w in band:
        w = w.replace("（", " ")
        w = w.replace("｜", " ")
        a = w.split(" ")
        new.append(a[1])
    return new

hsk1 = open('hsk1.txt', encoding="utf8").read().split('，')
hsk2 = open('hsk2.txt', encoding="utf8").read().split('，')
hsk3 = open('hsk3.txt', encoding="utf8").read().split('，')
hsk4 = open('hsk4.txt', encoding="utf8").read().split('，')
hsk5 = open('hsk5.txt', encoding="utf8").read().split('，')
hsk6 = open('hsk6.txt', encoding="utf8").read().split('，')

band1 = clean(open('wordlist_band1.txt', encoding="utf8").read().split('\n'))
band2 = clean(open('wordlist_band2.txt', encoding="utf8").read().split('\n'))
band3 = clean(open('wordlist_band3.txt', encoding="utf8").read().split('\n'))
band4 = clean(open('wordlist_band4.txt', encoding="utf8").read().split('\n'))
band5 = clean(open('wordlist_band5.txt', encoding="utf8").read().split('\n'))
band6 = clean(open('wordlist_band6.txt', encoding="utf8").read().split('\n'))


new1 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band1))))))
new2 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band2))))))
new3 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band3))))))
new4 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band4))))))
new5 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band5))))))
new6 = e(hsk6,e(hsk5,e(hsk4,e(hsk3, e(hsk2, e(hsk1, band6))))))

with open('new6.txt', 'w',encoding='utf8') as f:
    for item in new6:
        f.write("%s\n" % item)


