file_path = "day9input.txt"

contents = []

with open(file_path, "r") as file:
    for idx, line in enumerate(file):
        contents = list(map(int,line.strip()))

#print(contents)

file_id = 0
unpack_content = []
blank_dict = dict()
blank_keys = []
file_dict = dict()
file_keys = []
for i, file_size in enumerate(contents):
    # print(i, file_size)
    if i%2 == 0:
        m = len(unpack_content)
        if file_size > 0:
            file_dict[m] = file_size
            file_keys.append(m)
        for j in range(file_size):
            unpack_content.append(file_id)
        max_id = file_id
        file_id+=1
    else:
        m = len(unpack_content)
        if file_size > 0:
            blank_dict[m] = file_size
            blank_keys.append(m)
        for j in range(file_size):
            unpack_content.append(-1)

n = len(unpack_content)
i = 0
j = n - 1



# while j >= 0 and i < n and i <= j :
#     if unpack_content[i] < 0 and unpack_content[j] >= 0:
#         t = unpack_content[i]
#         unpack_content[i] = unpack_content[j]
#         unpack_content[j] = t
#     elif unpack_content[i] >= 0:
#         i+=1
#     elif unpack_content[j] < 0:
#         j-=1



# print(unpack_content)
# res = 0
# for i, file_size in enumerate(unpack_content):
#     if file_size < 0 :
#         break
#     res += (i*file_size)
# print(res)


# print(unpack_content)
# print(blank_dict, blank_keys)
# print(file_dict, file_keys)
# print(i,j, max_id)

for j in file_keys[::-1]:
    sze = file_dict[j]
    # print(unpack_content)
    # print(blank_dict, blank_keys)
    #print()
    cavity = -1
    for b in blank_keys:
        if b > j:
            #print('paar')
            break
        if b in blank_dict and blank_dict[b] >= sze:
            cavity = b
            break
    if cavity >= 0:
        for k in range(sze):
            t = unpack_content[cavity + k]
            unpack_content[cavity + k] = unpack_content[j + k]
            unpack_content[j + k] = t
        
        cs = blank_dict[cavity]
        del blank_dict[cavity]
        if cs > sze:
            idx = blank_keys.index(cavity)
            blank_keys[idx] = cavity + sze
            blank_dict[blank_keys[idx]] = (cs - sze)
        else:
            idx = blank_keys.index(cavity)
            blank_keys[idx] =  -1

# print(unpack_content)
# print(blank_dict, blank_keys)


res = 0
for i, file_size in enumerate(unpack_content):
    if file_size >= 0 :
        res += (i*file_size)
print(res)
