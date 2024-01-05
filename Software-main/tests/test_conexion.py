import unittest
from modelo import conexion as con

class TestConexion(unittest.TestCase):
    def test_consulta_s(self):
        # Supongamos que hay un usuario con el código 1 en la base de datos
        saldo = con.consulta_s(1)
        self.assertIsInstance(saldo, float)

    def test_insertar(self):
        # Verificar si el usuario ya existe antes de intentar la inserción
        usuario_existente = con.buscar_log("test@example.com", "testpassword")[0]
        if not usuario_existente:
            # Si el usuario no existe, realizar la inserción
            con.insertar("1234567890", "Usuario Test", "01/01/2000", 3, "test@example.com", "testpassword")
        else:
            print("Usuario ya existente. La inserción no se realizó.")

        # Verificar si el usuario ahora existe en la base de datos
        usuario_existente_despues = con.buscar_log("test@example.com", "testpassword")[0]
        self.assertTrue(usuario_existente_despues, "Se esperaba que el usuario exista después de la inserción")


    def test_consulta_c(self):
        # Supongamos que hay un usuario con el código 1 en la base de datos
        numero_cuenta = con.consulta_c(1234567891)
        self.assertIsInstance(numero_cuenta, int)

    def test_movimientos_transferencia(self):
        # Simulamos una transferencia y verificamos si la base de datos refleja el cambio
        codigo = "1234567891"
        cuenta_origen = 1001
        cuenta_destino = 2002
        accion = 'TRANSFERENCIA'
        monto = 1000.00  # Asegúrate de que este monto sea mayor al saldo de la cuenta de origen

        # Intentamos realizar la transferencia
        mensaje = con.movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto)

        # Verificamos si el mensaje indica que el saldo es insuficiente
        self.assertIn("Saldo insuficiente", mensaje)

        # Intentamos nuevamente con un monto más bajo
        monto = 50.00  # Ajusta este valor según la lógica de tu aplicación
        mensaje = con.movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto)

        # Verificamos si el mensaje indica que la transferencia fue exitosa
        self.assertIn("Transferencia exitosa", mensaje)

        # Verificamos si el saldo de la cuenta de origen se redujo
        saldo_origen = con.consulta_s(codigo)
        self.assertIsNotNone(saldo_origen, "Se esperaba un saldo de la cuenta de origen")
        self.assertLessEqual(saldo_origen, 950.00, "El saldo de la cuenta de origen debería ser menor o igual a 950.00")

        # Verificamos si el saldo de la cuenta de destino aumentó
        saldo_destino = con.consulta_s(cuenta_destino)
        self.assertIsNotNone(saldo_destino, "Se esperaba un saldo de la cuenta de destino")
        self.assertEqual(saldo_destino, 50.00, "El saldo de la cuenta de destino debería ser 50.00")

    def test_movimientos_deposito(self):
        # Simulamos un depósito y verificamos si la base de datos refleja el cambio
        # Simulamos un depósito y verificamos si la base de datos refleja el cambio
        codigo = "1234567890"
        cuenta_origen = 0  # Valor de cuenta de origen para depósito
        cuenta_destino = 1001
        accion = 'DEPOSITO'
        monto = 100.00  # Ajusta este valor según la lógica de tu aplicación

        # Realizamos el depósito
        mensaje = con.movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto)

        # Verificamos si el mensaje indica que el depósito fue exitoso
        self.assertIn("Depósito exitoso", mensaje)

        # Verificamos si el saldo de la cuenta de destino aumentó
        saldo_destino = con.consulta_s(cuenta_destino)

        # Ajustamos la prueba para manejar el caso en que la consulta devuelve None
        self.assertIsNotNone(saldo_destino, "Se esperaba un saldo de la cuenta de destino")
        self.assertEqual(saldo_destino, 100.00, "El saldo de la cuenta de destino debería ser 100.00")

    def test_movimientos_retiro(self):
        # Simulamos un retiro y verificamos si la base de datos refleja el cambio
        codigo = "1234567890"
        cuenta_origen = 4004
        cuenta_destino = 0
        accion = 'RETIRO'
        monto = 30.00

        con.movimientos(codigo, cuenta_origen, cuenta_destino, accion, monto)

        # Verificamos si la cuenta de origen tiene un saldo reducido
        saldo_origen = con.consulta_s(cuenta_origen)
        self.assertEqual(saldo_origen, 970.00)  # Ajusta este valor según la lógica de tu aplicación

if __name__ == '__main__':
    unittest.main()
