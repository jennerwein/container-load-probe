# A docker container for testing CPU load

This container will periodically generate CPU load. It can be used e.g. for testing a docker monitoring tool. Configure the container by environment variables:

* `NR_PROC`: Number of processes running parallel.  
* `REP_CYCLE`: After how many ticks (=seconds) the CPU load should be repeated? Default: `REP_CYCLE=10`.
* `LOAD_DUR`: How many seconds of CPU load? Default: `LOAD_DUR=2`.

Examples:

-----
`docker run -e NR_PROC=3 jennerwein/container-load-probe`  
Every 10 seconds 2 seconds (= standard config) full load with `NR_PROC=3` parallel processes.

-----
`docker run -e REP_CYCLE=10 -e LOAD_DUR=4 -e NR_PROC=1 jennerwein/container-load-probe`  
Every `10` seconds `4` seconds full load with `1` (parallel) process.
