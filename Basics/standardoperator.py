import operator
a = 4
b = 2
print("1")
print(operator.add(a,b))
print("2")
print(operator.sub(a,b))
print("3")
print(operator.mul(a,b))
print("4")
print(operator.add(a,b))
print("5")
print(operator.truediv(a,b))
print("6")
print(operator.floordiv(a,b))
print("7")
print(operator.pow(a,b))
print("8")
print(operator.mod(a,b))
print("9")
print(operator.lt(a,b))
print("10")
print(operator.le(a,b))
print("12")
print(operator.eq(a,b))
print("12")
print(operator.ne(a,b))
print("13")
print(operator.gt(a,b))
print("14")
print(operator.ge(a,b))
list = [1,2,3,4,5]
operator.setitem(list,3,7) 
print(list)
operator.delitem(list,3) 
print(list)
print(operator.getitem(list,3))
li = [6,7,8,9,0]
operator.setitem(li,slice(1,4),[2,3,4])
print(li)
operator.delitem(li,slice(1,4))
print(li)
print(operator.getitem(li,slice(0,2)))
s1 = "testing "
s2 = "operator"
print(operator.concat(s1,s2))
if(operator.contains(s1,s2)):
    print("Contains")
else:
    print("It doesn't"
)
a =1
b =0
print(operator.and_(a,b))
print(operator.or_(a,b))
print(operator.invert(a))

x = 10
y = 5
print(operator.iadd(x,y))
print(operator.isub(x,y))
print(operator.iconcat(s1,s2))
print(operator.imul(x,y))
print(operator.itruediv(x,y))
print(operator.imod(x,y))
print(operator.ixor(x,y))
print(operator.ipow(x,y))
print(operator.iand(x,y))
print(operator.ior(x,y))
print(operator.ilshift(x,y))
print(operator.irshift(x,y))