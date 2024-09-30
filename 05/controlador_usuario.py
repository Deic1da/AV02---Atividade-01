def tentativa_login(login, senha):
    with open('05/usuarios.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    logado = False
    for linha in conteudo:
        texte = linha.strip().split()
        if texte[1] == login and texte[3] == senha:
            logado = True
            return logado, f"Bem vindo {texte[1]}!"
    return logado, "Credenciais incoretas!"
    