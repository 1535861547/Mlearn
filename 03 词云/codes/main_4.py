# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open('E:/FreeGame/百度网盘/代码/精简版/03 词云/03 词云/xyj.txt',encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 生成对象
mask = np.array(Image.open("E:/FreeGame/百度网盘/代码/精简版/03 词云/03 词云/black_mask.png"))
wc = WordCloud(mask=mask, font_path='./fonts/simhei.ttf', mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file('wordcloud.png')