import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

import emoji
print(emoji.emojize('Hello World :earth_americas:', use_aliases=True))

print('task016')
num1 = float(input('Enter a value: '))
print('the value you entered was {} and your entire portion was {}'.format(num1,math.trunc(num1)))

print('task017')
a = float(input('length of the opposite side: '))
b = float(input('lenght of the adjunct bundle: '))
hy = math.hypot(a, b)
print('the hypotenuse will measure {:.2f} '.format(hy))

print('task018')
num3 = float(input('Enter an angle in degrees: '))
num3 = num*(math.pi)/180
print('The sine of {} is {:.2f}, The Cosine of {} is {:.2f} and the tangent of {} is {:.2f}'.format(num3, math.sin(num3), num3, math.cos(num3), num3, math.tan(num3)))

print('task019')

import random
s1 = str(input('First Student: '))
s2 = str(input('Second Student: '))
s3 = str(input('Third Student: '))
s4 = str(input('Fourth Student: '))
list = [s1, s2, s3, s4]
chosen = random.choice(list)
print('The chosen Student was {}'.format(chosen))

print('task020')
import pygame
pygame.mixer.init()
pygame.mixer.music.load('strangerthings.mp3')
pygame.mixer.music.play()
pygame.event.wait()











