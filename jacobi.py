import random #Se usa para generar el número aleatorio
import re     #Se usa para validar el string equations
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
        for numero in numeros:
            if not re.match(r'^-?\d+$', numero):
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
    
    def getB(self, n):
        equation = []
        nums = input(f"Ingrese los terminos independientes en el orden: ")
        while not self.evaluateFormat(nums, n):
            nums = input(f"ERROR, recuerde ingresar los numeros seguidos de un espacio y terminar con un punto y coma (;)\nIngrese los terminos independientes en el orden: ")
        equation.append(nums)
        print
        print(equation)
        equation = self.createMatrix(equation)
        print(equation)
        return equation[0]
    
    def getX0(self, n):
        x0 = []
        while len(x0) != n:
            x0.append(0)
        return x0
    
    def makejacobi(self, A, b, x0, max_iterations=100, tolerance=1e-6):
        n = len(A)
        x = list(x0)
    
        for iteration in range(max_iterations):
            x_prev = x[:]
        
            for i in range(n):
                sigma = 0.0
            
                for j in range(n):
                    if j != i:
                        sigma += A[i][j] * x_prev[j]
            
                x[i] = (b[i] - sigma) / A[i][i]
        
            diff_norm = sum((x[i] - x_prev[i]) ** 2 for i in range(n)) ** 0.5
        
            if diff_norm < tolerance:
                break
    
        return x
    
    def printMatrixA(self, matrix):
        print("\nA =     ")
        self.printMatrix(matrix)

    def printMatrixB(self, matrixB):
        print("\nb =     ")
        for value in matrixB:
            print("[   "+ str(value) +  "   ]")