import controlador_usuario

login = input("Digite o login: ")
senha = input("Digite a senha: ")

tentativa = controlador_usuario.tentativa_login(login,senha)

if tentativa[0] == True:
    print(tentativa[1])
else:
    print(tentativa[1])