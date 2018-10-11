import jieba
import pandas as pd
import numpy as np


data = pd.read_excel("data.xls")
# print(data.shape)
# print(data.head())

title = data.raw_title.values.tolist()
# print(title)
title_s = []
#对每个标题进行分词
print("#对每个标题进行分词...")
for line in title:
    title_cut = jieba.lcut(line)
    title_s.append(title_cut)

#导入停用词表
print("#导入停用词表...")
stopwords = ["的", "了", "在", "是", "我", "有", "和", "就",
        "不", "人", "都", "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你",
        "会", "着", "没有", "看", "好", "自己", "这" ]

# 删除停用词
print("# 删除停用词...")
title_cleand = []
for line in title_s:
    line_cleand = []
    for word in line:
        if word not in stopwords:
            line_cleand.append(word)
    title_cleand.append(line_cleand)

# 分词去重
print("# 分词去重...")
title_cleand_dist = []
for line in title_cleand:
    line_dist = []
    for word in line:
        if word not in line_dist:
            line_dist.append(word)
    title_cleand_dist.append(line_dist)

# 转化为list
print("# 转化为list...")
allwords_cleand_dist = []
for line in title_cleand_dist:
    for word in line:
        allwords_cleand_dist.append(word)

# 转为数据框
print("# 转为数据框...")
df_allwords_cleand_dist = pd.DataFrame({
    'allwords':allwords_cleand_dist
})

# 分类汇总
print("# 分类汇总...")
word_count = df_allwords_cleand_dist.allwords.value_counts().reset_index()
word_count.columns = ['word','count']

# word_count.to_csv("data_cleand_dist.csv")


'''
#添加新词
add_words = pd.read_excel('')
for w in add_words.words:
    jieba.add_word(w,freq = 1000)
'''

'''
统计所有标签的sale之和
'''

# 汇总sales
print("#汇总sales...")
w_s_sum = []
for word in word_count.word:
    i=0
    sale_list = []
    for line in title_cleand_dist:
        if word in line:
            sale_list.append(data.sales[i])
        i+=1
    # print(word,sum(sale_list))
    w_s_sum.append(sum(sale_list))

df_w_s_sum = pd.DataFrame({
    'w_s_sum':w_s_sum
})

df_word_sum = pd.concat([word_count,df_w_s_sum],axis=1,ignore_index=True)
df_word_sum.columns = ['word','count','w_s_sum']

df_word_sum.to_csv('df_word_sum.csv')




