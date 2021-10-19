dic={"a":{"b":10,"c":5},"d":{"e":6,"f":3}}
for i in dic:
    print(i)
    for j in dic[i]:
        print(j,end=" ")
        # print(dic[j])
        print(dic[i][j],end=" ")
