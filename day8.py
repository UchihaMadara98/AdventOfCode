from math import gcd
file_path = "day8input.txt"

city = []

with open(file_path, "r") as file:
    for idx, line in enumerate(file):
        row = list(line.strip())
        city.append(row)

m = len(city[0])
print(len(city),len(city[0]))

at_location_dict = dict()

for i, c in enumerate(city):
    for j, point in enumerate(c):
        if point != '.':
            if point in at_location_dict:
                at_location_dict[point].append([i,j])
            else:
                at_location_dict[point]=[[i,j]]

an_loc_set = set()
for loc in at_location_dict:
    arr = at_location_dict[loc]
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            p0 = arr[i]
            p1 = arr[j]
            #print(p0,p1)
            (x0, y0) = (p0[0], p0[1])
            (x1, y1) = (p1[0], p1[1])
            for t in [2,-1]:
                (xt, yt) = (((1-t)*x0 + t*x1),((1-t)*y0 + t*y1))
                if xt >=0 and yt>=0 and xt < m and yt < m:
                    an_loc_set.add(str(xt)+"_"+str(yt))
# print(an_loc_set)
print(len(an_loc_set))

an_loc_set = set()
for loc in at_location_dict:
    arr = at_location_dict[loc]
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            p0 = arr[i]
            p1 = arr[j]
            (x0, y0) = (p0[0], p0[1])
            (x1, y1) = (p1[0], p1[1])
            d = gcd(gcd(x0,x1),gcd(y0,y1))
            t = 0
            #print(p0,p1,d)
            while True:
                (xt, yt) = (((d-t)*(x0//d) + t*(x1//d)),((d-t)*(y0//d) + t*(y1//d)))
                if xt >=0 and yt>=0 and xt < m and yt < m:
                    an_loc_set.add(str(xt)+"_"+str(yt))
                    # print(xt,yt)
                else:
                    break
                t+=1

            t = 0
            while True:
                (xt, yt) = (((d-t)*(x0//d) + t*(x1//d)),((d-t)*(y0//d) + t*(y1//d)))
                if xt >=0 and yt>=0 and xt < m and yt < m:
                    an_loc_set.add(str(xt)+"_"+str(yt))
                    #print(xt,yt)
                else:
                    break
                t-=1

# print(an_loc_set)
print(len(an_loc_set))