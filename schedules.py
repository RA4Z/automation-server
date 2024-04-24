import schedule
import time
from services.functions import *

schedule.every().day.at('16:07:50').do(encerramento_ordens)
schedule.every().day.at('15:56').do(indicador_expedicao)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)