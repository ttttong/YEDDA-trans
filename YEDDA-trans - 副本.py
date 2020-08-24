import re

# txt2ner_train_data turn label str into ner trainable data
# save_path: ner_trainable_txt name
def str2ner_train_data(s, save_path):
    ner_data = []
    result_1 = re.finditer(r'\[\@', s)
    result_2 = re.finditer(r'\*\]', s)
    # result_3 = re.finditer(r'\[\$', s)
    begin = []
    end = []
    for each in result_1:
        begin.append(each.start())
    for each in result_2:
        end.append(each.end())
    assert len(begin) == len(end)
    # for each in result_3:
    #     begin.append(each.start())
    i = 0
    j = 0
    while i < len(s):
        if i not in begin:
            ner_data.append([s[i], 0])
            i = i + 1
        else:
            ann = s[i + 2:end[j] - 2]
            entity, ner = ann.rsplit('#')
            if (len(entity) == 1):
                ner_data.append([entity, 'S-' + ner])
            else:
                if (len(entity) == 2):
                    ner_data.append([entity[0], 'B-' + ner])
                    ner_data.append([entity[1], 'E-' + ner])
                else:
                    ner_data.append([entity[0], 'B-' + ner])
                    for n in range(1, len(entity) - 1):
                        ner_data.append([entity[n], 'I-' + ner])
                    ner_data.append([entity[-1], 'E-' + ner])

            i = end[j]
            j = j + 1

    f = open(save_path, 'w', encoding='utf-8')
    for each in ner_data:
        f.write(each[0] + ' ' + str(each[1]))
        f.write('\n')
    f.close()


# txt2ner_train_data turn label str into ner trainable data
# save_path: ner_trainable_txt name
def txt2ner_train_data(file_path, save_path):
    fr = open(file_path,'r',encoding='utf-8')
    lines = fr.readlines()
    s = ''
    for line in lines:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        s = s + line
    fr.close()
    str2ner_train_data(s, save_path)


if (__name__ == '__main__'):
    file_path = 'C:\\Users\\lenovo\\Desktop\\heri1.txt.ann'
    txt2ner_train_data(file_path, 's1.txt')