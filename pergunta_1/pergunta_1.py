# Pergunta 1

array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
search_num = 1

for pos, value in enumerate(array_exerc):
    print(f'{pos}, {value}')

print(f'\n\n')

for pos, value in enumerate(array_exerc):
    if value == search_num:
        print(f'{pos}, {value}')
    else:
        pass

# def align_values(num):
#     pass




# array_exerc.sort()
# for pos, value in enumerate(array_exerc):
#     print(f'{pos}, {value}')