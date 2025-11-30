from datetime import datetime

class Mensagem:
    def __init__(self, remetente, destinatario, conteudo):
        self.remetente = remetente
        self.destinatario = destinatario
        self.conteudo = conteudo
        self.data_envio = datetime.now()

    def __str__(self):
        hora = self.data_envio.strftime("%H:%M")
        return f"[{hora}] {self.remetente.nome}: {self.conteudo}"
