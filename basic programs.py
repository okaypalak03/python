#basic programs

'''#1
print('hello')
print('world')'''

'''#2
print("hello",'world')'''

'''#3
a=5
b=7
print(a+b)'''

'''#4
a=5
b=3
print(a-b)'''

'''#5
a=5
b=6
print(a*b)'''

'''#6
a=int(input('enter integer value:'))
b=int(input('enter power in integer:'))
print(a**b)'''

'''#7
length=int(input('enter length='))
breadth=int(input('enter breadth='))
print('area is:',length*breadth)
print('perimeter is:',2*(length+breadth))'''

'''#8
r=float(input('enter rdius:'))
area=22.7*r*r
circumference=2*22.7*r
print('area=',area)
print('circumference=',circumference)'''

'''#9
base=int(input('enter base:'))
height=int(input('enter height:'))
hypo=((base**2)+(height**2))**0.5
print(f'hypo={hypo:.2f}')'''

'''#10
a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
c=a
a=b
b=c
print('after swapping:a=',a,'b=',b)'''

'''#11
amount1=int(input('enter amount='))
amount2=amount1-100
amount3=amount2//2000
amount4=amount2%2000
amount5=amount4//500
amount6=amount4%500
amount7=amount6//100
amount8=(amount7)+1
print('no. of 2000 notes=',amount3)
print('no. of 500 notes=',amount5)
print('no. of 100 notes=',amount8)'''

'''#12
a=int(input('enter 1st side:'))
b=int(input('enter 2nd side:'))
c=int(input('enter 3rd side:'))
if (a**2+b**2==c**2) or (b**2+c**2==a**2) or (c**2+a**2==b**2):
    print('triangle is right angled')
elif (a==b) or (b==c) or (c==a):
    print('triangle is isosceles')
elif (a!=b!=c!=a):
    print('triangle is scalene')
else:
    print('triangle is invalid')'''

'''#13
p=int(input('enter principle='))
r=int(input('enter rate='))
t=int(input('enter time='))
print('si=',(p*r*t)/100)'''

'''#14
p=int(input('enter principal:'))
r=int(input('enter rate:'))
t=int(input('enter time:'))
compound_interest=p*(1+r)**t-p
print(f'compound interest={compound_interest:.2f}')'''

'''#15
floor_l = float(input('Enter the length of the floor: '))
floor_w = float(input('Enter the width of the floor: '))
tile_l = float(input('Enter the length of the tile: '))
tile_w = float(input('Enter the width of the tile: '))
floor_area=floor_l*floor_w
tile_area=tile_l*tile_w
tiles_required=floor_area/tile_area
print('total tile required:',tiles_required)'''

'''#16
over=int(input('enter number of overs:'))
runs=((over-1)*33)+36
print('runs=',runs)'''

'''#17
heads=int(input('enter no. of heads:'))
feets=int(input('enter no. of feets:'))
goats=(feets-2*heads)//2
chickens=heads-goats
print(goats,'goats and',chickens,'chickens')'''

#if-else:

'''#1
a=int(input('enter a number:'))
if a%2==0:
    print('number is even')
else:
    print('number is odd')'''

'''#2
a=int(input('enter a 1st number:'))
b=int(input('enter a 2nd number:'))
if a>b:
    print(a,'-',b,'=',a-b)
else:
    print(b,'-',a,'=',b-a)'''

'''#3
x=7
while True:
       if x%7==0 and x%6==1 and x%5==1 and x%4==1 and x%3==1 and x%2==1:
            print(x)
            break
       x+=1'''

#if-elif-else:

'''#1
a=int(input('enter 1st value:'))
b=int(input('enter 2nd value:'))
c=int(input('enter 3rd value:'))
if a>b and a>c:
    print('a is greater:')
elif b>c and b>a:
    print('b is greater:')
else:
    print('c is greater')'''

'''#2
cx = float(input("Enter the x-coordinate of the center of the circle: "))
cy = float(input("Enter the y-coordinate of the center of the circle: "))
radius = float(input("Enter the radius of the circle: "))
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))
distance_squared = (x - cx)**2 + (y - cy)**2
radius_squared = radius**2
if distance_squared < radius_squared:
    relation = "Inside"
elif distance_squared == radius_squared:
    relation = "On the circle"
else:
    relation = "Outside"
print(f"The point P({x},{y}) is {relation} the circle.")'''

'''#3
bill_amount=int(input('enter the bill amount:'))
if bill_amount>25000:
    discounted_amount=bill_amount-(bill_amount/100)*20
    print('You are in GOLD category and ur bill after discount is:',discounted_amount)
elif 10000<bill_amount<25000:
     discounted_amount=bill_amount-(bill_amount/100)*10
     print('You are in SILVER category and ur bill after discount is:',discounted_amount)
else:
    discounted_amount=bill_amount-(bill_amount/100)*5
    print('You are in BRONZE category and ur bill after discount is:',discounted_amount)'''

'''#4
d=int(input('enter day:'))
m=int(input('enter month:'))
y=int(input('enter year:'))
dc=0   #daycount
while m<=12:
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d>0:
            dc=31-d
            d=0
        else:
            dc=dc+31
    if m==2:
        if d>0:
            dc=28-d
            d=0
        else:
            dc=dc+28
    if m==4 or m==6 or m==9 or m==11:
        if d>0:
            dc=30-d
            d=0
        else:
            dc=dc+30
    m+=1
print('no. of days left:',dc)'''

#loops:

'''#1
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''

'''#2
a=int(input('enter the number:'))
fact=1
for i in range(a,0,-1):
    fact*=i
print('factorial of',a,'is:',fact)'''

'''#3
n=int(input('enter the number:'))
i=0
for j in str(n):
    i+=int(j)
print('sum of digit is:',i)'''

'''#4
n=int(input('enter the number:'))
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print('sum of digits:',total)'''

'''#5
a=int(input('enter the number:'))
for i in range(1,11):
    print(a,'*',i,'=',a*i)'''

'''#6
n=int(input('enter number of kids:'))
c=int(input('enter number of candies:'))
sum=0
for i in range(1,n+1):
    x=int(input(f'enter number of candies for student no.{i}'))
    sum+=x
    if sum<=c:
        print('yes we can make kids happy')
    else:
        print('we cant make them happy')'''
    
'''#7
L1=[1]*500
for i in range(1,51):
    for j in range(i,len(L1)+1,i):
        if L1[j-1]==0:
            L1[j-1]=1
        else:
            L1[j-1]=0
#print(L1)
for i in range(len(L1)):
    if L1[i]==0:
        print('roll no.',i+1)
print('the number of off phones:',L1.count(0))'''

'''#8
basket = 51
while basket > 0:
    print(f"Balls remaining: {basket}")
    user_pick = int(input("Pick 1 to 4 balls (according to remaining): "))
    if user_pick < 1 or user_pick > 4 or user_pick > basket:
        print("Invalid input. Please pick 1 to 4 balls according to remaining.")
        continue
    basket -= user_pick
    if basket <= 0:
        print("User loses!")
        break
    computer_pick = (basket - 1) % 5
    if computer_pick == 0:
        computer_pick = 1
    print("Computer picks:", computer_pick)
    basket -= computer_pick
    if basket <= 0:
        print("Computer loses!")
        break'''



    

            




    
    











                




