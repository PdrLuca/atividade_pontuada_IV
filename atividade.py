import csv

class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

funcionarios = []

def exibir_menu():
    print("\n=== Sistema de Cadastro de Funcionários ===")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionario = Funcionario(nome, cpf, cargo, salario)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\n=== Lista de Funcionários ===")
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. {funcionario}")

def atualizar_funcionario():
    listar_funcionarios()
    if funcionarios:
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

def excluir_funcionario():
    listar_funcionarios()
    if funcionarios:
        indice = int(input("Digite o número do funcionário que deseja excluir: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("Funcionário excluído com sucesso!")
        else:
            print("Funcionário não encontrado.")

def salvar_dados():
    with open("funcionarios.csv", "w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Nome", "CPF", "Cargo", "Salário"])
        for funcionario in funcionarios:
            escritor.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
    print("Dados salvos com sucesso no arquivo funcionarios.csv!")

def carregar_dados():
    try:
        with open("funcionarios.csv", "r") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor)  
            for linha in leitor:
                nome, cpf, cargo, salario = linha
                funcionario = Funcionario(nome, cpf, cargo, float(salario))
                funcionarios.append(funcionario)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo funcionarios.csv não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

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
            carregar_dados()
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    gerenciar_menu()