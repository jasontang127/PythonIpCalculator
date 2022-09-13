# PythonIpCalculator

This is a basic Network IP Calculator written in Python that returns the Network IP given an IP address and subnet mask.

It makes use of Python's bitwise operators which automatically convert decimal portions of the IP address and subnet mask into binary, performs the AND operation on each individual bit, and then converts back from binary to decimal.
  The subnet mask is made up of four bytes and split into two parts; the first portion is made up of all 1's, while the second portion is made up of all 0's. When performing the AND operation with an IP address and the subnet mask, the first portion of bits is designated for the network IP. 
  For example, using 182.90.2.5 and 255.255.255.0, the network IP is the same as the IP address wherever the subnet mask's bits are 1. In this case, the subnet mask's bits are 1 for the first three bytes, resulting in a network IP of 182.90.2.0. With 1 byte remaining, this means the network of IP 182.90.2.0 can host 253 IP addresses. 2 are reserved for the network IP itself and the special broadcast IP.

Usage steps:
- Download a version of Python
- Using Command Prompt, navigate to the file's location and run the Python file
- Input an IP address and subnet mask (in the form of 4 numbers between 0-255, separated by periods {e.g. 182.90.2.5 and 255.255.255.0})

![image](https://user-images.githubusercontent.com/45743962/189820272-90d41771-1501-4eb2-b6c2-d07fda75799f.png)
