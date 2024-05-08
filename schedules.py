import time
import os
import subprocess

def run_scheduler():
    queue = []
    atrasados = []
    while True:
        try:
            queue = check_files(queue)
            status = something_is_running(queue)

            if not status:
                if len(atrasados) > 0:
                    atrasados[0]['performed'] = True
                    subprocess.run(['python', atrasados[0]['filename']])
                    atrasados.pop(0)
                    
                now = time.time()
                hoje = time.strftime("%d/%m/%Y", time.localtime(now))
                now = time.strftime("%H:%M", time.localtime(now))

                for schedule in queue:
                    if schedule['time'] == now and (schedule['data'] == '' or schedule['data'] == hoje):
                        print(schedule)
                        schedule['performed'] = True
                        subprocess.run(['python', schedule['filename']])
            else:
                if schedule['time'] == now and not schedule['performed'] and schedule['time'] not in [item['time'] for item in atrasados]:
                    atrasados.append(schedule)

        except Exception as e:
            print(f'Error: {str(e)}')
        
        time.sleep(5)


def check_files(param_queue:list):
    path = 'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Central\__Automaticos_Python\__Agendamentos'
    files = os.listdir(path)

    queue = param_queue
    for file in files:
        time = file.replace('.txt','')
        time = time.replace('.',':')

        if time not in [item['time'] for item in queue]:
            with open(f'{path}/{file}', 'r', encoding='utf-8') as file:
                filename = file.readline().strip()
                data_exec = file.readline().strip()
                queue.append({'time':time, 'filename':filename,'data':data_exec,'performed':False})
    
    return queue


def something_is_running(queue:list):
    for schedule in queue:
        file = get_last_delimiter_segment(schedule['filename'])
        folder = str(schedule['filename']).replace(file,'')
        try:
            if os.path.exists(f'{folder}status.txt'):
                with open(f'{folder}status.txt', 'r', encoding='utf-8') as file:
                    file.readline().strip()
                    status = file.readline().strip()
                    if status == 'True': return True
        except:
            pass
    
    return False


def get_last_delimiter_segment(text):
    for delimiter in ["/", "\\"]:
        index = text.rfind(delimiter)
        if index != -1:
            return text[index + 1 :]
    return text

