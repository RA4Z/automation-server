import schedule
import time
from services.functions import *

schedule.every().day.at('16:14:15').do(indicador_expedicao)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)