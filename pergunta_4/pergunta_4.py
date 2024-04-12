# Pergunta 4

#TEST: Array proposto.
array_exerc = [9, 2, 3, 1, 4]
missing_numbers = []

# #TEST: Array com número repetido (deve não checar números repetidos).
# array_exerc = [9, 2, 3, 1, 4, 2, 4, 9]
# missing_numbers = []



existent_numbers = []

def get_existent_num(param_array):
    for item in param_array:
        # existent_numbers.append(item) if item not in existent_numbers else ...
        if item not in existent_numbers:
            print(f"Appending {item}")
            existent_numbers.append(item)
        else:
            print(f"{item} already checked")
            pass

get_existent_num(array_exerc)

print("array_exerc", f"{array_exerc}")
print("missing_numbers", f"{missing_numbers}")
print("existent_numbers", f"{existent_numbers}")