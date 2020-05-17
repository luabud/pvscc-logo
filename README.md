# pvscc-logo
Demo for creating a word cloud based on the [Python for VS Code](https://code.visualstudio.com/docs/python/python-tutorial) Getting Started Tutorial.


![Logo](images/logo.png)

## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Create a virtual environment 
- In the project's directory, create a new virtual environment using Python 3 and activate it.

    On Windows:
     ```shell
    $ py -m venv env
    $ env\Scripts\activate
    ```
    On MacOs/Linux:
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
## Install the dependencies
- Install dependencies from requirements.txt:
    On MacOs/Linux:
    ```shell
    (env)$ pip install -r requirements.txt
    ```

## Create a Flask app
- Open the project folder in VS Code:
    ```shell
    $ code .
    ```
- Create a folder called `logo_app` and move the `generate_logo.py` file to it
- In `logo_app`, create a `__init__.py` file with the following content:
    ```py
    from flask import Flask

    app = Flask(__name__)
    ```
- In the same folder, create a `webapp.py` file:    
    ```py
    from . import views

    from . import app
    ```
- Then create a `views.py` file:
    ```py
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
    ```
- Still under `logo_app`, create a folder called `templates`. Under `templates`, create a `index.html` file:
    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>{% block title %} Word Cloud Generator {% endblock %}</title>
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='site.css')}}" />
        </head>
        </body>
            <div class="body-content">
                
                {% block content %}      
                <img src= {{image}} >
                {% endblock %}
            </div>
        </body>
    </html>
    ```

- Create a folder called `static` located under `logo_app`. Under `static`, create a file called `site.css`:
    ```css
    * {
        background-color: black;
    }
    ```
- Move the `images` folder located under the project root to `logo_app/static`

## Run the Flask app
- Make sure the Python interpreter selected on the status bar (on the bottom left) matches the one from the environment you created. If not, select it opening the command palette (`View` > `Command Palette...`) and running the `Python: Select Interpreter` command)
- Press <kbd>F5</kbd> to start debugging, or <kbd>Ctrl</kbd> + <kbd>F5</kbd> to run without debugging

- From the debug configuration menu, select `Flask`. Then enter `logo_app/webapp` as the entry point to your application. 

- Press <kbd>Ctrl</kbd> and click on the link that will be displayed on the terminal:
    ```
    * Serving Flask app "logo_app.webapp" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 171-261-395
    * Running on http://127.0.0.1:5000/
    ```

