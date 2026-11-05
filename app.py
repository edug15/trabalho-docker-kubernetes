from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)
VERSION = "2.0" # Atualizado para a versão 2.0 para demonstrar versionamento
APP_NAME = "Demo GCS - Gerenciamento de Configuração de Software"

@app.route('/')
def home():
    hostname = socket.gethostname()
    # Usamos {{ e }} no CSS para escapar as chavetas na f-string do Python
    return f"""
    <!DOCTYPE html>
    <html lang="pt-PT">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #e9ecef;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: #ffffff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
            }}
            h1 {{
                color: #2c3e50;
                margin-top: 0;
                margin-bottom: 10px;
            }}
            .version {{
                font-size: 1.1em;
                color: #7f8c8d;
                margin-bottom: 25px;
            }}
            .status-box {{
                background-color: #d4edda;
                color: #155724;
                padding: 15px;
                border-radius: 6px;
                border: 1px solid #c3e6cb;
                margin-bottom: 30px;
                font-size: 1.1em;
            }}
            .pod-info {{
                background-color: #f8f9fa;
                padding: 25px 20px;
                border-radius: 8px;
                border: 1px dashed #ced4da;
                margin-bottom: 30px;
            }}
            .pod-info p {{
                margin: 0 0 15px 0;
                color: #6c757d;
                font-size: 1.05em;
            }}
            .hostname-badge {{
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 10px 25px;
                border-radius: 30px;
                font-size: 1.4em;
                font-weight: bold;
                font-family: monospace;
                letter-spacing: 1px;
                box-shadow: 0 4px 10px rgba(0, 123, 255, 0.3);
            }}
            .footer {{
                font-size: 0.9em;
                color: #adb5bd;
                border-top: 1px solid #f1f3f5;
                padding-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{APP_NAME}</h1>
            <div class="version">Versão da Imagem: <strong>{VERSION}</strong></div>
            
            <div class="status-box">
                ✅ <strong>Status:</strong> Funcionando perfeitamente em ambiente contentorizado!
            </div>
            
            <div class="pod-info">
                <p>Respondendo a partir do (Hostname/Pod):</p>
                <div class="hostname-badge">{hostname}</div>
            </div>
            
            <div class="footer">
                Trabalho 2 - PUCRS<br>
                <strong>Demonstração Prática: Docker & Kubernetes</strong>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": VERSION}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)