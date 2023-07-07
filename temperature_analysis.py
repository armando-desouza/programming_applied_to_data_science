temperature_user = int(input("Por favor, digite a temperatura atual: °C "))
if temperature_user < 7:
    print('Congelando🥶🌨️! Use casaco🧥.')
elif temperature_user < 10:
    print('Frio☃️! É bom preparar o gorro❄️.')
elif temperature_user < 26:
    print('Ótimo😄! A temperatura está boa para uma corrida🏃🏻‍♂️')
else:
    print('Muito quente🥵! Já pegar a camiseta🎽.')