
com1 = open('complete1.txt', encoding="utf8").read().split('\n')
com2 = open('complete2.txt', encoding="utf8").read().split('\n')
com3 = open('complete3.txt', encoding="utf8").read().split('\n')
com4 = open('complete4.txt', encoding="utf8").read().split('\n')
com5 = open('complete5.txt', encoding="utf8").read().split('\n')
com6 = open('complete6.txt', encoding="utf8").read().split('\n')
com = [com1, com2, com3, com4, com5, com6]

def clean(files):
    text = []
    for word in files:
        each = word.split(',')
        print(each)
        audio = each[3].replace('audios/', '[sound:').replace('3','3]')
        plus = word+","+audio
        text.append(plus)
    return text

for i in range(0,6):
    file = clean(com[i])
    with open(f'anki{i+1}.txt', 'w',encoding='utf8') as f:
        for item in file:
            f.write("%s\n" % item)
