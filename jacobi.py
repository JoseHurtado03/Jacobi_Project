import random

class Jacobi:
    def __init__(self):
        pass

    def getSize(self):
        n = input("\n¿Cuántas ecuaciones tiene el problema? (3/4/5): ")
        while n != "3" and n != "4" and n != "5":
            n = input("\n¡ERROR! Deben ser 3, 4 o 5 ecuaciones. ¿Cuántas ecuaciones tiene el problema? (3/4/5): ")
        return int(n)

    def evaluateFormat(self, equations, n):
        if not equations.endswith(";"):
            return False
        numeros = equations.rstrip(";").split()
        if len(numeros) != n:
            return False
        if not all(caracter.isdigit() for caracter in numeros):
            return False
        return True

    def createExample(self, n):
        if n == 3:
            example = "Ax + By + C = 0;"
        elif n == 4:
            example = "Ax + By + Cz + D = 0;"
        elif n == 5:
            example = "Ax + By + Cz + Ds + E = 0;"
        return example

    def getData(self, n):
        aux = n
        equations = []
        numEcu = 1
        example = self.createExample(n)
        while aux != 0:
            equation = input(f"Ingrese los coeficientes de la ecuación {numEcu} en el orden {example}: ")
            while not self.evaluateFormat(equation, n):
                equation = input(f"ERROR, recuerde ingresar los numeros seguidos de un espacio y terminar con un punto y coma (;)\nIngrese los coeficientes de la ecuación {numEcu} en el orden {example}: ")
            equations.append(equation)
            numEcu += 1
            aux -= 1
        return equations

    def createMatrix(self, equations):
        matrix = []
        for equation in equations:
            coefficient = equation.rstrip(";").split()
            row = [int(numero) for numero in coefficient]
            matrix.append(row)
        return matrix

    def printMatrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))
    
    def randomNum(self):
        return random.randint(0, 9)
    
    def createRandomMatrix(self, n):
        matrix = []
        for i in range(n):
            row = [self.randomNum() for i in range(n)]
            matrix.append(row)
        return matrix

    def isEDD(self, matrix):
        n = len(matrix)
        for i in range(n):
            diagonal = abs(matrix[i][i])
            sumOutsideDiagonal = sum(abs(matrix[i][j]) for j in range(n) if j != i)
            if diagonal <= sumOutsideDiagonal:
                return False
        return True

    def changeRowsToEDD(self, matrix):
        if self.isEDD(matrix):
            return matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                newMatrix = matrix[:]
                newMatrix[i], newMatrix[j] = newMatrix[j], newMatrix[i]
                if self.isEDD(newMatrix):
                    return newMatrix
        print("No se pudo convertir la matriz en una EDD.")
        return matrix