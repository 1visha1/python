n = int(input())
i =0
a = 0
b = 1
feb = 0
if n != 1:
    n -=1
while i < n:
    feb = a + b
    a = b
    b = feb
    i+=1
print(feb)