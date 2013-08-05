# Traceroute

A simple traceroute implementation in Python

## Setup

```
chmod +x traceroute.py
```

## Running

To open a raw socket, the process needs root permissions.

```
sudo ./traceroute.py www.google.com
```

```
1 192.168.202.1 (192.168.202.1) 1.729965 ms
2 69.64.202.65.nyc.electricfiber.net (69.64.202.65) 3.784895 ms
3 172.16.0.190 (172.16.0.190) 3.179073 ms
4 ae1-217.nyc30.ip4.tinet.net (173.241.128.189) 3.844023 ms
5 xe-0-0-1.nyc32.ip4.tinet.net (89.149.184.194) 18.513918 ms
6 72.14.216.137 (72.14.216.137) 3.937006 ms
7 209.85.255.68 (209.85.255.68) 17.874002 ms
8 72.14.236.208 (72.14.236.208) 4.000187 ms
9 72.14.239.93 (72.14.239.93) 12.793064 ms
10 66.249.95.231 (66.249.95.231) 29.438972 ms
11 72.14.239.66 (72.14.239.66) 23.499966 ms
12 72.14.239.83 (72.14.239.83) 101.364851 ms
13 64.233.174.177 (64.233.174.177) 192.428112 ms
14 209.85.255.35 (209.85.255.35) 176.832199 ms
15 64.233.175.0 (64.233.175.0) 191.023827 ms
16 66.249.94.105 (66.249.94.105) 282.645941 ms
17 72.14.233.105 (72.14.233.105) 309.727907 ms
18 sin04s02-in-f16.1e100.net (173.194.38.176) 291.933060 ms
```

## How does it work?

We send a UDP packet with increasing TTL until we reach our destination.

## How does it differ from real traceroute?

Real traceroute sends 3 packets, here we send 1. Also, there is no option to send ICMP packets instead of UDP packets.
