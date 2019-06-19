# MonDock
Just a proof-of-concept for monitoring docker-swarms

## Process
MonDock monitors a manager of a docker swarm and extracts various informtion of connected workers of the swarm.
MonDock checks for the availability and the status of the workers and informs the user of valid workers.
Additionally MonDock extracts the ip-address of the host, which runs the worker.

## Installation
No installation needed, just run `python mondock.py`
