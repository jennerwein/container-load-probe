##########################################################################################
import os
import time
import multiprocessing
from multiprocessing import Process

import defaults

def worker(duration):
    '''Just do something in the given time duration.
    Duration in seconds.                            '''
    start=time.time()
    while (time.time()-start) < duration:
        x=1
        for i in range(100): x=x+1

def do_worker(q,duration):
    '''Put the worker in the queue.'''
    q.put(worker(duration))

def halfworker(duration):
    '''Just do something in the given time duration.
    Use CPU half time
    Duration in seconds.                            '''
    start=time.time()
    while (time.time()-start) < duration:
        worker(0.05)
        time.sleep(0.05)

def do_halfworker(q,duration):
    '''Put the worker in the queue.'''
    q.put(halfworker(duration))


def parallelWorker(nr_processes,duration,HALF=False):
    q = multiprocessing.Queue()
    jobs = []
    for i in range(nr_processes):
        if HALF:
            p = Process(target=do_halfworker, args=(q,duration))
        else:
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
    NR_PROC = defaults.NR_PROC

# Variable REP_CYCLE: After how many ticks the load should be repeated 
try:
    REP_CYCLE = int(os.getenv('REP_CYCLE'))
except:
    REP_CYCLE = defaults.REP_CYCLE

# Variable LOAD_DUR: How many seconds of CPU load. how many tick load the load should be repeated 
try:
    LOAD_DUR = int(os.getenv('LOAD_DUR'))
except:
    LOAD_DUR = defaults.LOAD_DUR

# Variable HALF: If True, then use CPU only half time (= simulate 50% CPU).
try:
    HALF = os.getenv('HALF')
    if HALF == None:
        HALF = defaults.HALF
except:
    HALF = defaults.HALF

# With variable MODE you can set special effects.
# Default: None
MODE = os.getenv('MODE')

while True: # Run continuously
## for x in range(1): # Run once
    if trigger(REP_CYCLE):    # Every REP_CYCLE ticks
        if MODE == None:
            parallelWorker(NR_PROC,LOAD_DUR,HALF)
        else:
            for i in range(multiprocessing.cpu_count()):
                parallelWorker(1,i+1)
    #
    ##########################################################################
    # Increase the tick by 1 and sleep a durationTick
    tick += 1
    time.sleep(1)
