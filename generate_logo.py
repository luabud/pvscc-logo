# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Generating Logo for PVSC
# %% [markdown]
# Initial exploration for raw content of docs
# 

# %%
import requests
# from https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('(<.*?>)|\\n|\\r|\\t|\(|\)|\{|\}|\]|\[')
    return re.sub(clean, '', text)

r = requests.get(url="https://code.visualstudio.com/docs/python/python-tutorial")
raw_content = r.content.decode("utf-8")

clean_raw_content = remove_html_tags(raw_content)


# %%

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np 
from PIL import Image, ImageFile
from os import path
import os
#raw_words = clean_raw_content.split()
ImageFile.LOAD_TRUNCATED_IMAGES = True
stopwords = set(STOPWORDS)
stopwords.update(["see","quot","use", "using", "tutorial", "Python", "Node", "js", "file"])

python_mask = np.array(Image.open("images/python-colored-mask.png"))
wc = WordCloud(background_color="white", max_words=2000, mask=python_mask,
 contour_width=3, contour_color='steelblue',stopwords=stopwords).generate(clean_raw_content) 

image_colors = ImageColorGenerator(python_mask)
# %%
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,1)

# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.show()