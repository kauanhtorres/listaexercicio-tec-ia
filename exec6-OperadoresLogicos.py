nota_avaliacao = float(input("Nota da avaliação (0 a 10):"))
projetos_entregues = int(input("Projetos entregues no semestre: "))

if nota_avaliacao >= 8.0 and projetos_entregues >= 3:
    print("💰 Bonus de desempenho aprovado!")      
else:
    print("Bonus negado. Metas nao atingidas integralmente.")