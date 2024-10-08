class Funcionario:
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento

    def bonificar(self):
        self.salario *= 1.10

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, senha, numFuncionarios):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numFuncionarios = numFuncionarios

    def autenticarSenha(self, senha):
        return self.senha == senha

    def bonificar(self):
        self.salario *= 1.15

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, qntVendas, comissao):
        super().__init__(nome, cpf, salario, departamento)
        self.qntVendas = qntVendas
        self.comissao = comissao

    def atualizaQuantidadeVendas(self, quantidade):
        self.qntVendas += quantidade

    def calculaSalario(self):
        return self.salario + (self.qntVendas * self.comissao)
funcionarios = [Funcionario("Pedro", "12312123", 1500, "Contabilidade"),Funcionario("Matheus", "2143214235", 1500, "Contabilidade")]
gerentes = [Gerente("David", "1283457", 4000, "Administração", "123David", 1),Gerente("Marcelo","94183043", 5000, "Administração", "123Marcelo", 1)]
vendedores = [Vendedor("João", "543245", 2000, "Design", 10, 100),Vendedor("Carlos", "87915723", 2000, "Design", 50, 100)]

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Menu', width=800, height=600)

dpg.setup_dearpygui()
dpg.show_viewport()

with dpg.window(label='Menu'):
    dpg.add_button(label='Cadastrar')
    dpg.add_button(label='Bonificar')
    dpg.add_button(label='Autenticar senha')
    dpg.add_button(label='Atualizar vendas')
    dpg.add_button(label='Listar')
    dpg.add_button(label='Sair', callback=lambda sender, data: dpg.stop_dearpygui())

dpg.start_dearpygui()

while True:
    print("Menu:")
    print("1 - Cadastrar Funcionário")
    print("2 - Cadastrar Gerente")
    print("3 - Cadastrar Vendedor")
    print("4 - Bonificar Funcionário")
    print("5 - Bonificar Gerente")
    print("6 - Autenticar senha Gerente")
    print("7 - Atualizar quantidade de vendas do vendedor")
    print("8 - Calcular Salário do Vendedor")
    print("9 - Listar Funcionários")
    print("10 - Listar Gerentes")
    print("11 - Listar Vendedores")
    print("12 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        salario = float(input("Salário: "))
        departamento = input("Departamento: ")
        funcionario = Funcionario(nome, cpf, salario, departamento)
        funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        salario = float(input("Salário: "))
        departamento = input("Departamento: ")
        senha = input("Senha: ")
        numFuncionarios = int(input("Número de funcionários gerenciados: "))
        gerente = Gerente(nome, cpf, salario, departamento, senha, numFuncionarios)
        gerentes.append(gerente)
        print("Gerente cadastrado com sucesso!")

    elif opcao == 3:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        salario = float(input("Salário: "))
        departamento = input("Departamento: ")
        qntVendas = int(input("Quantidade de vendas: "))
        comissao = float(input("Comissão: "))
        vendedor = Vendedor(nome, cpf, salario, departamento, qntVendas, comissao)
        vendedores.append(vendedor)
        print("Vendedor cadastrado com sucesso!")

    elif opcao == 4:
        if not funcionarios:
            print("Não há funcionários cadastrados.")
        else:
            print("Funcionários:")
            for i, funcionario in enumerate(funcionarios):
                print(f"{i+1} - {funcionario.nome}")
            escolha = int(input("Escolha um funcionário: "))
            funcionarios[escolha-1].bonificar()
            print("Bonificação aplicada com sucesso!")

    elif opcao == 5:
        if not gerentes:
            print("Não há gerentes cadastrados.")
        else:
            print("Gerentes:")
            for i, gerente in enumerate(gerentes):
                print(f"{i+1} - {gerente.nome}")
            escolha = int(input("Escolha um gerente: "))
            gerentes[escolha-1].bonificar()
            print("Bonificação aplicada com sucesso!")

    elif opcao == 6:
        if not gerentes:
            print("Não há gerentes cadastrados.")
        else:
            print("Gerentes:")
            for i, gerente in enumerate(gerentes):
                print(f"{i+1} - {gerente.nome}")
            escolha = int(input("Escolha um gerente: "))
            senha = input("Senha: ")
            if gerentes[escolha-1].autenticarSenha(senha):
                print("Senha autenticada com sucesso!")
            else:
                print("Senha inválida.")

    elif opcao == 7:
        if not vendedores:
            print("Não há vendedores cadastrados.")
        else:
            print("Vendedores:")
            for i, vendedor in enumerate(vendedores):
                print(f"{i+1} - {vendedor.nome}")
            escolha = int(input("Escolha um vendedor: "))
            quantidade = int(input("Quantidade de vendas: "))
            vendedores[escolha-1].atualizaQuantidadeVendas(quantidade)
            print("Quantidade de vendas atualizada com sucesso!")

    elif opcao == 8:
        if not vendedores:
            print("Não há vendedores cadastrados.")
        else:
            print("Vendedores:")
            for i, vendedor in enumerate(vendedores):
                print(f"{i+1} - {vendedor.nome}")
            escolha = int(input("Escolha um vendedor: "))
            salario = vendedores[escolha-1].calculaSalario()
            print(f"Salário do vendedor: {salario:.2f}")

    elif opcao == 9:
        if not funcionarios:
            print("Não há funcionários cadastrados.")
        else:
            for funcionario in funcionarios:
                    print(f"Nome: {funcionario.nome}, CPF: {funcionario.cpf}, Salário: {funcionario.salario:.2f}, Departamento: {funcionario.departamento}")
 

    elif opcao == 10:
        if not gerentes:
            print("Não há gerentes cadastrados.")
        else:
            for gerente in gerentes:
                    print(f"Nome: {gerente.nome}, CPF: {gerente.cpf}, Salário: {gerente.salario:.2f}, Departamento: {gerente.departamento}, Senha: {gerente.senha}, Funcionários: {gerente.numFuncionarios}")

    elif opcao == 11:
        if not vendedores:
            print("Não há vendedores cadastrados.")
        else:
            for vendedor in vendedores:
                    print(f"Nome: {vendedor.nome}, CPF: {vendedor.cpf}, Salário: {vendedor.salario:.2f}, Salário com comissão: {vendedor.calculaSalario():.2f}, Departamento: {vendedor.departamento}, Comissao: {vendedor.comissao}, Quantidade de Vendas: {vendedor.qntVendas}")

    elif opcao == 12:
        print("Adeus!")
        break
    
    else:
        print("Opção inválida. Por favor, tente novamente.")