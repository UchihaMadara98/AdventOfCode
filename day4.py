file_path = "day4input.txt"

# All reports stored here
grid = []

with open(file_path, "r") as file:
    for line in file:
        row = list(line.strip())
        grid.append(row)

m = len(grid)
n = len(grid[0])

xmas_count = 0

#Horizontal vertical
for i in range(m):
    row = ""
    column = ""
    for j in range(n):
        row += grid[i][j]
        column += grid[j][i]
    xmas_count += row.count('XMAS')
    xmas_count += row.count('SAMX')
    xmas_count += column.count('XMAS')
    xmas_count += column.count('SAMX')

# The Diagonals
for s in range(m+n-1):
    sum_ind = s
    diag1 = ""
    diag2 = ""
    i = min(sum_ind,(m-1))
    j = sum_ind - i
    lim = i
    while(j <= lim):
        diag1 += grid[i][j]
        diag2 += grid[m-1-j][i]
        j+=1
        i-=1
    xmas_count += diag1.count('XMAS')
    xmas_count += diag1.count('SAMX')
    xmas_count += diag2.count('XMAS')
    xmas_count += diag2.count('SAMX')
print(xmas_count) 

xmas_count2 = 0

for i in range(1,m-1):
    for j in range(1,n-1):
        if grid[i][j] == 'A':
            diag1a = grid[i+1][j+1]
            diag1b = grid[i-1][j-1]
            diag2a = grid[i+1][j-1]
            diag2b = grid[i-1][j+1]
            if (diag1a == 'M' and diag1b == 'S') or (diag1a == 'S' and diag1b == 'M'):
                if (diag2a == 'M' and diag2b == 'S') or (diag2a == 'S' and diag2b == 'M'):
                    xmas_count2+=1


print(xmas_count2) 