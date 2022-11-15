import pandas as pd
import os
current_path = ['.']
path = current_path+ ['groups']
columns = ['session','instrument','group','root','interval','correct_ans','given_ans']
for x in os.walk("train_sessions"):
    if len(x[2]) < 1:
        continue
    group = x[0].split('\\')[-1]
    instrument = x[0].split('\\')[-2]
    session = x[0].split('\\')[-3][-2]
    file_name_g = os.path.join(x[0],file)
    with open(file_name, 'r') as f:
        for line in f:
            if file[0] == g

