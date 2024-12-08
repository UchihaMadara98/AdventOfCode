def isSafe(report):
    cnt_positive = 0
    cnt_negative = 0
    cnt_diff = 0
    res = False
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if diff >= 0:
            cnt_positive+=1
        else:
            cnt_negative+=1
    if cnt_positive == 0 or cnt_negative == 0:
        res = True
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
           cnt_diff+=1
    if cnt_diff >= 1:
        res = False
    return res

def isSafeDampener(report):
    cnt_positive = 0
    cnt_negative = 0
    cnt_diff = 0
    dampener = True
    res = False
    pos_idx = -1
    neg_idx = -1
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if diff >= 0:
            pos_idx = i
            cnt_positive+=1
        else:
            neg_idx = i
            cnt_negative+=1
    if cnt_positive == 0 or cnt_negative == 0:
        res = True
    elif cnt_positive == 1 or cnt_negative == 1:
        res = True
        dampener = False
        if cnt_positive ==1:
            del report[pos_idx]
        else:
            del report[neg_idx]
    else:
        return False
    
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or (abs(diff) > 3 and (i==1 or i == len(report) - 1)):
           cnt_diff+=1
        elif abs(diff) > 3:
            return False
    if cnt_diff == 0:
        return True
    elif cnt_diff == 1 and dampener == True:
        return True
    else:
        return False

    

file_path = "day2input.txt"

# All reports stored here
reports = []

with open(file_path, "r") as file:
    for line in file:
        report = list(map(int, line.strip().split()))
        reports.append(report)

#Without Dampner
# cnt = 0
# for report in reports:
#     if isSafe(report):
#         print(report)
#         cnt+=1
# print(cnt)

#With Dampner
cnt = 0
for report in reports:
    if isSafeDampener(report):
        print(report)
        cnt+=1
print(cnt)