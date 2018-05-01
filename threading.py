#most of this is form online tutorial at 
#https://www.youtube.com/watch?v=NwH0HvMI4EA

import threading
from queue import Queue
import time 


####
#Linearly should have taken 4 seconds with 20 jobs each .2 seconds long
#However with the threading, we had 10 threads, each thread did two jobs all
#at the same time so only took .4 seconds
#####


printLock = threading.Lock() 

q = Queue()

def exampleJob(worker):
    time.sleep(0.2)
    
    with printLock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

for i in range(0,10):
    t = threading.Thread(target = threader)
    t.daemon = True
    
    t.start()
    
start = time.time()


for worker in range(20):
    q.put(worker)
    
q.join()

print("Entire job took: ", time.time() - start)

