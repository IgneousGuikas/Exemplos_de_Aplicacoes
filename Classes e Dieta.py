
class Alimento(object):
    '''
    Representa um alimento e seus valores nutricionais
    '''
    
    def __init__(self, nutrientes):
        self.porcao = int(nutrientes[1])
        self.calorias = float(nutrientes[2])
        self.proteinas = float(nutrientes[3])
        self.carboidratos = float(nutrientes[4])
        self.gorduras = float(nutrientes[5])


fin = open('alimentos.csv','r', encoding='utf-8')

fin.readline()

middle = fin.readlines()
fin.close()


catalogo = dict()
for termo in middle:
    buffer = ''
    nutrientes = termo.strip().split(',')
    catalogo[nutrientes[0]] = Alimento(nutrientes)

print(catalogo)
print(catalogo['ABACATE'].calorias)
