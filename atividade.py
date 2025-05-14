import csv
from dataclasses import dataclass

# Classe para representar um funcionário
@dataclass
class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

# Lista para armazenar os funcionários em memória
funcionarios = []

# Função para exibir o menu principal
def exibir_menu():
    print("\n=== Sistema de Cadastro de Funcionários ===")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função para cadastrar um novo funcionário
def cadastrar_funcionario():
    try:
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        funcionario = Funcionario(nome, cpf, cargo, salario)
        funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")
    except ValueError:
        print("Salário inválido. Cadastro cancelado.")

# Função para listar todos os funcionários
def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\n=== Lista de Funcionários ===")
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. {funcionario}")

# Função para atualizar um funcionário existente
def atualizar_funcionario():
    listar_funcionarios()
    if funcionarios:
        try:
            indice = int(input("Digite o número do funcionário que deseja atualizar: ")) - 1
            if 0 <= indice < len(funcionarios):
                nome = input("Digite o novo nome do funcionário: ")
                cpf = input("Digite o novo CPF do funcionário: ")
                cargo = input("Digite o novo cargo do funcionário: ")
                salario = float(input("Digite o novo salário do funcionário: "))
                funcionarios[indice].nome = nome
                funcionarios[indice].cpf = cpf
                funcionarios[indice].cargo = cargo
                funcionarios[indice].salario = salario
                print("Funcionário atualizado com sucesso!")
            else:
                print("Funcionário não encontrado.")
        except ValueError:
            print("Entrada inválida. Atualização cancelada.")

# Função para excluir um funcionário
def excluir_funcionario():
    listar_funcionarios()
    if funcionarios:
        try:
            indice = int(input("Digite o número do funcionário que deseja excluir: ")) - 1
            if 0 <= indice < len(funcionarios):
                funcionarios.pop(indice)
                print("Funcionário excluído com sucesso!")
            else:
                print("Funcionário não encontrado.")
        except ValueError:
            print("Entrada inválida. Exclusão cancelada.")

# Função para salvar os dados em um arquivo CSV
def salvar_dados():
    try:
        with open("funcionarios.csv", "w", newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "CPF", "Cargo", "Salário"])
            for funcionario in funcionarios:
                escritor.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
        print("Dados salvos com sucesso no arquivo funcionarios.csv!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


# Função principal para gerenciar o menu
def gerenciar_menu():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            salvar_dados()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do sistema
if __name__ == "__main__":
    gerenciar_menu()