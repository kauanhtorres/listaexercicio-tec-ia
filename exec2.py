while True: # o loop infinito foi iniciado
    comando = input("digite 'sair' para desligar o motor : " )

    if comando.lower() == 'sair' :
       print("motor desligado")
       break # a trava de segurança foi adicionada!
    else:
       print("o motor continua a rodar...")