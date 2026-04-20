class Clinica:
    def __init__(self, nome_c="", endereco="", telefone="", horario=""):
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
              print("")
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
def classe_clinica():
  clinica = Clinica()
  clinica.menu()

########################################################################################################################

class Pessoa:
    def __init__(self, nome, data_de_nascimento, telefone, email):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.telefone = telefone
        self.email = email

class Profissional(Pessoa):
    def __init__(self, nome, data_de_nascimento, telefone, email, especialidade, registro, data_rgs):
        super().__init__(nome, data_de_nascimento, telefone, email)
        self.especialidade = especialidade
        self.registro = registro
        self.data_rgs = data_rgs

    def info_dispn(self):
        return f"Profissional: {self.nome}\nEspecialidade: {self.especialidade}\nTelefone: {self.telefone}\nEmail: {self.email}\nRegistro: {self.registro}\nData de Registro: {self.data_rgs}"
    def __str__(self):
        return self.nome
class ProfissionalRepository:
    def __init__(self):
        self.profissionais = []

    def adicionar_profissional(self, profissional):
        self.profissionais.append(profissional)

    def listar_profissionais(self):
        for profissional in self.profissionais:
            print(profissional.info_dispn())
            print("--------------------")

    def buscar_profissional_por_nome(self, nome):
        for profissional in self.profissionais:
            if profissional.nome == nome:
                return profissional
        return None

    def atualizar_profissional(self, nome, novos_dados):
        profissional = self.buscar_profissional_por_nome(nome)
        if profissional:
            for chave, valor in novos_dados.items():
                if hasattr(profissional, chave):
                    setattr(profissional, chave, valor)
            return True
        return False

    def excluir_profissional(self, nome):
        profissional = self.buscar_profissional_por_nome(nome)
        if profissional:
            self.profissionais.remove(profissional)
            return True
        return False

ramon = Profissional("Ramon", "13/07/1973", "87 4002-8922", "ramon@email.com", "Fisioterapeuta", "CRM 12345", "2020-01-01")
eduardo = Profissional("Eduardo", "01-01-1983", "87 9900-6969", "dudu@email.com", "Fisioterapeuta", "CRM 67890", "2018-06-01")
marcos = Profissional("Marcos", "27/02/1999", "87 9665-3562", "marcos@gmail.com", "Fisioterapeuta", "CRM 13265", "2021-03-02")
maria = Profissional ("Maria", "30/06/1995", "87 9856-6589", "maria@gmail.com", "Fisioterapeuta", "CRM 32565", "2019-07-05")

repositorio = ProfissionalRepository()
repositorio.adicionar_profissional(ramon)
repositorio.adicionar_profissional(eduardo)
repositorio.adicionar_profissional(marcos)
repositorio.adicionar_profissional(maria)

def buscar_profissional():
    nome = input("Nome do profissional: ")
    profissional = repositorio.buscar_profissional_por_nome(nome)
    print(profissional.info_dispn() if profissional else "Profissional não encontrado!")

def registrar_profissional():
    nome = input("Nome: ")
    data_de_nascimento = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    especialidade = input("Especialidade: ")
    registro = input("Registro: ")
    data_rgs = input("Data de Registro: ")

    novo_profissional = Profissional(nome, data_de_nascimento, telefone, email, especialidade, registro, data_rgs)
    repositorio.adicionar_profissional(novo_profissional)
    print("Profissional registrado com sucesso!")

def atualizar_profissional_info():
    nome = input("Nome do profissional a ser atualizado: ")
    novos_dados = {}

    print("Informe os novos dados (pressione Enter para manter o valor atual):")
    novos_dados['nome'] = input(f"Nome ({nome}): ") or nome
    novos_dados['data_de_nascimento'] = input("Data de Nascimento: ")
    novos_dados['telefone'] = input("Telefone: ")
    novos_dados['email'] = input("E-mail: ")
    novos_dados['especialidade'] = input("Especialidade: ")
    novos_dados['registro'] = input("Registro: ")
    novos_dados['data_rgs'] = input("Data de Registro: ")

    if repositorio.atualizar_profissional(nome, novos_dados):
        print("Profissional atualizado com sucesso!")
    else:
        print("Profissional não encontrado!")

def remover_profissional():
    nome = input("Nome do profissional a ser removido: ")
    if repositorio.excluir_profissional(nome):
        print("Profissional removido com sucesso!")
    else:
        print("Profissional não encontrado!")

