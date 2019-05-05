tuple1 = ("Hello","for","Hello")
tuple2 = ("Hell","or","heaven")
for i in tuple1:
    print(i)
for i in range(3):
    print(tuple1[i])

tuple3=tuple1+tuple2
print(tuple3)

tuple4 = tuple("thisispython3")
print(tuple4[1:])
print(tuple4[::-1])
print(tuple4[1:7])