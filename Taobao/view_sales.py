# coding = 'utf-8'

import numpy as np
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt

data = pd.read_csv('df_word_sum.csv')
data.sort_values('w_s_sum',inplace=True,ascending=True)
df_w_s = data.tail(30)

font = {'family':'SimHei'}
mplt.rc('font',**font)

index = np.arange(df_w_s.word.size)
plt.figure(figsize=(6,12))
# plt.barh(index,df_w_s.w_s_sum)

plt.barh(index,df_w_s.w_s_sum,color = 'pink',align = 'center',alpha=0.8)

#添加数字标签
for y,x in zip(index,df_w_s.w_s_sum):
    plt.text(x/2,y,'%.0f' %x,ha='left',va='center',fontsize = 11)
# plt.show()
i=0
for y,x,z in zip(index,df_w_s.w_s_sum,df_w_s.word):
    plt.text(x,y,z,ha='left',va='center',fontsize = 11)
    i+=1




plt.show()
