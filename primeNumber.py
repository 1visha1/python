n =int(input())
j=0
for i in range(1,n):
    if n%i==0:
        j+=1
if j==1 or n==1:
    print(True)
else:
    print(False)