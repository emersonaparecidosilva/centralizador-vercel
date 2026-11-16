import json
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

def carregar_links():
    caminho = os.path.join(os.path.dirname(__file__), "../data/links.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    categorias = carregar_links()
    return render_template("index.html", categorias=categorias)

# Necessário para execução local
if __name__ == "__main__":
    app.run(debug=True)