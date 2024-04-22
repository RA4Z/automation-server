from flask import Blueprint, request

error_log_blueprint = Blueprint('error_log_blueprint', __name__)

@error_log_blueprint.route('/error')
def get_error():
    try:
        return 'Hello, World!'
    except Exception as e:
        return f'Error: {str(e)}'

@error_log_blueprint.route('/error', methods=['POST'])
def registrar_error():
    try:
        if request.is_json:
            data = request.get_json()
            return data
        else:
            return 'Erro: a requisição não contém dados JSON!'
    except Exception as e:
        return f'Error: {str(e)}'

    