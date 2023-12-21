print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")
r1 = int(input("Seu SO anterior era Linux?\n(0) Não\n(1) Sim\n"))
if (r1 == 0):
    r2  = int(input("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n"))
    if (r2 == 0):
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
    elif (r2 == 1):
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.")
    else:
        print("Opção inválida, recomece o questionário.")
elif (r1 == 1):
    r2 = int(input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n"))
    if (r2 == 0):
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.")
    elif (r2 == 2):
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.")
    elif (r2 == 1):
        r3 = int(input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n"))
        if (r3 == 0):
            r4 = int(input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n"))
            if (r4 == 0):
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.")
            elif (r4 == 1):
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.")
            else:
                print("Opção inválida, recomece o questionário.")
        elif (r3 == 1):
            r4 = int(input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n"))
            if (r4 == 0):
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
            elif (r4 == 1):
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.")
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    else:
        print("Opção inválida, recomece o questionário.")
else:
    print("Opção inválida, recomece o questionário.")