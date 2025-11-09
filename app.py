from flask import Flask, render_template, request, jsonify
from save_lead import salvar_lead

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # exibe seu site

@app.route('/api')
def api_status():
    return jsonify({"message": "API funcionando!"})

@app.route('/salvar', methods=['POST'])
def salvar():
    data = request.get_json()
    salvar_lead(data)
    return jsonify({"message": "Lead salvo com sucesso!"})

if __name__ == '__main__':
    app.run()
