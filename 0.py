p=[]
r=0
x=int(input("enter the number x"))
y=int(input("enter the number y"))
z=int(input("enter the small"))
a=x-y
for i in range(a):
   x=x+1
   p.append(x)
for i in range(len(p)):
    remainder=p[i]%10
    r=r*10 + remainder
    p=p[i]//10
print(p)
# for(i in range())





    
