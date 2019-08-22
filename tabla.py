#!/usr/bin/env python
import random
import decoder as dec
import numpy as np
import sys
"""
B 1 - 15
I 16 - 30
N 31 - 45
G 46 - 60
O 61 - 75
"""

def formatoTabla(X):
    s = "\n "+str(X).replace("[","").replace("]","").replace("\'","")
    s = list(s)
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i-1] == " " and s[i-2] == "\n" and not(s[i+1].isdigit()):
                s.insert(i,"0")
    s = "".join(s)
    return s[1:]

def tablaLlena():
    inicio = 1
    fin = 15
    tabla = []
    for i in range(5):
        bingo_columna = []
        while len(bingo_columna) < 5:
            rand_number = random.randrange(inicio, fin)
            if rand_number not in bingo_columna:
                bingo_columna.append(rand_number)
        inicio += 15
        fin += 15
        random.shuffle(bingo_columna)
        tabla.append(bingo_columna)
    tabla[2][2] = dec.DEFCHAR
    return np.transpose(np.array(tabla))

def tablaLetra(letter,tabla_llena):
    new_tabla = np.copy(tabla_llena)
    dec.decode(letter,new_tabla)
    return new_tabla

def main():
    if len(sys.argv) != 2:
        print("use: make run_tabla LETTER=<alphabetic character>")
    letter = sys.argv[1]
    tabla_llena = tablaLlena()
    print(formatoTabla(tablaLetra(letter,tabla_llena)))

if __name__ == "__main__":
    main()
