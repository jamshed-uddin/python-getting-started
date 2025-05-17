print("hello")


#  primitive data types

count = 1

name = 'John Doe'

is_active = True


# string

str = 'hello'

# get the length
print(len(str))

# get certain character

print(str[1])
print(str[-1])
print(str[0:3])
print(str[0:])
print(str[:3])
print(str[:])

# escape sequence
print('hello \nworld')

# formated string
first = 'John'
last = 'Doe'

print(f"{first} {last}")

# string methods ------

newStr = 'string methods  '

print(newStr.upper())

print(newStr.find('r'))


print(newStr.replace('t', 'r'))

print('str' in newStr)
print('hello' not in newStr)
