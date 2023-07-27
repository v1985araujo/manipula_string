def manipular(palavra:str, posicao:int, letra:str) -> str:
    """
    Esse função vai trocar a letra de uma palavra em uma dada posição, começando de 1
    :param letra: uma ou mais letras a ser(em) colocada(s) na palavra
    :param posicao: a posição da letra a ser alterada
    :param palavra: a string a ser mexida
    :return: a palavra com a alteração feita
    """
    lista = list(palavra)
    lista[posicao - 1] = letra
    string = str(lista)
    string = string.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace(" ", "")

    return string


palavra = input("Digite uma palavra: ")
letra = input(f"Qual a letra que vai entrar na {palavra}? ")
num = [str(x) for x in range(1, len(palavra) + 1)]
pos = 0
while pos not in num:
    pos = input(f"A posição de {palavra} que vai ser alterada? ")
    if pos not in num:
        print(f"Esse dado precisa estar entre 1 e {len(palavra)}")


print(manipular(palavra, int(pos), letra))