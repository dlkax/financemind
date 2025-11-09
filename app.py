from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "API funcionando!"})

@app.route('/api/lead', methods=['POST'])
def create_lead():
    try:
        # Importar aqui para evitar problemas
        from save_lead import save_lead
        
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        
        result = save_lead(name, email, phone)
        return jsonify(result)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "message": str(e)}), 500