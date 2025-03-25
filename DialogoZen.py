class DialogoZen:
    def __init__(self, texto_original):
        self.texto_original = texto_original
        self.texto_formateado = ""

    def formatear_texto(self):
        # Elimina espacios extra y normaliza el texto
        self.texto_formateado = " ".join(self.texto_original.split()).capitalize()

    def obtener_texto_formateado(self):
        # Devuelve el texto formateado
        return self.texto_formateado