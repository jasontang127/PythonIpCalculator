

def ipCalculator(ip, subnet):
    ipList = ip.split(".");
    subnetList = subnet.split(".");
    ipBits = [0, 0, 0, 0, 0, 0, 0, 0];
    subnetBits = [0, 0, 0, 0, 0, 0, 0, 0];
    finalBits = [0, 0, 0, 0, 0, 0, 0, 0];
    finalNum = 0;
    finalStr = "Network IP: ";
    maxAddresses = 0;
    print(ipList)
    print(subnetList)
    for x in range(0, 4):
        # ipNum = int(ipList[x]);
        # subnetNum = int(subnetList[x]);
        # finalNum = 0;
        # for y in range(0,8):
        #     if (ipNum >= pow(2,(7-y))):
        #         ipNum -= pow(2,(7-y));
        #         ipBits[y] = 1;
        #     else:
        #         ipBits[y] = 0;
        #     if (subnetNum >= pow(2,(7-y))):
        #         subnetNum -= pow(2,(7-y));
        #         subnetBits[y] = 1;
        #     else:
        #         subnetBits[y] = 0;
        #         maxAddresses += pow(2, 7-y) + 1;
        #     if (ipBits[y] == 1 and subnetBits[y] == 1):
        #         finalBits[y] = 1;
        #         finalNum += pow(2,(7-y));
        #     else: 
        #         finalBits[y] = 0;
        finalNum = int(ipList[x]) & int(subnetList[x]);
        finalStr += str(finalNum) + ".";
        maxAddresses += 255 - int(subnetList[x]);
    maxAddresses += 1;
    finalStr = finalStr[:-1] + "Number of usable Hosts: " + str(maxAddresses - 2);
    
    print(finalStr);

    
ipCalculator(input("Enter ip: "), input("Enter subnet: "))
