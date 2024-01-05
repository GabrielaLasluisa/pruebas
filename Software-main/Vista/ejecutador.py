import sys
sys.path.append("C:/Users/mdjqp/PycharmProjects/Software-main/")
from Control import sesiones as rg
from Control import acciones as mv

def menu(op):
    match op:
        case 1:
            print("\n\t\tMenu")
            print("1) Registrar")
            print("2) Iniciar Sesion")
            print("3) Salir")
        case 2:
            print("\n\n************ Proximamente menu Administrador ************") 
        case 3:
            print("\n\t\tMenu de Empleado\n")
            print("1) Transferencias")
            print("2) Depositos")
            print("3) Retiros")
            print("4) Salir")
        case 4:
            print("\n\t\tMenu de Clientes\n")
            print("1) Transferencias")
            print("2) Saldo de Cuanta")
            print("3) Salir")
    

def reg():
    print("Registro")
    id_ = input("Ingrese Cedula de identidad:\n>")
    nombre = input("Ingrese Nombre:\n>")
    apellido = input("Ingrese Apellido:\n>")
    nombre_c = nombre + " " + apellido
    fecha = input("Ingrese fecha de nacimiento (dd/mm/yyyy):\n>")
    email = input("Ingrese Correo Electronico:\n>")
    pass_1 = input("Ingrese Contrasena:\n>")
    pass_2 = input("Confirmar Contrasena:\n>")
    if (rg.registro_u(id_, nombre_c, fecha, email, pass_1 ,pass_2)):
        print("\n\n\n\n************ Registro exitoso ************")
    else:
        print("\n\n\n\n************ Los datos ingresados son incorectos ************")

def S_Admin():
    print("\n\n************ Proximamente Administrador ************") 
    
def S_Empleado(user):
    c=0
    while (c!=1):
        menu(3)
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                print("\n************ Transferencias ************")
                mv.trans_2(user)
            case 2:
                print("\n************ Depositos ************")
                mv.deposito(user)
            case 3:
                print("\n************ Retiros ************")
                mv.retiro(user)
            case 4:
                print("\n\n************ Cerrando Sesion ************")
                c=1
    
def S_Cliente(user):
    c=0
    while (c!=1):
        menu(4)
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                print("\n************ Transferencias ************")
                mv.trans(user)
            case 2:
                print("\n************ Saldo ************")
                mv.saldos(user)
            case 3:
                print(f"\n\n************ Cerrando Sesion de {user[0][2]} ************")
                c=1

def sesion():
    print("Inicia Sesión")
    email = input("Ingrese su Correo Electronico:\n>")
    pass_ = input("Ingrese su Contrasena:\n>")
    if( len(email)!=0 and len(pass_)!=0 ):
        band, user = rg.user(email, pass_)
        if(band):
            print("\n\n\n\n************ Sesion Exitosa ************")
            rol = int(user[0][4])
            match rol:
                case 1: 
                    S_Admin(user)            
                case 2:
                    S_Empleado(user)
                case 3:
                    S_Cliente(user)
                                
                        
                
        else:
            print("\n\n\n\n************ Las credenciales ingresadas son incorectos ************")
    
def inicio():
    i=0
    while (i!=1):
        menu(1)
        op = int(input("Ingrese una opcion \n>"))
        match op:
            case 1:
                reg()               
            case 2:
                sesion()
            case 3:
                print("\t\tSaliendo del sistema \n Gracias por usar el banco de ahorros")
                i=1
            
inicio()