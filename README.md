# PythonIpCalculator
### Developed by Jason Tang

This is a basic Network IP Calculator written in Python, and requires an installation of Python (preferably 3) to run. By inputting an IP address and a subnet mask, users can calculate the network IP of said IP address.

The program makes use of Python's bitwise operators which automatically convert decimal portions of the IP address and subnet mask into binary, performs the AND operation on each individual bit, and then converts back from binary to decimal. The process is explained in this video: https://www.youtube.com/watch?v=Upk5MU7vGAg&list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO&index=27

To use, download Python and this Python file; then, using the Command Prompt, navigate to the file's location and type: python IpCalculator.py
Alternatively, you may append the file's file path beforehand instead of navigating to the specific folder: python (insert path here without the parentheses)\IpCalculator.py
