import matplotlib.pyplot as plt
from math import pi, cos, sin

class Circulo:
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio

    def desenhar_circulo(self):
        angulos = [i * 2 * pi / 360 for i in range(361)]
        coordenadas_x = [self.x + self.raio * cos(angulo) for angulo in angulos]
        coordenadas_y = [self.y + self.raio * sin(angulo) for angulo in angulos]

        plt.plot(coordenadas_x, coordenadas_y)
        plt.axis('equal')
        plt.show()

    def area_do_circulo(self):
        return pi * self.raio**2

    def comprimento_da_circuferencia(self):
        return 2 * pi * self.raio
    
    def mudar_posicao_plano_cartesiano(self, novo_x, novo_y, novo_raio):
        self.x = novo_x
        self.y = novo_y
        self.raio = novo_raio

x = float(input('X: '))
y = float(input('Y: '))
raio = float(input('RAIO: '))

circulo = Circulo(x, y, raio)

desenhar_circulo = circulo.desenhar_circulo()
area_do_circulo = circulo.area_do_circulo()
perimetro = circulo.comprimento_da_circuferencia()

print(desenhar_circulo)
print(f' Área do Circulo: {area_do_circulo:2f} , Perimetro: {perimetro:2f}')
