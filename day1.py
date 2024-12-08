file_path = "day1input.txt"

arr1 = []
arr2 = []

# Open and read the file
with open(file_path, "r") as file:
    for line in file:
        columns = line.strip().split()        
        arr1.append(int(columns[0]))
        arr2.append(int(columns[1]))

# Print results for 1 star 
arr1.sort()
arr2.sort()

res = 0
for i in range(len(arr1)):
    res += abs(arr1[i]-arr2[i])
print(res)

# Print results for 2 star 
cnt_mp = dict()
for ele in arr2:
    if ele in cnt_mp:
        cnt_mp[ele]+=1
    else:
        cnt_mp[ele]=1
res = 0
for ele in arr1:
    if ele in cnt_mp:
        res = res + (cnt_mp[ele]*ele)
print(res)