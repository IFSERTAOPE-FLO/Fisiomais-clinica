import random
from datetime import datetime

class Agendamento:
    def init(self, horarios_disponiveis, fisioterapeutas_disponiveis):
        self.horarios_disponiveis = horarios_disponiveis
        self.fisioterapeutas_disponiveis = fisioterapeutas_disponiveis
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

    def marcar_consulta(self, data, hora, paciente, medico, tipo_servico):
        if not self.validar_horario(hora):
            return f"Horário {hora} está em formato inválido."
        if hora not in self.horarios_disponiveis:
            return f"Horário {hora} não está disponível."
        if medico not in self.fisioterapeutas_disponiveis:
            return f"Médico {medico} não está disponível."
        
        codigo_acesso = self.gerar_codigo_acesso()
        consulta = {
            "codigo_acesso": codigo_acesso,
            "data": data,
            "hora": hora,
            "paciente": paciente,
            "medico": medico,
            "tipo_servico": tipo_servico
        }
        self.historico_consultas.append(consulta)
        self.horarios_disponiveis.remove(hora)
        return f"Consulta marcada com sucesso! Código de acesso: {codigo_acesso}"

    def notificar_consulta(self, codigo_acesso):
        consulta = next((c for c in self.historico_consultas if c["codigo_acesso"] == codigo_acesso), None)
        if consulta:
            return (f"Notificação: Consulta marcada para {consulta['data']} às {consulta['hora']} com o(a) médico(a) "
                    f"{consulta['medico']} para o(a) paciente {consulta['paciente']}.")
        return "Código de acesso inválido."

# Inicializar sistema
horarios_disponiveis = ["09:00", "10:00", "11:00", "14:00"]
fisioterapeutas_disponiveis = ["Dr. João", "Dra. Maria"]

agenda = Agendamento(horarios_disponiveis, fisioterapeutas_disponiveis)

# Funções auxiliares
def solicitar_dados():
    data = input("Informe a data da consulta (DD-MM-AAAA): ")
    hora = input(f"Informe a hora da consulta (horários disponíveis: {horarios_disponiveis}): ")
    paciente = input("Informe o nome do paciente: ")
    medico = input(f"Informe o nome do médico (disponíveis: {fisioterapeutas_disponiveis}): ")
    tipo_servico = input("Informe o tipo de serviço (exemplo: Fisioterapia): ")
    return data, hora, paciente, medico, tipo_servico

def main():
    data, hora, paciente, medico, tipo_servico = solicitar_dados()
    resultado = agenda.marcar_consulta(data, hora, paciente, medico, tipo_servico)
    print(resultado)

    if "Código de acesso" in resultado:
        codigo = resultado.split(": ")[1].strip()
        notificacao = agenda.notificar_consulta(codigo)
        print(notificacao)
    else:
        print("Erro ao marcar a consulta.")

if __name__ == "_main_":
    main()