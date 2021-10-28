from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

#Usted solo modifique de aqui para abajo

@app.route('/')
def hello_world():
    return 'Hola Mundo'

@app.route('/hola/<nombre>') 
def hola(nombre):
    print(nombre)
    return "Hola, " + nombre

@app.route('/usuario/<nombre>/<id>') 
def mostrar_perfil(nombre, id):
    print(nombre)
    print(id)
    return "Nombre: " + nombre + ", id: " + id

@app.route('/vista')                           
def hola_vista():
    return render_template('index.html') 

@app.route('/vista_atributos')                           
def hola_vista_atributos():
    return render_template('atributos.html',palabra='Hola',it = 5) 

@app.route('/mas_vista_atributos')
def mas_vista_atributos():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    personajes = [
       {'nombre' : 'Mia', 'pais' : 'EEUU'},
       {'nombre' : 'Jules', 'pais' : 'EEUU' },
       {'nombre' : 'Hans', 'pais' : 'Aleman' },
       {'nombre' : 'Rick', 'pais' : 'EEUU' }
    ]
    return render_template("lista_personajes.html", personajes = personajes)

@app.route('/formulario')
def formulario():
    return render_template("form.html")

@app.route('/crear_usuario', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("mostrar_usuario.html", name_on_template=name_from_form, email_on_template=email_from_form)

@app.route('/formulario_2')
def formulario2():
    return render_template("form2.html")

@app.route('/crear_usuario_2', methods=['POST'])
def create_user2():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect("/usuario_2")	

@app.route('/usuario_2')
def usuario():
    return render_template("mostrar_usuario_2.html")

#Usted solo modifique de aqui para arriba

if __name__=="__main__":
    app.run(debug=True)

