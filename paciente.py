class Paciente:
    def __init__(self, cpf, nome, data_de_nascimento, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, telefone, endereco, email, historico_hospitalar):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.plano_de_saude = plano_de_saude
        self.rg = rg
        self.tipo_sanguineo = tipo_sanguineo
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.historico_hospitalar = historico_hospitalar
    
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Data de nascimento: {self.data_de_nascimento}\n"
            f"Peso: {self.peso} kg\n"
            f"Altura: {self.altura} m\n"
            f"Sexo: {self.sexo}\n"
            f"Plano de Saúde: {self.plano_de_saude}\n"
            f"RG: {self.rg}\n"
            f"Tipo Sanguíneo: {self.tipo_sanguineo}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}\n"
            f"E-mail: {self.email}\n"
            f"Histórico Hospitalar: {self.historico_hospitalar}"
        )

pacientes = []

def buscar_paciente(cpf):
    for paciente in pacientes:
        if paciente.cpf == cpf:
            return paciente
    return None

def registrar_paciente():
    while True:
        try:
            cpf = int(input("CPF: "))
            nome = input("Nome: ")
            data_de_nascimento = input("Data de Nascimento: ")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))
            sexo = input("Sexo: ")
            plano_de_saude = input("Plano de Saúde: ")
            rg = input("RG: ")
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            email = input("E-mail: ")
            historico_hospitalar = input("Histórico Hospitalar: ")
            
            novo_paciente = Paciente(cpf, nome, data_de_nascimento, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, telefone, endereco, email, historico_hospitalar)
            pacientes.append(novo_paciente)
            print("Paciente registrado com sucesso!")
            print("")
            print("Deseja registrar outro paciente?")
            print("[1] - Sim | [2] - Não")
            print("")
            try:
                opcao_registrar_novamente = int(input("[Opção]: "))
                print("")
                if opcao_registrar_novamente == 1:
                    continue
                if opcao_registrar_novamente == 2:
                    break
                else:
                    print("Opção inválida! Retornando ao menu.")
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
                break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar os dados corretamente.")

def atualizar_paciente(cpf):
    while True:
        try:
            paciente = buscar_paciente(cpf)
            if paciente:
                print("Informe os novos dados (pressione Enter para manter o valor atual):")
                paciente.nome = input(f"Nome ({paciente.nome}): ") or paciente.nome
                paciente.peso = float(input(f"Peso ({paciente.peso} kg): ") or paciente.peso)
                paciente.altura = float(input(f"Altura ({paciente.altura} m): ") or paciente.altura)
                paciente.telefone = input(f"Telefone ({paciente.telefone}): ") or paciente.telefone
                paciente.endereco = input(f"Endereço ({paciente.endereco}): ") or paciente.endereco
                paciente.email = input(f"E-mail ({paciente.email}): ") or paciente.email
                paciente.historico_hospitalar = input(f"Histórico Hospitalar ({paciente.historico_hospitalar}): ") or paciente.historico_hospitalar
                print("Paciente atualizado com sucesso!")
            else:
                print("Paciente não encontrado!")
            print("")
            print("Deseja atualizar outro paciente?")
            print("[1] - Sim | [2] - Não")
            try:
                opcao_atualizar_novamente = int(input("[Opção]: "))
                if opcao_atualizar_novamente == 1:
                    continue
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar os dados corretamente.")   

def remover_paciente(cpf):
    global pacientes
    while True:
        try:
            pacientes = [p for p in pacientes if p.cpf != cpf]
            print("Paciente removido com sucesso!")
            print("")
            print("Deseja remover outro paciente?")
            print("[1] - Sim | [2] - Não")
            print("")
            try:
                opcao_remover_novamente = int(input("[Opção]: "))
                if opcao_remover_novamente == 1:
                    continue
                if opcao_remover_novamente == 2:
                    break
                else:
                    print("Opção inválida.")
                    break
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar os dados corretamente.")
        

while True:
    print("=================== PACIENTES ===================")
    print("[1] - Buscar Paciente    | [2] - Registrar Paciente")
    print("[3] - Atualizar Paciente | [4] - Remover Paciente")
    print("[5] - Sair")
    try:
        opcao = int(input("[Opção Desejada]: "))
        if opcao == 1:
            cpf = int(input("CPF do paciente: "))
            paciente = buscar_paciente(cpf)
            print(paciente if paciente else "Paciente não encontrado!")
            print("")
            print("[1] - Voltar ao menu | [2] - Encerrar o programa")
            try:
                opcao_retornar = int(input("[Opção]: "))
                if opcao_retornar == 1:
                    print("")
                    continue
                if opcao_retornar == 2:
                    break
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
                continue
        elif opcao == 2:
            registrar_paciente()
            print("")
            print("[1] - Voltar ao menu | [2] - Encerrar o programa")
            try:
                opcao_retornar = int(input("[Opção]: "))
                if opcao_retornar == 1:
                    print("")
                    continue
                if opcao_retornar == 2:
                    break
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
                continue
        elif opcao == 3:
            cpf = int(input("CPF do paciente para atualizar: "))
            atualizar_paciente(cpf)
            print("")
            print("[1] - Voltar ao menu | [2] - Encerrar o programa")
            try:
                opcao_retornar = int(input("[Opção]: "))
                if opcao_retornar == 1:
                    print("")
                    continue
                if opcao_retornar == 2:
                    break
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
                continue
        elif opcao == 4:
            cpf = int(input("CPF do paciente para remover: "))
            remover_paciente(cpf)
            print("")
            print("[1] - Voltar ao menu | [2] - Encerrar o programa")
            try:
                opcao_retornar = int(input("[Opção]: "))
                if opcao_retornar == 1:
                    print("")
                    continue
                if opcao_retornar == 2:
                    break
            except ValueError:
                print("Opção inválida. Retornando ao menu.")
                continue
        elif opcao == 5:
            break
        else:
            print("Opção inválida!")
            print("")
    except ValueError:
        print("Opção inválida, tente novamente!")
        print("")