with open('input/day01.txt') as f:
  stringList = ("".join(f.readlines()).split('\n'))
  inputList = list(map(int, stringList))

#Part 1
  def compareValues(startValue, list):
    counter = 0
    for currentValue in list:
      if startValue < currentValue:
        counter += 1
      
      startValue = currentValue
    print(counter)

  compareValues(inputList[0], inputList)

#Part 2
  startValue = sum(inputList[ 0 : 3])
  groupList = []
  
  for i, x in enumerate(inputList):
    if i + 3 > len(inputList):
      break
    groupList.append(sum(inputList[ i: i + 3]))

  compareValues(startValue, groupList)



