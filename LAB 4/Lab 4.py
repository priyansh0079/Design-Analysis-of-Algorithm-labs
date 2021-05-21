print("Enter N to get sol.s in N QUEEN PROBLEM")
print("Enter 0 to quit")
print()

backtracks=0
def isSafe (board, row, col,N):                           # N queen problem..
    for y in range(col):
        if board[row][y] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True
def generateSolution(board, col,N):
    global backtracks
    if col >= N:
        for i in board:
            print(i)
        print("No of backtracks= ",backtracks)
        print()
        return True
    res=False

    for i in range(N):
        if isSafe(board, i, col,N) == True:
            board[i][col] = 1


            res=generateSolution(board,col+1,N) or res
            backtracks+=1
            board[i][col] = 0
    return res

def N_queen():
    while True:
        N = int(input("enter N: "))
        if N==0:
            break
        else:
            startCol = 0

            board = [[0 for p in range(N)] for j in range(N)]

            if generateSolution(board, startCol, N) == False:
                print("No Solution Exists")
            else:
                pass
        # print("No of backtracks= ", backtracks)
N_queen()
print("-----------------------------")

print("-----------------------------")
print("SUDOKU PROBLEM")


matrix = [[5,1,7,6,0,0,0,3,4],                      #Sudoku problem
       [2,8,9,0,0,4,0,0,0],
       [3,4,6,2,0,5,0,9,0],
       [6,0,2,0,0,0,0,1,0],
       [0,3,8,0,0,6,0,4,7],
       [0,0,0,0,0,0,0,0,0],
       [0,9,0,0,0,0,0,7,8],
       [7,0,3,4,0,0,5,6,0],
       [0,0,0,0,0,0,0,0,0]]


def Empty_block():
    for i in range(0,9):
        for j in range (0,9):
            if matrix[i][j] == 0:
                row = i
                column = j
                block = [row, column]
                return block
    block = [-1, -1]
    return block

def validate_Matrix(num, r, c):
    for i in range(0,9):                              #To check if number is not present in that column.
        if matrix[r][i] == num:
            return False

    for i in range(0,9):                              #To check if number is not present in that row.
        if matrix[i][c] == num:
            return False

    Rstart = (r//3)*3
    Cstart = (c//3)*3

    for i in range(Rstart,Rstart+3):                  #To check if number is not present in
        for j in range(Cstart,Cstart+3):               # that particular 3X3 matrix.
            if matrix[i][j]==num:
                return False
    return True

backtrack=0

def solve_sudoku():
    global backtrack
    Block = Empty_block()
    if Block[0]==-1:
        return True
    row = Block[0]
    col = Block[1]
    for i in range(1,10):

        if validate_Matrix(i, row, col):
            matrix[row][col] = i
            if solve_sudoku():
                return True
            backtrack+=1
            matrix[row][col]=0
    return False

def print_ans():
    for i in matrix:
        print (i)

solve_sudoku()
print_ans()
print()
print("Number of backtracks= ",backtrack)


print("-----------------------------")
print("-----------------------------")

def combinationsSum(candidates: [int],target: int) -> [[int]]:
    nums=sorted(candidates)

    def dfs(space,path):
        if sum(path)>target:
            return
        if sum(path)==target:
            result.append(path)

        for i in range(len(space)):
            dfs(space[i:],path+[space[i]])

    result=[]
    dfs(nums,[])
    return result

candidates=[5, 10, 12, 13, 15, 18]
target=30
n=combinationsSum(candidates,target)
print("All unique combinations for target",target,"-->")
for i in n:
    print(i)




