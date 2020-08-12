##########################################################################################
import os
import time
import multiprocessing
from multiprocessing import Process

def worker(duration):
    '''Just do something in the given time duration.'''
    start=time.time()
    while (time.time()-start) < duration:
        x=1
        for i in range(1000): x=x+1

def do_worker(q,duration):
    '''Put the worker in the queue.'''
    q.put(worker(duration))

def parallelWorker(nr_processes,duration):
    q = multiprocessing.Queue()
    jobs = []
    for i in range(nr_processes):
        p = Process(target=do_worker, args=(q,duration))
        # target: the function to be executed by process p
        # args: the arguments to be passed to the target function
        jobs.append(p)
    for p in jobs:
        p.start()

def trigger(x):
    """Returns True each time the number x of ticks passes."""
    global tick
    teiler = int(x)
    if tick % teiler == 0:
        return True
    else:
        return False

##########################################################################################
##########################################################################################
##########################################################################################

tick = 0           # App time in ticks. Start with 0.
durationTick = 1   # Duration of a tick in seconds.

# Variable NR_PROC: Number of processes running parallel
try:
    NR_PROC = int(os.getenv('NR_PROC'))
except:
    NR_PROC = multiprocessing.cpu_count()

# Variable REP_CYCLE: After how many ticks the load should be repeated 
# Default: REP_CYCLE=10 (1 tick = 1 second).
try:
    REP_CYCLE = int(os.getenv('REP_CYCLE'))
except:
    REP_CYCLE=10

# Variable LOAD_DUR: How many seconds of CPU load. how many tick load the load should be repeated 
# Default: LOAD_DUR=2
try:
    LOAD_DUR = int(os.getenv('LOAD_DUR'))
except:
    LOAD_DUR=2


while True: # Run continuously
## for x in range(1): # Run once
    if trigger(REP_CYCLE):    # Every 10 ticks
        parallelWorker(NR_PROC,LOAD_DUR)
    #
    ##########################################################################
    # Increase the tick by 1 and sleep a durationTick
    tick += 1
    time.sleep(1)
