from . import app

@app.route('/')
def index():
    return 'Hello World!'
    # output = generate_fig("https://code.visualstudio.com/docs/python/python-tutorial")
    # return Response(output.getvalue(), mimetype="image/png")
    