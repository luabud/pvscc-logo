from . import app
from flask import render_template
import generate_logo

url = "https://code.visualstudio.com/docs/python/python-tutorial"
mask = "logo-app\static\images\python-colored-mask.png"
@app.route('/')
def index():
    output = generate_logo.generate_fig(url,mask)

    return render_template('index.html', image=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



# @app.route('/')
# def index():
#     return 'Hello World!'
    # output = generate_fig("https://code.visualstudio.com/docs/python/python-tutorial")
    # return Response(output.getvalue(), mimetype="image/png")
    

