from clear import clear

on_start = True
while on_start:
    caractere = input("Digite uma letra: ")

    def convert(caractere):
        decimal = ord(caractere)
        hexadecimal = hex(decimal)
        binario = bin(decimal)
        return print(f'A letra digitado foi: {caractere}. \nSeu valor em DECIMAL é: {decimal}. \nSeu valor em HEXADECIMAL é {hexadecimal}. \nSeu valor em binário é {binario}.')

    print(convert(caractere))
    continuar = str(input("Deseja converter novamente? [S/N] ").upper())
    if continuar == 'N':
        print("Até mais!🚀👨🏻‍💻")
        on_start = False
    clear()
