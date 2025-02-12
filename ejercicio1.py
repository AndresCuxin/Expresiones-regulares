import re

texto = """Estimados estudiantes,

Les recuerdo que la reunión para el curso de programación se llevará a cabo el próximo viernes 8 de febrero a las 10:00 AM. Estarán presentes varios miembros del equipo, entre ellos, Juan Pérez (juan.perez@example.com), quien es el encargado de la parte de backend. También estará María García (maria.garcia@dominio.com), responsable del frontend, así como Carlos López (carlos.lopez@correo.org), quien trabajará en la integración del sistema.

La dirección de la reunión es en la Calle Falsa 123, oficina 201. El evento será transmitido de forma remota y se podrá acceder a través del enlace http://reunion.curso-programacion.com.

Por favor, no olviden enviar sus informes antes del 7 de febrero a las 5:00 PM. Los informes deben enviarse a la siguiente dirección de correo electrónico: informes@empresa.com. Asegúrense de incluir todos los detalles relevantes. Además, está Silvia Martínez (silvia.martinez@correo.net), que revisará los informes para asegurarse de que estén completos.

Si tienen preguntas adicionales, pueden contactar a cualquiera de los siguientes miembros del equipo:

Ana Sánchez (ana.sanchez@empresa.org), encargada de la logística.
Pedro Gómez (pedro.gomez@dominio.com), responsable de la base de datos.
Luis Rodríguez (luis.rodriguez@correo.com), quien está a cargo de la documentación.
El teléfono de contacto para emergencias es el +34 612 345 678.

Si desean obtener más detalles, no duden en llamarnos al +34 678 910 112. Recuerden que la reunión también incluirá una breve sesión sobre la gestión de proyectos ágiles y cómo implementarlos en el entorno de programación."""

# expresiones regulares
regex_nombres = re.findall(r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+", texto)
regex_correos = re.findall(r"[\w.-]+@[\w.-]+\.[a-z]{2,3}", texto)
regex_fechas = re.findall(r"\d{1,2}\sde\s(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)", texto)
regex_horas = re.findall(r"\d{1,2}:\d{2}\s[APM]{2}", texto)
regex_telefonos = re.findall(r"\+?\d{1,3}\s\d{3}\s\d{3}\s\d{3}", texto)
regex_direcciones = re.findall(r"Calle\s[A-ZÁÉÍÓÚÑa-záéíóúñ]+\s\d+,\soficina\s\d+", texto)
regex_urls = re.findall(r"https?://[\w.-]+", texto)
regex_temas = re.findall(r"gestión de proyectos ágiles", texto, re.IGNORECASE)
regex_empresas = re.findall(r"@[\w.-]+\.[a-z]{2,3}", texto)

# limpiar nombres de empresas
empresas = list(set([e[1:] for e in regex_empresas]))

# mostrar resultados
print("Nombres completos:", regex_nombres)
print("Correos electrónicos:", regex_correos)
print("Fechas:", regex_fechas)
print("Horas:", regex_horas)
print("Teléfonos:", regex_telefonos)
print("Direcciones:", regex_direcciones)
print("Enlaces web:", regex_urls)
print("Títulos de temas:", regex_temas)
print("Organización de la empresa:", empresas)
