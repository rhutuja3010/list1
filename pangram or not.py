string="The quick brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
f=True
for char in alphabet:
    if char not in string.lower():
        f=False
if (f==True):
    print("pangram")
else:
    print("Not pangram")


# string=["The quick brown fox jumps over the lazy dog"] 
# for i in range(len(string)):
#     for j in range(len(string[i])):

#         print(string[i][j])









string="The quick brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
f=False or True
for char in alphabet:
    if char not in string.lower():
        f=False
    else:
        f==True
if (f==False):
    print("pangram n")
else:
    print(" pangram")


# string="The quick brown fox jumps over the lazy dog"
# alphabet="abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     if char not in string.lower():
#         print("n pangram")
#         break
#         # f=False
#     else:
#         print("pangram")
#         break
#         # f==True

