import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号

data = pd.read_excel('data/data.xls')
# print(data)

plt.figure(figsize=(8,4))
data.province.value_counts().plot(kind = 'bar',color = 'pink')
# rotation = 坐标标签旋转一定角度(美观)
plt.xticks(rotation = 0)
plt.xlabel('省份')
plt.ylabel('数量')
plt.title('不同省份伞数量分布')
# 绘制网格线
# plt.grid()
plt.show()

#建立透视表
data1 = data.pivot_table(index = 'province',values ='sales',aggfunc=np.mean)
data1.sort_values('sales',inplace=True,ascending=False)
data1 =  data1.reset_index()
index = np.arange(data1.sales.size)
plt.figure(figsize=(8,4))
plt.bar(index,data1.sales,color = 'pink')
plt.xticks(index,data1.province,fontsize = 11,rotation = 0)
plt.xlabel('省份')
plt.ylabel('平均销量')
plt.title('不同省份平均销量分布')
plt.show()

plt.figure(figsize=(8,4))
plt.imshow(data1)
plt.colorbar()
plt.show()
data1.to_excel('data/pro_sales.xlsx')