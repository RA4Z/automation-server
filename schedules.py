import schedule
import time
from services.functions import *

schedule.every().day.at('09:49:50').do(indicador_expedicao)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)