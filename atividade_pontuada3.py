import os

os.system("clear")

def login():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    print("\nLogin realizado com sucesso!\n")
    return matricula

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04

def calcular_irrf(base_calculo, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo -= deducao_dependentes

    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def main():
    print("=== Sistema de Folha de Pagamento ===")
    login()

    salario_base = float(input("Informe seu salário base (R$): "))
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower() == 's'
    valor_vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
    dependentes = int(input("Informe a quantidade de dependentes: "))

    # Descontos
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base - desconto_inss, dependentes)
    desconto_vt = salario_base * 0.06 if vale_transporte else 0
    desconto_vr = valor_vale_refeicao * 0.20
    desconto_saude = dependentes * 150.00

    total_descontos = desconto_inss + desconto_irrf + desconto_vt + desconto_vr + desconto_saude
    salario_liquido = salario_base - total_descontos

    print("\n--- Demonstrativo de Pagamento ---")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {desconto_saude:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
