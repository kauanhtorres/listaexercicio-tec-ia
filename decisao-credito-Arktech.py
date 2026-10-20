# ====================================================
# Sistema de Auditoria e Decisão de Crédito - ArkeTech
# ====================================================

print("--- SISTEMA DE CRÉDITO ARKETECH ---")

# 1. Entrada de dados (pedindo as informações pro usuário)
nome_empresa = input("Digite o nome da empresa: ")
faturamento = float(input("Digite o faturamento mensal (R$): "))
emprestimo = float(input("Digite o valor do empréstimo (R$): "))

# 2. Cálculos
# Dividindo em 12x sem juros
parcela = emprestimo / 12

# Descobrindo qual a porcentagem da parcela em relação ao faturamento
porcentagem = (parcela / faturamento) * 100

# 3. Árvore de Decisão (if / elif / else)
if porcentagem <= 30:
    parecer = "APROVADO"
elif porcentagem <= 50:
    parecer = "EM ANÁLISE (Risco Moderado)"
else:
    parecer = "RECUSADO"

# 4. Exibindo o resultado formatado com f-strings
print("\n--- RESULTADO DA ANÁLISE ---")
print(f"Empresa: {nome_empresa}")
print(f"Faturamento Mensal: R$ {faturamento:.2f}")
print(f"Valor da Parcela (12x): R$ {parcela:.2f}")
print(f"Comprometimento do Faturamento: {porcentagem:.2f}%")
print(f"Parecer Final: {parecer}")