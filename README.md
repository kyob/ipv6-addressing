# ipv6-addressing
Python program to help learn about IPv6 addresses

YouTube Video demonstrating this program:
https://www.youtube.com/playlist?list=PLMLm7-g0V0kfGg8g8KutNFK7rS3laA9QQ

Book:
IPv6 Fundamentals: A Straightforward Approach to Learning IPv6
by Rick Graziani
Cisco Press
https://www.amazon.com/IPv6-Fundamentals-Straightforward-Approach-Understanding/dp/1587144778

This program is intended to help you learn about IPv6 addresses.
The menu includes:

LEARN ABOUT IPv6 ADDRESSES
---------------------------
0. How do we represent an IPv6 address?

LEARN
1. Compress an IPv6 address to its shortest form
2. Display all 32 hexadecimal digits of an IPv6 address
3. Display the IPv6 address type and address information
4. Subnetting an IPv6 network address

SEE
5. Display your IPv4 and IPv6 addresses
6. Enter a URL and get the IPv4 and IPv6 addresses

F. Fun random facts about the number of IPv6 addresses
Q: Quit

Libraries required:
import ipaddress
import sys
import random
import socket
import requests
import dns.resolver
