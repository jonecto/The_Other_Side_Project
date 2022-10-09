# -*- coding: utf-8 -*-
"""
        Archivo destinado a la clase The other side
        contiene:
            Declaración de la clase
            Reglas
            
"""
import descriptor;

class the_other_side():
    def __init__(self):
        self.letras = descriptor.Descriptor()
    def rule_1(self):
        #Un objeto por casilla, pueden haber casillas vacías
        otf=[]
        modf=""
        for t in range(3):
            ot1=[]
            mod1=""
            for y in range(3):
                ot2=[]
                mod2=""
                for x in range(3):
                    ot3=[]
                    mod3=""
                    for p in range(2):
                        mod3 = f"({self.letras.code([p,x,y,t])}>-{self.letras.code([(p+1)%2,x,y,t])})"
                        ot3.append(mod3)
                    ot3.append(f"(-{self.letras.code([p,x,y,t])}Y-{self.letras.code([(p+1)%2,x,y,t])})")
                    mod2=descriptor.Otoria(ot3)
                    ot2.append(mod2)
                mod1=descriptor.Ytoria(ot2)
                ot1.append(mod1)
            modf=descriptor.Ytoria(ot1)
            otf.append(modf)
        return descriptor.Ytoria(otf)
    def rule_2(self):
        #El peon solo puede ocupar una casilla por turno
        otf=[]
        modf=""
        for t in range(3):
            ot1=[]
            mod1=""
            for y in range(3):
                ot2=[]
                mod2=""
                for x in range(3):
                    ot3=[]
                    mod3 = f"({self.letras.code([0,x,y,t])}>"
                    ot4=[]
                    mod4=""
                    for m in range(3):
                        for n in range (3):
                            if m!=x or n!= y:
                                mod4=f"-{self.letras.code([0,m,n,t])}"
                                ot4.append(mod4)
                    mod3+=descriptor.Ytoria(ot4)+")"
                    ot2.append(mod3)
                mod1=descriptor.Ytoria(ot2)
                ot1.append(mod1)
            modf=descriptor.Ytoria(ot1)
            otf.append(modf)
        return descriptor.Ytoria(otf)
    def rule_3(self):
        #Si la casilla de enfrente no está ocupada, al siguiente turno el peon la ocupa
        otf=[]
        modf=""
        for t in range(2):
            ot1=[]
            mod1=""
            for y in range(2):
                ot2=[]
                mod2=[]
                for x in range(3):
                    if y==0:
                        mod2=f"(({self.letras.code([0,1,0,t])}Y-{self.letras.code([1,1,1,t])})>{self.letras.code([0,1,1,t+1])}))"
                        ot2.append(mod2)
                        break
                    elif y==t:
                        mod2=f"(({self.letras.code([0,x,y,t])}Y-{self.letras.code([1,x,y+1,t])})>{self.letras.code([0,x,y+1,t+1])}))"
                        ot2.append(mod2)
                if y==t:
                    mod1=descriptor.Otoria(ot2)
                    ot1.append(mod1)
            modf=descriptor.Otoria(ot1)
            otf.append(modf)
        return descriptor.Ytoria(otf)
    def rule_4(self):
        #Si la casilla diagonal izquierda está ocupada, al siguiente turno el peón ocupa esa casilla
        otf=[]
        modf=""
        for t in range(2):
            ot1=[]
            mod1=""
            for y in range(2):
                ot2=[]
                mod2=[]
                for x in [1,2]:
                    if y==0:
                        mod2=f"(({self.letras.code([0,1,0,t])}Y{self.letras.code([1,0,1,t])})>{self.letras.code([0,0,1,t+1])}))"
                        ot2.append(mod2)
                        break
                    elif y==t:
                        mod2=f"(({self.letras.code([0,x,y,t])}Y{self.letras.code([1,x-1,y+1,t])})>{self.letras.code([0,x-1,y+1,t+1])}))"
                        ot2.append(mod2)
                if y==t:
                    mod1=descriptor.Otoria(ot2)
                    ot1.append(mod1)
            modf=descriptor.Otoria(ot1)
            otf.append(modf)
        return descriptor.Ytoria(otf)
    def rule_5(self):
        #Si la casilla diagonal derecha está ocupada, al siguiente turno el peón ocupa esa casilla
        otf=[]
        modf=""
        for t in range(2):
            ot1=[]
            mod1=""
            for y in range(2):
                ot2=[]
                mod2=[]
                for x in range(2):
                    if y==0:
                        mod2=f"(({self.letras.code([0,1,0,t])}Y{self.letras.code([1,2,1,t])})>{self.letras.code([0,2,1,t+1])}))"
                        ot2.append(mod2)
                        break
                    elif y==t:
                        mod2=f"(({self.letras.code([0,x,y,t])}Y{self.letras.code([1,x+1,y+1,t])})>{self.letras.code([0,x+1,y+1,t+1])}))"
                        ot2.append(mod2)
                if y==t:
                    mod1=descriptor.Otoria(ot2)
                    ot1.append(mod1)
            modf=descriptor.Otoria(ot1)
            otf.append(modf)
        return descriptor.Ytoria(otf)
    def rule_6(self):
        #debe llegar a la otra casilla para ganar
        rev=[]
        for i in range(3):
            rev.append(self.letras.code([0,i,2,2]))
        r6=descriptor.Otoria(rev)
        return r6
    
def see_fine(var):
    normal=0
    for i in var:
        if i=="(":
            normal=normal+1
        if i==")":
            normal=normal-1
    return normal


T_O_S= the_other_side()
print("Regla 1:")
print(descriptor.see_rule(T_O_S.rule_1()))
print("Regla 2:")
print(descriptor.see_rule(T_O_S.rule_2()))
print("Regla 3:")
print(descriptor.see_rule(T_O_S.rule_3()))
print("Regla 4:")
print(descriptor.see_rule(T_O_S.rule_4()))
print("Regla 5:")
print(descriptor.see_rule(T_O_S.rule_5()))
print("Regla 6:")
print(descriptor.see_rule(T_O_S.rule_6()))