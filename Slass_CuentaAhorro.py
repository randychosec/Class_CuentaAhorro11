class CuentaAhorro:
    def __init__(self, xtitular, xsaldo = 0):
        self.titular = xtitular
        self.saldo = xsaldo

    def depositar(self, xmonto):
        if xmonto >= 0:
            self.saldo += xmonto
            print(f"Su saldo actual es: { self.saldo }")
        else:
            print(f"El monto {xmonto} no puede ser depositado.")

    def retirar(self, xmonto):
        if self.saldo < xmonto:
            print(f"El monto a retirar { xmonto } es superior al saldo.")
        else:
            self.saldo -= xmonto
            print(f"Su saldo actual es: { self.saldo }")

    def cuenta(self):
        print(f"La cuenta del sr(a): {self.titular} tiene un saldo {self.saldo}.")



operacion = True

nombre_titular = input("Ingrese un titular: ")
cuenta1 = CuentaAhorro(nombre_titular)

while operacion == True:
    print("***/Menú de Operaciones /***")
    # print(" 1, para ingresar titular ")
    print(" 2, para depositar ")
    print(" 3, para retirar ")
    print(" 4, para imprimir cuenta ")
    print(" 9, para salir ")
    print("***//////////////////////***")

    opcion = int(input("Ingrese opción: "))
    # if opcion == 1:
    if opcion == 2:
        ingresar_deposito = int(input("Ingrese el monto a depositar: "))
        cuenta1.depositar(ingresar_deposito)
    if opcion == 3:
        retirar_saldo = int(input("Ingrese el monto a retirar: "))
        cuenta1.retirar(retirar_saldo)
    if opcion ==  4:
        cuenta1.cuenta()
    if opcion == 9:
        print("Programa finalizado")
        operacion = False
