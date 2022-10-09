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
    def rule_6(self):
        rev=[]
        for i in range(3):
            rev.append(self.letras.code([0,i,2,2]))
            print(self.letras.code([0,i,2,2]))
        r6=descriptor.Otoria(rev)
        return r6



T_O_S= the_other_side()
print(descriptor.see_rule(T_O_S.rule_6()))