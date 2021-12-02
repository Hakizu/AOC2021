with open('input/day02.txt') as f:
    stringList = ("".join(f.readlines()).split('\n'))

#Part1
    def calculatePosition(input):
        depth = 0
        horizontal = 0

        for x in input:
            segments = x.split(' ')
            movement = int(segments[1])
            
            if segments[0] == 'up':
                depth -= movement
            elif segments[0] == 'down':
                depth += movement
            else:
                horizontal += movement
                

        print(depth * horizontal)
    calculatePosition(stringList)

#Part2
    depth = 0
    horizontal = 0
    aim = 0

    for x in stringList:
        segments = x.split(' ')
        movement = int(segments[1])

        if segments[0] == 'up':
            aim -= movement
        elif segments[0] == 'down':
            aim += movement

        else:
            horizontal += movement
            depth += aim * movement

    print(depth * horizontal)