def classe_profissional():
  while True:
      print("=================== PROFISSIONAIS ===================")
      print("[1] - Listar Profissionais")
      print("[2] - Buscar Profissional")
      print("[3] - Registrar Profissional")
      print("[4] - Atualizar Profissional")
      print("[5] - Remover Profissional")
      print("[6] - Sair")

      try:
          opcao = int(input("[Opção Desejada]: "))
          if opcao == 1:
              repositorio.listar_profissionais()
          elif opcao == 2:
              buscar_profissional()
          elif opcao == 3:
              registrar_profissional()
          elif opcao == 4:
              atualizar_profissional_info()
          elif opcao == 5:
              remover_profissional()
          elif opcao == 6:
              print("")
              break
          else:
              print("Opção inválida!")
      except ValueError:
          print("Opção inválida, tente novamente!")

################################################################################

class Paciente(Pessoa):
    def __init__(self,cpf, nome, data_de_nascimento, telefone, email, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, endereco, historico_hospitalar):
        super().__init__(nome, data_de_nascimento, telefone, email)
        self.cpf = cpf
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.plano_de_saude = plano_de_saude
        self.rg = rg
        self.tipo_sanguineo = tipo_sanguineo
        self.endereco = endereco
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

paciente1 = Paciente(12312312312, "Roberto Siqueira", "23/09/1998", "(87) 1234-4321", "siqueirinha@gmail.com", 65.32, 1.73, "Masculino", "Unimed", "123123123123", "O+", "Rua A, 456", "Nenhum")
pacientes.append(paciente1)



def buscar_paciente(cpf):
    for paciente in pacientes:
        if paciente.cpf == cpf:
            return paciente
    return None

