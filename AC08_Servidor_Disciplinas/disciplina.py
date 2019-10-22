from flask import Flask, jsonify, request
import util
app = Flask(__name__)


@app.route('/disciplinas', methods=['GET'])
def disciplinas():
    return jsonify(util.all_for_database('DISCIPLINA'))


@app.route('/disciplinas/<int:id_disciplina>', methods=['GET'])
def disciplina_pelo_id(id_disciplina):
    try: 
        disciplina = util.localiza(id_disciplina,'DISCIPLINA')
        return jsonify(disciplina)
    except util.NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400
    


@app.route('/disciplinas', methods=['POST'])
def adiciona_disciplina():
    nova_disciplina = request.json
    util.adiciona(nova_disciplina, 'DISCIPLINA')
    return jsonify(util.all_for_database('DISCIPLINA'))


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
