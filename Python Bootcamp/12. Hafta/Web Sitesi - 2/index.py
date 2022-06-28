from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    books = [
        {
            "bookId": 1,
            "bookTitle": "Suç ve Ceza",
            "bookAutor": "Dosteyovski",
            "bookYear": 1897
        },
        {
            "bookId": 2,
            "bookTitle": "Hamlet",
            "bookAutor": "Shakspear",
            "bookYear": 1796
        },
        {
            "bookId": 3,
            "bookTitle": "Erteleme",
            "bookAutor": "Lewandovski",
            "bookYear": 2007
        }
    ]
    return render_template("index.html", books=books)


@app.route("/book/<string:id>")
def bookdetail(id):
    return "book id:" + id


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