def registrar_paciente():
    while True:
        try:
            cpf = int(input("CPF (apenas números): "))
            nome = input("Nome: ")
            data_de_nascimento = input("Data de Nascimento (**/**/****): ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            peso = float(input("Peso (kg - apenas números): "))
            altura = float(input("Altura (m - apenas números): "))
            sexo = input("Sexo: ")
            plano_de_saude = input("Plano de Saúde: ")
            rg = input("RG: ")
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            endereco = input("Endereço: ")
            historico_hospitalar = input("Histórico Hospitalar: ")

            novo_paciente = Paciente(cpf, nome, data_de_nascimento, telefone, email, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, endereco, historico_hospitalar)
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
                paciente.data_de_nascimento = input(f"Data de Nascimento ({paciente.data_de_nascimento}): ") or paciente.data_de_nascimento
                paciente.telefone = input(f"Telefone ({paciente.telefone}): ") or paciente.telefone
                paciente.email = input(f"E-mail ({paciente.email}): ") or paciente.email
                paciente.peso = float(input(f"Peso ({paciente.peso} kg): ") or paciente.peso)
                paciente.altura = float(input(f"Altura ({paciente.altura} m): ") or paciente.altura)
                paciente.sexo = input(f"Sexo ({paciente.sexo}): ") or paciente.sexo
                paciente.plano_de_saude = input(f"Plano de Saúde ({paciente.plano_de_saude}): ") or paciente.plano_de_saude
                paciente.rg = input(f"RG ({paciente.rg}): ") or paciente.rg
                paciente.tipo_sanguineo = input(f"Tipo Sanguíneo ({paciente.tipo_sanguineo}): ") or paciente.tipo_sanguineo
                paciente.endereco = input(f"Endereço ({paciente.endereco}): ") or paciente.endereco
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
                elif opcao_atualizar_novamente == 2:
                    break
                else:
                    print("Opção inválida. Retornando ao menu.")
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

def classe_paciente():
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
              print("[1] - Voltar ao menu paciente | [2] - Sair")
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
              print("[1] - Voltar ao menu paciente | [2] - Sair")
              try:
                  opcao_retornar = int(input("[Opção]: "))
                  if opcao_retornar == 1:
                      print("")
                      continue
                  if opcao_retornar == 2:
                      break
                  else:
                    print("Opção inválida. Retornando ao menu.")
                    continue
              except ValueError:
                  print("Opção inválida. Retornando ao menu.")
                  continue
          elif opcao == 3:
              cpf = int(input("CPF do paciente para atualizar: "))
              atualizar_paciente(cpf)
              print("")
              print("[1] - Voltar ao menu paciente | [2] - Sair")
              try:
                  opcao_retornar = int(input("[Opção]: "))
                  if opcao_retornar == 1:
                      print("")
                      continue
                  if opcao_retornar == 2:
                      break
                  else:
                    print("Opção inválida. Retornando ao menu.")
                    continue
              except ValueError:
                  print("Opção inválida. Retornando ao menu.")
                  continue
          elif opcao == 4:
              cpf = int(input("CPF do paciente para remover: "))
              remover_paciente(cpf)
              print("")
              print("[1] - Voltar ao menu paciente | [2] - Sair")
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

################################################################################

import random
from datetime import datetime

class Agendamento:
    def __init__(self, horarios_disponiveis, repositorio_profissionais):
        self.horarios_disponiveis = horarios_disponiveis
        self.repositorio_profissionais = repositorio_profissionais
        self.historico_consultas = []

    def gerar_codigo_acesso(self):
        while True:
            codigo = f"ACSS-{random.randint(1000, 9999)}"
            if not any(c['codigo_acesso'] == codigo for c in self.historico_consultas):
                return codigo

    def validar_horario(self, hora):
        try:
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False

    def marcar_consulta(self):
        data = input("Informe a data da consulta (DD-MM-AAAA): ")
        hora = input(f"Informe a hora da consulta (horários disponíveis: {self.horarios_disponiveis}): ")

        if not self.validar_horario(hora):
            return f"Horário {hora} está em formato inválido."
        if hora not in self.horarios_disponiveis:
            return f"Horário {hora} não está disponível."

        cpf = int(input("Informe o CPF do paciente: "))
        paciente = buscar_paciente(cpf)
        if not paciente:
            return "Paciente não encontrado! Registre o paciente antes de agendar a consulta."

        print("Profissionais disponíveis:")
        for profissional in self.repositorio_profissionais.profissionais:
            print(profissional.nome)

        profissional_nome = input("Informe o nome do profissional: ")
        profissional = self.repositorio_profissionais.buscar_profissional_por_nome(profissional_nome)
        if not profissional:
            return f"Profissional {profissional_nome} não encontrado."

        tipo_servico = input("Informe o tipo de serviço (por exemplo, consulta, fisioterapia, etc.): ")

        codigo_acesso = self.gerar_codigo_acesso()
        consulta = {
            "codigo_acesso": codigo_acesso,
            "data": data,
            "hora": hora,
            "paciente": paciente,
            "profissional": profissional,
            "tipo_servico": tipo_servico
        }
        self.historico_consultas.append(consulta)
        self.horarios_disponiveis.remove(hora)
        return f"Consulta marcada com sucesso! Código de acesso: {codigo_acesso}. Valor a pagar: R$ 90."

    def remarcar_consulta(self):
        codigo_acesso = input("Informe o código de acesso da consulta a ser remarcada: ")
        consulta = next((c for c in self.historico_consultas if c["codigo_acesso"] == codigo_acesso), None)

        if not consulta:
            return "Código de acesso inválido."

        nova_data = input("Informe a nova data da consulta (DD-MM-AAAA): ")
        novo_horario = input(f"Informe o novo horário da consulta (horários disponíveis: {self.horarios_disponiveis}): ")

        if novo_horario not in self.horarios_disponiveis:
            return f"Novo horário {novo_horario} não está disponível."

        self.horarios_disponiveis.append(consulta["hora"])
        consulta["data"] = nova_data
        consulta["hora"] = novo_horario
        self.horarios_disponiveis.remove(novo_horario)
        return f"Consulta remarcada para {nova_data} às {novo_horario}."

    def cancelar_consulta(self):
        codigo_acesso = input("Informe o código de acesso da consulta a ser cancelada: ")
        consulta = next((c for c in self.historico_consultas if c["codigo_acesso"] == codigo_acesso), None)

        if not consulta:
            return "Código de acesso inválido."

        self.historico_consultas.remove(consulta)
        self.horarios_disponiveis.append(consulta["hora"])
        return "Consulta cancelada com sucesso."

horarios_disponiveis = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"]
agenda = Agendamento(horarios_disponiveis, repositorio)

def main():
    while True:
        print("\nMenu:")
        print("1. Marcar consulta")
        print("2. Remarcar consulta")
        print("3. Cancelar consulta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(agenda.marcar_consulta())
        elif opcao == "2":
            print(agenda.remarcar_consulta())
        elif opcao == "3":
            print(agenda.cancelar_consulta())
        elif opcao == "4":
            print("")
            break
        else:
            print("Opção inválida! Tente novamente.")

################################################################################

class Pagamento:
    def __init__(self):
        self.data = ""
        self.paciente = None
        self.profissional = None
        self.forma_pagamento = ""
        self.valor_pagar = 90
        self.parcelas = 1
        self.pagamento_cancelado = False

    def iniciar_pagamento(self, agenda):
      while True:
        print("\n=================== PAGAMENTO ===================")
        print("===================================================")
        print("[1] - Gerenciar pagamento | [2] - Sair")
        try:
            opcao_pagamento = int(input("[Opção]: "))
    
            if opcao_pagamento == 1:
                codigo = input("Informe o código da consulta: ").strip()
                consulta = None
                for c in agenda.historico_consultas:
                    if c["codigo_acesso"] == codigo:
                        consulta = c
                        break
                if not consulta:
                    print("Consulta não encontrada!")
                    print("")
                    print("[1] - Tentar novamente | [2] - Retornar ao menu")
                    try:
                        opcao_retornar = int(input("[Opção]: "))
                        if opcao_retornar == 1:
                            continue  
                        elif opcao_retornar == 2:
                            break  
                        else:
                            print("Opção inválida. Retornando ao menu.")
                    except ValueError:
                        print("Opção inválida. Retornando ao menu.")
                        continue
                    continue
                self.paciente = consulta["paciente"]
                self.profissional = consulta["profissional"]
                print("\nConsulta encontrada:")
                print(f"Código: {codigo}")
                print(f"Data da consulta: {consulta['data']}")
                print(f"Hora: {consulta['hora']}")
                print(f"Paciente: {self.paciente.nome}")
                print(f"Profissional: {self.profissional}")
                print("=" * 50)
                self.escolher_pagamento()
                if self.pagamento_cancelado:
                    return
                self.data = input("Digite a data do pagamento (DD/MM/AAAA): ").strip()
                self.gerar_fatura()
                self.gerar_recibo()
            elif opcao_pagamento == 2:
                break  
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida! Tente novamente.")
            print("")
        
    def escolher_pagamento(self):
        if self.pagamento_cancelado:
            return

        compareceu = input("O paciente compareceu? (sim/não): ").strip().lower()
        if compareceu == "sim":
            print("=" * 50)
            print("            Escolher forma de pagamento")
            print("=" * 50)
            print("\n============== Selecione uma opção ==============")
            print("[1] - Dinheiro  | [2] - Crédito")
            print("[3] - Débito    | [4] - Pix")
            print("============== ___________________ ==============\n")
            while True:
                try:
                    escolha = int(input("Sua escolha: "))
                    if escolha == 1:
                        self.forma_pagamento = "Dinheiro"
                        break
                    elif escolha == 2:
                        self.forma_pagamento = "Crédito"
                        self.escolher_parcelas()
                        break
                    elif escolha == 3:
                        self.forma_pagamento = "Débito"
                        break
                    elif escolha == 4:
                        self.forma_pagamento = "Pix"
                        break
                    else:
                        print("Escolha inválida! Tente novamente.\n")
                except ValueError:
                    print("Entrada inválida! Digite um número entre 1 e 4.\n")
        elif compareceu == "não":
            self.cancelar_pagamento()
            self.iniciar_pagamento(agenda)
        else:
            print("Resposta inválida! Por favor, digite 'sim' ou 'não'.\n")
            self.escolher_pagamento()

    def escolher_parcelas(self):
        while True:
            try:
                print("Pagamento no crédito permite até 4 parcelas sem juros.")
                parcelas = int(input("Digite o número de parcelas (1 a 4): "))
                if 1 <= parcelas <= 4:
                    self.parcelas = parcelas
                    break
                else:
                    print("Número de parcelas inválido! Escolha entre 1 e 4.\n")
            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 4.\n")

    def gerar_fatura(self):
        if self.pagamento_cancelado:
            print("O pagamento foi cancelado. Não é possível gerar a fatura.")
            return

        print("\n              Fatura detalhada")
        print("=" * 50)
        print(f"Valor total: R$ {self.valor_pagar:.2f}")
        print(f"Forma de pagamento: {self.forma_pagamento}")
        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")
        print("=" * 50)

    def gerar_recibo(self):
        if self.pagamento_cancelado:
            print("Pagamento foi cancelado. Não é possível gerar o recibo.")
            return

        print("\n               Recibo de Pagamento")
        print("=" * 50)
        print(f"Valor total: R$ {self.valor_pagar:.2f} pago pelo paciente {self.paciente.nome}")
        print(f"Referente à consulta com {self.profissional}.")
        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Data do pagamento: {self.data}")
        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")
        print("=" * 50)

    def cancelar_pagamento(self):
        self.pagamento_cancelado = True
        print("Pagamento cancelado com sucesso!")

    def classe_pagamento():
      pagamento = Pagamento()
      pagamento.iniciar_pagamento(agenda)

################################################################################

class Menu:
  while True:
    print("================= FISIOMAIS =================")
    print("=============================================")
    print("----------- O que deseja acessar? -----------")
    print("[1] - Clínica")
    print("[2] - Profissional")
    print("[3] - Paciente")
    print("[4] - Agendamento")
    print("[5] - Pagamento")
    print("[6] - Sair")
    print("=============================================")

    try:
      opc = int(input("Opção: "))
      if opc == 1:
        clinica = Clinica()
        clinica.menu()
      elif opc == 2:
        classe_profissional()
      elif opc == 3:
        classe_paciente()
      elif opc == 4:
        main()
      elif opc == 5:
        pagamento = Pagamento()
        pagamento.iniciar_pagamento(agenda)
      elif opc == 6:
        print("Saindo do programa...")
        break
    except ValueError:
      print("Opção inválida! Tente novamente.")
