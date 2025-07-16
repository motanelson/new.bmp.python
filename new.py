
from PIL import Image
#pip install pillow
# Dicionário com as cores VGA (0-15)
VGA_COLORS = [
    (0x00, 0x00, 0x00),  # 0 - Preto
    (0x00, 0x00, 0xAA),  # 1 - Azul
    (0x00, 0xAA, 0x00),  # 2 - Verde
    (0x00, 0xAA, 0xAA),  # 3 - Ciano
    (0xAA, 0x00, 0x00),  # 4 - Vermelho
    (0xAA, 0x00, 0xAA),  # 5 - Magenta
    (0xAA, 0x55, 0x00),  # 6 - Castanho
    (0xAA, 0xAA, 0xAA),  # 7 - Cinzento claro
    (0x55, 0x55, 0x55),  # 8 - Cinzento escuro
    (0x55, 0x55, 0xFF),  # 9 - Azul claro
    (0x55, 0xFF, 0x55),  # 10 - Verde claro
    (0x55, 0xFF, 0xFF),  # 11 - Ciano claro
    (0xFF, 0x55, 0x55),  # 12 - Vermelho claro
    (0xFF, 0x55, 0xFF),  # 13 - Magenta claro
    (0xFF, 0xFF, 0x55),  # 14 - Amarelo
    (0xFF, 0xFF, 0xFF),  # 15 - Branco
]

def main():
    # Pedir dados ao utilizador
    try:
        largura = int(input("Introduz a largura da imagem (px): "))
        altura = int(input("Introduz a altura da imagem (px): "))
        cor_index = int(input("Introduz o índice da cor VGA (0 a 15): "))
    except ValueError:
        print("Erro: por favor introduz apenas números inteiros.")
        return

    if not (0 <= cor_index < 16):
        print("Erro: a cor deve estar entre 0 e 15.")
        return

    # Obter cor em formato RGB
    r, g, b = VGA_COLORS[cor_index]

    # Criar a imagem (RGBA, 32 bits)
    img = Image.new("RGBA", (largura, altura), (r, g, b, 255))

    # Gravar a imagem
    img.save("new.bmp", "BMP")
    print("Imagem 'new.bmp' criada com sucesso.")
print("\033c\033[43;30m\n")
if __name__ == "__main__":
    main()
