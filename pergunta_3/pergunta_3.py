# Pergunta 3

# TEST 1
array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
num_input = 2
possible_combos = []

def input_barrier(param_num):
    array_exerc.sort()
    
    min_sum = array_exerc[0] + array_exerc[1]
    max_sum = array_exerc[-1] + array_exerc[-2]

    if param_num < min_sum:
        print(f"Número inserido menor que combinação mínima possível, {min_sum}")
        return False
    elif param_num > max_sum:
        print(f"Número inserido maior que combinação máxima possível, {max_sum}")
        return False
    else:
        print(f"Input válido, {num_input}, executando função")

def check_combos(param_num):
    allowed = input_barrier(num_input)
    if allowed:
        print(f"Função executada")
    else:
        print(f"Função não executada")
    pass

combo_exists = check_combos(num_input)
print(combo_exists)

# if combo_exists:
#     print(combo_exists)
#     print(f"Combinações existem\n{possible_combos}")
# else:
#     print(combo_exists)
#     print(f"Não existem combinações para o número inserido")