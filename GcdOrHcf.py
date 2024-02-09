n1 = int(input())
n2 = int(input())
n =0
if n1 > n2:
    n = n1
else:
    n = n2
d = 1
for i in range(1,n+1):
    if i%n1==0:
        if i%n2==0:
            d =i
            
print(d)