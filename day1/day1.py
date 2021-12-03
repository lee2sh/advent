def countingDepthIncreases(inputFile):
    counter = 0
    prev = 0
    start = True
    with open(inputFile) as inFile:
        for line in inFile:
            if start:
                prev = int(line)
                start = False
                continue
            elif prev < int(line):
                counter += 1
            prev = int(line)
    return counter


def slidingWindow(inputFile):
    ##reading file
    nums = []
    k = 3
    with open(inputFile) as inFile:
        for line in inFile:
            nums.append(int(line))

    window_sum = sum(nums[:k])
    prev_sum = window_sum
    counter = 0

    for i in range(len(nums)-k):
        window_sum = window_sum - nums[i] + nums[i+k]
        if prev_sum < window_sum:
            counter += 1
        prev_sum = window_sum
    return counter

def main():
    count1 = countingDepthIncreases("./input")
    print(count1)
    count2 = slidingWindow("./input")
    print(count2)

if __name__ == '__main__':
    main()
