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
            example = "AX1 + BX2 + Cx3 = 0;"
        elif n == 4:
            example = "AX1 + BX2 + CX3 + DX4 = 0;"
        elif n == 5:
            example = "AX1 + BX2 + CX3 + DX4 + EX5 = 0;"
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
        return random.randint(-9, 9)
    
    def createRandomMatrix(self, n):
        matrix = []
        for i in range(n):
            row = [self.randomNum() for i in range(n)]
            matrix.append(row)
        #print(matrix)
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
        #print("\nNo se pudo convertir la matriz en una EDD.")
        return False
    
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
    
    def printMatrixA(self, matrix):
        print("\nA =     ")
        self.printMatrix(matrix)

    def printMatrixB(self, matrixB):
        print("\nb =     ")
        for value in matrixB:
            print("[   "+ str(value) +  "   ]")
    
    def createMatrixD(self, matrix):
        n_rows = len(matrix)
        n_columns = len(matrix[0]) if matrix else 0
        min_dimension = min(n_rows, n_columns)
        matrixD = []
        for i in range(min_dimension):
            fila_diagonal = [0] * i + [matrix[i][i]] + [0] * (min_dimension - i - 1)
            matrixD.append(fila_diagonal)
        return matrixD
    
    def printMatrixD(self, matrix):
        matrixD = self.createMatrixD(matrix)
        print("\nD =     ")
        self.printMatrix(matrixD)

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
    
    def printMatrixR(self, matrix):
        matrixR = self.createMatrixR(matrix)
        print("\nR =     ")
        self.printMatrix(matrixR)


    def matrix_inverse(self, matrix):
        n = len(matrix)

        # Crear una matriz identidad del mismo tamaño que la matriz original
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        # Convertir la matriz original en una matriz triangular superior
        for i in range(n):
            if matrix[i][i] == 0:
                # Si el elemento diagonal es cero, intercambiar filas con una fila no nula
                for j in range(i + 1, n):
                    if matrix[j][i] != 0:
                        matrix[i], matrix[j] = matrix[j], matrix[i]
                        identity[i], identity[j] = identity[j], identity[i]
                        break

            pivot = matrix[i][i]
            for j in range(i, n):
                matrix[i][j] /= pivot
            for j in range(n):
                identity[i][j] /= pivot

            for k in range(i + 1, n):
                factor = matrix[k][i]
                for j in range(i, n):
                    matrix[k][j] -= factor * matrix[i][j]
                for j in range(n):
                    identity[k][j] -= factor * identity[i][j]

        # Convertir la matriz triangular superior en una matriz identidad
        for i in range(n - 1, 0, -1):
            for k in range(i - 1, -1, -1):
                factor = matrix[k][i]
                for j in range(n):
                    identity[k][j] -= factor * identity[i][j]

        return identity  

    def matrix_transpose(self, matrix):
        n = len(matrix)
        transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
        return transpose 
    
    def imprimir_matriz_traspuesta(self, matriz):
        """
        Imprime la transpuesta de la matriz dada.
        """
        for i in range(len(matriz[0])):
            for j in range(len(matriz)):
                print(matriz[j][i], end=" ")
            print()