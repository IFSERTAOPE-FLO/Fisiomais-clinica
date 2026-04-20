class Pagamento:
    def __init__(self, forma_pagamento="", valor_pagar=90, parcelas=1): 
        self.forma_pagamento = forma_pagamento
        self.valor_pagar = valor_pagar
        self.parcelas = parcelas

    def escolher_pagamento(self):
        while True:
            print("=" * 50)
            print("Escolher forma de pagamento")
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
                    print(" Escolha inválida! Tente novamente.\n")
            except ValueError:
                print(" Entrada inválida! Digite um número entre 1 e 4.\n")

    def escolher_parcelas(self):
        """Permite ao usuário escolher de 1 a 4 parcelas para pagamento no crédito."""
        while True:
            try:
                print(" Pagamento no crédito permite até 4 parcelas sem juros.")
                self.parcelas = int(input("Digite o número de parcelas (1 a 4): "))

                if 1 <= self.parcelas <= 4:
                    break
                else:
                    print(" Número de parcelas inválido! Escolha entre 1 e 4.\n")
            except ValueError:
                print(" Entrada inválida! Digite um número entre 1 e 4.\n")

    def gerar_fatura(self):
        print("\n Fatura detalhada")
        print("=" * 50)
        print(f"Valor total: R$ {self.valor_pagar:.2f}")
        print(f"Forma de pagamento: {self.forma_pagamento}")

        if self.forma_pagamento == "Crédito":
            valor_parcela = self.valor_pagar / self.parcelas
            print(f"Parcelado em {self.parcelas}x de R$ {valor_parcela:.2f} sem juros")

        print("=" * 50)

    def gerar_recibo(self):
        print("\n Recibo de Pagamento")
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
