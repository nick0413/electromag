import pygame
from pygame.locals import *
import cv2
import numpy
import time
from datetime import datetime
import os
pygame.init()
timer_limit = 360
inicio=time.time()
sentido='0'
pinicial=1

tiempotutorial=time.time()

pygame.display.set_caption("ELECTROMAG")
icono = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\neutron.png")
pygame.display.set_icon(icono)

musica1 = pygame.mixer.music.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\musica1.ogg")
musica1 = pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
w= screen.get_width()
h=screen.get_height()

#Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
amarillo = (255, 255, 0)
green = (0, 255, 0)
blue= (0, 0, 255)

FPS = 60
reloj = pygame.time.Clock()
x=0
x_a=0

# Fondos-Imágenes Científicas.
fondo = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\Fondopaola.png").convert()
fondodiana = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\fondodiana.png").convert()
fondolise = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\fondolise.png").convert()
fondonubia = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\fondonubia.png").convert()
fondomarie = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\fondomarie.png").convert()
fondorosalind = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\fondoRosalind.png").convert()
pinilla= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\2.png").convert()
pinilla.set_colorkey(red)
diana= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\DianaT.png").convert()
diana.set_colorkey(red)
lise= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\lisem.png").convert()
lise.set_colorkey(white)
nubia= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\nubia1.png").convert()
nubia.set_colorkey(blue)
marie= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\mariec.png").convert()
marie.set_colorkey(amarillo)
rosalind= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\ImagenesCientificas\\Rosalind1.png").convert_alpha()
rosalind.set_colorkey(blue)
#VARIABLE NIVEL
n=0

