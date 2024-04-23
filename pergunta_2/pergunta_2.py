# Pergunta 2

"""
valor node: valor
l_br: None (vai receber outro node)
r_br: None (vai receber outro node)
l_flag: true ou false (indica se aquele caminho é válido ou não)
r_flag: true ou false (indica se aquele caminho é válido ou não) 
"""

found_term = 0
term_path = []

class Node():
    def __init__(self, node_value):
        self.node_value = node_value
        self.l_br = None
        self.r_br = None
        self.l_content = True
        self.r_content = True

    def create_node(self, left_value, right_value):
        self.l_br = Node(left_value)
        self.r_br = Node(right_value)
        print(f"C: {self.node_value}, L: {self.l_br.node_value if self.l_br.node_value else '-'}, R: {self.r_br.node_value if self.r_br.node_value else '-'}")
    
    def create_exerc_tree(self):
        self.create_node("Morango", "Pera")
        self.l_br.create_node("Goiaba", "Limão")
        self.r_br.create_node("", "Abacaxi")
        self.r_br.r_br.create_node("", "Laranja")
        self.r_br.r_br.r_br.create_node("Banana", "Cebola")
    
    def create_custom_tree(self):
        self.create_node("Uva", "Limão")
        self.l_br.create_node("Abóbora", "")
        self.r_br.create_node("Cenoura", "Costela")
    
    def search_node(self, term):
        
        global found_term

        while found_term == 0:

            print(f"Searching {self.node_value}...")
            self.fill_path(self.node_value)

            if self.node_value is term:
                print(f"Found {term}")
                self.write_path()
                found_term += 1
                break
            
            elif self.l_content:
                if self.l_br is None:
                    self.l_content = False
                    print(f"Nothing on left branch...")
                else:
                    print(f"Searching left branch, {self.l_br.node_value}...")
                    self.l_content = False
                    self.l_br.search_node(term)
            
            elif self.r_content:
                if self.r_br is None:
                    self.r_content = False
                    print(f"Nothing on right branch...")
                else:
                    print(f"Searching right branch, {self.r_br.node_value}...")
                    self.r_content = False
                    self.r_br.search_node(term)
            
            else:
                print(f"Searching {self.node_value} node done")
                break
        
        if found_term == 0:
            print(f"No path for {term}")

    def fill_path(self, term):
        global term_path

        if term in term_path:
            term_path.pop(-1)
        else:
            term_path.append(term)

    def write_path(self):
        global term_path

        this_path = " -> ".join(term_path)
        print(this_path)

# DEV-COMM
# tree = Node("Maçã")
# tree.create_node("Laranja", "")


# TEST: 
# Proposta inicial, buscando "Goiaba".
# Escrita de caminho, caminho direto ("Goiaba", tudo à esquerda)
tree = Node("Maçã")
tree.create_exerc_tree()
tree.search_node("Goiaba")

# # TEST: 
# # Buscar palavra na folha à direita (segunda busca de um node).
# # Escrita de caminho, caminho corrigido ("Limão", precisa apagar Goiaba do caminho)
# tree = Node("Maçã")
# tree.create_exerc_tree()
# tree.search_node("Limão")

# # TEST: Conferir no olho o caminho escrito.
# tree = Node("Maçã")
# tree.create_exerc_tree()
# tree.search_node("Abacaxi")

# # TEST: Buscar palavra na folha mais distante.
# tree = Node("Maçã")
# tree.create_exerc_tree()
# tree.search_node("Cebola")

# # TEST: Buscar palavra na primeira folha.
# tree = Node("Maçã")
# tree.create_exerc_tree()
# tree.search_node("Maçã")

# # TEST: Buscar palavra inexistente.
# tree = Node("Maçã")
# tree.create_exerc_tree()
# tree.search_node("Alho")

# # TEST: Alterar árvore inicial, e ver se o programa todo responde a essa alteração 1.
# tree = Node("Beterraba")
# tree.create_custom_tree()
# tree.search_node("Costela")

# # TEST: Alterar árvore inicial, e ver se o programa todo responde a essa alteração 2.
# tree = Node("Beterraba")
# tree.create_custom_tree()
# tree.search_node("Cenoura")

# # TEST: Alterar árvore inicial, e ver se o programa todo responde a essa alteração 3.
# tree = Node("Beterraba")
# tree.create_custom_tree()
# tree.search_node("Abóbora")