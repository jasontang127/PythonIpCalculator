

def ipCalculator(ip, subnet):
    
    # split input into individual decimal numbers
    ipList = ip.split(".");
    subnetList = subnet.split(".");
    ipBits = [0, 0, 0, 0, 0, 0, 0, 0];
    subnetBits = [0, 0, 0, 0, 0, 0, 0, 0];
    finalBits = [0, 0, 0, 0, 0, 0, 0, 0];
    finalStr = "Network IP: ";
    maxAddresses = 0;
    print(ipList)
    print(subnetList)
    
    # perform bitwise AND on each component of IP and subnet
    for x in range(0, 4):
        finalNum = int(ipList[x]) & int(subnetList[x]);
        finalStr += str(finalNum) + ".";
        maxAddresses += 255 - int(subnetList[x]);
    
    # present network IP and number of usable hosts    
    maxAddresses += 1;
    finalStr = finalStr[:-1] + "\nNumber of usable Hosts: " + str(maxAddresses - 2);
    print(finalStr);

    
ipCalculator(input("Enter ip: "), input("Enter subnet: "))
