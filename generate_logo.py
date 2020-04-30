from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import io
import requests

target_url = "https://code.visualstudio.com/docs/python/python-tutorial"
mask = "images/python-colored-mask.png"


def generate_fig(target_url, mask):
    r = requests.get(url=target_url)
    parsed_content = bs(r.content, features="html.parser")
    clean_raw_content= ''.join(parsed_content.findAll(text=True))
    
    stopwords = set(STOPWORDS)
    stopwords.update(["see","use", "using", "tutorial", "Node", "js", "file"])

    python_mask = np.array(Image.open(mask))
    
    wc = WordCloud(background_color="black", max_words=2000, mask=python_mask,
    contour_width=10, contour_color='white',stopwords=stopwords).generate(clean_raw_content) 

    image_colors = ImageColorGenerator(python_mask)
    fig, axes = plt.subplots(1,1)
    axes.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis('off')
    
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png', facecolor="black")
    return bytes_image
    