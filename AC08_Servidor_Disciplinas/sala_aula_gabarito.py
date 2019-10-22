from flask import Flask, jsonify, request
import util
app = Flask(__name__)


@app.route('/')
def all():
    return jsonify(database)

@app.route('/reseta', methods=['POST'])
def reseta():
    util.reseta()
    return 'banco resetado'
    

@app.route('/alunos', methods=['GET'])
def alunos():
    return jsonify(util.all_for_database('ALUNO'))



@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try: 
        aluno = util.localiza(id_aluno,'ALUNO')
        return jsonify(aluno)
    except util.NotFoundError:
        return jsonify({'erro':'aluno nao encontrado'}),400

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
    try: 
        aluno = util.localiza(id_aluno,'ALUNO')
        removido = util.remove(aluno,'ALUNO')
        return jsonify(removido)
    except util.NotFoundError:
        return jsonify({'erro':'aluno nao encontrado'}),400

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    try: 
        aluno = util.localiza(id_aluno,'ALUNO')
        novo_aluno = request.json
        if 'nome' not in novo_aluno:
            return jsonify({'erro':'aluno sem nome'}),400
        for key in aluno:
            if key in novo_aluno:
                aluno[key] = novo_aluno[key]
        return jsonify(aluno)
    except util.NotFoundError:
        return jsonify({'erro':'aluno nao encontrado'}),400

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    print('ola')
    novo_aluno = request.json
    print(request.method)
    if 'nome' not in novo_aluno:
        return jsonify({'erro':'aluno sem nome'}),400
    if 'id' not in novo_aluno:
        return jsonify({'erro':'aluno sem id'}),400
    try:
        aluno = util.localiza(novo_aluno['id'],'ALUNO')
        return jsonify({'erro':'id ja utilizada'}),400
    except util.NotFoundError:
        pass

    util.adiciona(novo_aluno,'ALUNO')
    return jsonify(util.all_for_database('ALUNO'))


@app.route('/professores')
def professores():
    return jsonify(util.all_for_database('PROFESSOR'))


def localiza_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return professor
    raise util.NotFoundError

@app.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try: 
        professor = util.localiza(id_professor,'PROFESSOR')
        if request.method == 'PUT':
            novo_professor = request.json
            if 'nome' not in novo_professor:
                return jsonify({'erro':'professor sem nome'}),400
            for key in professor:
                if key in novo_professor:
                    professor[key] = novo_professor[key]
        if request.method == 'DELETE':
            database['PROFESSOR'].remove(professor)
            dic = {}
            dic['removido'] = True
            dic['professor'] = professor
            return jsonify(dic)

        return jsonify(professor)
    except util.NotFoundError:
        return jsonify({'erro':'professor nao encontrado'}),400

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def edita_professor(id_professor):
    try: 
        professor = util.localiza(id_professor,'PROFESSOR')
        novo_professor = request.json
        if 'nome' not in novo_professor:
            return jsonify({'erro':'professor sem nome'}),400
        for key in professor:
            if key in novo_professor:
                professor[key] = novo_professor[key]
        return jsonify(professor)
    except util.NotFoundError:
        return jsonify({'erro':'professor nao encontrado'}),400

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    try: 
        professor = util.localiza(id_professor,'PROFESSOR')
        deletado = util.remove(professor,'PROFESSOR')
        return jsonify(deletado)
    except util.NotFoundError:
        return jsonify({'erro':'professor nao encontrado'}),400

@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.json
    print(request.method)
    if 'nome' not in novo_professor:
        return jsonify({'erro':'professor sem nome'}),400
    if 'id' not in novo_professor:
        return jsonify({'erro':'professor sem id'}),400
    try:
        professor = util.localiza(novo_professor['id'],'PROFESSOR')
        return jsonify({'erro':'id ja utilizada'}),400
    except util.NotFoundError:
        pass
    util.adiciona(novo_professor,'PROFESSOR')
    return jsonify(util.all_for_database('PROFESSOR'))


@app.route('/disciplinas', methods=['GET'])
def disciplinas():
    return jsonify(util.all_for_database('DISCIPLINA'))

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)

    
