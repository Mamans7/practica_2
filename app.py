from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
# Necesario cuando se usa sesion
#app.secret_key = 'clave_secreta'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/inscripcionCurso', methods=['GET', 'POST'])
def inscripcionCurso():
  if request.method == 'POST':
    nom = request.form['nombre']
    ap = request.form['apellido']
    cur = request.form['curso']
    return render_template('inscripcionCurso.html', nombre=nom, apellido=ap, curso=cur)
  return render_template('inscripcionCurso.html')


@app.route('/registroLibros', methods=['GET', 'POST'])
def registroLibros():
  if request.method == 'POST':
    titulo = request.form['titulo']
    autor = request.form['autor']
    resumen = request.form['resumen']
    medio = request.form['medio']
    return render_template('registroLibros.html', titulo=titulo, autor=autor, resumen=resumen, medio=medio)
  return render_template('registroLibros.html')


@app.route('/registroProductos', methods=['GET', 'POST'])
def registroProductos():
  if request.method == 'POST':
    prod = request.form['producto']
    cat = request.form['categoria']
    exist = request.form['existencia']
    prec = float(request.form['precio'])
    return render_template('registroProductos.html', producto=prod, categoria=cat, existencia=exist, precio=prec)
  return render_template('registroProductos.html')


@app.route('/registroUsuarios', methods=['GET', 'POST'])
def registroUsuarios():
  if request.method == 'POST':
    nom = request.form['nombre']
    ap = request.form['apellido']
    cor = request.form['correo']
    con = request.form['contrasena']
    return render_template('registroUsuarios.html', nombre=nom, apellido=ap, correo=cor, contrasena=con)
  return render_template('registroUsuarios.html')


if __name__ == '__main__':
  app.run(debug=True)