import schedule
import time
from services.functions import *

schedule.every().day.at('08:46:00').do(encerramento_ordens)
schedule.every().day.at('03:55:00').do(coletar_materiais_ecm)
schedule.every().day.at('16:19').do(indicador_expedicao)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)