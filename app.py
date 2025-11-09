from flask import Flask, render_template, request, jsonify
from save_lead import save_lead
import logging

# Configuração de logs (para depurar no Vercel)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza o site principal

@app.route('/api')
def api_status():
    return jsonify({"message": "API funcionando corretamente!"})

@app.route('/salvar', methods=['POST'])
def salvar():
    try:
        data = request.get_json()
        app.logger.debug(f"Dados recebidos: {data}")

        # Extrair dados do formulário
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        # Verificar campos obrigatórios
        if not name or not email or not phone:
            return jsonify({"success": False, "message": "Campos incompletos."}), 400

        # Salvar lead na planilha
        result = save_lead(name, email, phone)

        # Retornar resposta
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"Erro ao salvar lead: {str(e)}", exc_info=True)
        return jsonify({"success": False, "message": f"Erro no servidor: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
