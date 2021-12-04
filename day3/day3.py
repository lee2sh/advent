def getGamma(bn):
    gamma = ""
    for i in range(len(bn[0].strip("\n"))):
        count1 = 0
        count0 = 0
        for j in range(len(bn)):
            if bn[j][i] == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 > count0:
            gamma += "1" 
        else:
            gamma += "0"
    res = int(gamma, 2)
    return (res, gamma)


def getEp(gamma):
    gs = str(gamma)
    res = ""
    for s in gs:
        if s == "1":
            res += "0"
        else:
            res += "1"
    return (int(res, 2), res)

def findPosition(bn, position, pn):
    res = []
    for i in range(len(bn)):
        if bn[i][position] == pn:
            res.append(bn[i])
    return res

def findCommonBit(bn, position):
    count1 = count0 = 0
    for i in range(len(bn)):
        if bn[i][position] == "1":
            count1 += 1
        else:
            count0 += 1

    return "1" if count1 >= count0 else "0" 

    
def findUncommonBit(bn, position):
    count1 = count0 = 0
    for i in range(len(bn)):
        if bn[i][position] == "1":
            count1 += 1
        else:
            count0 += 1

    return "0" if count0 <= count1 else "1" 

def getLevels(bn):
    ores = bn
    cres = bn
    for i in range(len(bn[0].strip("\n"))):
        ## find common/uncommon next bit
        mostCommonBit = findCommonBit(ores, i)
        mostUncommonBit = findUncommonBit(cres, i)
        if len(ores) == 1 and len(cres) == 1:
            break
        if len(ores) > 1:
            ores = findPosition(ores, i, mostCommonBit) 
        if len(cres) > 1:
            cres = findPosition(cres, i, mostUncommonBit)
    return (ores[0], cres[0])

def importInput(inputFile):
    binary_nums = []
    with open(inputFile) as inFile:
        for line in inFile:
            binary_nums.append(line)
    return binary_nums

def main():
    bn = importInput("./input")
    gres, gamma = getGamma(bn)
    eres, ep = getEp(gamma)
    print("first part answer: " + str(gres*eres))
    goxy, gco2 = getLevels(bn)
    ans2 = int(goxy.strip("\n"), 2) * int(gco2.strip("\n"), 2)
    print("second part answer: " + str(ans2))

if __name__ == '__main__':
    main()
