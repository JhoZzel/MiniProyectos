import random

class Aleatorio:
    def __init__(self, semilla):
        self.semilla = semilla
        self.multiplicador = pow(7, 5)
        self.modulo = 2 ** 31 - 1

    def siguiente(self):
        self.semilla = (self.semilla * self.multiplicador) % self.modulo
        return self.semilla

    def elegir(self, limite):
        numero_aleatorio = self.siguiente()
        nuevo_entero = numero_aleatorio % limite
        return nuevo_entero


class Regla:
    def __init__(self, izquierda, derecha):
        self.left = izquierda
        self.right = tuple(derecha)
        self.cont = 1

    def __repr__(self):
        right_str = ' '.join(self.right)
        return f'{self.cont} {self.left} -> {right_str}'


class Gramatica:
    def __init__(self, semilla):
        self.generador = Aleatorio(semilla)
        self.reglas = {}

    def regla(self, izquierda, derecha):
        if izquierda not in self.reglas:
            self.reglas[izquierda] = [derecha]
        else:
            self.reglas[izquierda].append(derecha)

    def generar(self):
        if '<inicio>' not in self.reglas:
            raise Exception("No existe una regla para '<inicio>'")
        return self.generando(('<inicio>',))

    def generando(self, strings):
        resultado = ""
        for cadena in strings:
            if cadena not in self.reglas:
                resultado += cadena + " "
            else:
                nuevas_cadenas = self.seleccionar(cadena)
                nueva_generada = self.generando(nuevas_cadenas)
                resultado += nueva_generada
        return resultado

    def seleccionar(self, left):
        reglas = self.reglas[left]
        total = len(reglas)
        indice = self.generador.elegir(total)
        return reglas[indice]

#-----------------------------------------------------

# semilla = random.randint(1, 100)
gramatica = Gramatica(1)

gramatica.regla("<inicio>", ["<historia>"])
gramatica.regla("<historia>", ["<frase>"])
gramatica.regla("<historia>", ["<frase>", "y", "<historia>"])
gramatica.regla("<historia>", ["<frase>", "sino", "<historia>"])
gramatica.regla("<frase>", ["<articulo>", "<sustantivo>", "<verbo>", "<articulo>", "<sustantivo>"])
gramatica.regla("<articulo>", ["el"])
gramatica.regla("<articulo>", ["la"])
gramatica.regla("<articulo>", ["al"])
gramatica.regla("<sustantivo>", ["gato"])
gramatica.regla("<sustantivo>", ["niño"])
gramatica.regla("<sustantivo>", ["perro"])
gramatica.regla("<sustantivo>", ["niña"])
gramatica.regla("<verbo>", ["perseguia"])
gramatica.regla("<verbo>", ["besaba"])

# Generar frase aleatoria
frase_generada = gramatica.generar()
print(frase_generada)
