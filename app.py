from flask import Flask, request, jsonify
from flask_cors import CORS
from save_lead import save_lead

app = Flask(__name__)
CORS(app)  # Permitir requisições do frontend

@app.route('/')
def home():
    return jsonify({"message": "API funcionando!"})

@app.route('/api/lead', methods=['POST'])
def create_lead():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        
        result = save_lead(name, email, phone)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Para Vercel
if __name__ == '__main__':
    app.run()