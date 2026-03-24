from numpy import *

#Easy : 400870020080000400006300801700100080612098734000060019193427500807010302020003000

#Useful functions-------------------------------------------------------------------------------------------------------
def displaySudoku(sk, l = 10, c = 10):
    for i in range(9):
        if i%3 == 0:
            print("-------------------------")
        lgn = ""
        for j in range(9):
            if j%3 == 0:
                lgn += "| "
            if i == l and j == c:
                lgn += "# "
            else:
                tmp = sk[i][j]
                if tmp == 0:
                    lgn += ". "
                else:
                    lgn += str(sk[i][j]) + " "
        lgn += "|"
        print(lgn)
    print("-------------------------")

def update_matrices():
    for l in range(9):
        for r in range(9):
            if sudoku[l][r] != 0:
                for m in range(9):
                    if sudoku[l][r] == m+1:
                        matrices[m][l] = 1
                        matrices[m][:,r] = 1
                        s1 = (l//3)*3
                        s2 = (r//3)*3
                        matrices[m][s1:s1+3, s2:s2+3] = 1
                    else:
                        matrices[m][l][r] = 1



#Initialisation---------------------------------------------------------------------------------------------------------
#Initialise sudoku
sudoku = zeros((9, 9), dtype=int)

#Input sudoku
empty = ["", " ", "0", "."]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
mod = input("1 : Manually enter each cell\n2 : Enter the 81 digit long code (with 0 for empty cells)\n3 : Use screenshot / picture\n")
isAnsWrong = True
while isAnsWrong:
    if mod == "1":
        for i in range(9):
            for j in range(9):
                print("\n\n\n")
                displaySudoku(sudoku, i, j)
                inp = "10"
                while True:
                    inp = input("Enter the number shown above with # : ")
                    if inp in empty:
                        sudoku[i][j] = 0
                        break
                    if inp in numbers:
                        sudoku[i][j] = int(inp)
                        break
                    print("Invalid input")
        displaySudoku(sudoku)
        if input("Is this Sudoku correct ? (y/n)").lower() == "y":
            isAnsWrong = False

    elif mod == "2":
        while True:
            inp = input("Enter the numbers starting from the top left and moving to the bottom right, row by row, filling in 0 for any empty cells: ")
            if len(inp) != 81:
                print(f"Invalid input, should be 81 digit but only {len(inp)} were given.")
            else:
                tmp = True
                inp2 = ""
                for i in inp:
                    if i in empty:
                        inp2 += "0"
                    else:
                        if i in numbers:
                            inp2 += i
                        else:
                            tmp = False
                            print(f"Invalid input, only digits allowed, '{i}' is not")
                            break
                inp = inp2
                if tmp:
                    break
        sd = [int(i) for i in inp]
        sudoku = array(sd).reshape((9, 9))
        displaySudoku(sudoku)
        if input("Is this Sudoku correct ? (y/n)").lower() == "y":
            isAnsWrong = False
    else:
        print("Not codded yet !")
        exit()
print("\n\n\n\n\n")

# Initialise matrices for each number
matrices = []
for i in range(9):
    matrices.append(zeros((9, 9)))



#Strategies-------------------------------------------------------------------------------------------------------------
def full_house():
    #https://www.sudopedia.org/wiki/Full_House
    action = False
    for l in sudoku:
        if count_nonzero(l == 0) == 1:
            action = True
            missing = list(set(range(1,10))-set(l))[0]
            l[where(l == 0)[0][0]] = missing

    for r in range(9):
        if count_nonzero(sudoku[:,r] == 0) == 1:
            action = True
            row = sudoku[:,r]
            missing = list(set(range(1,10))-set(row))[0]
            sudoku[where(row == 0)[0][0]][r] = missing

    for s1 in range(0,9,3):
        for s2 in range(0,9,3):
            square = sudoku[s1:s1+3, s2:s2+3]
            if count_nonzero(square == 0) == 1:
                action = True
                missing = list(set(range(1,10))-set(square.flatten()))[0]
                l,r = argwhere(square == 0)[0]
                sudoku[s1+l][s2+r] = missing
    return action

def naked_single():
	#https://www.sudopedia.org/wiki/Naked_Single
	action = False
	sum1 = zeros((9,9))
	for m in matrices:
		sum1 += m
	if 8 in sum1:
		action = True
		pos = argwhere(sum1 == 8)
		for p in pos:
			l,r = p
			m = 0
			while matrices[m][l, r] == 1:
				m += 1
			sudoku[l, r] = m+1
	return action



#Main loop--------------------------------------------------------------------------------------------------------------
print("Initially filled to", round((81 - count_nonzero(sudoku == 0)) * 100 / 81), "%\n\n")

act = True
while act:
    act = False
    update_matrices()
    if full_house():
        act = True
        print("Full house : ")
    else:
        if naked_single():
            act = True
            print("Naked single : ")
        else:
            pass
    if act:
        displaySudoku(sudoku)
        print("Filled to", round((81 - count_nonzero(sudoku == 0)) * 100 / 81), "%")
        print("\n")
