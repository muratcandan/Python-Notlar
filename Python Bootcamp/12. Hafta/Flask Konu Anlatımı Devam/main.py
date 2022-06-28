from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") #Bu komutla yeni site içinde alt site oluşturabiliyoruz
def index():
    isim = "Murat Candan" #burada isim tanımladık altta html dosyasında kullanabilir hale getirdik
    yas = "37"

    book = dict()
    book["bookTitle"] = "Suç ve Ceza"
    book["bookDescription"] = "Rus Klasikleri"
    book["bookAutor"] = "Dosteyovski"
    book["bookYear"] = "1896"
    return render_template("index.html", name = isim, age = yas, book = book)

@app.route("/contact") #ikinci bir alt site oluşturduk
def contact():
    return "iletişim sayfası"

if __name__ == "__main__":
    app.run(debug = True)

