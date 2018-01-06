from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/assets")


@app.route('/')
def index():
    return render_template("en/index.html")


@app.route('/<name>/')
def ret(name):
    if len(name) == 2:
        return render_template("%s/index.html"%name)
    return render_template("en/%s.html" % name)


@app.route('/<language>/<name>/')
def retcn(language, name):
    print(language, name)
    return render_template("/%s/%s.html" % (language, name))


if __name__ == '__main__':
    app.run()
