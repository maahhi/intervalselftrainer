import pandas as pd
import matplotlib.pyplot as plt
from bidict import bidict

answerinterp = bidict(
    {'u': 0, 's': 1, '2': 2, '3min': 3, '3maj': 4, '4': 5, '5dim': 6, '5': 7, '6min': 8, '6maj': 9, '7min': 10,
     '7maj': 11, 'o': 12,
     '-s': -1, '-2': -2, '-3min': -3, '-3maj': -4, '-4': -5, '-5dim': -6, '-5': -7, '-6min': -8, '-6maj': -9,
     '-7min': -10, '-7maj': -11, '-o': -12, })


df = pd.read_csv('dataset.csv')
dft = pd.read_csv('traindataset.csv')

#dft[dft['correct_answer']==0].groupby('session')['difference','bin_difference'].mean().plot.bar()
#plt.xticks(rotation=0)
#plt.title('u')
#plt.show()
dft['inv_bin_diff'] = ~dft['bin_difference']
for k in answerinterp.keys():
    print(k)
    dft[dft['correct_answer']==answerinterp[k]].groupby('session')['inv_bin_diff'].count().plot()
    dft[dft['given_answer']==answerinterp[k]].groupby('session')['inv_bin_diff'].count().plot()
    plt.xticks(rotation=0)
    plt.title(k)
    #plt.savefig('.\\fig\\train_diff_by_session\\'+'i'+k)
    plt.show()