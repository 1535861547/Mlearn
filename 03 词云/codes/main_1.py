# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文本
text = open('E:/FreeGame/百度网盘/代码/精简版/03 词云/03 词云/constitution.txt').read()
# 生成对象
wc = WordCloud().generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')#确定字体的排列组合方式
plt.axis('off')#将坐标轴隐去
plt.show()

# 保存到文件
wc.to_file('wordcloud.png')