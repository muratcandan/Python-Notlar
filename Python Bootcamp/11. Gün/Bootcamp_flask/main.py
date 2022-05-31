from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    isim = "muratcandan"
    return render_template("index.html", name=isim)
    return "index sayfası burasıdır!!!"
    return "<h1> Index sayfası </h1>"


@app.route("/contact")
def contact():
    return "contact sayfası"


if __name__ == "__main__":
    app.run(debug=True)
# http://127.0.0.1:5000/contact yazarsak o sayfaya ulaşabliriz


# ctrl + c ile durdurabiliriz
