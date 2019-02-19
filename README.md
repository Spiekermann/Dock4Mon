# Dock4Mon
Just a proof-of-concept for monitoring docker-swarms

## Process
Dock4Mon monitors a manager of a docker swarm and extracts various informtion of connected workers of the swarm.
Dock4Mon checks for the availability and the status of the workers and informs the user of valid workers.
Additionally Dock4Mon extracts the ip-address of the host, which runs the worker.

## Installation
No installation needed, just run `python dock4mon.py`
