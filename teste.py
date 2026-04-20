class Pagamento:
    def __init__(self, forma_pagamento="", valor_pagar=90, parcelas=1, Comparecimento = None):
        self.forma_pagamento = forma_pagamento
        self.valor_pagar = valor_pagar
        self.parcelas = parcelas
        self.pagamento_cancelado = False  # Controle de pagamento cancelado

    def comparecimento():
        escolha = int(input("O paciente compareceu? [1] Sim | [2] Não"))
        if escolha == 1:
            print("Continue o pagamento")
        else:
            print("Paciente não compareceu ao dia agendado!")


    # CRUD - CREATE
    def criar_pagamento(self, forma_pagamento, valor_pagar, parcelas):
        self.forma_pagamento = forma_pagamento
        self.valor_pagar = valor_pagar
        self.parcelas = parcelas
        self.pagamento_cancelado = False
        print("Pagamento criado com sucesso!\n")

    # CRUD - READ
    def exibir_pagamento(self):
        if self.pagamento_cancelado:
            print("Pagamento cancelado. Não há detalhes disponíveis.")
            return
        
        print("\nDetalhes do Pagamento")
        print("=" * 50)
        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Valor total: R$ {self.valor_pagar:.2f}")
        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")
        print("=" * 50)

    # CRUD - UPDATE
    def atualizar_pagamento(self, forma_pagamento=None, valor_pagar=None, parcelas=None):
        if self.pagamento_cancelado:
            print("Não é possível atualizar. O pagamento foi cancelado.")
            return

        if forma_pagamento:
            self.forma_pagamento = forma_pagamento
        if valor_pagar is not None:
            self.valor_pagar = valor_pagar
        if parcelas:
            self.parcelas = parcelas
        print("Pagamento atualizado com sucesso!\n")

    # CRUD - DELETE
    def excluir_pagamento(self):
        self.forma_pagamento = ""
        self.valor_pagar = 0
        self.parcelas = 1
        self.pagamento_cancelado = True
        print("Pagamento cancelado com sucesso!\n")

    def escolher_pagamento(self):
        while True:
            print("=" * 50)
            print("           Escolher forma de pagamento")
            print("=" * 50)
            print("\n============== Selecione uma opção ==============")
            print("[1] - Dinheiro  | [2] - Crédito")
            print("[3] - Débito    | [4] - Pix ")
            print("[5] - Cancelar pagamento(Apenas se cliente não apareceu ou errou a forma de pagamento)")
            print("============== ___________________ ==============\n")

            try:
                escolha = int(input("Sua escolha: "))
                print("")

                if escolha == 1:
                    self.forma_pagamento = "Dinheiro"
                    self.pagamento_cancelado = False
                    break
                elif escolha == 2:
                    self.forma_pagamento = "Crédito"
                    self.escolher_parcelas()
                    self.pagamento_cancelado = False
                    break
                elif escolha == 3:
                    self.forma_pagamento = "Débito"
                    self.pagamento_cancelado = False
                    break
                elif escolha == 4:
                    self.forma_pagamento = "Pix"
                    self.pagamento_cancelado = False
                    break
                elif escolha == 5:
                    print("Pagamento cancelado. O paciente não compareceu ou errou a formaa de pagamento.")
                    print("Se o caso for o segunda alternativa, por favor refaça o Pagamento!")
                    self.excluir_pagamento()
                    break
                else:
                    print("Escolha inválida! Tente novamente.\n")
            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 5.\n")

    def escolher_parcelas(self):
        while True:
            try:
                print("Pagamento no crédito permite até 4 parcelas sem juros.")
                self.parcelas = int(input("Digite o número de parcelas (1 a 4): "))

                if 1 <= self.parcelas <= 4:
                    break
                else:
                    print("Número de parcelas inválido! Escolha entre 1 e 4.\n")
            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 4.\n")

    def gerar_fatura(self):
        if self.pagamento_cancelado:
            print("")
            return
        
        print("\n                  Fatura detalhada")
        print("=" * 50)
        print(f"Valor total: R$ {self.valor_pagar:.2f}")
        print(f"Forma de pagamento: {self.forma_pagamento}")

        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")

        print("=" * 50)

    def gerar_recibo(self):
        if self.pagamento_cancelado:
            print("")
            return
        5
        print("\n                Recibo de Pagamento")
        print("=" * 50)
        print(f"Importância de: R$ {self.valor_pagar:.2f}")
        print("Referente à consulta médica.")
        print(f"Forma de pagamento: {self.forma_pagamento}")
 

        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")

        print("=" * 50)



pagamento = Pagamento(valor_pagar=90)
pagamento.escolher_pagamento()
pagamento.gerar_fatura()
pagamento.gerar_recibo()
pagamento.comparecimento()