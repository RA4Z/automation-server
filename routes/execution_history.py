from flask import Blueprint, request

execution_history_blueprint = Blueprint('execution_history_blueprint', __name__)

@execution_history_blueprint.route('/registros')
def get_exec():
    try:
        return 'Hello, World!'
    except Exception as e:
        return f'Error: {str(e)}'

@execution_history_blueprint.route('/registros', methods=['POST'])
def registrar_exec():
    try:
        if request.is_json:
            data = request.get_json()
            return data
        else:
            return 'Erro: a requisição não contém dados JSON!'
    except Exception as e:
        return f'Error: {str(e)}'

    