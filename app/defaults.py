import multiprocessing

# Variable NR_PROC: Number of processes running parallel
NR_PROC = int((multiprocessing.cpu_count()+1)/2)

# Variable REP_CYCLE: After how many ticks the load should be repeated 
REP_CYCLE = 60

# Variable LOAD_DUR: How many seconds of CPU load. how many tick load the load should be repeated 
LOAD_DUR = 10

# Variable HALF: If True, then use CPU only half time (= simulate 50% CPU).
HALF = True