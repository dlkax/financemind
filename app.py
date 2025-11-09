from flask import Flask, render_template, request, jsonify
from save_lead import save_lead  # usa exatamente o nome da função correta
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

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

        result = save_lead(name, email, phone)

        if result["success"]:
            return jsonify({"message": "Lead salvo com sucesso!"}), 200
        else:
            return jsonify({"error": result["message"]}), 400

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
