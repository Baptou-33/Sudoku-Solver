from numpy import *
grid = [[0] * 9] * 9

def displayGrid(gd, l, c):
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
                tmp = gd[i][j]
                if tmp == 0:
                    lgn += ". "
                else:
                    lgn += str(gd[i][j]) + " "
        lgn += "|"
        print(lgn)
    print("-------------------------")

def main():
    for i in range(9):
        for j in range(9):
            print("\n\n\n")
            displayGrid(grid, i, j)
            grid[i][j] = input("Entrez le nombre ci dessus:")


main()