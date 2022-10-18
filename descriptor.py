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
    def visualizar(self, I):
        for z in self.turns:
            # Inicializo el plano que contiene la figura
            fig, axes = plt.subplots()
            axes.get_xaxis().set_visible(False)
            axes.get_yaxis().set_visible(False)
            # Dibujo el tablero
            step = 1./3
            tangulos = []
            # Creo los cuadrados claros en el tablero
            tangulos.append(patches.Rectangle((0, step), step, step,facecolor='cornsilk'))
            tangulos.append(patches.Rectangle(*[(step, 0), step, step],facecolor='cornsilk'))
            tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],facecolor='cornsilk'))
            tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],facecolor='cornsilk'))
            # Creo los cuadrados oscuros en el tablero
            tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],facecolor='lightslategrey'))
            tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],facecolor='lightslategrey'))
            tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],facecolor='lightslategrey'))
            tangulos.append(patches.Rectangle(*[(step, step), step, step],facecolor='lightslategrey'))
            tangulos.append(patches.Rectangle(*[(0, 0), step, step],facecolor='lightslategrey'))
            # Creo las líneas del tablero
            for j in range(3):
                locacion = j * step
                # Crea linea horizontal en el rectangulo
                tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],facecolor='black'))
                # Crea linea vertical en el rectangulo
                tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],facecolor='black'))
            for t in tangulos:
                axes.add_patch(t)
            # Cargando imagen de caballo
            arr_img = plt.imread("./img/Obstaculo.png", format='png')
            imagebox = OffsetImage(arr_img, zoom=0.1)
            imagebox.image.axes = axes
            # Creando las direcciones en la imagen de acuerdo a literal
            direcciones = {}
            direcciones[(0,2)] = [0.165, 0.835]
            direcciones[(1,2)] = [0.5, 0.835]
            direcciones[(2,2)] = [0.835, 0.835]
            direcciones[(0,1)] = [0.165, 0.5]
            direcciones[(1,1)] = [0.5, 0.5]
            direcciones[(2,1)] = [0.835, 0.5]
            direcciones[(0,0)] = [0.165, 0.165]
            direcciones[(1,0)] = [0.5, 0.165]
            direcciones[(2,0)] = [0.835, 0.165]
        
            for l in I:
                if I[l]:
                    if self.decode(l)[3]==z:
                        x = self.decode(l)[1]
                        y = self.decode(l)[2]
                        if self.decode(l)[0]==0:
                            arr_img = plt.imread("./img/Peon.png", format='png')
                            imagebox = OffsetImage(arr_img, zoom=0.1)
                            imagebox.image.axes = axes
                        else:
                            arr_img = plt.imread("./img/Obstaculo.png", format='png')
                            imagebox = OffsetImage(arr_img, zoom=0.1)
                            imagebox.image.axes = axes
                        ab = AnnotationBbox(imagebox, direcciones[(x,y)], frameon=False)
                        axes.add_artist(ab)
            plt.show()
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