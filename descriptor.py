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
        self.pieces=['Peon','Obstaculo']
        self.turns=[0,1,2]

    def code(self, n_args):
        '''
         n_args recibe una lista con los argumentos (pieza,x,y,turno)
         IMPORTANTE: El argumento Pieza es 0 si es peón, 1 si es ficha
        '''
        x= self.X[n_args[1]] #Posición en x
        y= self.Y[n_args[2]] #Posición en Y
        t= self.turns[n_args[3]] #Turno
        tot= 200 + n_args[0] + x*2 + y*10 + t*100 #Una operación simple
        return(chr(tot)) #Devuelve una letra rara como È
    
    def decode(self, car):
        '''
        Recibe un caracter raro como È
        Devuelve la información de la letra
        '''
        i=ord(car) #Sacar el ascii del caracter
        j=i-200 #Quitar el exceso
        pi=(j%10)%2 #Sacar el número de la pieza (peón o ficha)
        eq=(j%10)//2 #Sacar la posición en X
        ye=(j%100)//10 #Sacar la posición en Y
        tu=j//100 #Sacar el turno
        return [pi,eq,ye,tu]
    
    def write(self,car):
        '''
        Escribe la letra proposicional en lenguaje natural
        '''
        z=self.decode(car) #Recibe los argumentos 
        if(z[0]==1): #identifica que tipo de pieza es
            pieza="Obstaculo"
        else:
            pieza="Peon"
        return f"[Hay un {pieza} en la casilla ({z[1]},{z[2]}) en el turno {z[3]}]"
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
    '''
    Se encarga de escribir la regla, estando esta en formato str
    '''
    trad="" #Para guardar el string que se devolverá
    n=Descriptor() #Un objeto tipo descriptor para la decodificación
    for i in cadena:
        if ord(i)>199: #Revisa si es una letra rara como È
            trad+=n.write(i) #Añade la traducción de la letra 
        elif i=="-": #Si hay un -, añade un No al frente. 
            trad+="no "
        else: #Si no pasa ninguna de esas, coloca el argumento común y corriente
            trad+=i
    return trad

#Si quiere observar el funcionamiento de cada cosa, quite las comillas y corra el programa
'''
prueba = Descriptor()
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