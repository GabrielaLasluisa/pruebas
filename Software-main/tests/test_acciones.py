# test_acciones.py
import unittest
from Control import acciones

class TestAcciones(unittest.TestCase):
    def test_deposito(self):
        # Caso de prueba para la función de depósito
        saldo_inicial = 100.0
        monto_deposito = 50.0

        # Llama a la función de depósito
        nuevo_saldo = acciones.deposito(saldo_inicial, monto_deposito)

        # Verifica que el saldo después del depósito sea correcto
        self.assertEqual(nuevo_saldo, saldo_inicial + monto_deposito)

    def test_retiro(self):
        # Caso de prueba para la función de retiro
        saldo_inicial = 100.0
        monto_retiro = 30.0

        # Llama a la función de retiro
        nuevo_saldo = acciones.retiro(saldo_inicial, monto_retiro)

        # Verifica que el saldo después del retiro sea correcto
        self.assertEqual(nuevo_saldo, saldo_inicial - monto_retiro)

if __name__ == '__main__':
    unittest.main()
