from . import app
from flask import render_template
import generate_logo
import pathlib


@app.route("/")
def index():
    url = "https://code.visualstudio.com/docs/python/python-tutorial"
    mask = pathlib.Path(__file__).parent/"static"/"images"/"python-colored-mask.png"
    output = generate_logo.generate_fig(url, mask)

    return render_template("index.html", image=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
