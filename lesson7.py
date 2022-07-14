"""
# Problem 0
dates_of_birth = {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
dates_of_birth.discard(7)
print(dates_of_birth)
  
  
# Problem 1
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.intersection(farm_2))


# Problem 2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.difference(farm_2))


# Problem 3
my_set = {1, 2, 3, 4, 5}
my_set.add(10)
print(my_set)  # >= {1, 2, 3, 4, 5, 10}
my_set.pop()
print(my_set)  # >= {2, 3, 4, 5, 10}



# Problem 000
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['besh_barmak'] = 130
print(menu)


# Problem 10
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks'] = ['Coca-cola', 'Sprite', 'Fanta']
print(menu)


# Problem 020
methods_set = {'add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'pop', 'remove', 'union', 'update'}

methods_dict = {'clear', 'copy', 'pop', 'items', 'get', 'values', 'update', 'keys'}

print(methods_set.intersection(methods_dict))  # >= {'copy', 'update', 'clear', 'pop'}


# Problem 31
empty_dict = {}
for i in range(3):
    name = input('Text your name: ')
    password = input('Text your password: ')
    empty_dict[name] = password
print(empty_dict.items())


# Problem 27
name_profi = {
    'Nursultan': 'Biznes',
    'Bekbolsun': 'Programmer',
    'Bekzat': 'Arhitector',
    'Daniel': 'Menedgment',
    'Islam': 'Police',
}
for name, profi in name_profi.items():
    print(f'Здравствуйте {name}\nПрекрасная профессия {profi}')


# Problem 22
numbers = set()
for i in range(10):
    number = int(input('Text one number: '))
    numbers.add(number)
numbers = tuple(numbers)
print(numbers)


# Problem 11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
  'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
south_american_countries = list(set(south_american_countries))
print(south_american_countries)


# Problem 101
suitcase = []
suitcase.extend(['Mobile', 'Computer', 'Clothes', 'Eats', 'drinks'])
suitcase.pop()
print(suitcase)


# Problem 001

itcbootcamp = {'python', 'java', 'hpp', 'flutter'}
itrun = {'c++', 'html_css', 'python', 'java'}

general_lang = set(itcbootcamp.intersection(itrun))
print(general_lang)


# Problem 100
farm1 = {'Panda', 'Cheetah', 'Horse', 'Lion', 'Camel', 'Donkey'}
farm2 = {'Gorilla', 'Tiger', 'Dog', 'Cat', 'Cheetah', 'Camel', 'Donkey'}
print(farm1.difference(farm2))

"""






