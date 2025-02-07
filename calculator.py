def add():
    n=int(input('How many number you want to add: '))
    sum=0
    for i in range(n):
        a=int(input('Enter any number: '))
        sum+=a
    print(f'The sum of {n} numbers is {sum}')
def sub():
    n=int(input('How many number you want to subtract: '))
    sum=0
    for i in range(n):
        a=int(input('Enter any number: '))
        if sum==0:
            sum=a
        else:
            sum-=a
    print(f'The difference of {n} numbers is {sum}')
def multiply():
    n=int(input('How many number you want to multiply: '))
    sum=1
    for i in range(n):
        a=int(input('Enter any number: '))
        sum*=a
    print(f'The product of {n} numbers is {sum}')
def div():
    a=int(input('Enter any number: '))
    b=int(input('Enter any number: '))
    if b==0:
        print('Math Error!')
    else:
        print(f'The Division of {a} and {b} is {a/b}')
while True:
    print('****SIMPLE CALCULATOR****')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplycation')
    print('4. Division')
    print('5. Exit')
    choice=int(input('Enter your choice: '))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        multiply()
    elif choice==4:
        div()
    elif choice==5:
        break