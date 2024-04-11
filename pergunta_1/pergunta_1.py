# Pergunta 1

# TEST 1: Input número 1
array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
search_num = 1
number_stash = []

# # TEST 2: outro input
# array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
# search_num = 2
# number_stash = []

# # TEST 3: Input valor inválido (número que não consta, outro caractere...)
# array_exerc = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
# search_num = 'a'
# number_stash = []


def search_number(num):
    for pos, v in enumerate(array_exerc):
        if v == num:
            x = array_exerc.pop(pos)
            number_stash.append(x)
            break
        else:
            continue

def replenish_array():
    x = number_stash.pop(0)
    array_exerc.insert(0, x)

    
while search_num in array_exerc:
    search_number(search_num)

while search_num in number_stash:
    replenish_array()


print(array_exerc)
print(number_stash)
