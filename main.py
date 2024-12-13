from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html", judul='Home')

@app.route("/Profil")
def profil():
    return render_template ("profil.html", judul='Profil')

@app.route("/Visimisi")
def visimisi():
    return render_template ("visimisi.html", judul='Visi Misi')

@app.route("/Kontak")
def kontak():
    return render_template ("kontak.html", judul='Kontak')

@app.route("/Tentangkami")
def tentangkami():
    return render_template ("tentangkami.html", judul='Tentang Kami')

@app.route("/Produkkami")
def produkkami():
    return render_template ("produkkami.html", judul='Produk Kami')

@app.route("/Galeri")
def galeri():
    return render_template ("galeri.html", judul='Galeri')

@app.route("/Event")
def event():
    return render_template ("event.html", judul='Event')

@app.route("/Klient Kami")
def klient():
    return render_template ("klient.html", judul='Klient Kami')


if __name__ == "__main__":
    app.run(debug=True)