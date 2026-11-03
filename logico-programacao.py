# Exercicio 1
nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo: ")
print(f"Bem-vindo(a) à ArkeTech, {nome}! Seu cargo é {cargo}.") 

# Exercicio 2 
valor_hora = float(input("Valor da hora de trabalho: "))
horas_extras = float(input("Quantidade de horas extras: "))
total = valor_hora * horas_extras
print("Total a pagar:", total)

#Exercicio 3 
transporte = float(input("Gasto com transporte: "))
alimentacao = float(input("Gasto com alimentação: "))
hospedagem = float(input("Gasto com hospedagem: "))
total = transporte + alimentacao + hospedagem
print(f"Total do reembolso: R$ {total:.2f}")

#Exercicio 4 
custo = float(input("Custo de fabricação: "))
preco_venda = custo * 1.35
print(f"Preço de venda: R$ {preco_venda:.2f}")

#Exercicio 5 
ano_nascimento = int(input("Ano de nascimento: "))
idade = 2026 - ano_nascimento
print(idade <= 24)

#Exercicio 6
status = input("Status da credencial (ativa ou bloqueada): ")
if status == "ativa":
    print("Acesso Liberado")
else:
    print("Acesso Negado: Procure a portaria")

#Exercicio 7
faturamento = float(input("Faturamento da empresa: "))
if faturamento > 100000:
    print("Limite aprovado: R$ 20.000")
elif faturamento >= 50000:
    print("Limite aprovado: R$ 10.000")
else:
    print("Crédito Reprovado")

#Exercicio 8 
faltas = int(input("Número de faltas: "))
vendas = float(input("Valor de vendas: "))
if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")

#Exercicio 9 
regiao = input("Sigla da região (S, CO, SD, N, ND): ")
if regiao == "S" or regiao == "SD":
    print("Frete: R$ 15")
elif regiao == "CO":
    print("Frete: R$ 25")
elif regiao == "ND" or regiao == "N":
    print("Frete: R$ 35")
else:
    print("Região inválida")

#Exercio 10 
estoque = int(input("Quantidade em estoque: "))
if estoque <= 15:
    print("COMPRA URGENTE")
elif estoque <= 50:
    print("ESTOQUE REGULAR")
else:
    print("ESTOQUE CHEIO")

#Exercicio 11
while True:
    matricula = input("Digite a matrícula (0000 para sair): ")
    if matricula == "0000":
        break
    print("Ponto registrado!")

#Exercicio 12 
funcionarios = ["isaac", "kauan", "miguel", "joao"]
for nome in funcionarios:
    print(nome + "@arketech.com")

#Exercicio 13
senha_correta = "Admin123"
tentativas = 0
acertou = False

while tentativas < 3:

    senha = input("Digite a senha: ")
    if senha == senha_correta:
        acertou = True
        break
    tentativas = tentativas + 1

if acertou:
    print("Login efetuado")
else:
    print("Conta bloqueada")

#Exercicio 14
faturamentos = [12000, 15000, 18000]
total_faturamento = 0
for valor in faturamentos:
    total_faturamento = total_faturamento + valor
print("Faturamento total:", total_faturamento)