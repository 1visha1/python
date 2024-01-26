n=int(input())
p=1
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print(p,end=" ")
        p+=1
    print()