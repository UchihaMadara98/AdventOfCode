file_path = "day7input.txt"

puzzle = []

with open(file_path, "r") as file:
    for idx, line in enumerate(file):
        row = list(line.strip().split(':'))
        row = [int(row[0]), list(map(int, row[1].strip().split(' ')))]
        puzzle.append(row)



answer = 0
for p in puzzle:
    n = len(p[1])
    arr = p[1]
    for i in range(3**(n-1)):
        digits = i
        res = arr[0]
        for j in range(n-1):
            if digits%3 == 0: 
                res = res + arr[j+1]
            elif digits%3 == 1:
                res = res * arr[j+1]
            else:
                res = int(str(res) + str(arr[j+1]))
            digits = digits//3
        if res == p[0]:
            print(p[0])
            answer += p[0]
            break
print("Answer:")
print(answer)

