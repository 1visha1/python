# exploring the data types
# numberic data types
a = 5
# int
b = 3.12
# floast
c = 323.3j
# complex

print(type(a))
print(type(b))
print(type(c))

# string data type
str = 'this is string'
print(str)
print(type(str))

# performing slice operation on string
print(str[0:2]) 

# printing string 2 times
print(str*2)

# performing concatination on string
str2 = 'hi'
print(str2+str)

#list data types
list = [1,2,'hello','java']
print(list)

#slicing list
print(list[3:])

# list concatination
list2 = ['ehi','ewfs']
print(list+list2)

#tuple
tp = ('hi','sdf',1,2)
print(tp)
print(type(tp))

# dictionary
dct = {1 : 'ji',
2:'ef'}
print(dct)
print(type(dct))

print(type(True))

#set

set = {'james',12,'sdf'}

print(set)

#adding element to set
set.add('new')
print(set)

# removing element from set
set.remove('new')
print(set)