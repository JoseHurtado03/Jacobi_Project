from Jacobi import Jacobi

class Main:
    def main():
        jacobi = Jacobi()
        while True:
            print("\n*****MÉTODO JACOBI*****\n")
            option = input("¿Cómo deseas crear la matriz?\n1- Crear matriz con números al azar\n2- Crear matriz ingresando los coeficientes\n3- Salir \n-->")
            while option != "1" and option != "2" and option != "3":
                option = input("¡ERROR! ¿Cómo deseas crear la matriz? (1/2)\n1- Crear matriz con números al azar\n2- Crear matriz ingresando los coeficientes\n3- Salir \n-->")
            if option == "1":
                matrix = jacobi.createRandomMatrix(jacobi.getSize())
                jacobi.printMatrix(matrix)
                matrix = jacobi.changeRowsToEDD(matrix)
                jacobi.printMatrix(matrix)
            elif option == "2":
                matrix = jacobi.createMatrix(jacobi.getData(jacobi.getSize()))
                jacobi.printMatrix(matrix)
                matrix = jacobi.changeRowsToEDD(matrix)
                jacobi.printMatrix(matrix)
            elif option == "3":
                break
Main.main()
