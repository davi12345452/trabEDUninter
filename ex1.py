class ElementoDaListaSimples:
    def __init__(self, dado, cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return
    
    def inserirPrioridade(self, nodo):
        # Se a lista estiver vazia
        if self.head is None:
            self.head = nodo
            return
        
        # Quando o primeiro elemento da lista não for amarelo
        # Quando o primeiro elemento da lista for amarelo, mas seu dado maior que o nodo dado de entrada
        # Trata se há somente um elemento na lista
        elif self.head.cor != "A" or self.head.dado > nodo.cor or self.head.proximo is None:
            no_atual = self.head
            self.head = nodo
            self.head.proximo = no_atual
            return
            '''
                Aqui o programa irá verificar percorrendo a lista, de maneira a tratar elementos amarelos de acordo
                com o valor do seu dado. Considerei que deveria ser de maneira crescente, ou seja, o menor no topo
                da lista. Ele fará as mesma verificações de antes com o topo, porém em loop, verificando por cada nó
                até achar a condição desejada.
            '''
        else:
            no_atual = self.head
            while(True):
                if no_atual.proximo.cor != "A":
                    no_proximo = no_atual.proximo
                    no_atual.proximo = nodo
                    nodo.proximo = no_proximo
                    return
                else:
                    if no_atual.proximo.dado > nodo.dado:
                        no_proximo = no_atual.proximo
                        no_atual.proximo = nodo
                        nodo.proximo = no_proximo
                        return
                    else:
                        no_atual = no_atual.proximo



    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
            return

    def mostrarLista(self):
        nodo_atual = self.head
        while nodo_atual is not None:
            print(f"Dado: {nodo_atual.dado}, Cor: {nodo_atual.cor}")
            nodo_atual = nodo_atual.proximo
        print()  # Adicionar uma linha em branco após imprimir a lista

# Função para cadastrar um paciente na lista de triagem
def cadastrarPaciente(lista, dado, cor):
    lista.inserir(dado, cor)

# Interface para o cadastro de pacientes
def interfaceCadastro(lista):
    while True:
        print("Cadastro de Paciente")
        dado = input("Informe o número do paciente: ")
        cor = input("Informe a cor do cartão (V para verde ou A para amarelo): ").upper()
        cadastrarPaciente(lista, dado, cor)

        continuar = input("Deseja cadastrar outro paciente? (S/N): ")
        if continuar.lower() != 's':
            break

# Interface para visualização da lista de pacientes na triagem
def interfaceVisualizacao(lista):
    if lista.head is None:
        print("Lista de Pacientes na Triagem está vazia.")
    else:
        print("Lista de Pacientes na Triagem:")
        lista.mostrarLista()

# Função principal
def main():
    lista_triagem = ListaEncadeadaSimples()

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Paciente")
        print("2. Visualizar Lista de Pacientes")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            interfaceCadastro(lista_triagem)
        elif opcao == '2':
            interfaceVisualizacao(lista_triagem)  # Passar a lista como argumento
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
