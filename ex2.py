# Definindo a classe para uma fila de caminhoneiros
class FilaCaminhoneiros:
    def __init__(self):
        self.fila = []  # Inicializa a lista vazia para representar a fila de caminhoneiros

    def entrar_fila(self, caminhoneiro):
        if len(self.fila) < 10:
            self.fila.append(caminhoneiro)  # Adiciona um caminhoneiro ao final da fila
            print(f"{caminhoneiro} entrou na fila.")

    def sair_fila(self):
        if self.fila:
            caminhoneiro_atendido = self.fila.pop(0)  # Remove o primeiro caminhoneiro da fila
            print(f"{caminhoneiro_atendido} foi atendido e saiu da fila.")
        else:
            print("Fila vazia. Nenhum caminhoneiro para atender.")

    def listar_fila(self):
        if self.fila:
            print("Caminhoneiros na fila:")
            for i, caminhoneiro in enumerate(self.fila, start=1):
                print(f"{i}. {caminhoneiro}")  # Lista os caminhoneiros na fila, numerando-os
        else:
            print("Fila vazia.")

# Função principal
def main():
    fila_caminhoneiros = FilaCaminhoneiros()  # Cria uma instância da classe FilaCaminhoneiros

    while True:
        print("\n1. Entrar na fila\n2. Atender próximo caminhoneiro\n3. Listar fila\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            caminhoneiro = input("Digite o nome do caminhoneiro: ")
            fila_caminhoneiros.entrar_fila(caminhoneiro)  # Chama o método para entrar na fila
        elif opcao == '2':
            fila_caminhoneiros.sair_fila()  # Chama o método para atender o próximo caminhoneiro
        elif opcao == '3':
            fila_caminhoneiros.listar_fila()  # Chama o método para listar os caminhoneiros na fila
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Escolha novamente.")

    print("Encerrando o programa.")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
