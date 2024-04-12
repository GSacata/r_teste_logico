# Pergunta 4

#TEST: Array proposto.
array_exerc = [9, 2, 3, 1, 4]
missing_numbers = []
min_num = 0


# #TEST: Array com número repetido (deve não checar números repetidos).
# array_exerc = [9, 2, 3, 1, 4, 2, 4, 9]
# missing_numbers = []
# min_num = 0


# #TEST: Array com outro número maior que o original.
# array_exerc = [9, 2, 3, 1, 4, 13, 24, 1, 9]
# missing_numbers = []
# min_num = 0


print("array_exerc, start", f"{array_exerc}")

existent_numbers = []

def get_existent_num(param_array):
    for item in param_array:
        # existent_numbers.append(item) if item not in existent_numbers else ...
        if item not in existent_numbers:
            # print(f"Appending {item}")
            existent_numbers.append(item)
        else:
            # print(f"{item} already checked")
            pass

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