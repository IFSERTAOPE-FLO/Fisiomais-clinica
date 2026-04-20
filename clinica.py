class Clinica:
    def __init__(self, nome_c, endereco, telefone, horario):
        self.nome_c = nome_c
        self.endereco = endereco
        self.telefone = telefone
        self.horario = horario
        
    def menu(self):
        while True:
            print('''
            Menu da Clínica | Fisiomais
            ----------------------------------------------
            [1] - Registrar dados | [2] - Visualizar dados
            [3] - Atualizar dados | [4] - Sair
            ''')
            opc = int(input('Opção: '))
            if opc == 1:
                self.registrar_d()
            elif opc == 2:
                print(self)
            elif opc == 3:
                self.atualizar_d()
            elif opc == 4:
              print("Saindo do sistema...")
              break
            else:
                print("Opção inválida! Tente novamente.")
                print('''
                Menu da Clínica | Fisiomais
                ----------------------------------------------
                [1] - Registrar dados | [2] - Visualizar dados
                [3] - Atualizar dados | [4] - Sair
            ''')
                opc = int(input('Opção: '))

    def registrar_d(self):
        print('''         
        Cadastro da Clínica | Fisiomais
        -------------------------------------------------------------------------------------------------
        Para se cadastrar no sistema, insira as informações da clínica, assim como no exemplo a seguir:
        Nome da clínica: Saúde+
        Endereço da clínica: Rua Paulo Roberto Pereira, 18
        Telefone da clínica: (XX)XXXX-XXXX
        Horário de funcionamento da clínica: Seg-Sex | 06:00 ás 18:00.
        -------------------------------------------------------------------------------------------------''')
        self.nome_c = input('Nome da clínica: ')
        self.endereco = input('Endereço da clínica: ')
        self.telefone = input('Telefone da clínica: ')
        self.horario = input('Horário de funcionamento da clínica: ')
        print('Dados cadastrados com sucesso!')
        self.menu()

    def __str__(self):
        return (
        f"Nome da clínica: {self.nome_c}\n"
        f"Endereço da clínica: {self.endereco}\n"
        f"Telefone da clínica: {self.telefone}\n"
        f"Horário de funcionamento da clínica: {self.horario}"
    )
    
    def atualizar_d(self):
        print(f'Nome da clínica atual: {self.nome_c}')
        self.nome_c = input('Informe o novo nome: ')
        print(f'Endereço da clínica atual: {self.endereco}')
        self.endereco = input('Informe o novo endereço: ')
        print(f'Número de Telefone da clínica atual: {self.telefone}')
        self.telefone = input('Informe o novo número de telefone: ')
        print(f'Horário de funcionamento atual: {self.horario}')
        self.horario = input('Informe o novo horário de funcionamento: ')
        print('Dados Atualizados com sucesso!')
        self.menu()

clinica = Clinica()
clinica.menu