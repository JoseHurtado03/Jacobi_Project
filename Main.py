from Jacobi import Jacobi

class Main:
    def main():
        jacobi = Jacobi()
        print("*****MÉTODO JACOBI*****")
        option = input("¿Cómo deseas crear la matriz?\n1- Crear matriz con números al azar\n2- Crear matriz ingresando los coeficientes\n-->")
        while option != "1" and option != "2":
            option = input("¡ERROR! ¿Cómo deseas crear la matriz? (1/2)\n1- Crear matriz con números al azar\n2- Crear matriz ingresando los coeficientes\n-->")
        if option == "1":
            print("Esa opción aún no está, jeje")
        elif option == "2":
            matrix = jacobi.createMatrix(jacobi.getData(jacobi.getSize()))
            jacobi.printMatrix(matrix)
Main.main()
