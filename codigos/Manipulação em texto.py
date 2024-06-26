def analyze_name():
    full_name = input("Please enter your full name: ")
    names.append(full_name)

    # Deixa em maiúsculo
    uppercase_name = full_name.upper()
    print("Todas as letras maiúsculas:", uppercase_name)

    # Em minúsculo
    lowercase_name = full_name.lower()
    print("Todas as letras minúsculas:", lowercase_name)

    # quantidade s/espaço
    num_letters = len(full_name) - full_name.count(' ')
    print("Quantas letras tem o nome desconsiderando os espaços:", num_letters)

    # Quantidade de letras no primeiro nome
    first_name = full_name.split()[0]
    num_first_name_letters = len(first_name)
    print("Quantas letras tem o primeiro nome:", num_first_name_letters)

    # Verifica se tem ou não a no nome
    letter_to_check = 'a'
    if letter_to_check in full_name:
        print(f"A letra '{letter_to_check}' aparece no nome.")
    else:
        print(f"A letra '{letter_to_check}' não aparece no nome.")

    # Quantas vezes aparece 
    num_a = full_name.count('a')
    print(f"A letra 'A' aparece {num_a} vezes no nome.")

    # Posição do A
    first_a_pos = full_name.find('a')
    last_a_pos = full_name.rfind('a')
    print(f"A letra 'A' aparece pela primeira vez na posição {first_a_pos}.")
    print(f"A letra 'A' aparece pela última vez na posição {last_a_pos}.")

    # Primeiro e ultimo nome
    words = full_name.split()
    first_name = words[0]
    last_name = words[-1]
    print(f"O primeiro nome é {first_name} e o último nome é {last_name}.")


if __name__ == "__main__":
    names = []
    while True:
        analyze_name()
        play_again = input("Deseja analisar outro nome? (y/n) ")
        if play_again.lower() != "y":
            break
    print("Nomes anteriores analisados:")
    for name in names:
        print(name)



def verifica_silva(nome_completo):
    # Converte o nome completo para minúsculas para facilitar a comparação
    nome_minusculo = nome_completo.lower()
    # Verifica se "silva" está presente no nome completo
    if 'silva' in nome_minusculo:
        return True
    else:
        return False

# Função para receber o nome completo do usuário
def main():
    nome_completo = input("Digite seu nome completo: ")
    if verifica_silva(nome_completo):
        print("O sobrenome Silva está presente no nome digitado.")
    else:
        print("O sobrenome Silva não está presente no nome digitado.")

if _name_ == "__main__":
    main()