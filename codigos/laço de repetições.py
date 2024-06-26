#1

import sqlite3
from faker import Faker

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('dados_fake.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    endereco TEXT,
                    email TEXT
                )''')


fake = Faker()


quantidade_dados = 100


for _ in range(quantidade_dados):
    nome = fake.name()
    endereco = fake.address()
    email = fake.email()
    

    cursor.execute("INSERT INTO usuarios (nome, endereco, email) VALUES (?, ?, ?)", (nome, endereco, email))


conn.commit()


conn.close()

print("Dados falsos foram inseridos no banco de dados com sucesso!")


#2

def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        while numero > 0:
            fatorial *= numero
            numero -= 1
        return fatorial

def main():
    while True:
        try:
            numero = int(input("Digite um número para calcular o fatorial (ou digite 0 para sair): "))
            if numero == 0:
                print("Encerrando o programa.")
                break
            resultado = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {resultado}")
        except ValueError:
            print("Por favor, digite um número que seja válido.")

if _name_ == "_main_":
    main()


#3

def obter_sexo():
    while True:
        sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper()
        if sexo == 'M' or sexo == 'F':
            return sexo
        else:
            print("Sexo inválido. Por favor, digite apenas M para Masculino ou F para Feminino.")

def main():
    sexo = obter_sexo()
    print(f"Sexo selecionado: {sexo}")

if _name_ == "_main_":
    main()


#4

def soma(num1, num2):
    return num1 + num2

def multiplicacao(num1, num2):
    return num1 * num2

def qual_e_maior(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Os números são iguais."

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    while True:
        print("\nMenu de Opções:")
        print("1 - Soma")
        print("2 - Multiplicação")
        print("3 - Qual é Maior")
        print("4 - Digitar novos números")
        print("5 - Sair do Programa")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Resultado da soma:", soma(num1, num2))
        elif opcao == 2:
            print("Resultado da multiplicação:", multiplicacao(num1, num2))
        elif opcao == 3:
            print("O maior número é:", qual_e_maior(num1, num2))
        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        elif opcao == 5:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if _name_ == "_main_":
    main()

#5

def calcular_altura_piramide(blocos):
    altura = 0
    blocos_na_camada = 1
    
    while blocos >= blocos_na_camada:
        altura += 1
        blocos -= blocos_na_camada
        blocos_na_camada += 1
    
    return altura

def main():
    try:
        blocos = int(input("Digite o número de blocos: "))
        altura = calcular_altura_piramide(blocos)
        print("Altura da pirâmide:", altura)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if _name_ == "_main_":
    main()

#6

import time

def contagem_regressiva():
    for i in range(5, -1, -1):
        print(i)
        time.sleep(1)

    print("Feliz Ano Novo!")

def main():
    print("Contagem regressiva para o Ano Novo:")
    contagem_regressiva()

if _name_ == "_main_":
    main()


#7

def numeros_pares():
    for numero in range(2, 101, 2):
        print(numero)

def main():
    print("Números pares de 1 a 100:")
    numeros_pares()

if _name_ == "_main_":
    main()



#8

def soma_impares_multiplos_de_3():
    soma = 0
    for numero in range(1, 501, 2): 
        if numero % 3 == 0:  
            soma += numero

    return soma

def main():
    soma = soma_impares_multiplos_de_3()
    print("A soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500 é:", soma)

if _name_ == "_main_":
    main()


#9

def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    try:
        numero = int(input("Digite um número para ver toda a sua tabuada: "))
        tabuada(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if _name_ == "_main_":
    main()


#10

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    try:
        numero = int(input("Digite um número para verificar se é primo: "))
        if verificar_primo(numero):
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if _name_ == "_main_":
    main()


#11


from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    menores = 0
    maiores = 0

    for i in range(1, 7):
        try:
            ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
            idade = calcular_idade(ano_nascimento)
            if idade < 18:
                menores += 1
            else:
                maiores += 1
        except ValueError:
            print("Por favor, digite um ano de nascimento válido.")

    print(f"\n{menores} pessoas são menores de idade.")
    print(f"{maiores} pessoas são maiores de idade.")

if _name_ == "_main_":
    main()

#12

def main():
    pesos = []

    for i in range(1, 6):
        try:
            peso = float(input(f"Digite o peso da pessoa {i} em kg: "))
            pesos.append(peso)
        except ValueError:
            print("Por favor, digite um peso válido.")

    if len(pesos) > 0:
        mais_pesado = max(pesos)
        mais_leve = min(pesos)
        print(f"\nO mais pesado pesa {mais_pesado} kg.")
        print(f"O mais leve pesa {mais_leve} kg.")
    else:
        print("Nenhum peso válido foi inserido.")

if _name_ == "_main_":
    main()

#13

def main():
    total_idades = 0
    idade_homens = []
    mulheres_menos_de_20 = 0
    nome_homem_mais_velho = ""
    idade_homem_mais_velho = 0

    for i in range(1, 7):
        print(f"\nDados da pessoa {i}:")
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

        total_idades += idade

        if sexo == 'M':
            idade_homens.append(idade)
            if idade > idade_homem_mais_velho:
                idade_homem_mais_velho = idade
                nome_homem_mais_velho = nome
        elif sexo == 'F' and idade < 20:
            mulheres_menos_de_20 += 1

    if len(idade_homens) > 0:
        media_idade = total_idades / len(idade_homens)
        print(f"\nA média de idade dos homens é: {media_idade:.2f}")
    else:
        print("\nNenhum homem foi registrado.")

    print(f"O homem mais velho é {nome_homem_mais_velho} e tem {idade_homem_mais_velho} anos.")

    print(f"Existem {mulheres_menos_de_20} mulheres com menos de 20 anos.")

if _name_ == "_main_":
    main()


#14

import getpass

def jogar_forca():
    print("Bem-vindo! Vamos jogar Forca!")
    
    # Solicita a palavra secreta sem mostrar na tela
    palavra_secreta = getpass.getpass("Digite a palavra secreta: ").lower()
    
    # Cria uma lista de letras adivinhadas, iniciando com '_'
    letras_adivinhadas = ['_' for _ in palavra_secreta]
    
    tentativas_restantes = 6
    letras_erradas = []

    while tentativas_restantes > 0 and '_' in letras_adivinhadas:
        print("\nPalavra secreta:", ' '.join(letras_adivinhadas))
        print("Letras erradas:", ' '.join(letras_erradas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        
        # Solicita uma letra do usuário
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_adivinhadas or letra in letras_erradas:
            print("Você já tentou essa letra. Por favor, tente colocar outra.")
            continue

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_adivinhadas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1

    # Verifica se o jogador ganhou ou perdeu
    if '_' not in letras_adivinhadas:
        print("\nParabéns! Você ganhou! A palavra secreta era:", palavra_secreta)
    else:
        print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)

def main():
    jogar_forca()

if __name__ == "__main__":
    main()

#15

def substituir_zeros(numero):
    numero_formatado = ""
    for digito in numero:
        if digito == '0':
            numero_formatado += 'ex'
        else:
            numero_formatado += digito
    return numero_formatado

def main():
    try:
        numero = input("Digite um número de 14 dígitos: ")
        if len(numero) != 14 or not numero.isdigit():
            print("O número deve ter 14 dígitos.")
        else:
            numero_formatado = substituir_zeros(numero)
            print("Número formatado:", numero_formatado)
    except ValueError:
        print("Por favor, digite um número válido.")

if _name_ == "_main_":
    main()
