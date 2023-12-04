from backend import *

with app.app_context():
    @app.route('/')
    def rota():
        return 'backend'

    @app.route('/listarPalavras')
    def listarPlavras():
        dados = db.session.query(palavrasAcertadas).all()
        lista = []
        for dado in dados:
            lista.append(dado.json())
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista})
        return jsonify(meujson)


    app.run(debug=True)