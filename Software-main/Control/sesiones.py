import sys
sys.path.append("C:/Users/mdjqp/PycharmProjects/Software-main/")
from modelo import conexion as con
import datetime

def f_fecha(fecha_entrada):
    fecha_objeto = datetime.datetime.strptime(fecha_entrada, "%d/%m/%Y")
    fecha_salida = fecha_objeto.strftime("%Y-%m-%d")
    return fecha_salida

def registro_u(id, nombres, fecha, email, pass_1, pass_2, rol=3):

    """
    Realiza el registro de un usuario.

    :param id: Identidad del usuario.
    :param nombres: Nombres del usuario.
    :param fecha: Fecha de nacimiento del usuario.
    :param email: Correo electrónico del usuario.
    :param pass_1: Contraseña del usuario.
    :param pass_2: Confirmación de contraseña del usuario.
    :param rol: Rol del usuario (por defecto 3).
    :return: True si el registro fue exitoso, False si los datos son incorrectos.

    Ejemplo de uso:

    >>> registro_u("1234567890", "Juan Perez", "01/01/1990", "juan@example.com", "password123", "password123")
    True

    >>> registro_u("9876543210", "Maria Lopez", "01/01/1985", "maria@example.com", "pass", "pass")
    False
    """

    if(pass_1 == pass_2 and len(id)==10):
        fecha = f_fecha(fecha)
        # print(f"\n\nDatos Ingresados\n\n{id}, \n{nombres}, \n{fecha}, \n{rol}, \n{email}, \n{pass_1} ")
        con.insertar(id, nombres, fecha, rol, email, pass_1)
        return True
    else:
        return False

def user(email, pass_):
    band, user = con.buscar_log(email, pass_)
    return band, user
        