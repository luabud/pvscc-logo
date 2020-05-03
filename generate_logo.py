import io
from bs4 import BeautifulSoup as bs
import pathlib
from os import path
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud
import httpx
import matplotlib.pyplot as plt
import numpy as np


def generate_fig(url, mask_path):
    logo_path = mask_path.parent / "logo.png"
    if not logo_path.exists():

        content = parse_content(url)
        wc_mask = np.array(Image.open(mask_path))
        wc = generate_wordcloud(content, wc_mask)
        generate_image(logo_path, wc, wc_mask)

    return "/static/images/logo.png"


def parse_content(url):
    r = httpx.get(url)
    parsed_content = bs(r.content, features="html.parser")
    clean_raw_content = "".join(parsed_content.findAll(text=True))
    return clean_raw_content


def generate_wordcloud(content, mask=None):
    stopwords = STOPWORDS | {
        "see",
        "use",
        "using",
        "tutorial",
        "Node",
        "js",
        "file",
    }
    
    wc = WordCloud(
        background_color="black",
        max_words=2000,
        mask=mask,
        contour_width=10,
        contour_color="white",
        stopwords=stopwords,
    )

    return wc.generate(content)


def generate_image(logo_path, wc, mask=None):
    fig, axes = plt.subplots(1, 1)
    plt.axis("off")
    if not mask:
        image_colors = ImageColorGenerator(mask)
        wc = wc.recolor(color_func=image_colors)

    axes.imshow(wc, interpolation="bilinear")

    plt.savefig(logo_path, format="png", facecolor="black")
