n = int(input())

a = n
i=0
while a != 0:
    a=int(a/10)
    i+=1
sum = 0
a = n
while a != 0:
    b = int(a%10)
    sum+= b ** i
    a=int(a/10)
print(sum)
if n==sum:
    print("true")
else:
    print("false")
