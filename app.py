from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = ""
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 12))
        senha_gerada = gerar_senha(tamanho)

    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)