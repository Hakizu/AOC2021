#Thanks to @aufbakanleitung for this 5head solution
#separate input and boards
numbers, *boards  = open('input/day04.txt').read().split('\n\n')

#convert inputs to list[int]
#iterate over elements and convert them to int, wrap in []
numbers = [int(n) for n in numbers.split(',')] 

#put boards into their own array by using empty lines
#between lines as separator, resulting in e.g. list[list[str]]
boards = [line.split('\n') for line in boards] 

#put board lines into their own array & remove spaces
#split items on emtpy spaces and remove them with
#filter(None) - that is shorthand for removing false elements
# e.g. one board looks like:
# [ [line],
#   [line],
#   [line],
#   [line] ]
boards = [[list(filter(None, line.split(' '))) for line in board] for board in boards]

#Put all fieldNumber into their own array, convert them into integers
#and attach a False Flag e.g. [7, False] for a field and nest them
#respectively
boards = [[[[int(nr), False] for nr in line] for line in board] for board in boards]

#Check every field, in every line, on each board
#and mark the field on a match by setting their flag to true
def markField(nr):
  for board in boards:
    for line in board:
      for field in line:
        if field[0] == nr:
          field[1] = True

#Check if one element in line is unmarked
#if unmarked return false
def checkRow(line):
  for nr in line:
    if nr[1] == False:
      return False
  return False

#A board has 5 columns, check the column,
# on each line, if field is marked,
# all columns have marked field, we're in the
# 5th iteration and check with i == 4 (i starts on 0)
# if all columns were checked & return true
def checkColumn(board):
  for col in range(len(board)):
    for i, line in enumerate(board):
      if line[col][1] == False:
        break
      elif i == 4:
        return True

def runBingo(boards):
  #for a number in inputs
  for nr in numbers:
    markField(nr)
    #check for winner
    for board in boards:
      if checkColumn(board):
        # f is a formatted string, allowing us to reference
        # variables within the string
        print(f"Column Winner:: {nr}")
        return nr, board
      for line in board:
        if checkRow(line):
          print(f'row winner: {nr}')
          return nr, board

def finalScore(winNo, board):
  total = 0
  for line in board:
    for nr in line:
      if nr[1] == False:
        total += nr[0]
  print(f'Total: {total}')
  print(f'Final score: {winNo * total}')

winNo, winBoard = runBingo(boards)
finalScore(winNo, winBoard)

#Part 2
# unique entries
finishedBoards = set()

def checkRowLast(board):
  for line in board:
    for i, nr in enumerate(line):
      if nr[1] == False:
        break
      if i == 4:
        return True

def checkColumnLast(board):
  for col in range(len(board)):
    for i, line in enumerate(board):
      if line[col][1] == False:
        break
      elif i == 4:
        return True
  return False

def runLast(boards):
  for nr in numbers:
    markField(nr)
    for i, board in enumerate(boards):
      #if iteration of board alreyady saved, skip
      if i in finishedBoards:
        continue

      if checkRowLast(board):
        # check if it's the last board
        if len(finishedBoards) == len(boards) -1:
          return nr, board
        finishedBoards.add(i)
      
      if checkColumnLast(board):
        if len(finishedBoards) == len(boards) -1:
          return nr, board
        finishedBoards.add(i)

lastNr, lastBoard = runLast(boards)
finalScore(lastNr, lastBoard)