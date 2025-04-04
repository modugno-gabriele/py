from flask import Flask, render_template
app = Flask(__name__)
x = "ciao"
lista = ["pane","ramen","cipolla","gatto","cane"]
@app.route('/aggiungi',methods=["POST"])
def home():
 return render_template("index.html",lista = lista)
if __name__ == '__main__':
  app.run(debug=True)