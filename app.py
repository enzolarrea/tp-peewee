from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from models import db, Usuario, Bloc, Nota
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
app.secret_key = 'secreto'
app.config['DATABASE'] = 'sqlite:///notas.db'

@app.before_request
def before_request():
    db.connect()
    db.create_tables([Usuario, Bloc, Nota], safe=True)

@app.teardown_request
def teardown_request(exception):
    if not db.is_closed():
        db.close()

@app.route('/', methods=['GET'])
def index():
    usuario = Usuario.get_or_none(Usuario.id == session.get("usuario_id"))
    blocs = Bloc.select()
    return render_template('index.html', blocs=blocs, usuario=usuario)

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    usuario, created = Usuario.get_or_create(nombre=nombre)
    session['usuario_id'] = usuario.id
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/crear_bloc', methods=['POST'])
def crear_bloc():
    nombre = request.form['nombre']
    privado = request.form.get('privado') == 'true'
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        return jsonify(success=False)
    bloc = Bloc.create(nombre=nombre, creador=usuario_id, privado=privado)
    return jsonify(success=True, bloc_id=bloc.id)

@app.route('/agregar_nota', methods=['POST'])
def agregar_nota():
    texto = request.form['texto']
    bloc_id = int(request.form['bloc_id'])
    usuario_id = session.get("usuario_id")
    bloc = Bloc.get_by_id(bloc_id)
    if bloc.privado and bloc.creador.id != usuario_id:
        return jsonify(success=False)
    nota = Nota.create(texto=texto, bloc=bloc_id, autor=usuario_id)
    return jsonify(success=True, nota_id=nota.id)

@app.route('/editar_nota/<int:nota_id>', methods=['POST'])
def editar_nota(nota_id):
    nota = Nota.get_or_none(Nota.id == nota_id)
    if nota and nota.autor.id == session.get("usuario_id"):
        nuevo_texto = request.json.get("texto")
        if nuevo_texto:
            nota.texto = nuevo_texto
            nota.editado = True
            nota.save()
            return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 403

@app.route('/eliminar_nota/<int:nota_id>', methods=['POST'])
def eliminar_nota(nota_id):
    nota = Nota.get_or_none(Nota.id == nota_id)
    usuario_id = session.get("usuario_id")

    if nota:
        bloc = nota.bloc
        if nota.autor.id == usuario_id or bloc.creador.id == usuario_id:
            nota.delete_instance()
            return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 403


@app.route('/borrar_bloc', methods=['POST'])
def borrar_bloc():
    bloc_id = request.form['id']
    usuario_id = session.get("usuario_id")
    bloc = Bloc.get_or_none(Bloc.id == bloc_id)
    if bloc and bloc.creador.id == usuario_id:
        bloc.delete_instance(recursive=True)
        return jsonify(success=True)
    return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)
