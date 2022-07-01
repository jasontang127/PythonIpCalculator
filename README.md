# PythonIpCalculator

This is a basic Network IP Calculator written in Python. 

It makes use of Python's bitwise operators which automatically convert decimal portions of the IP address and subnet mask into binary, performs the AND operation on each individual bit, and then converts back from binary to decimal. The process is explained in this video: https://www.youtube.com/watch?v=Upk5MU7vGAg&list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO&index=27

Usage steps:
- Download a version of Python
- Using Command Prompt, navigate to the file's location and type: python IpCalculator.py
- Input an IP address and subnet mask (in the form of 4 numbers between 0-255, separated by periods {e.g. 182.90.2.5 and 255.255.255.0})