class Text:

    def __init__(self, text, pos, fontsize, color, fontname='C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\Letra\\MP16OSF.ttf', ):
        self.text = text
        self.len = len(self.text)+1
        self.pos = pos
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = Color(color)
        self.set_font()
        self.move = True


    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def tfin(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos
        screen.blit(self.img, self.rect)
        #pygame.display.update()

    def draw(self):

        while self.move:
            pygame.mixer.music.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\Musica\\musicacientificas.mp3")
            pygame.mixer.music.play(-1)
            for n in range(0, self.len):
                if n == self.len-1:
                    self.move = False
                self.img = self.font.render(self.text[0:n], True, self.fontcolor)
                self.rect = self.img.get_rect()
                self.rect.center = self.pos
                R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
                pygame.draw.rect(screen, (0,0,0), R)
                screen.blit(self.img, self.rect)
                pygame.display.update()
                pygame.time.wait(200)
        self.tfin()


def fondom(d):
    global x
    global x_a
    ##print('x====', x)
    ##print('d=   ', d)
    x_a = x % fondo.get_rect().width
    screen.blit(fondo, (x_a - fondo.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondo,(x_a,0))
        screen.blit(pinilla, [384+400, 104])
        k.draw()
    if x==-1280:
        d=True
        return d
    x-=1

def fondomd(d):
    global x
    global x_a
    ##print('x====', x)
    ##print('d=   ', d)
    x_a = x % fondodiana.get_rect().width
    screen.blit(fondodiana, (x_a - fondodiana.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondodiana,(x_a,0))
        screen.blit(diana, [384+400, 104])
        D.draw()
    if x==-1280:
        d=True
        return d
    x-=1

def fondoml(d):
    global x
    global x_a
    ##print('x====', x)
    ##print('d=   ', d)
    x_a = x % fondolise.get_rect().width
    screen.blit(fondolise, (x_a - fondolise.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondolise,(x_a,0))
        screen.blit(lise, [384+400, 104])
        L.draw()
    if x==-1280:
        d=True
        return d
    x-=1

def fondomn(d):
    global x
    global x_a
    ##print('x====', x)
    ##print('d=   ', d)
    x_a = x % fondonubia.get_rect().width
    screen.blit(fondonubia, (x_a - fondonubia.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondonubia,(x_a,0))
        screen.blit(nubia, [24, 230])
        N.draw()
    if x==-1280:
        d=True
        return d
    x-=1


def fondomm(d):
    global x
    global x_a
    ##print('x====', x)
    ##print('d=   ', d)
    x_a = x % fondomarie.get_rect().width
    screen.blit(fondomarie, (x_a - fondomarie.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondomarie,(x_a,0))
        screen.blit(marie, [384+400, 104])
        M.draw()
    if x==-1280:
        d=True
        return d
    x-=1

def fondomr(d):
    global x
    global x_a
    ##print('x==== rosalind', x)
    ##print('d=   ', d)
    x_a = x % fondorosalind.get_rect().width
    screen.blit(fondorosalind, (x_a - fondorosalind.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondorosalind,(x_a,0))
        screen.blit(rosalind, [0,200])
        R.draw()
    if x==-1280:
        d=True
        return d
    x-=1

#Texto Cientifícas
k = Text('¡Hola!, soy Paola Pinilla. Astrofísica Colombiana ', (w/2.0,h-650), 35, white )
D = Text('¡Hola!, soy Diana Trujillo. Ingeniera Aeroespacial Colombiana ', (w/2.0,h-650), 35, white )
L = Text('¡Hola!, soy Lise Meitner. Física Nuclear', (w/2.0,h-650), 35, white )
N = Text('¡Hola!, soy Nubia Muñoz. Médica Patóloga Colombiana ', (w/2.0,h-650), 35, white )
M = Text('¡Hola!, soy Marie Curie. Científica Polaca ', (w/2.0,h-650), 35, white )
R = Text('¡Hola!, soy Rosalind Franklin.  ', (w/2.0,h-650), 35, white )


def mouseover(imagen,coordenadas):
    mouse=False
    y,x,_ = cv2.imread(imagen).shape
    mx,my = pygame.mouse.get_pos()
    tx,ty=coordenadas[0],coordenadas[1]
    if tx+x > mx >tx:
        if ty+y > my > ty:
            mouse=True
    ###print(coordenadas,x,y,imagen)
    return mouse

class Boton():
    def __init__(self,tipo,imagen,coordenadas):
        self.mouse=False
        self.tipo=tipo
        self.coordenadas=coordenadas
        self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_1.png").convert_alpha()

        #JUGAR
        if self.tipo=='jugar':
            mouse1=mouseover(imagen,coordenadas)
            if mouse1==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_1.png").convert_alpha()
                self.mouse=True
            if mouse1==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_0.png").convert_alpha()
                self.mouse=False

        #NIVEL
        if self.tipo=='nivel':
            mouse2=mouseover(imagen,coordenadas)
            if mouse2==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\niveles_1.png").convert_alpha()
                self.mouse=True
            if mouse2==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\niveles_0.png").convert_alpha()
                self.mouse=False

        #PAUSA
        if self.tipo=='pausa':
            mouse3=mouseover(imagen,coordenadas)
            if mouse3==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_1.png").convert_alpha()
                self.mouse=True
            if mouse3==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png").convert_alpha()
                self.mouse=False

        #CONTINUAR
        if self.tipo=='continuar':
            mouse4=mouseover(imagen,coordenadas)
            if mouse4==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\continuar_1.png").convert_alpha()
                self.mouse=True
            if mouse4==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\continuar_0.png").convert_alpha()
                self.mouse=False
        #SALIR
        if self.tipo=='salir':
            mouse5=mouseover(imagen,coordenadas)
            if mouse5==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\salir_1.png").convert_alpha()
                self.mouse=True
            if mouse5==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\salir_0.png").convert_alpha()
                self.mouse=False

        #NIVEL 1
        if self.tipo=='n1':
            mouse6=mouseover("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\1_1.png",coordenadas)
            if mouse6==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\1_1.png").convert_alpha()
                self.mouse=True
            if mouse6==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\1_0.png").convert_alpha()
                self.mouse=False

        #NIVEL 2
        if self.tipo=='n2':
            mouse7=mouseover("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\2_1.png",coordenadas)
            if mouse7==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\2_1.png").convert_alpha()
                self.mouse=True
            if mouse7==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\2_0.png").convert_alpha()
                self.mouse=False

        #NIVEL 3
        if self.tipo=='n3':
            mouse8=mouseover("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\3_1.png",coordenadas)
            if mouse8==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\3_1.png").convert_alpha()
                self.mouse=True
            if mouse8==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\3_0.png").convert_alpha()
                self.mouse=False

        #NIVEL 4
        if self.tipo=='n4':
            mouse9=mouseover("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\4_1.png",coordenadas)
            if mouse9==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\4_1.png").convert_alpha()
                self.mouse=True
            if mouse9==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\4_0.png").convert_alpha()
                self.mouse=False

        #NIVEL 5
        if self.tipo=='n5':
            mouse10=mouseover("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\5_1.png",coordenadas)
            if mouse10==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\5_1.png").convert_alpha()
                self.mouse=True
            if mouse10==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\5_0.png").convert_alpha()
                self.mouse=False

        #INFO
        if self.tipo=='info':
            mouse11=mouseover(imagen,coordenadas)
            if mouse11==True:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_1.png").convert_alpha()
                self.mouse=True
            if mouse11==False:
                self.ima = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png").convert_alpha()
                self.mouse=False
class Objeto():
    def __init__(self,nombre,ubx,uby,obj):

        self.image = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\carga_pos_2.png").convert_alpha()
        self.nombre = nombre
        ###print(nombre,'====================== ingame',obj)
        if obj==False:
            self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\vacio.png").convert_alpha()
        elif nombre == "positivo":
            self.image = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\carga_pos_2.png").convert_alpha()

        elif nombre == "negativo":
            self.image = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\carga_neg_2.png").convert_alpha()

        elif nombre == "neutro":
            self.image = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\carga_net_2.png").convert_alpha()

        elif nombre == "maquina":
            self.image = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\maquina_fusion.png").convert_alpha()

        elif nombre == "tablero":
          self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha()

        self.posip= m.trannp(ubx,uby)
        self.posin=[ubx,uby]

class Grid():
    def __init__(self,size,start):
        mb=[]
        mb1=[]
        mn=[]

        for j in range(8):
            mb1=[]
            mn1=[]
            for i in range(8):
                b=(j,i)
                k=(((i*size)+start[0]),((j*size)+start[1]))
                mb1.append(b)
                mn1.append(k)
                ###print(mb1)
            mb.append(mb1)
            mn.append(mn1)

        ###print(mb[5][3])
        ###print(mn[5][3])
        self.matrizp=mn
        self.matrizb=mb

    # traduce de numeros a pixeles
    def trannp(self,x,y):
        p=self.matrizp[x][y]
        return p
    # traduce de pixeles a numeros
    def tranpn(self,x,y):
        p=self.matrizb[x][y]
        return p

m=Grid(64,(390,110))

class Player(Objeto):
  def __init__(self,nombre,posxn,posyn, obj,sentido='0'):
    super().__init__(nombre,posxn,posyn, obj)

    ###print('objjjjjj====================/////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\=====================',obj)
    self.grab=None
    self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\personaje.png").convert_alpha()
    #print(sentido, 'SE ESTÁ VOLVIENDO TRUE WTF')
    if sentido=='down':
        self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\perdown.png").convert_alpha()
        ###print('cambio abajo')
    if sentido=='up':
        self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\perup.png").convert_alpha()
        # ##print('cambio up')
    if sentido=='left':
        self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\perleft.png").convert_alpha()
        # ##print('cambio izquiera')
    if sentido=='right':
        self.image=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\perright.png").convert_alpha()
        # ##print('cambio derecha')



#FONDOS
fondo1 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo1.png").convert()
fondo2 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo2.png").convert()
fondo3 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo3.png").convert()
fondo4 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo4.png").convert()
fondo5 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo5.png").convert()
fondo_niveles= pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo_niveles.png").convert()
menu_pausa = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\menu_pausa_.png").convert()
menu_pausa.set_colorkey([0,0,0])
game_over=pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\game_over.png").convert()
tutorial = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tutorial.png").convert_alpha()
tutorial2 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tutorial_2.png").convert_alpha()
fondo_ganaste = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\ganaste.png").convert_alpha()

class Gamestate():
    def __init__(self):
        self.state='intro'

    def cambia_nivel(self):
        if self.state=='intro':
           self.intro()
        if self.state=='gameover':
           self.gameover()
        if self.state=='tutorial':
           self.tutorial()
        if self.state=='menu_pausa':
           self.menu_pausa()
        if self.state=='continuar':
           self.continuar()
        if self.state=='salir':
           self.salir()
        if self.state=='niveles':
           self.niveles()
        if self.state=='nivel_1':
           self.nivel_1()
        if self.state=='nivel_2':
           self.nivel_2()
        if self.state=='nivel_3':
           self.nivel_3()
        if self.state=='nivel_4':
           self.nivel_4()
        if self.state=='nivel_5':
           self.nivel_5()
        if self.state=='info':
           self.info()
        if self.state== "videoCoulomb":
           self.videoCoulomb()
        if self.state=='videoc_1':
           self.videoc_1()
        if self.state=='videoc_2':
           self.videoc_2()
        if self.state=='videoc_3':
           self.videoc_3()
        if self.state=='videoc_4':
           self.videoc_4()
        if self.state=='videoc_5':
           self.videoc_5()
        if self.state=='videoc_6':
           self.videoc_6()
        if self.state=='ganaste':
           self.ganaste()

    def videoc_1(self):
        global donep
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial
        pinicial=2
        while not donep :
            donep=fondom(donep)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    donep = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        global timer_limit
        global inicio
        timer_limit=70
        inicio=time.time()

        carga1pos_pos=pos('positivo', [2,1])
        carga2pos_pos=pos('positivo', [5,5])
        carga3pos_pos=pos('positivo', [4,2])
        carga4pos_pos=pos('positivo', [4,5])

        carga1neg_pos = pos('negativo', [3,6])
        carga2neg_pos = pos('negativo', [7,3])
        carga3neg_pos = pos('negativo', [3,6])
        carga4neg_pos = pos('negativo', [0,5])

        carga1net_pos=pos('neutro', [3,5])
        carga2net_pos= pos('neutro', [1,5])
        carga3net_pos=pos('neutro', [1,7])
        carga4net_pos= pos('neutro', [3,4])

        playerpos=pos('personaje',[0,0])
        maquinapos=pos('maquina', [7,1])
        pinicial=2
        self.state='nivel_2'
    def videoc_2(self):
        global doned
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial
        pinicial=2
        while not doned :
            doned=fondomd(doned)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    doned = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        global timer_limit
        global inicio
        timer_limit=40
        inicio=time.time()
        inicio=time.time()

        carga1pos_pos=pos('positivo',[2,1])
        carga2pos_pos=pos('positivo', [5,5])
        carga3pos_pos=pos('positivo', [4,2])
        carga4pos_pos=pos('positivo', [4,7])
        carga1neg_pos = pos('negativo', [3,6])
        carga2neg_pos = pos('negativo', [7,3])
        carga1net_pos=pos('neutro', [3,5])
        carga2net_pos= pos('neutro', [1,5])
        carga3net_pos= pos('neutro', [2,7])

        playerpos=pos('personaje',[0,0])
        maquinapos=pos('maquina', [7,6])
        self.state='nivel_3'
    def videoc_3(self):
        global donel
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial
        pinicial=2
        while not donel :
            donel=fondoml(donel)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    donel = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        global timer_limit
        global inicio
        timer_limit=30
        inicio=time.time()

        carga1pos_pos=pos('positivo',[2,1])
        carga2pos_pos=pos('positivo', [5,5])
        carga1neg_pos = pos('negativo', [3,6])
        carga2neg_pos = pos('negativo', [0,3])
        carga3neg_pos = pos('negativo', [1,7])
        carga1net_pos=pos('neutro', [3,5])
        carga2net_pos= pos('neutro', [1,5])
        carga3net_pos=pos('neutro', [2,7])
        carga4net_pos= pos('neutro', [4,1])

        playerpos=pos('personaje',[0,0])
        maquinapos=pos('maquina', [7,2])
        self.state='nivel_4'
    def videoc_4(self):
        global doneN
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial
        pinicial=3
        while not doneN :
            doneN=fondomn(doneN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    doneN = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        global timer_limit
        global inicio
        timer_limit=30
        inicio=time.time()

        carga1pos_pos=pos('positivo',[2,1])
        carga2pos_pos=pos('positivo', [5,5])
        carga3pos_pos=pos('positivo',[0,1])
        carga4pos_pos=pos('positivo', [5,7])
        carga1neg_pos = pos('negativo', [3,7])
        carga2neg_pos = pos('negativo', [2,6])
        carga3neg_pos = pos('negativo', [4,1])
        carga1net_pos=pos('neutro', [0,5])
        carga2net_pos=pos('neutro', [7,7])
        carga3net_pos=pos('neutro', [6,1])
        playerpos=pos('personaje',[0,0])
        maquinapos=pos('maquina', [7,4])
        self.state='nivel_5'
    def videoc_5(self):
        global donem
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial
        pinicial=3
        while not donem:
            donem=fondomm(donem)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        global x
        x=0
        self.state='videoc_6'
    def videoc_6(self):
        global doner
        while not doner:
            doner=fondomr(doner)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.update()
            reloj.tick(FPS)
            pygame.display.flip()
        self.state='ganaste'
    def videoCoulomb(self):
        global tiempotutorial
        coulomb ='C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\Coulomb'
        num_of_frames = len(os.listdir(coulomb))
        pygame.mixer.music.load("Musica/musicacoulomb.mp3")
        pygame.mixer.music.play(-1)
        for i in range (0, num_of_frames):
            img1= pygame.image.load(f"Coulomb/myphotos{i}.png")
            screen.blit(img1, (0,0))
            pygame.display.update()
            time.sleep(0.01)
        for event in pygame.event.get():
            pass
            tiempotutorial=time.time()
            self.state='tutorial'
            ###print(self.state)
        pygame.display.flip()
    def intro(self):
        global done
        coorxy=[640-152,420-32]
        coorxy2=[640-152,420+50]
        boton1=Boton('jugar','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('nivel','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\niveles_0.png',coorxy2)
        imagenboton2=boton2.ima
        for event in pygame.event.get():
            screen.blit(portada, [0, 0])
            coorxy=[640-152,420-32]
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            ###print('intro')
            #SALIR
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:

                #NIVEL 1
                if boton1.mouse==True:
                    global timer_limit
                    global inicio
                    global tiempotutorial
                    timer_limit=100
                    inicio=time.time()
                    tiempotutorial=time.time()
                    self.state= 'videoCoulomb'

                #MENÚ NIVELES
                if boton2.mouse==True:
                    inicio=time.time()
                    self.state='niveles'
        pygame.display.flip()
    def gameover(self):
        global done
        ##print('aqui hay ejecucion-----------------------------------')
        screen.blit(game_over,(0,0))
        coorxy=[482,544]
        boton1=Boton('salir','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\salir_0.png',coorxy)
        imagenboton1=boton1.ima
        screen.blit(imagenboton1,coorxy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:

                    self.state='salir'
        pygame.display.flip()

    def tutorial(self):
        global done
        global tiempotutorial
        global inicio
        coorxy=[900,500]
        t=time.time()-tiempotutorial
        ##print(int(t))
        boton1=Boton('jugar','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\continuar_0.png',coorxy)
        imagenboton1=boton1.ima
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if t<10:
            screen.blit(tutorial, [0, 0])
            pygame.display.flip()
        if int(t)>20:
            screen.blit(imagenboton1,coorxy)
        if t>10:
            screen.blit(tutorial2, [0, 0])
            if int(t)>20:
                screen.blit(imagenboton1,coorxy)
            pygame.display.flip()

        if int(t)>20:            ###print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if boton1.mouse==True:
                        global timer_limit
                        global inicio
                        timer_limit=40
                        inicio=time.time()

                        carga1pos_pos=pos('positivo',[2,1])
                        carga2pos_pos=pos('positivo', [5,5])

                        carga3pos_pos=pos('positivo', [4,2])
                        carga1neg_pos = pos('negativo', [3,6])
                        carga2neg_pos = pos('negativo', [7,3])

                        carga1net_pos=pos('neutro', [3,5])
                        carga2net_pos= pos('neutro', [1,5])

                        playerpos=pos('personaje',[0,0])
                        maquinapos=pos('maquina', [6,2])
                        inicio=time.time()
                        self.state='nivel_1'
                        pygame.display.flip()
            ##print(self.state)
        pygame.display.flip()

    def info(self):
        global done
        coorxy=[482,232]
        boton1=Boton('continuar','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\continuar_0.png',coorxy)
        imagenboton1=boton1.ima
        for event in pygame.event.get():

            screen.blit(menu_pausa, [0, 0])
            screen.blit(tutorial, [0, 0])
            coorxy=[482,232]
            screen.blit(imagenboton1,coorxy)
            #SALIR
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    if n == 1:
                        self.state='nivel_1'
                    if n == 2:
                        self.state='nivel_2'
                    if n == 3:
                        self.state='nivel_3'
                    if n == 4:
                        self.state='nivel_4'
                    if n == 5:
                        self.state='nivel_5'

        pygame.display.flip()
    #GENERA MENÚ NIVELES
    def niveles(self):
        global done
        global carga1pos_pos
        global carga2pos_pos
        global carga3pos_pos
        global carga4pos_pos
        global carga1neg_pos
        global carga2neg_pos
        global carga3neg_pos
        global carga4neg_pos
        global carga1net_pos
        global carga2net_pos
        global carga3net_pos
        global carga4net_pos
        global pinicial

        global playerpos
        global pinicial

        global timer_limit
        global inicio

        #COORDENADAS DE LOS BOTONES DE LOS NIVELES
        coorxy=[192,232]
        coorxy2=[192+153,232]
        coorxy3=[192+(153*2),232]
        coorxy4=[192+(153*3),232]
        coorxy5=[192+(153*4),232]

        #BOTONES
        boton1=Boton('n1','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\1_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('n2','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\2_0.png',coorxy2)
        imagenboton2=boton2.ima
        boton3=Boton('n3','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\3_0.png',coorxy3)
        imagenboton3=boton3.ima
        boton4=Boton('n4','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\4_0.png',coorxy4)
        imagenboton4=boton4.ima
        boton5=Boton('n5','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\5_0.png',coorxy5)
        imagenboton5=boton5.ima


        for event in pygame.event.get():
            screen.blit(fondo_niveles, [0, 0])
            #coorxy=[492,232]
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            screen.blit(imagenboton3,coorxy3)
            screen.blit(imagenboton4,coorxy4)
            screen.blit(imagenboton5,coorxy5)
            if event.type == pygame.QUIT:
                done = True

            if event.type==pygame.MOUSEBUTTONDOWN:

                #BOTÓN NIVEL 1
                if boton1.mouse==True:

                    timer_limit=40
                    inicio=time.time()
                    pinicial=1

                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])

                    carga3pos_pos=pos('positivo', [4,2])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])

                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])

                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [6,2])
                    self.state="nivel_1"

                #BOTÓN NIVEL 2
                if boton2.mouse==True:

                    pinicial=2
                    timer_limit=70
                    inicio=time.time()

                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [4,1])
                    carga3neg_pos = pos('negativo', [0,7])
                    carga4neg_pos = pos('negativo', [3,2])
                    carga1net_pos= pos('neutro', [1,5])
                    carga2net_pos= pos('neutro', [1,7])
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [7,1])
                    self.state='nivel_2'

                #BOTÓN NIVEL 3
                if boton3.mouse==True:
                    pinicial=2
                    timer_limit=40
                    inicio=time.time()
                    inicio=time.time()

                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    carga3pos_pos=pos('positivo', [4,2])
                    carga4pos_pos=pos('positivo', [4,7])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    carga3net_pos= pos('neutro', [2,7])

                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [7,6])
                    self.state='nivel_3'

                #BOTÓN NIVEL 4
                if boton4.mouse==True:
                    pinicial=2
                    timer_limit=30
                    inicio=time.time()


                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [0,3])
                    carga3neg_pos = pos('negativo', [1,7])
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    carga3net_pos=pos('neutro', [2,7])
                    carga4net_pos= pos('neutro', [4,1])

                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [7,2])
                    self.state='nivel_4'

                #BOTÓN NIVEL 5
                if boton5.mouse==True:
                    pinicial=3
                    timer_limit=30
                    inicio=time.time()

                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    carga3pos_pos=pos('positivo',[0,1])
                    carga4pos_pos=pos('positivo', [5,7])
                    carga1neg_pos = pos('negativo', [3,7])
                    carga2neg_pos = pos('negativo', [2,6])
                    carga3neg_pos = pos('negativo', [4,1])
                    carga1net_pos=pos('neutro', [0,5])
                    carga2net_pos=pos('neutro', [7,7])
                    carga3net_pos=pos('neutro', [6,1])
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [7,4])
                    self.state='nivel_5'
        pygame.display.flip()

    def salir(self):
        self.state='intro'
        pygame.display.flip()

    def ganaste(self):
        global done
        coorxy=[482,102]
        boton1=Boton('salir','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\salir_0.png',coorxy)
        imagenboton1=boton1.ima
        for event in pygame.event.get():
            screen.blit(fondo_ganaste, [0, 0])
            screen.blit(imagenboton1,coorxy)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                   self.state='salir'

        pygame.display.flip()

    def menu_pausa(self):
        global done
        coorxy=[482,232]
        coorxy2=[482,328]
        coorxy3=[482,424]
        boton1=Boton('continuar','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\continuar_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('nivel','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\niveles_0.png',coorxy2)
        imagenboton2=boton2.ima
        boton3=Boton('salir','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\niveles_0.png',coorxy3)
        imagenboton3=boton3.ima
        for event in pygame.event.get():
            screen.blit(menu_pausa, [0, 0])
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            screen.blit(imagenboton3,coorxy3)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    if n == 1:
                        self.state='nivel_1'
                    if n == 2:
                        self.state='nivel_2'
                    if n == 3:
                        self.state='nivel_3'
                    if n == 4:
                        self.state='nivel_4'
                    if n == 5:
                        self.state='nivel_5'

                if boton2.mouse==True:
                    self.state='niveles'

                if boton3.mouse==True:
                    self.state='salir'
        pygame.display.flip()

    def nivel_1(self):
        ##print('esto es un ciclo----------------------------------------------------------------')
        pygame.display.flip()
        #Cositas para el Reloj
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit
        global inicio
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        global pinicial
        n = 1

        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        ###print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        #counter=timer_font.render(pinicial,True,(255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos,carga1net_pos]
          #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]

        for event in pygame.event.get():
            ###print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    self.state='menu_pausa'
                if boton4.mouse==True:
                    self.state='info'
            screen.blit(fondo1, [0, 0])


            #print(sentido, '=================================>')
            player=Player('player',playerpos.posxn,playerpos.posyn, playerpos.ingame,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn),carga1pos_pos.ingame)
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn),carga2pos_pos.ingame)
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn),carga1neg_pos.ingame)
            carga4=Objeto('neutro', (carga1net_pos.posxn), (carga1net_pos.posyn),carga1net_pos.ingame)
            maquina=Objeto('maquina', (maquinapos.posxn-1), (maquinapos.posyn-1),maquinapos)
            ###print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha(), (390,110))
            screen.blit(UI,[0,0])
            screen.blit(maquina.image, maquina.posip)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(carga4.image, carga4.posip)

            if event.type == pygame.KEYDOWN:

              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    #print(sentido)
                    sentido='down'
                    #print(sentido)
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger
              if event.key == pygame.K_SPACE:
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  ##print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      ###print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      ###print(parent,dx,dy)
              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  ###print('grab false')
              if grab==True:
                player.grab=True


              if player.grab==True:
                  ##print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)


            proton=proximomaquinap(L,(maquinapos.posxn),(maquinapos.posyn))
            electron=proximomaquinae(L,(maquinapos.posxn),(maquinapos.posyn))
            neutron=proximomaquinan(L,(maquinapos.posxn),(maquinapos.posyn))
            ##print(pinicial)
            if proton!=None and electron!=None and neutron!=None:
                contador=atomo(maquinapos,proton,electron,neutron,pinicial,proximo,player)
            else:
                contador=None
            if contador!=None:
                pinicial=contador
            ##print(pinicial)
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        counter=timer_font.render(datetime.utcfromtimestamp(pinicial).strftime('%S'),True,(255, 255, 255))
        if pinicial==0:
            for i in L:
                i.ingame=True
            global x
            x=0
            self.state='videoc_1'
        ##print(timer_sec)
        if timer_sec==0:
            ##print('llega aqui----------------------------------')
            self.state='gameover'
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1085, 18])
        screen.blit(counter, [1085-230, 18])
        pygame.display.flip()

    def nivel_2(self):
        pygame.display.flip()
        #Cositas para el Reloj
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit
        global inicio
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        global pinicial
        n = 2

        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        ###print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        #counter=timer_font.render(pinicial,True,(255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png',coorxy2)
        imagenboton4=boton4.ima
        #L=[carga1neg_pos, carga2neg_pos, carga3neg_pos, carga4neg_pos, carga1pos_pos, carga2pos_pos, carga1net_pos, carga2net_pos]
        L=[carga1neg_pos, carga2neg_pos, carga1pos_pos, carga2pos_pos, carga1net_pos, carga2net_pos]
          #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]

        for event in pygame.event.get():
            ###print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    self.state='menu_pausa'
                if boton4.mouse==True:
                    self.state='info'
            screen.blit(fondo2, [0, 0])


            ##print(playerpos.ingame)
            player=Player('player',playerpos.posxn,playerpos.posyn, playerpos.ingame,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn),carga1pos_pos.ingame)
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn),carga2pos_pos.ingame)
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn),carga1neg_pos.ingame)
            carga4=Objeto('negativo', (carga2neg_pos.posxn), (carga2neg_pos.posyn),carga2neg_pos.ingame)
            #carga5=Objeto('negativo', (carga3neg_pos.posxn), (carga3neg_pos.posyn),carga3neg_pos.ingame)
            #carga6=Objeto('negativo', (carga4neg_pos.posxn), (carga4neg_pos.posyn),carga4neg_pos.ingame)
            carga7=Objeto('neutro', (carga1net_pos.posxn), (carga1net_pos.posyn),carga1net_pos.ingame)
            carga8=Objeto('neutro', (carga2net_pos.posxn), (carga2net_pos.posyn),carga2net_pos.ingame)
            maquina=Objeto('maquina', (maquinapos.posxn-1), (maquinapos.posyn-1),maquinapos)

            ###print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha(), (390,110))
            screen.blit(UI,[0,0])
            screen.blit(maquina.image, maquina.posip)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(carga4.image, carga4.posip)
            #screen.blit(carga5.image,carga5.posip)
            #screen.blit(carga6.image,carga6.posip)
            screen.blit(carga7.image, carga7.posip)
            screen.blit(carga8.image, carga8.posip)
            if event.type == pygame.KEYDOWN:

              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

              if event.key == pygame.K_SPACE:
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  ###print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      ###print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      ###print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  ###print('grab false')
              if grab==True:
                player.grab=True
              if player.grab==True:
                  ##print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

            proton=proximomaquinap(L,(maquinapos.posxn),(maquinapos.posyn))
            electron=proximomaquinae(L,(maquinapos.posxn),(maquinapos.posyn))
            neutron=proximomaquinan(L,(maquinapos.posxn),(maquinapos.posyn))
            ##print(pinicial,' coooooooooooooooooontador')
            if proton!=None and electron!=None and neutron!=None:
                contador=atomo(maquinapos,proton,electron,neutron,pinicial,proximo,player)
                ##print('proton--',proton.posxn,proton.posyn,'estadoooo----- ingame',proton.ingame)
                ##print('electron--',electron.posxn,electron.posyn,'estadoooo----- ingame',electron.ingame)
                ##print('neutron--',neutron.posxn,neutron.posyn,'estadoooo----- ingame',neutron.ingame)
                proton=None
                electron=None
                neutron=None
            else:
                contador=None
            if contador!=None:
                pinicial=contador
            ###print(pinicial)
            #Relo
            if contador!=None:
                pinicial=contador
            ###print(pinicial)
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        counter=timer_font.render(datetime.utcfromtimestamp(pinicial).strftime('%S'),True,(255, 255, 255))
        if pinicial==0:
            for i in L:
                i.ingame=True
            global x
            x=0
            self.state='videoc_2'
        ##print(timer_sec)
        if timer_sec==0:
            ##print('llega aqui----------------------------------')
            self.state='gameover'
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1085, 18])
        screen.blit(counter, [1085-230, 18])
        pygame.display.flip()


    def nivel_3(self):
        pygame.display.flip()
        #Cositas para el Reloj
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit
        global inicio
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        global pinicial
        n = 3

        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        ###print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        #counter=timer_font.render(pinicial,True,(255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga2neg_pos, carga1pos_pos, carga2pos_pos,carga3pos_pos, carga4pos_pos, carga1net_pos, carga2net_pos, carga3net_pos]
          #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]

        for event in pygame.event.get():
            ###print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    self.state='menu_pausa'
                if boton4.mouse==True:
                    self.state='info'
            screen.blit(fondo3, [0, 0])


            ##print(playerpos.ingame)
            player=Player('player',playerpos.posxn,playerpos.posyn, playerpos.ingame,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn),carga1pos_pos.ingame)
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn),carga2pos_pos.ingame)
            carga3=Objeto('positivo',(carga3pos_pos.posxn),(carga3pos_pos.posyn),carga3pos_pos.ingame)
            carga4=Objeto('positivo',(carga4pos_pos.posxn),(carga4pos_pos.posyn),carga4pos_pos.ingame)
            carga5=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn),carga1neg_pos.ingame)
            carga6=Objeto('negativo', (carga2neg_pos.posxn), (carga2neg_pos.posyn),carga2neg_pos.ingame)
            carga7=Objeto('neutro', (carga1net_pos.posxn), (carga1net_pos.posyn),carga1net_pos.ingame)
            carga8=Objeto('neutro', (carga2net_pos.posxn), (carga2net_pos.posyn),carga2net_pos.ingame)
            carga9=Objeto('neutro', (carga3net_pos.posxn), (carga3net_pos.posyn),carga3net_pos.ingame)
            maquina=Objeto('maquina', (maquinapos.posxn-1), (maquinapos.posyn-1),maquinapos)

            ###print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha(), (390,110))
            screen.blit(UI,[0,0])
            screen.blit(maquina.image, maquina.posip)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(carga4.image, carga4.posip)
            screen.blit(carga5.image,carga5.posip)
            screen.blit(carga6.image,carga6.posip)
            screen.blit(carga7.image, carga7.posip)
            screen.blit(carga8.image, carga8.posip)
            screen.blit(carga9.image, carga9.posip)

            if event.type == pygame.KEYDOWN:

              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger



              if event.key == pygame.K_SPACE:
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  ##print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      ###print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      ###print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  ###print('grab false')



              if grab==True:
                player.grab=True


              if player.grab==True:
                  ##print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
            proton=proximomaquinap(L,(maquinapos.posxn),(maquinapos.posyn))
            electron=proximomaquinae(L,(maquinapos.posxn),(maquinapos.posyn))
            neutron=proximomaquinan(L,(maquinapos.posxn),(maquinapos.posyn))
            ##print(pinicial)

            if proton!=None and electron!=None and neutron!=None:
                contador=atomo(maquinapos,proton,electron,neutron,pinicial,proximo,player)
            else:
                contador=None
            if contador!=None:
                pinicial=contador
            ##print(pinicial)
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        counter=timer_font.render(datetime.utcfromtimestamp(pinicial).strftime('%S'),True,(255, 255, 255))
        if pinicial==0:
            for i in L:
                i.ingame=True
            global x
            x=0
            self.state='videoc_3'

        ##print(timer_sec)
        if timer_sec==0:
            ##print('llega aqui----------------------------------')
            self.state='gameover'
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1085, 18])
        screen.blit(counter, [1085-230, 18])
        pygame.display.flip()

    def nivel_4(self):
        pygame.display.flip()
        #Cositas para el Reloj
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit
        global inicio
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        global pinicial
        n = 4

        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        ###print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        #counter=timer_font.render(pinicial,True,(255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga2neg_pos, carga3neg_pos, carga1pos_pos, carga2pos_pos, carga1net_pos, carga2net_pos, carga3net_pos, carga4net_pos]
          #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]

        for event in pygame.event.get():
            ###print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    self.state='menu_pausa'
                if boton4.mouse==True:
                    self.state='info'
            screen.blit(fondo4, [0, 0])


            ##print(playerpos.ingame)
            player=Player('player',playerpos.posxn,playerpos.posyn, playerpos.ingame,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn),carga1pos_pos.ingame)
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn),carga2pos_pos.ingame)
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn),carga1neg_pos.ingame)
            carga4=Objeto('negativo', (carga2neg_pos.posxn), (carga2neg_pos.posyn),carga2neg_pos.ingame)
            carga5=Objeto('negativo', (carga3neg_pos.posxn), (carga3neg_pos.posyn),carga3neg_pos.ingame)
            carga6=Objeto('neutro', (carga1net_pos.posxn), (carga1net_pos.posyn),carga1net_pos.ingame)
            carga7=Objeto('neutro', (carga2net_pos.posxn), (carga2net_pos.posyn),carga2net_pos.ingame)
            carga8=Objeto('neutro', (carga3net_pos.posxn), (carga3net_pos.posyn),carga3net_pos.ingame)
            carga9=Objeto('neutro', (carga4net_pos.posxn), (carga4net_pos.posyn),carga4net_pos.ingame)
            maquina=Objeto('maquina', (maquinapos.posxn-1), (maquinapos.posyn-1),maquinapos)

            ###print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha(), (390,110))
            screen.blit(UI,[0,0])
            screen.blit(maquina.image, maquina.posip)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(carga4.image, carga4.posip)
            screen.blit(carga5.image,carga5.posip)
            screen.blit(carga6.image,carga6.posip)
            screen.blit(carga7.image, carga7.posip)
            screen.blit(carga8.image, carga8.posip)
            screen.blit(carga9.image, carga9.posip)

            if event.type == pygame.KEYDOWN:

              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger



              if event.key == pygame.K_SPACE:
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  ##print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      ###print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      ###print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  ###print('grab false')



              if grab==True:
                player.grab=True


              if player.grab==True:
                  ##print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

            proton=proximomaquinap(L,(maquinapos.posxn),(maquinapos.posyn))
            electron=proximomaquinae(L,(maquinapos.posxn),(maquinapos.posyn))
            neutron=proximomaquinan(L,(maquinapos.posxn),(maquinapos.posyn))
            ##print(pinicial)
            if proton!=None and electron!=None and neutron!=None:
                contador=atomo(maquinapos,proton,electron,neutron,pinicial,proximo,player)
            else:
                contador=None
            if contador!=None:
                pinicial=contador
            ##print(pinicial)
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        counter=timer_font.render(datetime.utcfromtimestamp(pinicial).strftime('%S'),True,(255, 255, 255))
        if pinicial==0:
            for i in L:
                i.ingame=True
            global x
            x=0
            self.state= 'videoc_4'

        ##print(timer_sec)
        if timer_sec==0:
            ##print('llega aqui----------------------------------')
            self.state='gameover'
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1085, 18])
        screen.blit(counter, [1085-230, 18])
        pygame.display.flip()


    def nivel_5(self):
        pygame.display.flip()
        #Cositas para el Reloj
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit
        global inicio
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        global pinicial
        n = 5

        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        ###print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        #counter=timer_font.render(pinicial,True,(255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga2neg_pos, carga3neg_pos, carga1pos_pos, carga2pos_pos, carga3pos_pos, carga4pos_pos, carga1net_pos, carga2net_pos, carga3net_pos]
          #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]

        for event in pygame.event.get():
            ###print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    self.state='menu_pausa'
                if boton4.mouse==True:
                    self.state='info'
            screen.blit(fondo5, [0, 0])


            ##print(playerpos.ingame)
            player=Player('player',playerpos.posxn,playerpos.posyn, playerpos.ingame,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn),carga1pos_pos.ingame)
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn),carga2pos_pos.ingame)
            carga3=Objeto('positivo',(carga3pos_pos.posxn),(carga3pos_pos.posyn),carga3pos_pos.ingame)
            carga4=Objeto('positivo',(carga4pos_pos.posxn),(carga4pos_pos.posyn),carga4pos_pos.ingame)
            carga5=Objeto('negativo',(carga1neg_pos.posxn), (carga1neg_pos.posyn),carga1neg_pos.ingame)
            carga6=Objeto('negativo',(carga2neg_pos.posxn), (carga2neg_pos.posyn),carga2neg_pos.ingame)
            carga7=Objeto('negativo', (carga3neg_pos.posxn), (carga3neg_pos.posyn),carga3neg_pos.ingame)
            carga8=Objeto('neutro', (carga1net_pos.posxn), (carga1net_pos.posyn),carga1net_pos.ingame)
            carga9=Objeto('neutro', (carga2net_pos.posxn), (carga2net_pos.posyn),carga2net_pos.ingame)
            carga10=Objeto('neutro', (carga3net_pos.posxn), (carga3net_pos.posyn),carga3net_pos.ingame)
            maquina=Objeto('maquina', (maquinapos.posxn-1), (maquinapos.posyn-1),maquinapos)

            ###print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\tablero MK II.png").convert_alpha(), (390,110))
            screen.blit(UI,[0,0])
            screen.blit(maquina.image, maquina.posip)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(carga4.image, carga4.posip)
            screen.blit(carga5.image,carga5.posip)
            screen.blit(carga6.image,carga6.posip)
            screen.blit(carga7.image, carga7.posip)
            screen.blit(carga8.image, carga8.posip)
            screen.blit(carga9.image, carga9.posip)
            screen.blit(carga10.image, carga10.posip)

            if event.type == pygame.KEYDOWN:

              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger



              if event.key == pygame.K_SPACE:
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  ##print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      ###print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      ###print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  ###print('grab false')



              if grab==True:
                player.grab=True


              if player.grab==True:
                  ##print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

            proton=proximomaquinap(L,(maquinapos.posxn),(maquinapos.posyn))
            electron=proximomaquinae(L,(maquinapos.posxn),(maquinapos.posyn))
            neutron=proximomaquinan(L,(maquinapos.posxn),(maquinapos.posyn))
            ##print(pinicial)
            if proton!=None and electron!=None and neutron!=None:
                contador=atomo(maquinapos,proton,electron,neutron,pinicial,proximo,player)
            else:
                contador=None
            if contador!=None:
                pinicial=contador
            ##print(pinicial)
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        counter=timer_font.render(datetime.utcfromtimestamp(pinicial).strftime('%S'),True,(255, 255, 255))
        if pinicial==0:
            for i in L:
                i.ingame=True
            global x
            x=0
            self.state='videoc_5'
        ##print(timer_sec)
        if timer_sec==0:
            ##print('llega aqui----------------------------------')
            self.state='gameover'
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1085, 18])
        screen.blit(counter, [1085-230, 18])
        pygame.display.flip()

