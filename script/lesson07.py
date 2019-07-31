print('Arithmetic Operations')
print('Lets test the Arithmetic Operations')
n1 = int(input('Enter a value:  '))
n2 = int(input('Other value:  '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('The Sum is {}, The Product is {}, the Division is {}'.format(s, m, d), end='')
print(', The whole division is {} and the Potency is {}'.format(di, e))

print('Task 06')
n3 = int(input('Enter a value: '))
d = n3 * 2
t = n3 * 3
print('The double n3 is {} and the triple n3 is {}'.format(d, t))

print('task 07')
b1 = float(input('Math Note: '))
b2 = float(input('History Note: '))
b3 = float(input('Biology Note: '))

print('task 08')

Metro = float(input('Digite um valor para converter "Metro" em  Quilometro, Centimetro, \n Milimetro, Milha, Jarda, Polegada e Milha Nautica:'))
Quilometro   = Metro/1000
Centimetro   = Metro*100
Milimetro    = Metro*1000
Milha        = Metro/1609,344
Polegada     = Metro*39,37
MilhaNautica = Metro/1852

print(('Metro:{} \nQuilometro:{} \nCentimetro{} \nMilimetro{} ').format(Metro, Quilometro, Centimetro, Milimetro))
print(('Milha:{} \nPolegada:{} \nMilha Nautica{}').format(Milha, Polegada, MilhaNautica))

print('task 09')

x = int(input('Enter the value and see your multiplication table: '))
a = x*1
b = x*2
c = x*3
d = x*4
e = x*5
f = x*6
g = x*7
h = x*8
i =  x*9
j = x*10

print('Value: {} x1: {}  x2: {}  x3: {}  x4: {}  x5: {}  x6: {}  x7: {}  x8: {}  x9: {}  x10: {} .  '.format(x,a,b,c,d,e,f,g,h,i,j))

print('Task 10')
v1 = float(input('What is the current dollar value? '))
v2 = float(input('How many reais do you have in your wallet? '))
x = v2/v1
print('With this dollar price: {} and what you have in your wallet: {}, you can buy: {:.3f} Dollars '.format(v1, v2, x))

print('task 11')
n1 = float(input('How wide is the wall? '))
n2 = float(input('How tall is the wall? '))
x = n1*n2
y = x/2
print(('Wall Height:{}m² \nWall width:{}m² \nYour wall have {}m² Its take:{} Liters of paint to paint there').format(n2, n1, x, y))








