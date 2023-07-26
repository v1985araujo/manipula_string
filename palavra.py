def manipular_palavra(palavra:str, letra:str, posicao:int) -> str:
    """
    Esse função vai trocar a letra de uma plalavra em uma dada posição, começando de 1
    :param letra: uma ou mais letras a ser(em) colocada(s) na palavra
    :param posicao: a posição da letra a ser alterada
    :param palavra: a string a ser mexida
    :return: a palavra com a alteração feita
    """
    string = palavra[:int(posicao) - 1]
    string += letra
    string += palavra[int(posicao):]

    return string

# A maior palavra em língua portuguesa: pneumoultramicroscopicossilicovulcanoconiótico
num = [str(x) for x in range(1, 47)]

pos = 0
palavra = input("Digite uma palavra: ")
letra = input(f"Qual a letra que vai entrar na {palavra}? ")

while pos not in num:
    pos = input(f"Qual a posição da {palavra} que vai ser alterada? ")
    if pos not in num:
        print(f"Esse dado precisa estar entre 1 e {len(palavra)}")


if(int(pos) <= len(palavra)):
    string = manipular_palavra(palavra, letra, int(pos))

else:
    string = f"A posição {pos} não existe em {palavra}!"

print(string)