class pos():
    def __init__(self,tipo,pos):
        self.tipo=tipo
        self.pos=pos
        self.posxn=pos[0]
        self.posyn=pos[1]
        self.posn=[self.posxn,self.posyn]
        self.posp=m.trannp(self.posxn,self.posyn)
        self.grabbed = False
        self.ingame= True

    def changepos(self,dirc):
        if self.posxn!=7:
            if dirc=='down':
                self.posxn= self.posxn+1
        if self.posxn!=0:
            if dirc=='up':
                self.posxn= self.posxn-1
        if self.posyn!=7:
            if dirc=='right':
                self.posyn= self.posyn+1
        if self.posyn!=0:
            if dirc=='left':
                self.posyn= self.posyn-1
            self.posn=[self.posxn,self.posyn]


    def changeparent(self,obj,dirc,parent):

      ##print(parent,'parent')
      ##print(dirc,'direccion')

      #MOVIMIENTO HACIA ABAJO
      if dirc=='down':
        if self.posxn!=7:
            #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posxn= self.posxn+1
              obj.posxn= self.posxn
              ##print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posxn= self.posxn+1
              obj.posxn= self.posxn
              ##print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posxn= self.posxn+1
              obj.posxn=self.posxn-1
              ##print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje
            if parent=='abajo':
              if self.posxn!=6:
                self.posxn= self.posxn+1
                obj.posxn=self.posxn+1

              ##print('moviendo abajo',obj.posxn)



      if dirc=='up':
        if self.posxn!=0:
            #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posxn= self.posxn-1
              obj.posxn= self.posxn
              ##print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posxn= self.posxn-1
              obj.posxn= self.posxn
              ##print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              if self.posxn!=1:
                self.posxn= self.posxn-1
                obj.posxn=self.posxn-1
              ##print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje
            if parent=='abajo':
              self.posxn= self.posxn-1
              obj.posxn=self.posxn+1
              ##print('moviendo abajo',obj.posxn)



      if dirc=='right':
        if self.posyn!=7:
          #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posyn= self.posyn+1
              obj.posyn= self.posyn-1

              ##print('moviendo izquierda',obj.posyn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              if self.posyn!=6:
                self.posyn= self.posyn+1
                obj.posyn= self.posyn+1
              ##print('moviendo derecha',obj.posyn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              ##print('moviendo arriba',obj.posyn)
            #Carga abajo del personaje
            if parent=='abajo':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              ##print('moviendo abajo',obj.posyn)


      if dirc=='left':
        if self.posyn!=0:
          #Carga a la izquierda del personaje
            if parent=='izquierda':
              if self.posyn!=1:
                self.posyn= self.posyn-1
                obj.posyn= self.posyn-1
                ##print('moviendo izquierda',obj.posyn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posyn= self.posyn-1
              obj.posyn= self.posyn+1
              ##print('moviendo derecha',obj.posyn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn-1
              obj.posyn=self.posyn
              ##print('moviendo arriba',obj.posyn)
            #Carga abajo del personaje
            if parent=='abajo':
              self.posyn= self.posyn-1
              obj.posyn=self.posyn
              ##print('moviendo abajo',obj.posyn)




    def parent(self,obj):

        dy=self.posxn-obj.posxn
        dx=self.posyn-obj.posyn



        posobj=[0,0]
        if dx==1 and dy==0:
          parent='izquierda'
          obj.grabbed = True
          ##print('1')

        elif dx==-1 and dy==0 :
          parent='derecha'
          obj.grabbed = True
          ##print('2')

        elif dy==1 and dx==0:
          parent='arriba'
          obj.grabbed = True
          ##print('3')

        elif dy==-1 and dx==0:
          parent='abajo'
          obj.grabbed = True
          ##print('4')

        else:
          parent='no'

        return parent,dx,dy

        return posobj

