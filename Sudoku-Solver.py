from numpy import *

#Useful functions-------------------------------------------------------------------------------------------------------
def displaySudoku(sk, l, c):
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
	#https://www.sudoku.academy/learn/the-rules-of-sudoku/
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
inp = input("1 : Manually enter each cell\n2 : Enter the 81 digit long code (with 0 for empty cells)\n3 : Use screenshot / picture\n")
if inp == "1":
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
elif inp == "2":
    inp = input("Enter the numbers starting from the top left and moving to the bottom right, row by row, filling in 0 for any empty cells: ")
    assert (len(inp) == 81)
    sd = [int(i) for i in inp]
    sudoku = array(sd).reshape((9, 9))
else:
    print("Not codded yet !")
    exit()

#Initialise matrices for each number
matrices = []
for i in range(9):
    matrices.append(zeros((9, 9)))



#Strategies-------------------------------------------------------------------------------------------------------------



#Main loop--------------------------------------------------------------------------------------------------------------
act = True
while act:
    act = False




    print("Rempli à", round((81 - count_nonzero(sudoku == 0)) * 100 / 81), "%")
