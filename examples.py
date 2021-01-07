# comment

# Data types
name = 'Alan'
name2 = 'avery'
age = 36
is_old = False
sei_1019 = True

print(name)

# String methods ——————————————————————————————
sentence = 'Today is Nicole\'s birthday.'

# split()
nicole_birthday = sentence.split(' ')
print(nicole_birthday)

# join()
new_sentence = " ".join(nicole_birthday)
print(new_sentence)

# index()
print(new_sentence.index('N'))

# lower
print(name.lower())

# upper()
print(name2.upper())

# replace()
print(sentence.replace('Today is', 'Yesterday was'))

# in
print('birthday' in sentence)
print('anniversary' in sentence)

# len()
print(len(sentence))

# Ranges ——————————————————————————————
print(sentence[-1])
print(sentence[0:5])
print(sentence[:10])
print(sentence[6:])
print(sentence[::-1])
print(sentence[::2])

# Logical operators ——————————————————————————————
number = 10
good_movie = True
print(number == 10)
print(number != 10)
print(not good_movie)
print(number == 10 and not good_movie)
print(number == 10 or not good_movie)

# Lists ——————————————————————————————
arr = [1, 2, 3]
print(arr)
print(len(arr))
ten_apples = ['apple'] * 5
print(ten_apples)
print(len(ten_apples))
fruit = ['apple', 'orange', 'banana', 'peach']
print(fruit[-1])
zero_through_nineteen = list(range(20))
print(zero_through_nineteen)

for i in range(len(fruit)):
    fruit_type = fruit[i]
    print(fruit_type)

random_num = [45, 99, 12, 1, 69, 32]
random_num.sort()
random_num.append(18)
random_num = random_num[::-1]
pop_result = random_num.pop()
print(random_num)
print(pop_result)
random_num.insert(0, 'Numbers:')
print(random_num)

if 99 in random_num:
    print('It\'s in there alright.')

# Dictionaries ——————————————————————————————
furniture = {
    "type": 'dining table',
    "producer": 'Article',
    "price": 350,
    "materials": {
        "material1": 'wood',
        "material2": 'steel'
    }
}

print(furniture["type"])
print(furniture["price"])
print(furniture["materials"]["material1"])

print(furniture.keys())

# Type conversions ——————————————————————————————
print(int('100'))
print(str(200))
print(float(200))
print(bool(200))
print(bool(0))
print(bool('Hello.'))
print(bool(''))

# String interpolation ——————————————————————————————
instructor_name = 'Rome'
print(instructor_name + ' is my instructor.')
print(f'{instructor_name} is my instructor.')

phrase = 'My name is {} and I love {}!'
print(phrase.format('Alan', 'rainbows'))
print(phrase)

# Functions ——————————————————————————————


def print_name(someone):
    return someone


def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:
        return 'You can have a beer.'
    else:
        return 'Go home, old man.'


print(old_enough(30))


def add(lover1, lover2):
    return '{} has the hots for {}.'.format(lover1, lover2)


print(add('Romeo', 'Juliet'))


def subtract(num1, num2):
    return num1 - num2


print(subtract(100, 50))
