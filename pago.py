class Pago:
    def __init__(self, codigoPago, concepto):
        self.codigoPago = codigoPago
        self.valor = 0.0
        self.concepto = concepto
        self.estado = "Pendiente"

    def registrarPago(self, valor):
        self.valor = valor
        self.estado = "Pagado"

    def consultarPago(self):
        return self.valor

    def actualizarEstado(self, estado):
        self.estado = estado