def proximidad(L,posxn,posyn):
    encontrado=False
    for i in L:
        k=i.posxn
        j=i.posyn
        if i.ingame==True:
            ##print('posicion obj===',k,j,'posicion player===', posxn, posyn)

            if abs(k-posxn)==1 and abs(j-posyn)==0:
                ##print('k=',k, 'posxn=', posxn)
                return i

            if abs(j-posyn)==1 and abs(k-posxn)==0:
                ##print('j=',j, 'posyn=', posyn)
                return i

    else:
        return encontrado

def proximomaquinap(L,posxnm,posynm):
    ###print('llega a la funcion')

    positivo=None
    for i in L:
        if i.ingame==True:
            if i.posyn==posynm-1 and i.tipo=='positivo' and i.posxn==posxnm:
                positivo=i
            if positivo!=None:
                return positivo

def proximomaquinae(L,posxnm,posynm):
    ###print('llega a la funcion')
    negativo=None
    for i in L:
        if i.ingame==True:
            if i.posyn==posynm+1 and i.tipo=='negativo' and i.posxn==posxnm:
                negativo=i
            if negativo!=None:
                return negativo

def proximomaquinan(L,posxnm,posynm):
    ###print('llega a la funcion')
    neutro=None
    for i in L:
        if i.ingame==True:
            if i.posyn==posynm and i.tipo=='neutro' and i.posxn==posxnm-1:
                neutro=i
            if  neutro!=None:
                return neutro

