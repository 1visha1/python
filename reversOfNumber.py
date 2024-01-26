n = int(input())  
is_negative = False  

if n < 0:
    is_negative = True
    n = abs(n)  

r = 0  

while n != 0:
    r = r * 10  
    r += n % 10  
    n = int(n / 10) 

if is_negative:
    r = -r  

print(r)  
