word = 'Hello World, Thanks'
print(word.lower().find('World'))
print(word.split())


print('task022')
name = str(input('Type your Name:  ')).strip()
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {} '.format(name.lower()))
print('Your name has all {} letters '.format(len(name)  - name.count(' ')))
print('Your first name has {} letters '.format(name.find(' ')))

print('task023')

n = int(input('Enter a number: '))
n2 = str(int(10000 + n))
print('The number {} have {} thousands.'.format(n, n2[1]))
print('The number {} have {} hundreds. '.format(n, n2[2]))
print('The number {} have {} tens. '.format(n, n2[3]))
print('The number {} have {} units.'.format(n, n2[4]))

print('task024')
city = str(input('What city were you born in?  ')).strip()
print(city[:5].upper() == 'Santo')

print('task025')

name = str(input('Whats your name? ')).strip()
print('Your name has Barros? {}'.format('Barros' in name.lower()))

print('task026')
wd = str(input('Type a sentence: ')).strip()
print('The letter A appears {} times'.format(wd.upper().count('A')))
print('The first position is {}'.format(wd.upper().find('A')+1))
print('The last position is {}'.format(wd.upper().rfind('A')+1))

