from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():

    lstDepartamentos = ['Ancash','Lima','Piura','La Libertad','Lambayeque']
    return jsonify({

    "ok":True,
    "content": lstDepartamentos,
    "message": "Bienvenido a mi API REST Flask"

    })


app.run(debug=True,port=5000)
