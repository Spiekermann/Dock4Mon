import subprocess
import time
import shlex


worker=set()        # All workers of the investigated swarm
noworker=set()      # hosts that are not a worker
mapping={}          # Store the ips of the hosting systems

# capture process
# implement your own technique
# in this poc, we use ssh-based iptables manipulation
def capture(ip):
    ip = ip.lstrip()
    print "Create capture process on host: " + ip


# remove capture process
# just remove the things you've done before
def undo(ip):
    ip=ip.lstrip()
    print "Remove capture for " + ip

# monitoring process
def monitor():
    time.sleep(1)
    c=shlex.split("docker node ls --format \"{{.ID}}:{{.ManagerStatus}}:{{.Availability}}:{{.Status}}\"")  # type: str
    res=subprocess.Popen(c,stdout=subprocess.PIPE)
    line = res.communicate()[0]
    member=line.splitlines()
    for m in member:
        u = m.split(":")
        if u[3] == "Ready":                # online
            if u[2] != "Drain":            # Manager without working thread
                if u[0] not in worker:
                    worker.add(u[0])
                    print len(worker)
                    inspect(u[0])
            else:
                if u[0] not in noworker:
                    noworker.add(u[0])
        else:   # Manager, check for worker capabilities
            if u[3] == "Down":  # Worker was in swarm, delete it from set
                if u[0] in worker:
                    undo(mapping[u[0]])
                  #  print "Please remove worker " + mapping[u[0]] + " from capture."
                    worker.remove(u[0])
                    print "Swarm has " + str(len(worker)) + " members"


# Gather data
def inspect(worker):
        cmd="docker node inspect " + worker + " --pretty"
        c2 = shlex.split(cmd)
        res = subprocess.Popen(c2, stdout=subprocess.PIPE)
        line = res.communicate()[0]
        ip = line.splitlines()
        for x in ip:
            if "Addr" in x:
                if worker not in mapping:
                    print "New member of swarm found."
                    a,ip = x.split(":")
                    capture(ip)
                    mapping[worker]=ip
                    print "Swarm has " + str(len(mapping)) + " members"


if __name__ == "__main__":
    print "Starting Dock4Mon..."
    print "Press Ctrl-C to quit."
    try:
        while True:
            monitor()
    except (KeyboardInterrupt):
        print "Ctrl-C received..."
        print "Quitting Dock4Mon"