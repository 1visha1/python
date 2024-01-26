n = int(input())
e=0
o=0
while n !=0:

    a = n%10
    if a % 2 == 0:
        e+=a
        
    else:
        o+=a
    n = int(n/10)
print(e, " ", o)
