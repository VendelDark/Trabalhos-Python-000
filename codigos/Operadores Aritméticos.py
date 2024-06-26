import math
# 1. Mostrar o sucessor e o antecessor de um número inteiro

def mostrar_sucessor_antecessor():
    numero = int(input("Digite um número inteiro: "))
    sucessor = numero + 1
    antecessor = numero - 1
    print(f"O sucessor de {numero} é {sucessor} e o antecessor é {antecessor}.")

mostrar_sucessor_antecessor()


# 2. Mostrar o dobro, o triplo e a raiz quadrada de um número

def calcular_dobro_triplo_raiz():
    numero = float(input("\nDigite um número: "))
    dobro = numero * 2
    triplo = numero * 3
    raiz_quadrada = math.sqrt(numero)
    print(f"O dobro de {numero} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz_quadrada}.")

calcular_dobro_triplo_raiz()


# 3. Calcular a média de duas notas

def calcular_media():
    nota1 = float(input("\nDigite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média das notas {nota1} e {nota2} é {media}.")

calcular_media()


# 4. Converter metros em centímetros

def converter_metros_centimetros():
    metros = float(input("\nDigite o valor em metros: "))
    centimetros = metros * 100
    print(f"{metros} metros equivalem a {centimetros} centímetros.")

converter_metros_centimetros()


# 5. Converter dólares em reais

def converter_dolar_real():
    dolares = float(input("\nDigite o valor em dólares: "))
    taxa_cambio = float(input("Digite a taxa de câmbio atual: "))
    reais = dolares * taxa_cambio
    print(f"O valor de {dolares} dólares é equivalente a {reais} reais.")

converter_dolar_real()


# 6. Calcular 10% de aumento em um salário

def calcular_aumento_salario():
    salario = float(input("\nDigite o salário do funcionário: "))
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O novo salário após o aumento de 10% é {novo_salario}.")

calcular_aumento_salario()



if __name__ == "__main__":
    mostrar_sucessor_antecessor()
    calcular_dobro_triplo_raiz()
    calcular_media()
    converter_metros_centimetros()
    converter_dolar_real()
    calcular_aumento_salario()