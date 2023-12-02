import time
import random
from src.eColor import *

def simulacion(listap):
    horaglobal.time()
    min_wait_time = 5
    max_wait_time = 10

    #cada un segundo llega un paciente nuevo
    for i in range(len(listap)):
        print(str(listap[i]))
        current_time = time.localtime()
        # Calcula el tiempo de espera aleatorio entre min y max segundos
        time_elapsed = time.mktime(current_time) - time.mktime(time_0)
        wait_time = random.randint(min_wait_time, max_wait_time)
        
        if time_elapsed < wait_time:
            time.sleep(wait_time - time_elapsed)
        else:
            time.sleep(1)
            
    return time.localtime()
        
    
    