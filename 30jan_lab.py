#30jan(python lab)
'''#wap to fnd value of a%b without % operator
a=int(input('enter integer:'))
b=int(input('enter integer:'))
c=a//b
print(a-(b*c))'''

'''#swapping by third variable(assignment variable)
a=int(input('enter integer:'))
b=int(input('enter integer:'))
c=a
a=b
b=c
print('number after swapping is:a=',a,'b=',b)'''

'''# swap using airthmetic operator
a=int(input('enter integer:'))
b=int(input('enter integer:'))
a=a+b
b=a-b
a=a-b
print('number after swapping is:a=',a,'b=',b)'''

'''#swap using bitwise operator
a=int(input('enter integer:'))
b=int(input('enter integer:'))
a=a^b
b=a^b
a=a^b
print('number after swapping is:a=',a,'b=',b)'''

'''#wap to multiply a no. by 64 without multiplication operator
x=int(input('enter integer:'))
x=x<<6
print(x)'''

'''#wap to divide a no. by 32 without division operator
x=int(input('enter integer:'))
x=x>>5
print(x)'''

'''#wap to multiply a no. by 63 without multiplication operator
x=int(input('enter integer:'))
x=(x<<6)-x
print(x)'''

'''#suppose shyam live 9489days in jungle. calculate how many years,months,days he lived.
days=9489
years=days//365
days=days%365
months=days//30
days=days%30
weeks=days//7
days=days%7
print('years=',years,'months=',months,'weeks=',weeks,'days=',days)'''

'''#even or odd using airthmetic operator
a=int(input('enter a number:'))
if a%2==0:
    print('even')
else:
    print('odd')'''

'''#even or odd without using airthmetic operator
a=int(input('enter a number:'))
if a&1:
    print('odd')
else:
    print('even')'''

'''#input sides of triangle using heroin's formula
import math
a=float(input('enter 1st side:'))
b=float(input('enter 2nd side:'))
c=float(input('enter 3rd side:'))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'the area of the triangle is:,{area:.2f}')'''

'''#compound interest
p=int(input('enter principal:'))
r=int(input('enter rate:'))
t=int(input('enter time:'))
compound_interest=p*(1+r)**t-p
print(f'compound interest={compound_interest:.2f}')'''

'''#wap to input to height & weight in cm&kgs & convert its into feets & pounds
height=float(input("enter height in cm:"))
weight=float(input('enter weight in kgs:'))
height_in_feets=0.033*height
weight_in_pounds=2.205*weight
print('height=',height_in_feets,'feets')
print('weight=',weight_in_pounds,'pounds')'''





    





