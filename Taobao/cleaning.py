import missingno as msno
import pandas as pd

datamsp = pd.read_excel('datamap.xls')

print(datamsp.shape)
'''
# msno.matrix(datamsp,labels=True,inline=True)


msno.bar(datamsp.sample(len(datamsp)),figsize=(10,4),inline=True)



#删除缺失值过半的列
half_count = len(datamsp)/2
datamsp = datamsp.dropna(thresh =half_count,axis= 1)

#删除重复行
datamsp = datamsp.drop_duplicates()
print(datamsp.shape)

'''

#提取数据

data=datamsp[['item_loc','raw_title','view_price','view_sales']].copy()


#拆分省会和城市
data['province'] = data.item_loc.apply(lambda x: x.split()[0])
data['city'] = data.item_loc.apply(lambda x: x.split()[0] if len(x)<4 else x.split()[1])
data['sales'] = data.view_sales.apply(lambda x: x.split('人')[0])
data = data.drop(['item_loc','view_sales'],axis=1)

data.to_excel('data.xls',index = False)
