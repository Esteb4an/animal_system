import flask
import system

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/infer', methods=['GET'])
def inferir():
    texto = flask.request.args.get('q', '')
    mostrar = flask.request.args.get('display', '')
    resultado = system.ejecutar(texto, mostrar)
    return resultado

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
