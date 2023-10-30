import  serial
import time
from BOTCNC import BOTCNC



cnc = BOTCNC()
cnc.initial_config()
cnc.marco_real()
cnc.end_gcode()

# Nombre del archivo de texto en el que se guardará la cadena
nombre_archivo = "prueba1.txt"
with open(nombre_archivo, "w") as archivo:
    # Escribe la cadena en el archivo
    archivo.write(cnc.gcode)

print(f"La cadena se ha guardado en {nombre_archivo}")

# Configura la conexión serial
puerto_serial = serial.Serial('COM12', 115200, 8, 'N', 1, timeout=1)
# Cadena de texto a enviar
g_code = cnc.gcode
partes = g_code.split('\n')

respuesta = puerto_serial.readline().decode('utf-8').strip()
while "[MSG:'$H'|'$X' to unlock]" != respuesta:
    a = 1
try:
    for parte in partes:
        # Envía la parte de la cadena a través del puerto serial
        puerto_serial.write((parte + '\n').encode('utf-8'))
        print(f"Enviado: {parte}")

        # Espera y recibe una respuesta
        respuesta = puerto_serial.readline().decode('utf-8').strip()
        print(f"Respuesta: {respuesta}")
        if parte == 'M9': time.sleep(1.5)

except Exception as e:
    print(f"Error al enviar/recibir datos: {e}")

finally:
    # Cierra la conexión serial
    puerto_serial.close()