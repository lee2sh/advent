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
    print(res)
    return res

def getEpsilon(bn):
    ep = ""
    for i in range(len(bn[0].strip("\n"))):
        count1 = 0
        count0 = 0
        for j in range(len(bn)):
            if bn[j][i] == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 < count0:
            ep += "1" 
        else:
            ep += "0"

    res = int(ep, 2)
    print(res)
    return res

def importInput(inputFile):
    binary_nums = []
    with open(inputFile) as inFile:
        for line in inFile:
            binary_nums.append(line)
    return binary_nums

def main():
    bn = importInput("./input")
    gamma = getGamma(bn)
    epsilon = getEpsilon(bn)
    print("first part answer: " + str(gamma*epsilon))

if __name__ == '__main__':
    main()
