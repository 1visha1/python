n = int(input())

for i in range(1,n+1):
    space = " "*(n-i)
    stars = "*"*(2*i-1)
    print(space+stars)
i = n 
while i>=0:
    space = " "*(n-i)
    stars = "*"*(2*i-1)
    print(space+stars)
    i-=1