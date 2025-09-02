import sys
from scapy.all import rdpcap, ICMP, IP

def extraer_bytes_icmp(pcap_file, src_ip, dst_ip):
    packets = rdpcap(pcap_file)
    mensaje_bytes = []

    for pkt in packets:
        if IP in pkt and ICMP in pkt:
            ip_layer = pkt[IP]
            icmp_layer = pkt[ICMP]

            if ip_layer.src == src_ip and ip_layer.dst == dst_ip:
                if len(icmp_layer.payload) > 8:  # verificamos que haya al menos 9 bytes
                    noveno_byte = bytes(icmp_layer.payload)[8]
                    mensaje_bytes.append(noveno_byte)

    mensaje = ''.join(chr(b) for b in mensaje_bytes)
    return mensaje

def cesar_descifrar(texto, desplazamiento):
    resultado = ''
    for char in texto:
        if 'a' <= char <= 'z':
            resultado += chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} archivo.pcapng")
        sys.exit(1)

    archivo_pcap = sys.argv[1]
    src_ip = "192.168.182.128"
    dst_ip = "8.8.8.8"

    mensaje = extraer_bytes_icmp(archivo_pcap, src_ip, dst_ip)
    print(f"Mensaje extraído: {mensaje}")

    print("\nProbando todas las rotaciones de César (1 a 25):")
    for i in range(1, 26):
        descifrado = cesar_descifrar(mensaje, i)
        print(f"Rotación {i}: {descifrado}")
