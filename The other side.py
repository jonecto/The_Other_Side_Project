# -*- coding: utf-8 -*-
"""
        Archivo destinado a la clase The other side
        contiene:
            Declaración de la clase
            Reglas
            
"""
import descriptor

class the_other_side():
    def __init__(self):
        self.letras = descriptor.Descriptor()
    def rule_1(self):
        #Un objeto por casilla
        a=12
    def rule_2(self):
        #El peon solo puede ocupar una casilla por turno
        a=12
    def rule_3(self):
        #Si la casilla de enfrente no está ocupada, al siguiente turno el peon la ocupa
        a=12
    def rule_4(self):
        #Si la casilla diagonal izquierda está ocupada, al siguiente turno el peón ocupa esa casilla
        a=12
    def rule_5(self):
        #Si la casilla diagonal derecha está ocuoada, al siguiente turno el peón ocupa esa casilla
        a=12
    def rule_6(self):
        #debe llegar a la otra casilla para ganar
        rev=[]
        for i in range(3):
            rev.append(self.letras.code([0,i,2,2]))
            print(self.letras.code([0,i,2,2]))
        r6=descriptor.Otoria(rev)
        return r6



T_O_S= the_other_side()
print(descriptor.see_rule(T_O_S.rule_6()))