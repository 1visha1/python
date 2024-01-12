a = input("Enter a character: ")
o = -1
for char in range(ord('a'), ord('z')+1):

    if chr(char) == a:
        o = 0
        break
for char in range(ord('A'), ord('Z')+1):
    if chr(char) == a:
        o = 1
        break

print(o)

