import schedule
import time
import os
import subprocess
from services.functions import *

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def check_files():
    path = 'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Central\__Automaticos_Python\__Agendamentos'
    files = os.listdir(path)

    schedule.clear()
    for file in files:
        filename = file.replace('.txt','')
        filename = filename.replace('.',':')
        schedule.every().day.at(filename).do(run_schedule_today)

    print(schedule.jobs)
        

def run_schedule_today():
    now = time.time()
    now = time.strftime("%H.%M", time.localtime(now))
    filename = open(f'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Central\__Automaticos_Python\__Agendamentos/{now}.txt','r',encoding='utf-8').readline().strip()
    print(f'ABRINDO O ARQUIVO {filename}')
    subprocess.run(['python', filename], check=True)


schedule.every(1).minutes.do(check_files)