def atomo(posm,posp,pose,posn,atomos,proximo,player):

    neutron=False
    electron=False
    proton=False
    if posp.ingame!=False and pose.ingame!=False and posn.ingame!=False:
        ###print(posm.posxn,'-',pose.posxn,'=0       ',posm.posyn,'-',pose.posyn,'===1')
        if posm.posxn-posn.posxn==1 and posm.posyn-posn.posyn==0:
            ###print('si es la distancia')
            if posn.tipo=='neutro':
                neutron=True

        if posm.posyn-posp.posyn==1 and posm.posxn-posp.posxn==0:
            ###print('si es la distancia',posp.tipo)
            if posp.tipo=='positivo':
                proton=True

        if posm.posyn-pose.posyn==-1 and posm.posxn-pose.posxn==0:
            ###print('si es la distancia',pose.tipo)
            if pose.tipo=='negativo':
                electron=True
                ###print('electro======>')

        if neutron==True and proton==True and electron==True:
            atomos=atomos-1
            posp.ingame=False
            pose.ingame=False
            posn.ingame=False
            player.grab=False
            proximo.grabbed = False
            ##print('===========//////////////////////////////////////////////////_________________________________________\\\\\\\\\\\\\\\\\\\\\\\\ atomo debe ser 2----',atomos)
            return atomos

