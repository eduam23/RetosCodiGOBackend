from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB']= 'semana2reto2'

mysql = MySQL(app)

@app.route('/')
def index():

    return jsonify({

    "ok":True,
    "content": 'Utiliza /vacunas para ingresar una vacuna y /listadovacunas para listarlas',
    "message": "Bienvenido a mi API REST Flask"

    })

@app.route('/listadovacunas')
def get_listado():
    cursor =  mysql.connection.cursor()

    cursor.execute('select * from vacunas')

    data = cursor.fetchall()

    cursor.close()
    return jsonify({

    "ok":True,
    "content":data,
    "message": "Se ha realizado la consulta con éxito"

    })

@app.route('/vacunas', methods=['POST'])
def setVacunas():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']

    cursor =  mysql.connection.cursor()

    cursor.execute("insert into vacunas(nombre, descripcion) values('"+nombre+"','"+descripcion+"')")

    mysql.connection.commit()

    cursor.close()

    return jsonify({

    "ok":True,
    "content":'',
    "message": "Registro insertado exitosamente"

    })

app.run(debug=True,port=5000)
