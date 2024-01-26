n = int(input())
p = 0
for i in range(1,(1+n)):
    if(i %2 == 0):
        p = 0
    else:
        p =1
    for j in range(1,(1+i)):
        if j != 1:
            if p==0:
                p=1
            else:
                p = 0
        print(p,end="")
    print()