sum = 1
for i in range(1, 100):
    print(i)
    sum *= i
print(sum)


def fun(a, b, c, d):
    print(a, b, c, d)


list = [1, 2, 3, 4]
fun(*list)


def new_sum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum += args[i]
    return sum


print(new_sum(1, 2, 3, 4, 5))


def function(a, b, c, d):
    print(a, b, c, d)


d = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
function(**d)


# Python code to demonstrate Type conversion
# using  tuple(), set(), list()

# initializing string
s = 'SAURABH'

# printing string converting to tuple
c = tuple(s)
print("After converting string to tuple : ", end="")
print(c)

# printing string converting to set
c = set(s)
print("After converting string to set : ", end="")
print(c)


a = "Thats it."
c = b'Thats it.'

d = a.encode('ASCII')
e = c.decode('ASCII')

a, b = 10, 20
min = a if a < b else b

#sequence of or
print (any([False, False, False, False]))
print (any([False, True, False, False]))

#sequence of and
print (all([True, True, True, True])) 
print (all([False, True, True, False])) 