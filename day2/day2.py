def HorizontalVsDepth(inputFile):
    hor = 0
    dep = 0

    with open(inputFile) as inFile:
        for line in inFile:
            splits = line.split(" ")
            if splits[0] == "down":
                dep += int(splits[1])
            elif splits[0] == "up":
                dep -= int(splits[1])
            elif splits[0] == "forward":
                hor += int(splits[1])
    return hor * dep

def HorizontalVsDepthVsAim(inputFile):
    hor = 0
    dep = 0
    aim = 0

    with open(inputFile) as inFile:
        for line in inFile:
            splits = line.split(" ")
            if splits[0] == "down":
                aim += int(splits[1])
            elif splits[0] == "up":
                aim -= int(splits[1])
            elif splits[0] == "forward":
                hor += int(splits[1])
                dep += int(splits[1]) * aim
    return hor * dep

def main():
    hd = HorizontalVsDepth("./input")
    print(hd)

    hd2 = HorizontalVsDepthVsAim("./input")
    print(hd2)
if __name__ == '__main__':
    main()

