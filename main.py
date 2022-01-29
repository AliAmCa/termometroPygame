import pygame,sys
from pygame.locals import *


class Termometro():
    
    def __init__(self):
        self.custome= pygame.image.load("images/termo1.png")
    
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32)* 5/9
        else:
            resultado = grados
        return resultado
    
   
        
class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = 'C'):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
    
    def getCustome(self):
        if self.__tipoUnidad == 'C':
            return self.__customes[1]
        else:
            return self.__customes[0]
        
    def change(self,event):
        
        if self.__tipoUnidad== 'C':
            self.__tipoUnidad = 'F'
        else:
            self.__tipoUnidad= 'C'
            
    def getUnidad(self):
        return self.__tipoUnidad
    
class NumberInput():
    __value = 0
    __strValue= ""
    __position = [0,0]
    __size = [0,0]
    __pointsCount = 0
   
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial",24)
        print(self.__strValue)
        self.value(value)
        
    def on_event(self,event):
        if event.type ==KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue)<10 or (event.unicode == '.' and self.__pointsCount ==0):
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount +=1
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)
                
    
    
    def render(self):
        textBlock = self. __font.render(self.__strValue, True, (74,74,74))
        rectangulo = textBlock.get_rect()
        rectangulo.left = self.__position[0]
        rectangulo.top = self.__position[1]
        rectangulo.size = self.__size
        
        return (rectangulo,textBlock)
    
    def value(self, val=None):
        
        if val==None:
            return self.__value
        else:
            val= str(val)
         
            try:
                self.__value= float(val)
                self.__strValue = val[:10]
                if '.' in self.__strValue:
                    self.__pointsCount=1
                else:
                    self.__pointsCount=0
            except:
                print("Se ha producido un error")
            
    def width(self, val=None):
        if val==None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
    
    def height(self, val=None):
        if val==None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
            
    def size(self, val= None):
        if val==None:
             return self.__size
        else:
            try:
                self.__size = [int(val[0]),int(val[1])]
            except:
                pass
        

    def posX(self, val=None):
        if val==None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
    
    def posY(self, val=None):
        if val==None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def position(self, val= None):
        if val==None:
             return self.__position
        else:
            try:
                self.__position = [int(val[0]),int(val[1])]
            except:
                pass
        
        
        
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244,236,203))
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.position((106,58))
        self.entrada.size((133,28))
        
        self.selector= Selector()
        
    def __close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__close()
                
                self.entrada.on_event(event)
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change(event)
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.getUnidad()
                   
                    temperatura = self.termometro.convertir(grados,nuevaUnidad)
                    
                    self.entrada.value(temperatura)
                    
            self.__screen.fill((244,236,203))
            #Pintamos el termometro en su posicion
            self.__screen.blit(self.termometro.custome,(50,34))
            
            #Pintamos el cuadro de texto
            texto = self.entrada.render() #Obtenemos el rectangulo blanco y foto del texto
            
            pygame.draw.rect(self.__screen, (255,255,255), texto[0]) #Creamos el rectangulo blanco en su posicion
            
            self.__screen.blit(texto[1], self.entrada.position()) #Pintamos la foto del texto
            
            #Pintamos el selector
            
            self.__screen.blit(self.selector.getCustome(), (106,153))
            pygame.display.flip()

if __name__ == "__main__":
    pygame.font.init()
    app= mainApp()
    app.start()
    