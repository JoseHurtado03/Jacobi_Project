def getSize():
    n = int(input("\n¿Cuántas ecuaciones tiene el problema? (3/4): "))
    while n != 3 and n != 4:
        n = int(input("\n¡ERROR! Deben ser 3 o 4 ecuaciones. ¿Cuántas ecuaciones tiene el problema? (3/4): "))
    return n

def evaluateFormat(equations, n):
    if not equations.endswith(";"):
        return False
    numeros = equations.rstrip(";").split()
    if len(numeros) != n:
        return False
    if not all(caracter.isdigit() for caracter in numeros):
        return False
    return True

def createExample(n):
    if n == 3:
        example = "Ax + By + C = 0;"
    elif n == 4:
        example = "Ax + By + Cz + D = 0;"
    return example

def getData(n):
    aux = n
    equations = []
    numEcu = 1
    example = createExample(n)
    while aux != 0:
        equation = input(f"Ingrese los coeficientes de la ecuación {numEcu} en el orden {example}: ")
        while not evaluateFormat(equation, n):
            equation = input(f"ERROR, recuerde ingresar los numeros seguidos de un espacio y terminar con un punto y coma (;)\nIngrese los coeficientes de la ecuación {numEcu} en el orden {example}: ")
        equations.append(equation)
        numEcu += 1
        aux -= 1
    return equations

def createMatrix(equations):
    matrix = []
    for equation in equations:
        coefficient = equation.rstrip(";").split()
        row = [int(numero) for numero in coefficient]
        matrix.append(row)
    return matrix

def printMatrix(matrix):
    for fila in matrix:
        print(" ".join(map(str, fila)))

matrix = (createMatrix(getData(getSize())))
printMatrix(matrix)