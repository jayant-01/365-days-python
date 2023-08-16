#line continuation

print("hello world")


# print("hello 
# world")  error

print("hello \
world") # ok



#unpacking sequence into separate variables

s= "hello"
a,b,c,d,e=s
print(a,b,c,d,e)

p=(4,50)
x,y=p
print(x,y)

l={1,2,3,4,5}
a1,a2,a3,a4,a5=l
print(a1,a2,a3,a4,a5)

lst = [1,"hello",(4,6),{1,2,3}]
a0,b0,c0,d0=lst
_,hh,hhh,_=lst
print(hh,hhh,_) 
print(a0,b0,c0,d0)



#unpacking elements from iterables of arbitrary length