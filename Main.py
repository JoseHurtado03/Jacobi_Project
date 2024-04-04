from jacobi import Jacobi

class Main:
    def main():
        jacobi = Jacobi()
        matrix = None
        n = 0
        while True:
            option = input("\n*****SUCESIÓN JACOBI*****\n\n1- Crear matriz\n2- Crear matriz aleatoria\n3- Resolver sistema por Jacobi\n4- Ver traspuesta e inversa de la matriz\n5- Descomposición LU\n6- Salir\n--> ")
            
            if option == "1":
                n= jacobi.getSize()
                matrix = jacobi.createMatrix(jacobi.getData(n))
                jacobi.printMatrixA(matrix)

            elif option == "2":
                n = jacobi.getSize()
                matrix = jacobi.createRandomMatrix(n)
                jacobi.printMatrixA(matrix)

            elif option == "3":
                if jacobi.isCreatedMatrix(matrix):
                    matrixJ = jacobi.changeRowsToEDD(matrix)
                    if jacobi.isEDD(matrixJ):
                        print("\n*****Matriz EDD*****")
                        jacobi.printMatrix(matrixJ)
                        matrixB = jacobi.getB(len(matrix))
                        result = jacobi.makejacobi(matrixJ,matrixB,jacobi.getX0(len(matrixJ)),max_iterations=100, tolerance=1e-6)
                        input("ENTER para ver los resultados finales")
                        jacobi.printMatrixA(matrixJ)
                        jacobi.printMatrixB(matrixB)
                        jacobi.printMatrixD(matrixJ)
                        jacobi.printMatrixR(matrixJ)
                        print("Solución:", result)
                        input("PRESIONE ENTER PARA VOLVER AL MENÚ")

            elif option == "4":
                if jacobi.isCreatedMatrix(matrix):
                    print("\n*****MATRIZ TRASPUESTA*****")
                    traspose = jacobi.matrixTranspose(matrix)
                    jacobi.printMatrix(traspose)
                    print("\n*****MATRIZ INVERSA*****")
                    inverse = jacobi.matrixInverse(matrix)
                    jacobi.printMatrix(inverse)
                    input("\nPRESIONE ENTER PARA CONTINUAR Y VOLVER AL MENÚ")

            elif option == "5":
                if jacobi.isCreatedMatrix(matrix):
                    matrixL, matrixU = jacobi.convertLU(matrix, n)
                    if matrixL is None or matrixU is None or not matrixL.any() or not matrixU.any():
                        print("La matriz no puede ser convertida a LU")
                    else:
                        print("\n*****MATRIZ L*****")
                        jacobi.printMatrix(matrixL)
                        print("\n*****MATRIZ U*****")
                        jacobi.printMatrix(matrixU)
            
            elif option == "6":
                break
            else:
                print("\n¡ERROR! Marque el número correspondiente a la opción que desea realizar.")
Main.main()