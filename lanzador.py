def formatear_dialogo(self):
        # Dividir el texto en partes usando el carácter '#'
        partes = self.texto_original.split('#')
        
        # Capitalizar la primera letra de la primera parte y añadir puntos suspensivos
        partes[0] = partes[0].capitalize() + "..."
        
        # Capitalizar la primera letra de las demás partes y añadir un punto al final
        for i in range(1, len(partes)):
            partes[i] = partes[i].capitalize() + "."
        
        # Unir las partes con saltos de línea
        self.texto_formateado = "\n\n".join(partes)
        
def convertir_a_dialogo(self):
            # Dividir el texto formateado en líneas
    lineas = self.texto_formateado.split("\n\n")
            
            # Agregar un prefijo de diálogo a cada línea
    dialogo = []
    for i, linea in enumerate(lineas):
        dialogo.append(f"Personaje {i + 1}: {linea}")
            
            # Unir las líneas con saltos de línea
    self.dialogo = "\n".join(dialogo)