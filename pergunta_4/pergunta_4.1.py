# Pergunta 4.1
# Tentativa de fazer o exercício 4 como class, para fins de estudo e prática mesmo.

class Array:
    def __init__(self, array, min_value):
        self.array = array
        self.min_value = min_value
        pass

    def find_min_max(self):
        ordered_array = self.array.sort()