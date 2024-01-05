
import mysql.connector

__host = "localhost"
__port = "3306"
__database = "prueba"
__user = "root"
__password = ""

def __conec():
  # Establecer la conexión
  conn = mysql.connector.connect(
      host=__host,
      port=__port,
      database=__database,
      user=__user,
      password=__password
  )
  return conn

def buscar_log(email, passw):
    """
        Busca un usuario en la base de datos por correo electrónico y contraseña.

        :param email: Correo electrónico del usuario.
        :param passw: Contraseña del usuario.
        :return: Tupla (bool, rows) donde bool indica si se encontró el usuario y rows contiene los resultados.

        Ejemplo de uso:

        >>> buscar_log("juan@example.com", "password123")
        (True, [(1, 'Juan Perez', '01/01/1990', 3, 'juan@example.com', 'password123')])

        >>> buscar_log("usuario@noexistente.com", "claveincorrecta")
        (False, [])
        """
    conn = __conec()
    cursor = conn.cursor()
    consulta = "SELECT * FROM usuarios WHERE {} = %s AND {} = %s".format("email", "password")
    valores = (email, passw)
    cursor.execute(consulta, valores)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return bool(rows), rows

def insertar(id, nombres, fecha, rol, email, pass_1):
    """
    Inserta un nuevo usuario en la base de datos.

    :param id: Identidad del usuario.
    :param nombres: Nombres del usuario.
    :param fecha: Fecha de nacimiento del usuario.
    :param rol: Rol del usuario.
    :param email: Correo electrónico del usuario.
    :param pass_1: Contraseña del usuario.

    Ejemplo de uso:

    >>> insertar("1234567890", "Ana Rodriguez", "01/05/1988", 2, "ana@example.com", "password456")
    """

    conn = __conec()
    cursor = conn.cursor()
    sql = "INSERT INTO `usuarios` (id, nombres, fecha_n, id_rol, email, password) VALUES (%s, %s, %s, %s, %s, %s);"
    values = (id, nombres, fecha, rol, email, pass_1)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
  
def consulta_s(id):
    conn = __conec()
    cursor = conn.cursor()
    try:
        consulta = "SELECT Saldo FROM cuenta WHERE {} = %s".format("codigo")
        valores = (id,)
        cursor.execute(consulta, valores)
        rows = cursor.fetchall()
        return rows[0][0]
    except Exception as e:
        print("\n\nError en la consulta:", e)
    finally:
        cursor.close()
        conn.close()

def consulta_c(id):
    """
    Consulta el número de cuenta asociado a un usuario.

    :param id: Identidad del usuario.
    :return: Número de cuenta del usuario.

    Ejemplo de uso:

    >>> consulta_c("1234567890")
    1001

    >>> consulta_c("9876543210")
    2002
    """

    conn = __conec()
    cursor = conn.cursor()
    try:
        consulta = "SELECT N_Cuenta FROM cuenta WHERE {} = %s".format("codigo")
        valores = (id,)
        cursor.execute(consulta, valores)
        rows = cursor.fetchall()
        if rows:
            return rows[0][0]
        else:
            return 0
    except Exception as e:
        print("\n\nError en la consulta:", e)
    finally:
        cursor.close()
        conn.close()

def movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto):

    """
    Realiza movimientos en la base de datos, como transferencias, depósitos y retiros.

    :param codigo: Código del usuario.
    :param cuenta_origen: Número de cuenta de origen.
    :param cuenta_destino: Número de cuenta de destino.
    :param accion: Acción a realizar (TRANSFERENCIA, DEPOSITO, RETIRO).
    :param monto: Monto de la operación.

    Ejemplo de uso:

    >>> movimientos("1234567890", 1001, 2002, "TRANSFERENCIA", 50.00)
    'Transferencia exitosa'

    >>> movimientos("9876543210", 3003, 0, "DEPOSITO", 100.00)
    'Depósito exitoso'
    """

    try:
        conn = __conec()
        
        cursor = conn.cursor()
        # Llamada a la función Movimientos_t
        cursor.callproc('Movimientos_t', (codigo, cuenta_origen, cuenta_destino, accion, monto))

        # Recuperar el mensaje de la función (si devuelve uno)
        for result in cursor.stored_results():
          mensaje = result.fetchone()[0]
          print(mensaje)

        conn.commit()

    except mysql.connector.Error as error:
        print("Error al llamar a la función:", error)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

    return mensaje
