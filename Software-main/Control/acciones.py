import sys
sys.path.append("C:/Users/mdjqp/PycharmProjects/Software-main/")
from modelo import conexion as con

def saldos(user):
    saldo = con.consulta_s(user[0][0])
    print(f"\nSaldo disponible: ${saldo}\n")
    
def trans(user):
    saldos(user)
    origen = con.consulta_c(user[0][0])
    destino = int(input("Ingrese el numero de cuenta a tranferir:\n>"))
    accion = 'TRANSFERENCIA'
    monto = input("Ingrese el monto a transferir:\n>")
    mensaje = con.movimientos(user[0][0], origen, destino, accion, monto)
    print(f"\n\n{mensaje}\n\n")
    
def trans_2(user):
    origen = int(input("Ingrese el numero de cuenta del titular:\n>"))
    destino = int(input("Ingrese el numero de cuenta a tranferir:\n>"))
    accion = 'TRANSFERENCIA'
    monto = input("Ingrese el monto a transferir:\n>")
    mensaje = con.movimientos(user[0][0], origen, destino, accion, monto)
    print(f"\n\n{mensaje}\n\n")
    
def deposito(user):
    origen = int(input("Ingrese el numero de cuenta:\n>"))
    destino = 0
    accion = 'DEPOSITO'
    monto = input("Ingrese el monto a Depositar:\n>")
    mensaje = con.movimientos(user[0][0], origen, destino, accion, monto)
    print(f"\n\n{mensaje}\n\n")
    
def retiro(user):
    origen = int(input("Ingrese el numero de cuenta del titular:\n>"))
    destino = 0
    accion = 'RETIRO'
    monto = input("Ingrese el monto a retirar:\n>")
    mensaje = con.movimientos(user[0][0], origen, destino, accion, monto)
    print(f"\n\n{mensaje}\n\n")