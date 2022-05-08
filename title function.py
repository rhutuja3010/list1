def title_function(a):
    # a="rhutuja"
    l=[]
    for i in range(len(a)):
        if i==0:
            l.append(a[i].upper())
        else:
            l.append(a[i])
    print("".join(l))
title_function("rhutuja")
