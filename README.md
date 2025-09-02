# Laboratorio 1: Criptografía y Seguridad en Redes
## Actividad 1: Cifrado César
- Implementación de un cifrado César en Python.
- Uso:
  ```bash
  python cesar.py "texto" valor_desplazamiento
  ```
- El script cifra el texto usando el desplazamiento indicado con el abecedario sin la ñ.

## Actividad 2: Envío de datos ocultos en paquetes ICMP
- Se utiliza el script `ping.py` para enviar pings a una IP destino, ocultando datos un carácter en el payload de cada paquete.
- Uso:
  ```bash
  sudo venv/bin/python ping.py "8.8.8.8" "mensaje oculto"
  ```
- El string enviado se oculta en el noveno byte del payload de los paquetes ICMP.

## Actividad 3: Extracción y descifrado de datos ocultos
- Se analiza un archivo de captura (`.pcapng`) para extraer los datos ocultos en los paquetes ICMP y probar todas las rotaciones posibles del descifrado César.
- Uso:
  ```bash
  sudo venv/bin/python mitm.py captura_ping.pcapng
  ```
- El script imprime el mensaje extraído y todas las posibles rotaciones del descifrado César.

## Requisitos
- Python 3
- Paquete `scapy` instalado en el entorno virtual
- Para las actividades 2 y 3, es necesario activar el entorno virtual por la libreria ScaPy y usar el comando con `sudo` para el envio de los ping.


