from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import random
import numpy as np

text = open('E:/FreeGame/百度网盘/代码/精简版/03 词云/03 词云/xyj.txt',encoding='utf-8').read()
text = ''.join(jieba.cut(text))

mask = np.array(Image.open('E:/FreeGame/百度网盘/代码/精简版/03 词云/03 词云/color_mask.png'))
wc = WordCloud(font_path='./fonts/simhei.ttf',width=900,height=400,ranks_only=0.5,mask=mask,mode='RGBA',background_color=None).generate(text)


def random_color(word, font_size, position, orientation, font_path, random_state):
	s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
	print(s)
	return s

image_colors=ImageColorGenerator(mask)
wc.recolor(color_func=random_color)

plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file('wordcloud.png')