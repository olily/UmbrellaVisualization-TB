#coding = 'utf-8'
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

#可视化
word_count = pd.read_csv('data_cleand_dist.csv')

plt.figure(figsize=(20,10))
# pic = imread("mask.png") mask=pic,
w_c = WordCloud(
    font_path='shaonv.ttf',
    background_color='white',
    max_font_size=60,margin = 1
)

wc = w_c.fit_words({
    x[1]:x[2] for x in word_count.head(100).values
})
# 图优化
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.show()
