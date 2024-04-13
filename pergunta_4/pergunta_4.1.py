# Pergunta 4.1
# Tentativa de fazer o exercício 4 como class, para fins de estudo e prática mesmo.

def check_array_item(param_item):
    try:
        int(param_item)
        return True
    except:
        print(f"{param_item} not an integer number")
        return False

class Array_class:
    def __init__(self, array, min_value):
        self.array = array
        self.min_value = min_value
        pass

    @property
    def max_value(self):
        self.array.sort()
        return self.array[-1]
    
    @property
    def valid_values(self):
        existent_numbers = []

        for item in self.array:
            item_flag = check_array_item(item)
            if item_flag:
                if item not in existent_numbers:
                    existent_numbers.append(item)
                else:
                    pass
            else:
                continue
        
        return existent_numbers
    
    @property
    def missing_values(self):

        missing_num_array = []
        func_min_value = self.min_value

        while func_min_value <= self.max_value:
            if func_min_value not in self.valid_values:
                missing_num_array.append(func_min_value)
                func_min_value += 1
            else:
                func_min_value += 1

        return missing_num_array
    
    # @property
    # def filled_array(self):
    #     temp_array = self.array
    #     temp_missing_values = self.missing_values

    #     return temp_array.append(temp_missing_values)
    
a1 = Array_class([9, 2, 3, 1, 4], 0)
print(vars(a1))
print(a1.array)
print(a1.min_value)
print(a1.max_value)
print(a1.valid_values)
print(a1.missing_values)
print(a1.filled_array)