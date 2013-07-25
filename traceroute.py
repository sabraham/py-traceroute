#!/usr/bin/env python

import sys
import socket
import time

class Traceroute(object):
    def __init__(self, dest_name, port=33434, max_ttl=64, packet_size=10,
                 timeout=5.0):
        self.dest_name = dest_name
        self.port = port
        self.max_ttl = max_ttl
        self.packet_size = packet_size
        self.curr_name = None
        self.dest_addr = socket.gethostbyname(dest_name)
        self.send_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                                    socket.getprotobyname("UDP"))
        self.list_s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                    socket.getprotobyname("ICMP"))
        self.send_s.connect((self.dest_addr, self.port))
        self.list_s.settimeout(timeout)
        self.ttl = 1
        self.timeout = False
    def ping(self):
        while self.curr_name != self.dest_name and self.ttl <= self.max_ttl:
            self.send_s.setsockopt(socket.getprotobyname("IP"),
                                   socket.IP_TTL, self.ttl)
            self.start_time = time.clock()
            # if connection refused, break
            try:
                self.send_s.send(" " * self.packet_size)
            except socket.error:
                break
            # we only care about the address, so discard data and since the
            # message is sent back icmp, there is no port.
            try:
                _, [self.curr_addr, _] = self.list_s.recvfrom(1024)
            except socket.timeout:
                self.curr_addr = "*"
                self.curr_name = "*"
                self.timeout = True
            self.elapsed = (time.clock() - self.start_time) * 1000
            if not self.timeout:
                try:
                    self.curr_name, _, _ = socket.gethostbyaddr(self.curr_addr)
                except socket.herror:
                    self.curr_name = self.curr_addr
            yield "%d %s (%s) %f ms" % (self.ttl, self.curr_name,
                                        self.curr_addr, self.elapsed)
            self.timeout = False
            self.ttl += 1

if __name__ == "__main__":
    t = Traceroute(sys.argv[1])
    tp = t.ping()
    while True:
        try:
            print tp.next()
        except StopIteration:
            break
