# Pergunta 3

# TEST: Valor proposto pelo exercício
array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
num_input = 2
existent_combos = []
checked_combinations = []


# # TEST: Valor possível de sua escolha
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
# num_input = 9
# existent_combos = []
# checked_combinations = []


# # TEST: Valor acima do máximo possível
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
# num_input = 100
# existent_combos = []
# checked_combinations = []


# # TEST: Valor abaixo do mínimo possível
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
# num_input = -4
# existent_combos = []
# checked_combinations = []


# # TEST: Testar in_array_count com 8 (seria um 4 + 4, mas não existem dois 4 no array)
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
# num_input = 8
# existent_combos = []
# checked_combinations = []


# # TEST: Outros valores repetidos
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4]
# num_input = 4
# existent_combos = []
# checked_combinations = []


# # TEST: Modificar array de forma que uma combinação que não existia (ex.: 3, 5) passe a existir. Insira 3 no array
# array_exerc = [1, 15, 2, 7, 2, 5, 7, 1, 4, 3, 6]
# num_input = 8
# existent_combos = []
# checked_combinations = []


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
        return True

def check_combos(param_num):
    allowed = input_barrier(num_input)
    if allowed:
        print(f"Função executada")

        [i, j, in_array_count] = [0, param_num, None]

        while not i > param_num:
            
            current_tuple = (i, j)
            reverse_current_tuple = (j, i)
            in_array_count = array_exerc.count(i)

            if reverse_current_tuple in checked_combinations:
                # print(f"{current_tuple} already checked")
                i += 1; j -= 1
            
            else:
                if i in array_exerc and j in array_exerc:
                    if i != j:
                        existent_combos.append(current_tuple)
                        # checked_combinations.append(current_tuple)
                        i += 1; j -= 1

                    elif i == j and in_array_count >= 2:
                        existent_combos.append(current_tuple)
                        checked_combinations.append(current_tuple) # continue cria outra volta de while e não deixa o código chegar até o momento apropriado para a inserção no 'checked_combinations'
                        i += 1; j -= 1
                        continue
                    
                    else:
                        i += 1; j -= 1

                else:
                    i += 1; j -= 1
            
            checked_combinations.append(current_tuple)
        
        return True
    
    else:
        print(f"Função não executada")
        return False

combo_exists = check_combos(num_input)

if combo_exists:
    print(f"Combinações existem: {existent_combos}")
    print(f"Combinações testadas: {checked_combinations}")
    print(combo_exists)
else:
    print(f"Não existem combinações para o número inserido: {num_input}")
    print(f"Combinações testadas: {checked_combinations}")
    print(combo_exists)