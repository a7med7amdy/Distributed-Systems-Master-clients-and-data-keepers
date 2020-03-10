import zmq
import time
import sys
from utility import log , remove_log


remove_log()
def update_table( port , ips , free_ports , lookup_table ):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    for ip in ips :
        for i in range(3):
            socket.connect (ip + str(int(port)+i))

    topicfilter = "update"
    socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
    while True:
        log(" Event file started successfully")
        string = socket.recv_string()
        topic , id , port , filename = string.split()
        log(" Recived from id "+ id +" filename " + filename + " port free "+port)
        free_ports[int(id)].append(port)
        if filename in lookup_table :
            temp = lookup_table[filename]
            temp.append(id)
            lookup_table[filename] = temp
        else :
            lookup_table[filename] = [id]

