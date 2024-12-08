file_path = "day6input.txt"

maan_chitro = []

with open(file_path, "r") as file:
    for idx, line in enumerate(file):
        row = list(line.strip())
        if '^' in row:
            j = row.index('^')
            turtle = [idx,j]
        maan_chitro.append(row)

print(len(maan_chitro), len(maan_chitro[0]))
n = len(maan_chitro)

orig_turtle = turtle

dir_dict = {
    'w' :{'next': 'd', 'dir':[-1,0]},
    'a' :{'next': 'w', 'dir':[0,-1]},
    's' :{'next': 'a', 'dir':[1,0]},
    'd' :{'next': 's', 'dir':[0,1]}
}

def solve(maan_chitro, turtle, n):
    dir = 'w'
    cnt = 0
    print(n)
    while turtle[0] > 0 and turtle[1] > 0 and turtle[0] < (n-1) and turtle[1] < (n-1):
        delta = dir_dict[dir]['dir']
        cnt+=1
        if cnt > n*n:
            return (n*n + 1)
        prev_turtle = turtle
        turtle = [turtle[0]+delta[0], turtle[1]+delta[1]]
        if maan_chitro[turtle[0]][turtle[1]] != '#':
            maan_chitro[turtle[0]][turtle[1]] = 'X'
        else:
            dir = dir_dict[dir]['next']
            turtle = prev_turtle
    return cnt

dir = 'w'
s = set()
while turtle[0] > 0 and turtle[1] > 0 and turtle[0] < (n-1) and turtle[1] < (n-1):
    delta = dir_dict[dir]['dir']
    prev_turtle = turtle
    turtle = [turtle[0]+delta[0], turtle[1]+delta[1]]
    if maan_chitro[turtle[0]][turtle[1]] != '#':
        mp = [row[:] for row in maan_chitro]
        mp[turtle[0]][turtle[1]] = '#'
        ans = solve(mp, orig_turtle, n)
        if ans >= (n*n + 1):
            s.add(str(turtle[0])+'_'+str(turtle[1]))
    else:
        dir = dir_dict[dir]['next']
        turtle = prev_turtle
