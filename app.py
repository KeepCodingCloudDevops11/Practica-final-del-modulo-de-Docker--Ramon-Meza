import os
import mysql.connector
from flask import Flask, request, jsonify, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Función para obtener una conexión a la base de datos
def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )
    return conn

@app.route('/', methods=['GET'])
def home():
    try:
        # Obtener el valor del contador desde la base de datos
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT count_value FROM counter WHERE id = 1')
        result = cursor.fetchone()
        conn.close()

        # Si no se encuentra el valor, maneja el caso
        if result is None:
            return jsonify({"error": "No se encontró el contador en la base de datos"}), 404

        # Renderizar la página HTML con el valor actual del contador
        return render_template('count.html', count=result['count_value'])
    except Exception as e:
        # Si ocurre un error, devuelve un mensaje de error
        return jsonify({"error": str(e)}), 500

    # Verificar si el resultado es None, en caso de que no haya un valor en la base de datos
    if result is None:
        count_value = 0  # Asignar un valor inicial en caso de no encontrar un registro
    else:
        count_value = result['count_value']

    # Renderizar la página HTML con el valor actual del contador
    return render_template('index.html', count=count_value)

@app.route('/count', methods=['POST'])
def update_count():
    try:
        new_count = request.json.get('count')
        if new_count is None:
            return jsonify({"error": "No se proporcionó el valor de 'count'"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE counter SET count_value = %s WHERE id = 1', (new_count,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Count updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
