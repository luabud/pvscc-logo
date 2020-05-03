import pathlib

from flask import Flask, render_template

from . import generate_logo
from . import app


@app.route("/")
def index():
    url = "https://code.visualstudio.com/docs/python/python-tutorial"
    mask_path = (
        pathlib.Path(__file__).parent / "static" / "images" / "python-colored-mask.png"
    )
    output = generate_logo.generate_fig(url, mask_path)

    return render_template("index.html", image=output)
