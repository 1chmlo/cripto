#!/usr/bin/env python3
from scapy.all import IP, ICMP, Raw, send
import sys
import os
import time

def build_payload(char: str) -> bytes:
    """
    Construye un payload de 40 bytes:
    - Bytes 0-7 : timestamp (4s + 4µs)
    - Byte 8    : carácter del string
    - Bytes 9-39: patrón incremental tipo ping real
    """
    # Timestamp (8 bytes: 4s + 4µs)
    now = time.time()
    sec = int(now)
    usec = int((now - sec) * 1_000_000)
    timestamp = sec.to_bytes(4, "big") + usec.to_bytes(4, "big")

    # Carácter
    data = char.encode("utf-8")

    # Patrón incremental para completar 40 bytes
    pattern = bytes([0x10 + i for i in range(40 - len(timestamp) - len(data))])

    payload = timestamp + data + pattern
    return payload[:40]

def main():
    if len(sys.argv) < 3:
        print(f"Uso: {sys.argv[0]} <ip_destino> <string>")
        sys.exit(1)

    dst_ip = sys.argv[1]
    text = sys.argv[2]

    print(f"Enviando pings a {dst_ip} con datos ocultos en payload...")

    for seq, char in enumerate(text, start=1):
        payload = build_payload(char)

        print(char)  # Imprime solo la letra enviada

        # Armamos el paquete IP + ICMP
        pkt = IP(dst=dst_ip, id=os.getpid() & 0xFFFF) / \
              ICMP(id=os.getpid() & 0xFFFF, seq=seq) / \
              Raw(load=payload)

        #pkt.show2()  # Muestra cómo queda el paquete

        send(pkt, verbose=1)
        time.sleep(1)

if __name__ == "__main__":
    main()