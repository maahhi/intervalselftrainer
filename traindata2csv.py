import pandas
import pandas as pd
import os
current_path = ['.','train_sessions']
path = current_path
columns = ['session', 'root', 'interval', 'instrument', 'group', 'given_answer',
       'correct_answer', 'difference', 'bin_difference', 'ascending']
#df = pandas.DataFrame(columns=columns)
dflist = []
path_ = os.path.join(*path)
for x in os.walk(path_):
    #print(x)
    if len(x[2]) < 1:
        continue

    group = x[0].split('\\')[-1]
    instrument = x[0].split('\\')[-2]
    session = int(x[0].split('\\')[-3][-2:])

    file_path = x[0]
    #print(group,session,instrument,file_path)
    q_file = os.path.join(file_path,'question.txt')
    a_file = os.path.join(file_path,'given_answer.txt')

    with open(q_file, 'r') as qf,open(a_file, 'r') as af:
        while True:
            qline = qf.readline().strip()
            aline = af.readline().strip()
            print('--------',qline,aline)
            if qline == None or aline== None or qline == '' or aline == '':
                break
            root = int(qline.split()[0])
            interval = int(qline.split()[1])
            correct_answer = interval-root
            given_answer = int(aline)
            row = [session,root,interval,instrument,group,given_answer,correct_answer,
                   abs(correct_answer-given_answer),correct_answer==given_answer,interval>root]
            print(row)
            dflist.append(row)
print(len(dflist))
df = pd.DataFrame.from_records(dflist,columns=columns)
print(df)
df.to_csv('traindataset.csv',index= False)


