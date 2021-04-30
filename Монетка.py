import random

print('Прога считает количество выпадений монетки.')
reshka = 0
orel = 0
number_podbros = 0
while number_podbros != 100:
    podbros = random.randint(1, 2)
    if podbros == 1:
        orel += 1
    else:
        reshka += 1
    number_podbros += 1
print('Орлов выпало', orel, 'решек выпало', reshka)
