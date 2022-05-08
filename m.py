m=[[8,3,4],
   [1,5,9],
   [6,7,2]]
A=15
i=0
while i<len(m):
    row=0
    sum=0
    while row<len(m[i]):
        sum+=m[row][row]
        row+=1
    print(sum,"row")
    x=sum+sum+sum
    i+=1
print(x)
j=0
while j<len(m):
    column=0
    sum1=0
    l=len(m[j])
    while column<l:
        sum1+=m[j][column]
        column+=1
    print(sum1,"column")
    y=sum1+sum1+sum1
    j+=1
print(y)
a=m[0][0]+m[1][1]+m[2][2]
b=m[0][2]+m[1][1]+m[2][0]
if a==A:
    if b==A:
        c=a+b
        print("it is digonal:",c)
        if sum==sum1==A:
            print("it is magic square")
        else:
            print("it is not magic square")
    else:
        print("it is not magic square")
else:
    print("it is not magic square")