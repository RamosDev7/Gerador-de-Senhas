from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
        
    if not caracteres:
        return "Selecione uma opção."

    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = "vR8!kQ2#pL7@xM4$" # Senha inicial visual
    
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 20))
        maiusculas = request.form.get("maiusculas") == "on"
        minusculas = request.form.get("minusculas") == "on"
        numeros = request.form.get("numeros") == "on"
        simbolos = request.form.get("simbolos") == "on"
        
        senha_gerada = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)
    
    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)