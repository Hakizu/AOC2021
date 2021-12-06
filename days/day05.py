stringList = open('input/day05.txt').read().splitlines()

#Part 1
fields = {}
for line in stringList:
  #destructure into  left/right
  left, right = line.split(' -> ')
  #convert to int and destructure
  x1, y1 = map(int, left.split(','))
  x2, y2 = map(int, right.split(','))

  if y1 == y2:
    for i in range(min(x1,x2), max(x1,x2) +1):
      #set field value to = existing field value or if undefined 0 + 1
      fields[(y1, i)] = fields.get((y1, i), 0) +1
  
  if x1==x2:
    for i in range(min(y1,y2), max(y1,y2)+1):
      fields[(i, x1)] = fields.get((i, x1), 0) +1
  
  #Only for part2, diagonal lines
  #if line is not on same x or y field it has to be diagonal
  if not (x1 == x2 or y1 == y2):
    #get fields to move
    xDiagonal = x2 - x1
    yDiagonal = y2 - y1
    #mark start point
    fields[(y1, x1)] = fields.get((y1, x1), 0) +1

    #as long as not same field it is still diagonal, keep marking fields
    while not x1 == x2:
      x1 = x1 + (xDiagonal // abs(xDiagonal))
      y1 = y1 + (yDiagonal // abs(yDiagonal))
      fields[(y1, x1)] = fields.get((y1, x1), 0) +1

counter = 0
for field in fields.items():
  if field[1] >= 2:
    counter +=1
print(counter)