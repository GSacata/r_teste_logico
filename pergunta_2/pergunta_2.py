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
        print(f"{self.node_value}, L: {self.l_br.node_value if self.l_br.node_value else '-'}, R: {self.r_br.node_value if self.r_br.node_value else '-'}")
    
    def create_exerc_tree(self):
        self.create_node("Morango", "Pera")
        self.l_br.create_node("Goiaba", "Limão")
        self.r_br.create_node("", "Abacaxi")
        self.r_br.r_br.create_node("", "Laranja")
        self.r_br.r_br.r_br.create_node("Banana", "Cebola")
    
    def search_node(self, term):
        
        # while self.node_value is not term:
        #     print(f"Searching {self.node_value}...")

        #     if self.l_open:
        #         if self.l_br is not None and self.l_open:
        #             self.l_open = False
        #             self.l_br.search_node(term)
        #         else:
        #             print("No available node found, closing path...")
        #             self.l_open = False
        #             continue
            
        #     if self.r_open:
        #         if self.r_br is not None and self.r_open:
        #             self.r_open = False
        #             self.r_br.search_node(term)
        #         else:
        #             print("No available node found, closing path...")
        #             self.r_open = False
        #             continue
            
        #     else:
        #         pass

        #     print(f"Found {term}")
        #     break

        if self.node_value is term:
            print(f"Found {term}")
        elif self.l_open:
            print(f"Searching {self.node_value}...")
            if self.l_br is None:
                print("Nothing here")
            else:
                self.l_br.search_node(term)
        elif self.r_open:
            print(f"Searching {self.node_value}...")
            if self.r_br is None:
                print("Nothing here")
            else:
                self.r_br.search_node(term)
        else:
            print("Searching done")


# DEV-COMM
# tree = Node("Maçã")
# tree.create_node("Laranja", "")

tree = Node("Maçã")
tree.create_exerc_tree()
# tree.search_node("Goiaba")
tree.search_node("Limão")
# tree.search_node("Banana")