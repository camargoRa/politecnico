from flask import Flask, render_template, redirect, request
import MySQLdb

app = Flask(__name__)

DB_HOST = 'localhost'
DB_NAME = 'ruta_db'
DB_USER = 'root'
DB_PASSWORD = ''

def connectar_db():
    try:
        return MySQLdb.connect(host = DB_HOST,
                            db = DB_NAME,
                            user = DB_USER, 
                            passwd = DB_PASSWORD)
    except MySQLdb.Error as e:
        print(f"Error AL conectar a MySql: {e}")
        return None
@app.route('/', methods=['GET', 'POST'])
def mi_formulario():
    conexion = connectar_db()
    cursor = None
    resultados = []
    mensaje = None

    if conexion:
        cursor = conexion.cursor()
        if request.method == 'POST':
            # Obtener los datos del formulario
            campo1 = request.form['campo1']
            campo2 = request.form['campo2']
            # ... obtener otros campos ...

            try:
                # Insertar datos en la tabla (ejemplo)
                cursor.execute("INSERT INTO users (user, password) VALUES (%s, %s)", (campo1, campo2))
                conexion.commit()
                mensaje = "Datos guardados exitosamente."
            except MySQLdb.Error as e:
                mensaje = f"Error al guardar datos: {e}"
                conexion.rollback()

        # Consultar datos de la tabla para mostrar en el formulario (ejemplo)
        try:
            cursor.execute("SELECT * FROM users")
            resultados = cursor.fetchall()
        except MySQLdb.Error as e:
            print(f"Error al consultar datos: {e}")

        cursor.close()
        conexion.close()

    return render_template('mi_formulario.html', resultados=resultados, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)