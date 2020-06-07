lst=list(range(1,6))
print(min(lst))

lst=[1,2,3]
result=1*2*3
print(result)


lst=list(range(1,6))
print(len(lst))
print(sum(lst))
result= ((sum(lst))/(len(lst)))
print(result)


num=int(input("enter the number"))
factorial=1
if num<0:
    print("factorial not there for negative numbers")
elif num==0:
    print("print factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)

lst1=[]
lst2=[]
lst3=[]
lst=list(range(1,6))

for i in lst:
    if i%2==0:
        lst1.append(i)
        
    else:
        lst2.append(i)
print(lst1)
print(lst2)
lst3=(lst1+lst2)
print(lst3)
    

lst=list(range(1,31))
lst1=[i**2 for i in lst]
print(lst1)
print(lst1[:6])
print(lst1[-1:-6])

from random import shuffle
lst=list(range(1,6))
shuffle(lst)
print(lst)
      
