import requests
import subprocess
import time
from datetime import timedelta
from routes.execution_history import *
from routes.error_log import *

def indicador_expedicao():
    indicator_name = 'Indicador da Expedição'
    try:
        start_time = time.time()
        subprocess.run(['python', 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Central/__Automaticos_Python/02-indicador_expedicao/executable.py'], check=True)
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        response = requests.post('http://127.0.0.1:5000/registros', 
                                json={'indicator_name':indicator_name,
                                    'end_execution':str(end_time),
                                    'duration':str(elapsed_time)})
        return response
    except Exception as e:
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        requests.post('http://127.0.0.1:5000/error', 
                    json={'indicator_name':indicator_name,
                        'end_execution':str(end_time),
                        'duration':str(elapsed_time)})
        return f'Error: {str(e)}'
   
def encerramento_ordens():
    indicator_name = 'Encerramento de Ordens'
    try:
        start_time = time.time()
        subprocess.run(['python', 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Central/__Automaticos_Python/03-encerramento_ordens/executable.py'], check=True)
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        response = requests.post('http://127.0.0.1:5000/registros', 
                                json={'indicator_name':indicator_name,
                                    'end_execution':str(end_time),
                                    'duration':str(elapsed_time)})
        return response
    except Exception as e:
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        requests.post('http://127.0.0.1:5000/error', 
                    json={'indicator_name':indicator_name,
                        'end_execution':str(end_time),
                        'duration':str(elapsed_time)})
        return f'Error: {str(e)}'
     
def controle_de_estoque():
    indicator_name = 'Controle de Estoque'
    try:
        start_time = time.time()
        subprocess.run(['python', 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Robert/Testes/controle_de_estoque.py'], check=True)
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        response = requests.post('http://127.0.0.1:5000/registros', 
                                json={'indicator_name':indicator_name,
                                    'end_execution':str(end_time),
                                    'duration':str(elapsed_time)})
        return response
    except Exception as e:
        end_time = time.time()
        elapsed_time = timedelta(seconds=(end_time - start_time))
        requests.post('http://127.0.0.1:5000/error', 
                    json={'indicator_name':indicator_name,
                        'end_execution':str(end_time),
                        'duration':str(elapsed_time)})
        return f'Error: {str(e)}'
    