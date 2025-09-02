import sys

def cifrado_cesar(texto, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for char in texto.lower():
        if char == " ":  # mantener espacios
            resultado += " "
        elif char in abecedario:
            indice = abecedario.index(char)
            nuevo_indice = (indice + desplazamiento) % len(abecedario)
            resultado += abecedario[nuevo_indice]
        else:
            raise ValueError(f"Carácter no permitido: '{char}'")
    
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python lab1.py \"texto\" desplazamiento")
        sys.exit(1)

    texto = sys.argv[1]
    desplazamiento = int(sys.argv[2])

    try:
        cifrado = cifrado_cesar(texto, desplazamiento)
        print(cifrado)
    except ValueError as e:
        print(e)
        sys.exit(1)
