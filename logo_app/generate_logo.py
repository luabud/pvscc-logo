import base64
import io
import pathlib
from os import path

import httpx
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup as bs
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

def generate_fig(url, mask_path):
    logo_path = mask_path.parent / "logo.png"
    if not logo_path.exists():
        parsed_content = parse_content("https://code.visualstudio.com/docs/python/editing")
        wc = generate_wordcloud(parsed_content,np.array(Image.open(mask_path)))
        generate_image(logo_path, wc, np.array(Image.open(mask_path)))

    return "/static/images/logo.png"

def parse_content(url):
    parsed_content = bs(httpx.get(url).content, features="html.parser")
    clean_raw_content = "".join(parsed_content.findAll(text=True))
    return clean_raw_content

def generate_wordcloud(content, mask=None):
    stopwords = STOPWORDS | {"see", "use", "using", "tutorial", "Node", "js", "file" }
    
    wc = WordCloud(background_color="black", max_words=2000, mask=mask, contour_width=10, contour_color="white", stopwords=stopwords)

    return wc.generate(content)

def generate_image(logo_path, wc, mask=None):
    fig, axes = plt.subplots(1, 1)
    plt.axis("off")
    if mask is not None:
        image_colors = ImageColorGenerator(mask)
        wc = wc.recolor(color_func=image_colors)

    axes.imshow(wc, interpolation="bilinear")

    plt.savefig(logo_path, format="png", facecolor="black")

if __name__ == "__main__":
    url="https://code.visualstudio.com/docs/python/editing"
    mask_path = (
        pathlib.Path(__file__).parent /  "images" / "python-colored-mask.png"
    )
    generate_fig("https://code.visualstudio.com/docs/python/python-tutorial",mask_path)