file_path = "day5input.txt"

# All reports stored here
pages = []

rules_map = dict()
with open(file_path, "r") as file:
    for line in file:
        if '|' in line:
            row = list(map(int,line.strip().split('|')))
            if row[0] in rules_map:
                rules_map[row[0]].append(row[1])
            else:
                rules_map[row[0]] = [row[1]]
        if ',' in line:
            row = list(map(int,line.strip().split(',')))
            pages.append(row)

# print(rules_map)
s = set(rules_map.keys())

# res = 0
# for page in pages:
#     prefix_arr = []
#     corrFlag = True
#     for rule in page:
#         after_arr = []
#         if rule in rules_map:
#             after_arr = rules_map[rule]
#         for p in prefix_arr:
#             if p in after_arr:
#                 corrFlag = False
#                 break
#         prefix_arr.append(rule)
#         if corrFlag == False:
#             break
#     if corrFlag == False:
#         n = len(page)
#         print(page)
#         res += page[n//2]
# print(res)

res = 0
for page in pages:
    corrFlag = True
    n = len(page)
    for i in range(1,n):
        after_arr = []
        rule = page[i]
        if rule in rules_map:
            after_arr = rules_map[rule]
        for j in range(i):
            p = page[j]
            if p in after_arr:
                temp = page[i]
                del page[i]
                page.insert(j, temp)
                corrFlag = False
                break
        
    if corrFlag == False:
        res += (page[n//2])
print(res)
