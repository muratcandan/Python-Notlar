from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3


def veriEkle(product_name, product_type, product_price, history, user, kalanpara):
    with sqlite3.connect("product.db") as con:
        cur = con.cursor()
        cur.execute(
            "insert into tblproduct (product_name, product_type, product_price,history,user,kalanpara) values (?, ?, ?, ?, ?,?)", (product_name, product_type, product_price, history, user, kalanpara))
        con.commit()
    print("veriler eklendi")


data = []


def veriAl():
    global data
    with sqlite3.connect("product.db") as con:
        cur = con.cursor()
        cur.execute("select * from tblproduct order by id desc ")
        data = cur.fetchall()
        for i in data:
            print(i)


def veriSil(id):
    with sqlite3.connect("product.db") as con:
        cur = con.cursor()
        cur.execute("delete from tblproduct where id=?", (id,))


def veriGuncelle(id, product_name, product_type, product_price, history, user, kalanpara):
    with sqlite3.connect("product.db") as con:
        cur = con.cursor()
        cur.execute("update tblproduct set product_name = ?, product_type = ?, product_price = ?, history = ?, user = ?, kalanpara = ? where id = ?",
                    (product_name, product_type, product_price, history, user, kalanpara, id,))
        con.commit()
    print("Veriler Guncellendi...")


veriAl()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product/<string:id>")
def urundetay(id):
    detayveri = []
    for d in data:
        if str(d[0]) == id:
            detayveri = list(d)
    return render_template("urundetay.html", veri=detayveri)


@app.route("/productedit/<string:id>", methods=["GET", "POST"])
def productedit(id):
    if request.method == "POST":
        id = request.form["id"]
        product_name = request.form["product_name"]
        product_type = request.form["product_type"]
        product_price = request.form["product_price"]
        history = request.form["history"]
        user = request.form["user"]
        kalanpara = request.form["kalanpara"]
        print("Guncellenecek Veriler : ", product_name,
              product_type, product_price, history, user, kalanpara)
        veriGuncelle(id, product_name, product_type,
                     product_price, history, user, kalanpara)
        return redirect(url_for("gelirgider"))
    else:
        guncellenecekveri = []
        for d in data:
            if str(d[0]) == id:
                guncellenecekveri = list(d)
        return render_template("productedit.html", veri=guncellenecekveri)


@app.route("/productadd", methods=["POST", "GET"])
def productadd():
    if request.method == "POST":
        product_name = request.form["product_name"]
        product_type = request.form["product_type"]
        product_price = request.form["product_price"]
        history = request.form["history"]
        user = request.form["user"]
        kalanpara = request.form["kalanpara"]

        print("Eklenecek Veriler : ", product_name,
              product_type, product_price, history)
        veriEkle(product_name, product_type,
                 product_price, history, user, kalanpara)

    return render_template("productadd.html")


@app.route("/gelirgider")
def gelirgider():
    veriAl()
    return render_template("gelirgider.html", veri=data)


@app.route("/productdelete/<string:id>")
def productdelete(id):
    veriSil(id)
    return redirect(url_for("gelirgider"))


@app.route("/api", methods=["GET"])
def api():
    veriAl()
    print(data)
    veri = [{'id': str(row[0]), 'product_name': row[1],
             'product_type': row[2], 'product_price': row[3], 'history': row[4], 'user': row[5], 'kalanpara': row[6]} for row in data]
    return jsonify(veri)


@app.route("/api/add", methods=["POST"])
def apiAdd():
    product_name = request.form['product_name']
    product_type = request.form['product_type']
    product_price = request.form['product_price']
    history = request.form['history']
    user = request.form['user']
    kalanpara = request.form['kalanpara']

    veriEkle(product_name, product_type,
             product_price, history, user, kalanpara)

    message = 'The product has been successfully saved.'

    return jsonify({'status': 'success', 'result': message})


if __name__ == "__main__":
    app.run(debug=True)
