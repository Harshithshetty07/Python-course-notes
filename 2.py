import math

print('hello world')

text = 'names'
student = '10000'
print(student[2])
print(text[1])

first = 'Rakshith'
last = 'shetty'
full = f"{first} {last}"
print(full)

x = 10 ** 3
print(x)

print(math.floor(3.002125))

#y = input('x: ')
#z = int(y) + 1
#print(z)


age = 62
if age == 18:
    print('You are an adult')
elif age >= 60:
      print('You are old')
else: 
        print('You are a minor')


array = [1, 3, 4]
total = 0

#for i in range(len(array)):
      #total += array[i]
#print(total)

if not array:
     print('Array is empty')
else: 
     
    for number in range(len(array)):
        total += array[number]
        print(total)


def greet(a, b): 
     print(a + b)

greet(30, 40)
greet(20, 80)
