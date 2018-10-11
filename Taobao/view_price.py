import numpy as np
import pandas as pd
from pandas import Series as sr,DataFrame as df
import matplotlib.pyplot as plt
#matplotlib的一个高级接口
import seaborn as sns

datas = pd.read_excel('data/data.xls')
# print(data.head())

sr1 = sr(datas.view_price)
sr2 = sr(datas.sales)
index = np.arange(sr1.size)
sr3 = sr(sr1*sr2)
data = df(data = list(zip(sr1,sr2,sr3)),index = index,columns=["price","sales","GMV"])
datan = df(data = list(zip(sr1,sr3)),index = index,columns=["price","GMV"])
# print(datan)
data = data.groupby("price").sum()
data.reset_index()
#绘图
# plt.figure(figsize=(6,12))


plt.bar(data.index,np.log(data["sales"]),color = 'pink')
plt.show()
'''
mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
x, y = np.random.multivariate_normal(mean, cov, 80).T
sns.regplot(x=x, y=y, color="g", marker="+")
'''
#pycharm中无法绘制图,可以选择spyder执行本脚本
sns.regplot(x="price",y = "GMV",data = datan,order = 2)



