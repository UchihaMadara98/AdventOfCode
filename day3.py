import re
file_path = "day3input.txt"
pattern = r"mul[(](\d{1,3}),(\d{1,3})[)]|(do)[(][)]|(don't)[(][)]"
# All reports stored here
multiplications = []

with open(file_path, "r") as file:
    for line in file:
        matches = re.finditer(pattern, line)
        all_matches = []
        for match in matches:
            all_matches.append(match.groups())
        multiplications += all_matches

print(len(multiplications))

res = 0
do_flag = True
for exp in multiplications:
    if exp[2] == "do":
        do_flag = True
    elif exp[3] == "don't":
        do_flag = False
    elif do_flag == True:
        res += (int(exp[0]) * int(exp[1]))

print(res)