# Pergunta 2

"""
valor node: valor
l_br: None (vai receber outro node)
r_br: None (vai receber outro node)
l_flag: true ou false (indica se aquele caminho é válido ou não)
r_flag: true ou false (indica se aquele caminho é válido ou não) 
"""

class Node():
    def __init__(self, node_value):
        self.node_value = node_value
        self.l_br = None
        self.r_br = None
        self.l_open = True
        self.r_open = True

    def create_node(self, left_value, right_value):
        self.l_br = Node(left_value)
        self.r_br = Node(right_value)
        print(f"{self.node_value}, L: {self.l_br.node_value}, R: {self.r_br.node_value}")
    
    def create_exerc_tree(self):
        self.create_node("Morango", "Pera")
        self.l_br.create_node("Goiaba", "Limão")
        self.r_br.create_node("", "Abacaxi")
        self.r_br.r_br.create_node("", "Laranja")
        self.r_br.r_br.r_br.create_node("Banana", "Cebola")


# DEV-COMM
# tree = Node("Maçã")
# tree.create_node("Laranja", "")

tree = Node("Maçã")
tree.create_exerc_tree()