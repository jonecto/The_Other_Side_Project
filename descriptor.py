'''
        THE OTHER SIDE
    Este archivo tendrá el descriptor con: 
        Codificador
        Decodificador
        Letra
        
        

'''

class Descriptor():
    def __init__(self):
        self.X=[0,1,2]
        self.Y=[0,1,2]
        self.pieces=['Peon','Ficha']
        self.turns=[0,1,2]
        
    def code(self, n_args): #n_args recibe una lista con los argumentos (pieza,x,y,turno)
        x= self.X[n_args[1]]    #IMPORTANTE: El argumento Pieza es 0 si es peón, 1 si es ficha
        y= self.Y[n_args[2]]
        t= self.turns[n_args[3]]
        tot= 200 + n_args[0] + x*2 + y*10 + t*100
        return(chr(tot))
    
    def decode(self, car):
        i=ord(car)
        j=i-200
        pi=(j%10)%2
        eq=(j%10)//2
        ye=(j%100)//10
        tu=j//100
        return [pi,eq,ye,tu]
    
    def write(self,car):
        z=self.decode(car)
        if(z[0]==1):
            pieza="Ficha"
        else:
            pieza="Peon"
        return f"[Hay {pieza} en la casilla ({z[1]},{z[2]}) en el turno {z[3]}]"
def Ytoria(lista_forms):
    form = ''
    inicial = True
    for f in lista_forms:
        if inicial:
            form = f
            inicial = False
        else:
            form = '(' + form + 'Y' + f + ')'
    return form

def Otoria(lista_forms):
    form = ''
    inicial = True
    for f in lista_forms:
        if inicial:
            form = f
            inicial = False
        else:
            form = '(' + form + 'O' + f + ')'
    return form
    
def see_rule(cadena):
    trad=""
    n=Descriptor()
    for i in cadena:
        if ord(i)>199:
            trad+=n.write(i)
        elif i=="-":
            trad+="no "
        else:
            trad+=i
    return trad
'''
prueba = descriptor()
rev=[]
i=0
print(prueba.code([0,0,0,0]))
print(prueba.decode("È"))
for i in range(3):
    rev.append(prueba.code([0,i,2,2]))
    print(prueba.code([0,i,2,2]))
r6=Otoria(rev)
print(r6)
print(see_rule(r6))
'''