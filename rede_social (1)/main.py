from servicos.gerenciador_usuarios import GerenciadorUsuarios
from servicos.gerenciador_chat import GerenciadorChat

def main():
    print("=== Backend da Rede Social (falta conectar com HTML ainda) ===")

    ger_usuarios = GerenciadorUsuarios()
    ger_chat = GerenciadorChat()

    usuario1 = ger_usuarios.cadastrar_usuario("lucas", "123")
    usuario2 = ger_usuarios.cadastrar_usuario("ana", "abc")

    ger_chat.enviar_mensagem(usuario1, usuario2, "Oi Ana, tudo bem?")
    ger_chat.enviar_mensagem(usuario2, usuario1, "Tudo sim e você?")

    print("
Histórico de mensagens:")
    mensagens = ger_chat.listar_mensagens(usuario1, usuario2)
    for msg in mensagens:
        print(msg)

if __name__ == "__main__":
    main()
