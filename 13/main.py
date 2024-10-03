import verificador_email

email = input("Digite o email: ").strip()

verificacao = verificador_email.verificador(email)

if verificacao == True:
    print("Email Valido")
else:
    print("Email Invalido")