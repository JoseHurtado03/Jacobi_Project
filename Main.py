from jacobi import Jacobi

class Main:
    def main():
        jacobi = Jacobi()
        while True:
            option = input("\n*****MÉTODO JACOBI*****\n\n¿Cómo deseas crear la matriz?\n1- Crear matriz con números al azar\n2- Crear matriz ingresando los coeficientes\n3- Salir \n-->")
            if option == "1":
                size = jacobi.getSize()
                matrix = jacobi.createRandomMatrix(size)
                matrix = jacobi.changeRowsToEDD(matrix)
                while matrix == False:
                    matrix = jacobi.createRandomMatrix(size)
                    matrix = jacobi.changeRowsToEDD(matrix)
                jacobi.printMatrix(matrix)
                matrixB = jacobi.getB(len(matrix))
                result = jacobi.makejacobi(matrix,matrixB,jacobi.getX0(len(matrix)),max_iterations=100, tolerance=1e-6)
                input("PRESIONE ENTER PARA VER LOS RESULTADOS FINALES")
                jacobi.printMatrixA(matrix)
                jacobi.printMatrixB(matrixB)
                jacobi.printMatrixD(matrix)
                jacobi.printMatrixR(matrix)
                print("Solución:", result)
                input("\nPRESIONE ENTER PARA CONTINUAR Y VOLVER AL MENU")

            elif option == "2":
                matrix = jacobi.createMatrix(jacobi.getData(jacobi.getSize()))
                matrix = jacobi.changeRowsToEDD(matrix)
                if matrix != False:
                    jacobi.printMatrix(matrix)

                    matrixB = jacobi.getB(len(matrix))
                    result = jacobi.makejacobi(matrix,matrixB,jacobi.getX0(len(matrix)),max_iterations=100, tolerance=1e-6)
                    input("PRESIONE ENTER PARA VER LOS RESULTADOS FINALES")
                    jacobi.printMatrixA(matrix)
                    jacobi.printMatrixB(matrixB)
                    jacobi.printMatrixD(matrix)
                    jacobi.printMatrixR(matrix)
                    print("Solución:", result)
                    input("\nPRESIONE ENTER PARA CONTINUAR Y VOLVER AL MENU")
                else:
                    print("\nNo se pudo convertir la matriz en una EDD.")
                    input("PRESIONE ENTER PARA VOLVER AL MENÚ")

            elif option == "3":
                break
            else:
                print("\n¡ERROR! Marque el número correspondiente a las opciones disponibles")
Main.main()
