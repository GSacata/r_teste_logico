# Pergunta 4

# # TEST: Array proposto.
# array_exerc = [9, 2, 3, 1, 4]
# missing_numbers = []
# min_num = 0


# # TEST: Array com número repetido (deve não checar números repetidos).
# array_exerc = [9, 2, 3, 1, 4, 2, 4, 9]
# missing_numbers = []
# min_num = 0


# # TEST: Array com outro número maior que o original.
# array_exerc = [9, 2, 3, 1, 4, 13, 24, 1, 9]
# missing_numbers = []
# min_num = 0


# # TEST: Array com número negativo.
# array_exerc = [9, 2, 3, 1, 4, 25, 18, 3]
# missing_numbers = []
# min_num = -4


# # TEST: Não-números (ex.: letra) no array.
# array_exerc = [9, 2, 3, 'c', 1, 'f', 4]
# missing_numbers = []
# min_num = 0


# TEST: Não-números (ex.: array com números) no array.
array_exerc = [9, [1, 5], 2, 3, 1, 4]
missing_numbers = []
min_num = 0


print("array_exerc, start", f"{array_exerc}")

existent_numbers = []

def check_array_item(param_item):
    try:
        int(param_item)
        return True
    except:
        print(f"{param_item} not an integer number")
        return False

def get_existent_num(param_array):
    for item in param_array:
        # existent_numbers.append(item) if item not in existent_numbers else ...
        item_flag = check_array_item(item)
        if item_flag:
            if item not in existent_numbers:
                # print(f"Appending {item}")
                existent_numbers.append(item)
            else:
                # print(f"{item} already checked")
                pass
        else:
            continue

get_existent_num(array_exerc)

existent_numbers.sort()

max_num = existent_numbers[-1]

def find_missing_num():
    global min_num
    
    while min_num <= max_num:
        if min_num not in existent_numbers:
            # print(f"Appending {min_num}")
            missing_numbers.append(min_num)
            min_num += 1
        else:
            # print(f"{min_num} already exists")
            min_num += 1

find_missing_num()

def append_miss_to_main():
    for item in missing_numbers:
        array_exerc.append(item)

append_miss_to_main()


print("array_exerc, end", f"{array_exerc}")
print("missing_numbers", f"{missing_numbers}")
print("existent_numbers", f"{existent_numbers}")