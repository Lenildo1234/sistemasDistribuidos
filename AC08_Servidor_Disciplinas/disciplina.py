from flask import Flask, jsonify, request
import util
app = Flask(__name__)

@app.route('/disciplinas', methods=['GET'])
def disciplinas():
    return jsonify(util.all_for_database('DISCIPLINA'))


@app.route('/disciplinas', methods=['POST'])
def adiciona_disciplina():
    nova_disciplina = request.json()
    util.adiciona(nova_disciplina, 'DISCIPLINA')


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
