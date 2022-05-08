# list=[5,0,1,8,2,6,3,9,4,7]
# for j in range(len(list)):
#     for i in range(len(list)-1):
#         if list[i]>list[i+1]:
#             a=list[i]
#             list[i]=list[i+1]
#             list[i+1]=a
# print(list)

# l=[5,0,1,8,2,6,3,9,4,7]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l)-1:
#         if l[j]>l[j+1]:
#             a=l[j]
#             l[j]=l[j+1]
#             l[j+1]=a
#         j+=1
#     i+=1
# print(l)

# list=[5,0,1,8,2,6,3,9,4,7]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list)-1:
#         if list[j]>list[j+1]:
#             a=list[j]
#             list[j]=list[j+1]
#             list[j+1]=a
#         j+=1
#     i+=1
# print(list)

# l1=[9,6,8,7,4,1,2,0,5,3]
# i=0
# while i<len(l1):
#     j=0
#     while j<len(l1)-1:
#         if l1[j]>l1[j+1]:
#             a=l1[j]
#             l1[j]=l1[j+1]
#             l1[j+1]=a
#         j+=1
# print(l1)

a=[1,3,6,7,9,2,4,0]
i=0
l=[]
while i<len(a):
    if a[i]%2==0:

        l.append(a[i])
    i+=2
print(l)

