from flask import Flask, request
from save_lead import salvar_lead
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite acesso do site local

@app.route("/salvar", methods=["POST"])
def salvar():
    data = request.get_json()
    salvar_lead(
        data.get("nome"),
        data.get("email"),
        data.get("telefone"),
        data.get("renda"),
        data.get("gastos")
    )
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
