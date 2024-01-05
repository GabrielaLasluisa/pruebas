# test_sesiones.py
import unittest
from Control import sesiones

class TestSesiones(unittest.TestCase):
    def test_registro_u(self):
        # Caso de prueba para la función de registro_u
        id_valido = "1234567890"
        nombres_validos = "John Doe"
        fecha_valida = "01/01/1990"
        email_valido = "john.doe@example.com"
        pass_1_valida = "password123"
        pass_2_valida = "password123"

        # Llama a la función de registro_u
        resultado = sesiones.registro_u(id_valido, nombres_validos, fecha_valida, email_valido, pass_1_valida, pass_2_valida)

        # Verifica que el resultado sea True (éxito en el registro)
        self.assertTrue(resultado)

    def test_user(self):
        # Caso de prueba para la función de user
        email_existente = "john.doe@example.com"
        pass_existente = "password123"

        # Llama a la función de user
        band, usuario = sesiones.user(email_existente, pass_existente)

        # Verifica que la bandera sea True (credenciales válidas)
        self.assertTrue(band)

if __name__ == '__main__':
    unittest.main()
