from modelos.usuario import Usuario

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, senha):
        if self.buscar_usuario(nome):
            print(f"Já existe alguém com o nome '{nome}'.")
            return None
        novo = Usuario(nome, senha)
        self.usuarios.append(novo)
        print(f"Usuário '{nome}' cadastrado!")
        return novo

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return usuario
        return None

    def validar_login(self, nome, senha):
        usuario = self.buscar_usuario(nome)
        if usuario and usuario.senha == senha:
            return usuario
        return None
