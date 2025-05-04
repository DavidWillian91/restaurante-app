import sys
sys.path.append('/storage/emulated/0/modelos/restauranteoo.py')

from restauranteoo import Restaurante

# Criação dos objetos
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

# Função principal
def main():
    Restaurante.listar_restaurantes()

# Ponto de entrada do programa
if __name__ == '__main__':
    main()