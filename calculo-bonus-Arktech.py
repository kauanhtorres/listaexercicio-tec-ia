# ==========================================
# MÓDULOS DE PROCESSAMENTO (def)
# ==========================================
def calcular_bonus(salario):
    """Calcula o bônus padrão de 15% da ArkeTech"""
    return salario * 0.15

# ==========================================
# INTERFACE DO SISTEMA
# ==========================================
print("========================================")
print("       RH ARKETECH - BÔNUS INICIAL      ")
print("========================================\n")

while True:
    print("\n--- NOVO REGISTRO ---")
    
    # O .strip() remove espaços em branco digitados sem querer
    nome = input("Nome completo (ou digite '0' para sair): ").strip()
    
    if nome == '0':
        print("\n🚪 Encerrando o painel de bônus. Bom trabalho!")
        break
        
    # Blindagem 1: Impede que o nome fique em branco se o usuário só apertar 'Enter'
    if not nome:
        print("⚠️ ERRO: O campo de nome não pode ficar vazio.")
        continue
        
    cargo = input("Cargo contratado: ").strip()
    
    # Blindagem 2: A Zona de Perigo (Tratamento de Exceções)
    try:
        salario_base = float(input("Salário Base (use ponto. Ex: 1500.00): R$ "))
        
        # Blindagem 3: Regra de Negócio (Não existe salário negativo ou zero)
        if salario_base <= 0:
            print("\n⚠️ ERRO LOGÍSTICO: O salário deve ser maior que zero.")
            print("Registo cancelado. Tente novamente.")
            continue
            
    except ValueError:
        print("\n⚠️ ERRO DE SINTAXE: Digite apenas números com ponto (ex: 1500.50).")
        print("Registo cancelado. Tente novamente.")
        continue 
    
    # Processamento chamando a função (def) isolada lá em cima
    valor_bonus = calcular_bonus(salario_base)
    salario_final = salario_base + valor_bonus
    
    # Saída de Dados Formatada
    print("\n" + "="*42)
    print(f"|{'RESUMO DE CONTRATAÇÃO':^40}|")
    print("="*42)
    
    print(f"| 👤 NOME:    {nome.title():<28} |")
    print(f"| 💼 CARGO:   {cargo.title():<28} |")
    print("-" * 42)
    
    print(f"| 💰 SALÁRIO: R$ {salario_base:<23.2f} |")
    print(f"| 🎁 BÔNUS:   R$ {valor_bonus:<23.2f} |")
    print(f"| 🏆 TOTAL:   R$ {salario_final:<23.2f} |")
    print("="*42)