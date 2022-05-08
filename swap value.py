# l=[12,19,5,6,10]
def swap(l,a,b):
    l[a],l[b]=l[b],l[a]
    return l
l=[12,19,5,6,10]
a,b=1,3
print(swap(l,a-1,b-1))
