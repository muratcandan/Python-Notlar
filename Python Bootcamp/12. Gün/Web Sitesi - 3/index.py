
from flask import Flask, render_template, request, redirect, url_for
import sqlite3


# veri tabanına veri ekleme


con = sqlite3.connect("book.db")


def veriekle(title, autor, year):
    with sqlite3.connect("book.db") as con:
        cur = con.cursor()
        cur.execute(
            "insert into tblBook (bookTitle, bookAutor, bookYear) values(?,?,?)", (title, autor, year))
        con.commit()
    print("veriler eklendi")


veriekle("yeni kitap", "yeni yazar", "yeni yıl")

data = []


def veriAl():
    global data
    with sqlite3.connect("book.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tblBook order by id desc")
        data = cur.fetchall()
        """print(data)"""
        for i in data:
            print(i)


def veriSil(id):
    with sqlite3.connect("book.db") as con:
        cur = con.cursor()
        cur.execute("delete from tblBook where id = ?", {id})


"""
veriAl()
print("----")
print(data)
"""

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


@app.route("/bookadd", methods=["POST", "GET"])
def bookadd():

    if request.method == "POST":
        bookTitle = request.form["bookTitle"]
        bookAutor = request.form["bookAutor"]
        bookYear = request.form["bookYear"]
        veriekle(bookTitle, bookAutor, bookYear)
        print(bookTitle, bookAutor, bookYear)

        return "Veri başarılı bir Şekilde Gönderildi"
    return render_template("bookadd.html")


@app.route("/kitap")
def kitap():
    veriAl()
    return render_template("kitap.html", veri=data)


@app.route("/bookdelete/<string:id>")
def bookdelete(id):
    veriSil(id)
    return redirect(url_for("kitap"))


if __name__ == "__main__":
    app.run(debug=True)
