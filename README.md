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

## How does it work?

We send a UDP packet with increasing TTL until we reach our destination.

## How does it differ from real traceroute?

Real traceroute sends 3 packets, here we send 1. Also, there is no option to send ICMP packets instead of UDP packets.
