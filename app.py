from flask import Flask, render_template, request, jsonify
import csv, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()

    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')

    if not all([nome, email, telefone]):
        return jsonify({'message': 'Preencha todos os campos!'}), 400

    file_exists = os.path.isfile('leads.csv')
    with open('leads.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Nome', 'Email', 'Telefone'])
        writer.writerow([nome, email, telefone])

    return jsonify({'message': 'Lead cadastrado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
