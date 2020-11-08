# A docker container for testing CPU load

This container will periodically generate CPU load. It can be used e.g. for testing a docker monitoring tool. Configure the container by environment variables:

* `NR_PROC`: Number of processes running parallel. Default: Half of the available CPUs, at least one.
* `REP_CYCLE`: After how many ticks (=seconds) the CPU load should be repeated? Default: `REP_CYCLE=60`.
* `LOAD_DUR`: How many seconds of CPU load? Default: `LOAD_DUR=10`.
* `HALF`: If true use only a load with 50% CPU. Default: `HALF=True`

Examples:  

* Every minute `10` seconds (= standard config) half load with half of the available CPUs:  
`docker run jennerwein/container-load-probe`

* Every minute `10` seconds (= standard config) half load with `NR_PROC=3` parallel processes:  
`docker run -e NR_PROC=3 jennerwein/container-load-probe`

* Every minute `10` seconds full load using all CPUs in parallel processes.  
`docker run -e HALF=False jennerwein/container-load-probe`

* Every hour one minute full load with `1` (parallel) process:  
`docker run -e REP_CYCLE=3600 -e LOAD_DUR=60 -e HALF=False -e NR_PROC=1 jennerwein/container-load-probe`
