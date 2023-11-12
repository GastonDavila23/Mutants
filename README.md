# Mutants
* Luis Gastón Dávila Ibaceta
* 51520
* gastonn520@gmail.com

 ## De qué va el proyecto
 
    Queremos averiguar si un ADN ingresado por el usuario corresponde a un Mutante o no.
    Para ello debemos solicitar que ingresen una matriz 6x6 que contenga solo letras (A,T,C,G) correspondiete a un ADN. 
    Luego debemos comprobar si en la matriz ingresada hay secuencias "horizontales", "verciales" o "diagonales" de 4 letras iguales.
    Si existe más de una secuencia que cumpla esa condición el ADN ingresado corresponde a un Mutante, en caso contrario es No-Mutante.
    En resumen, el usuario debe ingresar el ADN y nosotros debemos decirle si corresponde o no a un Mutante.

## Cómo lo resolvimos

    Creo la función adn_valido(dna) que toma una lista de cadenas de ADN como entrada y verifica si cada carácter en cada cadena es una de las letras ‘A’, ‘C’, ‘G’ o ‘T’. Si encuentra un carácter que no es una de estas letras, devuelve False. Si todas las letras son válidas, devuelve True.

    Creo La función is_mutant(dna) que toma una lista de cadenas de ADN como entrada y verifica si hay más de una secuencia de cuatro letras iguales en cualquier dirección en la matriz de ADN.

    Mediante la implementación del doble bucle for verifico si hay una secuencia de cuatro letras iguales en la dirección horizontal, vertical o diagonal. Si encuentra más de una de estas secuencias, devuelve True. Si no encuentra más de una secuencia, devuelve False.

    Entrada del usuario: Solicita al usuario que ingrese las filas de la matriz de ADN. Verifica si cada fila ingresada es válida utilizando la función adn_valido. Si la fila no es válida, solicita al usuario que la ingrese nuevamente.

    Verificación de si el ADN es mutante: Una vez que se ha ingresado todo el ADN, utiliza la función is_mutant para verificar si el ADN corresponde a un mutante. Imprimo el resultado para el usuario.
