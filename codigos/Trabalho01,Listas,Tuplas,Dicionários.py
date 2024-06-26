from PIL import Image, ImageFilter, ImageEnhance
import os

# Verifica e cria, se necessário, os diretórios de entrada e saída
diretorio_imagens_originais = 'imagens_originais'
diretorio_imagens_modificadas = 'imagens_modificadas'

for diretorio in [diretorio_imagens_originais, diretorio_imagens_modificadas]:
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)


def aplicar_operacoes(imagem, operacoes):
    for operacao, valor in operacoes.items():
        if operacao == 'rotacionar':
            imagem = imagem.rotate(valor)
        elif operacao == 'filtro':
            imagem = imagem.filter(valor)
        elif operacao == 'redimensionar':
            imagem = imagem.resize(valor)
        elif operacao == 'brilho':
            imagem = ImageEnhance.Brightness(imagem).enhance(valor)
        elif operacao == 'contraste':
            imagem = ImageEnhance.Contrast(imagem).enhance(valor)
    return imagem


def selecionar_operacoes():
    operacoes = {}
    print("\nDisponível operações para aplicar na imagem:")
    print("1. Rotacionar")
    print("2. Aplicar Filtro de Desfoque")
    print("3. Redimensionar")
    print("4. Ajustar Brilho")
    print("5. Ajustar Contraste")
    print("6. Finalizar Seleção")

    while True:
        escolha = input("Selecione uma operação (1-6): ")

        if escolha == '1':
            angulo = int(input("Ângulo de rotação (90, 180, 270): "))
            operacoes['rotacionar'] = angulo
        elif escolha == '2':
            # Pode-se expandir para outros filtros solicitando ao usuário
            operacoes['filtro'] = ImageFilter.BLUR
        elif escolha == '3':
            largura = int(input("Largura: "))
            altura = int(input("Altura: "))
            operacoes['redimensionar'] = (largura, altura)
        elif escolha == '4':
            brilho = float(input("Brilho (valores >1 aumentam o brilho, <1 diminuem): "))
            operacoes['brilho'] = brilho
        elif escolha == '5':
            contraste = float(input("Contraste (valores >1 aumentam o contraste, <1 diminuem): "))
            operacoes['contraste'] = contraste
        elif escolha == '6':
            break
        else:
            print("Opção inválida, tente novamente.")

    return operacoes


def processar_imagens():
    imagens = os.listdir(diretorio_imagens_originais)
    for imagem_nome in imagens:
        print(f"\nProcessando '{imagem_nome}'...")
        imagem_path = os.path.join(diretorio_imagens_originais, imagem_nome)
        imagem = Image.open(imagem_path)

        operacoes = selecionar_operacoes()
        imagem_modificada = aplicar_operacoes(imagem, operacoes)

        # Salva a imagem modificada no diretório de saída
        imagem_modificada_path = os.path.join(diretorio_imagens_modificadas, imagem_nome)
        imagem_modificada.save(imagem_modificada_path)
        print(f"Imagem modificada salva em: {imagem_modificada_path}")


if __name__ == "__main__":
    processar_imagens()