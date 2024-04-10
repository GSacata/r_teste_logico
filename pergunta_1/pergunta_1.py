# Pergunta 1

array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
search_num = 1
number_stash = []

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
def search_number(num):
    for pos, v in enumerate(array_exerc):
        if v == num:
            x = array_exerc.pop(pos)
            number_stash.append(x)
            break
        else:
            continue
    
while search_num in array_exerc:
    search_number(search_num)


print(array_exerc)
print(number_stash)


# array_exerc.sort()
# for pos, value in enumerate(array_exerc):
#     print(f'{pos}, {value}')