import os
import threading

ips = ["192.168.1.227", "192.168.1.252"]
names = ["Liz","Matt"]


def check():
    for i in range(len(ips)):
        print i
        response = os.system("ping -c 1 " + ips[i]+" 2>&1 >/dev/null")
        if response == 0:
              print names[i], ' is home!'
    threading.Timer(5.0,check).start()

check()
