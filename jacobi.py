import random #Se usa para generar el número aleatorio
import re     #Se usa para validar el string equations
import numpy as np
class Jacobi:
    def __init__(self):
        pass

    #Solicita el tamaño de la matriz al usuario
    def getSize(self):
        n = input("\n¿Cuántas ecuaciones tiene el problema? (3/4/5): ")
        while n != "3" and n != "4" and n != "5":
            n = input("\n¡ERROR! Deben ser 3, 4 o 5 ecuaciones. ¿Cuántas ecuaciones tiene el problema? (3/4/5): ")
        return int(n)

    #Evalúa el formato ingresado de los valores de la matriz 
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

    #Imprime un ejemplo de ingreso de valores
    def createExample(self, n):
        if n == 3:
            example = "AX1 + BX2 + Cx3 = 0;"
        elif n == 4:
            example = "AX1 + BX2 + CX3 + DX4 = 0;"
        elif n == 5:
            example = "AX1 + BX2 + CX3 + DX4 + EX5 = 0;"
        return example

    #Solicita los valores para armar la matriz
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

    #A partir de el string generado en getData() se crea la matriz A
    def createMatrix(self, equations):
        matrix = []
        for equation in equations:
            coefficient = equation.rstrip(";").split()
            row = [int(numero) for numero in coefficient]
            matrix.append(row)
        return matrix

    #Imprime la matriz que recibe por parámetro
    def printMatrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))
    
    #Genera números aleatorios
    def randomNum(self):
        return random.randint(-9, 9)
    
    #Crea una matriz con números aleatorios
    def createRandomMatrix(self, n):
        matrix = []
        for i in range(n):
            row = [self.randomNum() for i in range(n)]
            matrix.append(row)
        #print(matrix)
        return matrix

    #Retorna True si la matriz es EDD
    def isEDD(self, matrix):
        n = len(matrix)
        for i in range(n):
            diagonal = abs(matrix[i][i])
            sumOutsideDiagonal = sum(abs(matrix[i][j]) for j in range(n) if j != i)
            if diagonal <= sumOutsideDiagonal:
                return False
        return True

    #Si la matriz no es EDD, intercambia filas hasta que lo sea
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
        print("\nNo se pudo convertir la matriz en una EDD.")
        return matrix
    
    #Solicita al usuario los valores para la matriz b (términos independientes)
    def getB(self, n):
        equation = []
        nums = input(f"Ingrese los terminos independientes en el orden: ")
        while not self.evaluateFormat(nums, n):
            nums = input(f"ERROR, recuerde ingresar los numeros seguidos de un espacio y terminar con un punto y coma (;)\nIngrese los terminos independientes en el orden: ")
        equation.append(nums)
        equation = self.createMatrix(equation)
        return equation[0]
    
    def getX0(self, n):
        x0 = []
        while len(x0) != n:
            x0.append(0)
        return x0
    
    #Realiza la sucesión de Jacobi
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

            print(f"Iteracion {iteration + 1}:")
            print(f"x{iteration + 1} = ----------->", x)
            print(f"x{iteration} previa usada= ", x_prev)
            print("Tolerancia Actual =", diff_norm)
            print("----------------------------------------------------------------------------------")

            if diff_norm < tolerance:
                break
    
        return x
    
    #Imrpime la matriz A
    def printMatrixA(self, matrix):
        print("\n*****MATRIZ A*****")
        self.printMatrix(matrix)

    #Imrpime la matriz B
    def printMatrixB(self, matrixB):
        print("\n*****MATRIZ b*****")
        for value in matrixB:
            print("[   "+ str(value) +  "   ]")
    
    #Crea la matriz D
    def createMatrixD(self, matrix):
        n_rows = len(matrix)
        n_columns = len(matrix[0]) if matrix else 0
        min_dimension = min(n_rows, n_columns)
        matrixD = []
        for i in range(min_dimension):
            fila_diagonal = [0] * i + [matrix[i][i]] + [0] * (min_dimension - i - 1)
            matrixD.append(fila_diagonal)
        return matrixD
    
    #Imrpime la matriz D
    def printMatrixD(self, matrix):
        matrixD = self.createMatrixD(matrix)
        print("\n*****MATRIZ D*****")
        self.printMatrix(matrixD)

    #Crea la matriz R
    def createMatrixR(self, matrix):
        matrixR = []
        for i in range(len(matrix)):
            fila = []
            for j in range(len(matrix[i])):
                if i == j:
                    fila.append(0)  # Reemplazar diagonal con cero
                else:
                    fila.append(matrix[i][j])  # Mantener el mismo elemento
            matrixR.append(fila)
        return matrixR
    
    #Imrpime la matriz R
    def printMatrixR(self, matrix):
        matrixR = self.createMatrixR(matrix)
        print("\n*****MATRIZ R*****")
        self.printMatrix(matrixR)


    def matrixInverse(self, matrix):
        try:
            inversa = np.linalg.inv(matrix)
            return inversa
        except np.linalg.LinAlgError:
            print("La matriz no es invertible.")
            return None 

    def matrixTranspose(self, matrix):
        n = len(matrix)
        transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
        return transpose 

    def isCreatedMatrix(self, matrix):
        if matrix == None:
            print("Por favor, cree una matriz con la opción 1 o 2 antes de intentar esto.")
            return False
        return True