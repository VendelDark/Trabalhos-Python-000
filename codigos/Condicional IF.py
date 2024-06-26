# Pergunta 1: Maior número
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Ambos os números são iguais")

# Pergunta 2: Peso ideal
height = float(input("Digite sua altura em metros: "))
gender = input("Digite seu gênero (M para masculino, F para feminino): ")

if gender.upper() == "M":
    ideal_weight = (72.7 * height) - 58
else:
    ideal_weight = (62.1 * height) - 44.7

print(f"Seu peso ideal é {ideal_weight:.2f} kg")

# Pergunta 3: BMI
weight = float(input("Digite seu peso em kg: "))
height = float(input("Digite sua altura em metros: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Seu BMI é", bmi, "- Você está abaixo do peso.")
elif bmi < 24.9:
    print("Seu BMI é", bmi, "- Você está no peso normal.")
elif bmi < 29.9:
    print("Seu BMI é", bmi, "- Você está acima do peso.")
else:
    print("Seu BMI é", bmi, "- Você está obeso.")

# Pergunta 4: Par, ímpar ou zero
number = int(input("Digite um número: "))

if number == 0:
    print("O número é zero.")
elif number % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
