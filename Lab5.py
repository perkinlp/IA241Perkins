#5.1
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points')

#5.2
alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points')

else:
    print('You just earned 10 points')

#5.3
favorite_fruits = ['strawberry','blueberry','honeydew']

if 'strawberry' in favorite_fruits:
    print('You really like strawberries')
    
if 'blueberry' in favorite_fruits:
    print('You really like blueberries')
    
if 'apple' in favorite_fruits:
    print('You really like apples')
    
#5.4
age = 67

#if age < 10:
 #   print('You are a kid')
    
#elif age < 20:
#    print('You are a teenager')
    
#else:
#    print('You are an adult')
#    if age > 65:
#        print('You are an elder')
        
if age >= 20:
    print('You are an adult')
    if age > 65:
        print('You are an elder')
elif age > 10:
    print('You are a teenager')
else:
    print('You are a kid')