def display(floor, row, col):
    print("Floor Matrix :")

    for i in range(len(floor)):
        for j in range(len(floor[i])):
            if i == row and j == col:
                print(">" + str(floor[i][j]) +"<", end ="")
            else:
                print(" " + str(floor[i][j]) +" ", end ="")
        print(end = "\n")
    print(end = "\n")

def clean(floor):
    i = 0
    j = 0
    row = len(floor)
    col = len(floor[0])

    for i in range(row):
        if i%2==0:
            for j in range(col):
                if floor[i][j] == 1:
                    display(floor, i, j)
                    floor[i][j] = 0
                display(floor, i, j)
        else:
            for j in range(col-1, -1, -1):
                if floor[i][j] == 1:
                    display(floor, i, j)
                    floor[i][j] = 0
                display(floor, i, j)

def main():
    floor = []

    m = int(input("Enter number of Rows :"))
    n = int(input("Enter number of Columns :"))
    
    print("Enter status of each floor (1-dirty, 0-clean)")

    for i in range(m):
        f = list(map(int, input().split(" ")))
        g = f[0:n]
        floor.append(g)
    
    print(end = "\n")

    clean(floor)

main()