from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") #Bu komutla yeni site içinde alt site oluşturabiliyoruz
def index():
    isim = "Murat Candan" #burada isim tanımladık altta html dosyasında kullanabilir hale getirdik
    return render_template("index.html", name = isim)

@app.route("/contact") #ikinci bir alt site oluşturduk
def contact():
    return "iletişim sayfası"

if __name__ == "__main__":
    app.run(debug = True)