#INTERACCIÓN OBJETO A OBJETO
def cercania(L):
  q=[]
  for i in L:
    q.append(i)
  for i in q:
    k=i.posxn
    j=i.posyn
    ###print('nuevo i', 'k=',k,'j=', j)
    for o in q:
      g= o.posxn
      h=o.posyn
      ###print('nuevo o', 'k=',k,'j=', j)
      if i.ingame==True and o.ingame==True:
    #REPELER

          #REPELER VERTICAL
          if abs(k-g)==1:   #uno esta encima del otro
            if abs(j-h)==0:
                if i.tipo!='neutro' and o.tipo!='neutro':

                  if i.tipo==o.tipo:

                    if i.posxn>o.posxn:
                      ##print('alejo')
                      if i.grabbed==False:
                          i.posxn=i.posxn+1
                      if o.grabbed==False:
                          o.posxn=o.posxn-1

                    if i.posxn<o.posxn:
                      ##print('alejo2')
                      if i.grabbed==False:
                          i.posxn=i.posxn-1
                      if o.grabbed==False:
                          o.posxn=o.posxn+1

                    ##print('repeler===>vertical',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))


                    q.remove(i)
                    q.remove(o)


          #REPELER HORIZONTAL
          if abs(j-h)==1:   #uno esta al lado del otro
            if abs(k-g)==0:

                if i.tipo!='neutro' and o.tipo!='neutro':

                  if i.tipo==o.tipo:

                    if i.posyn>o.posyn:
                      ##print('alejo')
                      if i.grabbed==False:
                          i.posyn=i.posyn+1
                      if o.grabbed==False:
                          o.posyn=o.posyn-1

                    if i.posyn<o.posyn:
                      ##print('alejo2')
                      if i.grabbed==False:
                          i.posyn=i.posyn-1
                      if o.grabbed==False:
                          o.posyn=o.posyn+1

                    ##print('repeler===>lados',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))


                    q.remove(i)
                    q.remove(o)
    #ACABA REPELER
    #ATRAER
         #ATRAER VERTICAL
          if abs(k-g)==2 and abs(j-h)==0:   #uno esta encima del otro
              if i.tipo!='neutro' and o.tipo!='neutro':
                  if i.tipo!=o.tipo:
                      if i.posxn>o.posxn:
                          ##print('atrae')
                          if i.grabbed==False:
                              i.posxn=i.posxn-1
                          if o.grabbed==False:
                             if i.posxn!=o.posxn+1:
                                 o.posxn=o.posxn+1

                      if i.posxn<o.posxn:
                          ##print('atare2')
                          if i.grabbed==False:
                              i.posxn=i.posxn+1
                          if o.grabbed==False:
                              if i.posxn!=o.posxn-1:
                                  o.posxn=o.posxn-1


                      ##print('atraer===>VERTICAL',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))

                      q.remove(i)
                      q.remove(o)


          #ATRAER HORIZONTAL
          if abs(j-h)==2 and abs(k-g)==0:

                if i.tipo!='neutro' and o.tipo!='neutro':

                  if i.tipo!=o.tipo:

                    if i.posyn>o.posyn:
                      ##print('atrae')
                      if i.grabbed==False:
                          i.posyn=i.posyn-1
                      if o.grabbed==False:
                          o.posyn=o.posyn+1

                    if i.posyn<o.posyn:
                      ##print('atrae2')
                      if i.grabbed==False:
                          i.posyn=i.posyn+1
                      if o.grabbed==False:
                          o.posyn=o.posyn-1

                    ##print('atraer===>LADOS',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))
                    ##print(i.grabbed, o.grabbed)

                    q.remove(i)
                    q.remove(o)

    #MISMA POSICIÓN
          ##print('tipo i=',i.tipo,'tipo o= ',o.tipo,i.posxn,'-',o.posxn,'===0               ',i.posyn,'-',o.posyn,'=====0')
          if i!=o:
              if abs(i.posxn-o.posxn)==0 and abs(i.posyn-o.posyn)==0:
                      pass

