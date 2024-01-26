n = int(input())
space = " "*n
for i in range(1,(n+1)):
    j =1
    while j <= i:
        print(j,end="")
        j+=1
    if(i != n):
        space=" "*(n-i-1)
        print(space,space,end="")
    j-=1
    while j !=0:
        print(j,end="")
        j-=1
    print()
    