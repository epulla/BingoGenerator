"""
En este archivo, se decodificara un caracter (solo letra alfabeticas) a una matriz
5x5 con la forma del caracter
Los caracteres que es excluyen son: K, tildes, ENIE, Q, V
"""

import numpy as np


DEFCHAR = "##"

def decode(letter,X):
    if letter=='A':toA(X)
    elif letter=='B':toB(X)
    elif letter=='C':toC(X)
    elif letter=='D':toD(X)
    elif letter=='E':toE(X)
    elif letter=='F':toF(X)
    elif letter=='G':toG(X)
    elif letter=='H':toH(X)
    elif letter=='I':toI(X)
    elif letter=='J':toJ(X)
    elif letter=='L':toL(X)
    elif letter=='M':toM(X)
    elif letter=='N':toN(X)
    elif letter=='O':toO(X)
    elif letter=='P':toP(X)
    elif letter=='R':toR(X)
    elif letter=='S':toS(X)
    elif letter=='T':toT(X)
    elif letter=='U':toU(X)
    elif letter=='W':toW(X)
    elif letter=='X':toX(X)
    elif letter=='Y':toY(X)
    elif letter=='Z':toZ(X)
    else:
        print("Caracter desconocido "+letter)


def toA(X):
    for i in range(1,4):
        X[1,i] = X[3,i] = X[4,i] = DEFCHAR

def toB(X):
    for i in range(1,4):
        X[1,i] = X[3,i] = DEFCHAR
    X[2,4] = DEFCHAR

def toC(X):
    for i in range(1,4):
        X[1,i] = X[2,i] = X[3,i] = X[i,4] = DEFCHAR

def toD(X):
    for i in range(1,4):
        X[1,i] = X[2,i] = X[3,i] = DEFCHAR
    X[0,4] = DEFCHAR
    X[4,4] = DEFCHAR

def toE(X):
    for i in range(1,5):
        X[1,i] = X[3,i] = DEFCHAR

def toF(X):
    for i in range(1,5):
        X[1,i] = X[3,i] = X[4,i] = DEFCHAR

def toG(X):
    for i in range(1,4):
        X[1,i] = X[3,i] = DEFCHAR
    X[2,1] = DEFCHAR
    X[1,4] = DEFCHAR

def toH(X):
    for i in range(1,4):
        X[0,i] = X[1,i] = X[3,i] = X[4,i] = DEFCHAR

def toI(X):
    for i in range(1,4):
        X[i,0] = X[i,1] = X[i,3] = X[i,4] = DEFCHAR

def toJ(X):
    for i in range(1,4):
        X[i,0] = X[i,1] = X[i,3] = X[i,4] = DEFCHAR
    X[4,3] = X[4,4] = DEFCHAR

#Omitimos K

def toL(X):
    for i in range(1,5):
        X[0,i] = X[1,i] = X[2,i] = X[3,i] = DEFCHAR

def toM(X):
    for i in range(1,4):
        X[0,i] = X[2,i] = X[3,i] = X[4,i] = DEFCHAR
    X[1,2] = DEFCHAR

def toN(X):
    for i in range(1,4):
        X[0,i] = X[4,i] = DEFCHAR
    for i in range(1,3):
        X[1,i+1] = X[3,i] = DEFCHAR
    X[2,1] = X[2,3] = DEFCHAR

def toO(X):
    for i in range(1,4):
        X[1,i] = X[2,i] = X[3,i] = DEFCHAR

def toP(X):
    for i in range(1,5):
        X[3,i] = X[4,i] = DEFCHAR
    for i in range(1,4):
        X[1,i] = DEFCHAR

#Omitimos Q

def toR(X):
    for i in range(1,4):
        X[1,i] = X[4,i] = DEFCHAR
    X[3,1] = X[3,2] = X[3,4] = DEFCHAR

def toS(X):
    for i in range(4):
        X[3,i] = X[1,i+1] = DEFCHAR

def toT(X):
    for i in range(1,5):
        X[i,0] = X[i,1] = X[i,3] = X[i,4] = DEFCHAR

def toU(X):
    for i in range(1,4):
        X[0,i] = X[1,i] = X[2,i] = X[3,i] = DEFCHAR

def toW(X):
    for i in range(1,4):
        X[0,i] = X[1,i] = X[2,i] = X[4,i] = DEFCHAR
    X[3,2] = DEFCHAR

def toX(X):
    for i in range(1,4):
        X[0,i] = X[i,0] = X[4,i] = X[i,4] = DEFCHAR
        X[2,i] = X[i,2] = DEFCHAR

def toY(X):
    for i in range(1,5):
        X[i,0] = X[i,4] = DEFCHAR
    for i in range(2,5):
        X[i,1] = X[i,3] = X[0,i-1] = DEFCHAR
    X[1,2] = DEFCHAR

def toZ(X):
    for i in range(3):
        X[1,i] = X[3,i+2] = DEFCHAR
    for i in range(2):
        X[2,i] = X[2,i+3] = DEFCHAR
    X[3,0] = X[1,4] = DEFCHAR
