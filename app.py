from flask import Flask, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def serve_html():
    # Ejecuta el script de Python para actualizar output.html
    subprocess.run(["python", "Finance.py"])
    # Sirve el archivo HTML
    return send_from_directory('.', 'output.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
