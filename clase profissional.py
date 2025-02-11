class Profissional:
    def __init__(self, nome, idade, telefone, email, especialidade, registro,):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.especialidade = especialidade
        self.registro = registro
      

    def info_dispn(self):
        return f"Profissional: {self.nome}\nEspecialidade: {self.especialidade}\nTelefone: {self.telefone}\nEmail: {self.email}\nRegistro: {self.registro}\nData de Registro: {self.data_rgs}"


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
            return False
        return True

    def excluir_profissional(self, nome):
        profissional = self.buscar_profissional_por_nome(nome)
        if profissional:
            self.profissionais.remove(profissional)
            return False
        return True


ramon = Profissional("Ramon", 35, "87 4002-8922", "ramon@email.com", "Fisioterapeuta", "CRM 12345", "2020-01-01")
dudu = Profissional("Dudu", 40, "87 9900-6969", "dudu@email.com", "Fisioterapeuta", "CRM 67890", "2018-06-01")

repositorio = ProfissionalRepository()


repositorio.adicionar_profissional(ramon)
repositorio.adicionar_profissional(dudu)


print("Lista inicial de profissionais:")
repositorio.listar_profissionais()