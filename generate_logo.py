from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io
import base64
import requests
from os import path


def generate_fig(url, mask):
    if path.exists("logo-app/static/images/logo.png"):
        with open("logo-app/static/images/logo.png", "rb") as imageFile:
            str = "data:image/png;base64,"
            str += base64.b64encode(imageFile.read()).decode("utf8")
            return str
    content = parse_content(url)
    wc_mask = np.array(Image.open(mask))
    wc = generate_wordcloud(content, wc_mask)
    return generate_image(wc, wc_mask)


def parse_content(url):
    r = requests.get(url)
    parsed_content = bs(r.content, features="html.parser")
    clean_raw_content = "".join(parsed_content.findAll(text=True))
    return clean_raw_content


def generate_wordcloud(content, mask=None):
    stopwords = set(STOPWORDS)
    stopwords.update(["see", "use", "using", "tutorial", "Node", "js", "file"])

    if mask is not None:
        wc = WordCloud(
            background_color="black",
            max_words=2000,
            mask=mask,
            contour_width=10,
            contour_color="white",
            stopwords=stopwords,
        ).generate(content)
    else:
        wc = WordCloud(
            background_color="black",
            max_words=2000,
            contour_width=10,
            contour_color="white",
            stopwords=stopwords,
        ).generate(content)
    return wc


def generate_image(wc, mask=None):
    fig, axes = plt.subplots(1, 1)
    plt.axis("off")
    if mask is not None:
        image_colors = ImageColorGenerator(mask)
        axes.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # TODO TEST TO SEE IF THIS WORKS
    else:
        axes.imshow(wc, interpolation="bilinear")

    bytes_image = io.BytesIO()
    plt.savefig("logo-app/static/images/logo.png", format="png", facecolor="black")
    plt.savefig(bytes_image, format="png", facecolor="black")
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(bytes_image.getvalue()).decode("utf8")

    return pngImageB64String
