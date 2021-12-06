with open('input/day03.txt') as f:
    stringList = (''.join(f.readlines()).split('\n'))

#Part1
    def findMostCommon(list):
        mostCommon = 0
        for element in list:
            if int(element):
                mostCommon +=1
        return mostCommon >= len(list)/2

    #first output
    output = ''
    for i in range(0, len(stringList[0])):
        newLine = ''
        for char in stringList:
            newLine += char[i]
        if findMostCommon(newLine):
            output += '1'
        else:
            output += '0'

    #reverse
    gamma = ''
    for char in output:
        if char == '1':
            gamma += '0'
        else:
            gamma += '1'
    print(int(gamma, 2) * int(output, 2))
