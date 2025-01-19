class Pagamento:
    def __init__(self, paciente, valor_pagar=90):
        self.paciente = paciente  
        self.valor_pagar = valor_pagar
        self.forma_pagamento = ""

    def escolher_pagamento(self):
        while True:
            try:
                escolha = int(input("Escolha sua forma de pagamento: 1- Dinheiro, 2- Crédito, 3- Débito, 4- Pix: "))
                if escolha == 1:
                    self.forma_pagamento = "Dinheiro"
                    break
                elif escolha == 2:
                    self.forma_pagamento = "Crédito"
                    break
                elif escolha == 3:
                    self.forma_pagamento = "Débito"
                    break
                elif escolha == 4:
                    self.forma_pagamento = "Pix"
                    break
                else:
                    print("Escolha inválida! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 4.")

    def gerar_fatura(self):
        fatura = f"Fatura detalhada: Valor total a pagar: R$ {self.valor_pagar:.2f}, Forma de pagamento: {self.forma_pagamento}"
        print(fatura)

    def gerar_recibo(self):
        recibo = (f"Aqui está o seu recibo: \n"
                  f"Recebemos de: {self.paciente['nome']} (Código: {self.paciente['codigo']})\n"
                  f"Importância de: R$ {self.valor_pagar:.2f}, Referente à consulta médica.\n"
                  f"Forma de pagamento: {self.forma_pagamento}\n"
                  f"RG (CPF): {self.paciente['rg']}\n")
        print(recibo)



paciente_encontrado = {
    "nome": "João Silva",
    "codigo": "123",
    "rg": "123.456.789-00"
}

if paciente_encontrado:
    pagamento = Pagamento(paciente_encontrado, 90)  
    pagamento.escolher_pagamento()  
    pagamento.gerar_fatura()      
    pagamento.gerar_recibo()