def equilibrio(l):
    q=cercania(l)
    if q!=l:
        equi=False
        ###print('equilibrio ============>', equi)
    if q==l:
        equi=True
        ###print('q y l son iguales')
        ###print('equilibrio ============>', equi)
timer_limit = 360
inicio=time.time()
sentido='0'
pinicial=1
game_state = Gamestate()
tiempotutorial=time.time()

carga1pos_pos=pos('positivo', [2,1])
carga2pos_pos=pos('positivo', [5,5])
carga3pos_pos=pos('positivo', [4,2])
carga4pos_pos=pos('positivo', [4,5])

carga1neg_pos = pos('negativo', [3,6])
carga2neg_pos = pos('negativo', [7,3])
carga3neg_pos = pos('negativo', [3,6])
carga4neg_pos = pos('negativo', [0,5])

carga1net_pos=pos('neutro', [3,5])
carga2net_pos= pos('neutro', [1,5])
carga3net_pos=pos('neutro', [1,7])
carga4net_pos= pos('neutro', [3,4])

maquinapos=pos('maquina', [6,4])

playerpos=pos('personaje',[0,0])



fondo2 = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\fondo2.png").convert()

portada = pygame.image.load("C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\assets\\title card.png").convert()

boton1a = pygame.image.load('C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_0.png').convert_alpha()
boton1b = pygame.image.load('C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_1.png').convert_alpha()
boton1 = Boton('jugar', 'C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\jugar_0.png', [640 - 152, 420 - 32])

UI = pygame.image.load('C:\\Users\\valer\\Desktop\\Prog\\electromag-main\\botones\\margenes.png').convert_alpha()

clock = pygame.time.Clock()

done = False
doneN=False
donep=False
donem=False
doned=False
doner=False
donel=False

parent = None

grab = False
proximo=False
###print(dir(Gamestate))
inicio=time.time()
while not done:

    game_state.cambia_nivel()
    clock.tick(60)


pygame.quit()
