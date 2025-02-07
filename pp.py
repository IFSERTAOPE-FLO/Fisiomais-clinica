class Pagamento:
    def __init__(self, forma_pagamento="", valor_pagar=90, parcelas=1):
        self.forma_pagamento = forma_pagamento
        self.valor_pagar = valor_pagar
        self.parcelas = parcelas
        self.pagamento_cancelado = False  

    # Criar
    def criar_pagamento(self, forma_pagamento, valor_pagar, parcelas):
        self.forma_pagamento = forma_pagamento
        self.valor_pagar = valor_pagar
        self.parcelas = parcelas
        self.pagamento_cancelado = False
        print("Pagamento criado com sucesso!\n")

    # Ler
    def exibir_pagamento(self):
        if self.pagamento_cancelado:
            print("Pagamento foi cancelado. Não há detalhes disponíveis.")
            return
        
        print("\nDetalhes do Pagamento")
        print("=" * 50)
        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Valor total: R$ {self.valor_pagar:.2f}")
        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")
        print("=" * 50)

    # Apagar
    def excluir_pagamento(self):
        self.forma_pagamento = ""
        self.valor_pagar = 0
        self.parcelas = 1
        self.pagamento_cancelado = True
        print("Pagamento cancelado. O paciente não compareceu ao dia e à hora agendadas.\n")

    def escolher_pagamento(self):
        while True:
            if self.pagamento_cancelado:
                break

            compareceu = input("O paciente compareceu? (sim/não): ").strip().lower()

            if compareceu == "sim":
                print("=" * 50)
                print("           Escolher forma de pagamento")
                print("=" * 50)
                print("\n============== Selecione uma opção ==============")
                print("[1] - Dinheiro  | [2] - Crédito")
                print("[3] - Débito    | [4] - Pix ")
                print("============== ___________________ ==============\n")

                try:
                    escolha = int(input("Sua escolha: "))
                    print("")

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
                break
            elif compareceu == "não":
                self.excluir_pagamento()
                break
            else:
                print("Resposta inválida! Por favor, digite 'sim' ou 'não'.\n")

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
            print("Pagamento foi cancelado. Não é possível gerar a fatura.")
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
            print("Pagamento foi cancelado. Não é possível gerar o recibo.")
            return
        
        print("\n                Recibo de Pagamento")
        print("=" * 50)
        print(f"Importância de: R$ {self.valor_pagar:.2f}")
        print("Referente à consulta médica.")
        print(f"Forma de pagamento: {self.forma_pagamento}")
 
        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")

        print("=" * 50)


pagamento = Pagamento()

pagamento.escolher_pagamento()

if not pagamento.pagamento_cancelado:
    pagamento.exibir_pagamento()

    pagamento.gerar_fatura()

    pagamento.gerar_recibo()

else:
    print("Não foi possível gerar fatura ou recibo devido ao cancelamento do pagamento.")
