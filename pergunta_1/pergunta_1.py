# Pergunta 1

# array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
array_exerc = [2, 1, 5, 1, 1, 1, 7, 9, 13, 127, 21] #DEV-ER
search_num = 1

"""
for pos, value in enumerate(array_exerc):
    print(f'{pos}, {value}')

print(f'\n\n')

for pos, value in enumerate(array_exerc):
    if value == search_num:
        print(f'{pos}, {value}')
    else:
        pass
"""

def replace_values(num):
    x = array_exerc.pop(num)
    array_exerc.insert(0, x)

def arrange_number(num):
    for v in array_exerc:
        if v == num:
            replace_values(v)
        else:
            continue



arrange_number(search_num)

print(array_exerc)


# array_exerc.sort()
# for pos, value in enumerate(array_exerc):
#     print(f'{pos}, {value}')