def adn_valido(dna):
    for fila in dna:
        for letra in fila:
            if letra not in ['A','C','G','T']:
                return False
    return True

def is_mutant(dna):
    LONGITUD_SECUENCIA = 4
    contador = 0
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            horizontal = dna[i][j:j + LONGITUD_SECUENCIA] if j + LONGITUD_SECUENCIA <= len(dna[i]) else None
            vertical = dna[i][j] + dna[i + 1][j] + dna[i + 2][j] + dna[i + 3][j] if i + LONGITUD_SECUENCIA <= len(dna) else None
            diagonal = dna[i][j] + dna[i + 1][j + 1] + dna[i + 2][j + 2] + dna[i + 3][j + 3] if i + LONGITUD_SECUENCIA <= len(dna) and j + LONGITUD_SECUENCIA <= len(dna[i]) else None
            if horizontal == dna[i][j] * LONGITUD_SECUENCIA or vertical == dna[i][j] * LONGITUD_SECUENCIA or diagonal == dna[i][j] * LONGITUD_SECUENCIA:
                contador += 1
            if contador > 1:
                return True
    return False

dna = []
print("Ingrese un ADN, matriz 6x6, el mismo solo puede contener las letras (A,T,C,G): ")
for i in range(6):
    while True:
        fila = input()
        if adn_valido(fila):
            dna.append(fila)
            break
        else:
            print("El ADN ingresada no es válido. Intentelo nuevamente: ")

if is_mutant(dna):
    print("Mutante")
else:
    print("No-Mutante")