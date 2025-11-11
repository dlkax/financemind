from flask import Flask, render_template, request, jsonify
from save_lead import save_lead
import logging
from flask_cors import CORS

# Inicializa app e ativa CORS corretamente
app = Flask(__name__)
CORS(app, resources={
    r"/*": {"origins": ["https://financemind.net", "https://www.financemind.net"]}
})

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def api_status():
    return jsonify({"message": "API funcionando!"})

@app.route('/salvar', methods=['POST'])
def salvar():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        if not all([name, email, phone]):
            return jsonify({"error": "Campos incompletos."}), 400

        result = save_lead(name, email, phone)

        if result.get("success"):
            return jsonify({
                "message": "Formulario Enviado!\nEm breve um assistente entrará em contato."
            }), 200
        else:
            return jsonify({
                "error": result.get("message", "Erro ao salvar lead.")
            }), 500

    except Exception as e:
        logging.exception("Erro ao salvar lead:")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
