# ============================================================
# El juego del destino - Aplicación Flask
# Rutas:
#   /        -> muestra el formulario (GET)
#   /enviar  -> recibe el formulario (POST), guarda en sesión y redirige
#   /futuro  -> muestra la predicción usando los datos de la sesión (GET)
# ============================================================
import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# La sesión necesita una clave secreta para firmar la cookie
app.secret_key = "clave_secreta_del_dojo"

# Lista de profesiones que aparecerán en el <select> (BONUS DE PLATA)
PROFESIONES = [
    "Programador/a",
    "Astronauta",
    "Chef",
    "Piloto",
    "Músico/a",
    "Detective",
]


@app.route("/")
def index():
    """Muestra el formulario."""
    return render_template("index.html", profesiones=PROFESIONES)


@app.route("/enviar", methods=["POST"])
def enviar():
    """Recibe los datos del formulario y los guarda en la sesión."""
    session["nombre"] = request.form["nombre"]
    session["lugar"] = request.form["lugar"]
    session["numero"] = request.form["numero"]
    session["comida"] = request.form["comida"]
    session["profesion"] = request.form["profesion"]

    # BONUS DE ORO: elegir al azar el tipo de predicción
    # y guardarlo en sesión para que no cambie al recargar la página
    session["tipo_destino"] = random.choice(["bueno", "malo"])

    # Redirigimos para evitar que el formulario se reenvíe al recargar
    return redirect("/futuro")


@app.route("/futuro")
def futuro():
    """Muestra la predicción con los datos guardados en la sesión."""
    # Si alguien entra directo a /futuro sin llenar el formulario,
    # lo mandamos de vuelta al inicio
    if "nombre" not in session:
        return redirect("/")
    return render_template("futuro.html")


if __name__ == "__main__":
    app.run(debug=True)
