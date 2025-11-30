from modelos.mensagem import Mensagem

class GerenciadorChat:
    def __init__(self):
        self.mensagens = []

    def enviar_mensagem(self, remetente, destinatario, conteudo):
        msg = Mensagem(remetente, destinatario, conteudo)
        self.mensagens.append(msg)
        print(f"{remetente.nome} -> {destinatario.nome}: mensagem enviada.")

    def listar_mensagens(self, usuario1, usuario2):
        return [
            msg for msg in self.mensagens
            if (msg.remetente == usuario1 and msg.destinatario == usuario2)
            or (msg.remetente == usuario2 and msg.destinatario == usuario1)
        ]
