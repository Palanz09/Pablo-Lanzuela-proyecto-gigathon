import time
import re
import random
import sys
import os
import subprocess
from turtle import *
from math import *
verde = "\033[38;2;0;255;120m"
reset = "\033[0m"

class Traje_Astronauta:
    def __init__(self,oxigeno,llave):
        self.oxigeno=oxigeno
        self.llave=llave
class Cohete:
    def __init__(self,oxigeno,combustible,vida,x,y,ang):
        self.oxigeno=oxigeno
        self.vida=vida
        self.combustible=combustible
        self.x = x
        self.y = y
        self.ang = ang
        self.id = []
class persona:
    def __init__(self,x,y,vehiculo,vida):
        self.x=x
        self.y=y
        self.vehiculo = vehiculo
        self.vida = vida
        self.id = []
        self.inventario = []
class Enemigo:
    def __init__(self,x,y,tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.id = []
class Cofre:
    def __init__(self,x,y,contenido):
        self.x = x
        self.y = y
        self.contenido =contenido
        self.id = []
class Botiquines:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.id = []
class Puertas:
    def __init__(self):
        self.id = []
class Habitacion:
    def __init__(self,x,y,w,h,anterior,estado,i):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.anterior=anterior
        self.estado=estado
        self.i=i
        self.puertas = []
    def centro (self):
        return (self.x+self.w//2, self.y+self.h//2)
    def colisiona(self, otra):
        return (
            self.x < otra.x + otra.w and
            self.x + self.w > otra.x and
            self.y < otra.y + otra.h and
            self.y + self.h > otra.y)
    def unir (self, otra):
        x,y = self.centro ()
        X,Y = otra.centro ()
        dx = x-X
        dy = y-Y
        pasillo = []
        for dxx in range (abs (dx)):
            if dx > 0:
                pasillo.append ((X+dxx,Y))
            elif dx < 0:
                pasillo.append ((X-dxx,Y))
        for dyy in range (abs (dy)):
            if dy > 0:
                pasillo.append ((x,Y+dyy))
            elif dy < 0:
                pasillo.append ((x,Y-dyy))
        return pasillo
class Asteroide:
    def __init__(self,x,velocidad):
        self.x = x
        self.v = velocidad
        self.id = []
def main():
    global dificultad,angulo,p,cohete,nombre_nave,nombre_expedicion,xi,yi,eventos_destacados,nombre_persona
    eventos_destacados = []
    print (verde, end="")
    if len (sys.argv) > 1 and sys.argv[1].strip():
        nombre_persona = sys.argv[1].strip().title()
        print ()
        printt (f"Bienvenido de nuevo, {nombre_persona}. Ya sabes en que consiste la misión, así que comencemos cuanto antes.")
    else:
        nombre_persona = input ("¿Cómo se llama?: ").title()
        if nombre (nombre_persona) == False: 
            printt ("Hmm, conque quiere mantener su nombre en el anonimato")
            nombre_persona = "Agente secreto"
        texto = (f"Hola {nombre_persona}, usted es la última esperanza para la humanidad. Algo horrible va a ocurrir en Marte y es el único que puede evitarlo gracias a su puesto como conserje en la NASA.")
        printt (texto)
        texto = ("Ahora no hay tiempo para más explicaciones, si desea ayudarnos introduzca a continuación sus coordenadas y el nombre de la nave que va a tomar.")
        printt (texto)
        texto= ("Si por el contrario rechaza nuestra propuesta, rece por la salvación de su alma, porque acabará de condenar a toda la humanidad.")
        printt (texto) 
    while True: 
        nombre_expedicion = (input ("Nombre de la expedición: "))
        if nombre_expedicion == "": printt ("No aceptar la misión no es una opción")
        else: break
    while True:
        nombre_nave = (input ("Nave: "))
        if nombre_nave == "": printt ("Sin una nave no va a llegar muy lejos")
        else: break
    while True:
        try: 
            xy= input ("Coordenadas (x,y): ")
            x,y = map (int, re.findall(r"-?\d+(?:\d+)?", xy))
            if 0< x < 100 and 0<y<100:break
            else: printt ("Revise esas coordenadas, su edificio se encuentra entre el (1,1) y el (99,99)")
        except:
            printt ("Coordenadas no válidas")
            time.sleep (0.2)
    while True:
        try: 
            dificultad = int (input ("Nivel de seguridad (1-5): "))
            if 1 <= dificultad <= 5:break
            else: printt ("El número debe estar entre 1 y 5")
        except: printt ("Ingrese un número")
    p = persona (x,y,"humano",100-5*(dificultad-1))
    xi,yi=p.x,p.y
    for _ in range (3):
        n = 0.5 # Escribir 0.5
        print ("Hackeando   ", end= "\r", flush=True)
        time.sleep (n)
        print ("Hackeando.", end= "\r", flush=True)
        time.sleep (n)
        print ("Hackeando..", end= "\r", flush=True)
        time.sleep (n)
        print ("Hackeando...", end= "\r", flush=True)
        time.sleep (n)
    printt ("He conseguido descargar un mapa del edificio y le he desbloqueado todas las puertas que he podido, debería aparecerle en su teléfono")
    crear_mapa (p)
    rellenar_habitaciones ()
    dibujar_mapa (p)
    printt ("No logro localizar su nave, si me pudiera indicar los niveles de oxígeno y de gasolina")
    cohete = Cohete ("","","",10,0,"")
    while True:
        try:
            oxigeno = int (input ("Oxígeno (min.150): "))
            if oxigeno >= 150: 
                cohete.oxigeno = oxigeno - 5*dificultad
                break
            else: printt ("Por favor, sea más colaborativo e introduzca un número válido")
        except: printt ("Por favor, sea más colaborativo e introduzca un número válido")
    while True:
        try:
            combustible = int (input ("Combustible (min.100): "))
            if combustible >= 100: 
                cohete.combustible = combustible - 5*dificultad
                break
            else: printt ("Por favor, sea más colaborativo e introduzca un número válido")
        except: printt ("Por favor, sea más colaborativo e introduzca un número válido")
    cohete.vida = 200 - 20*dificultad
    printt ("Para finalizar, indíqueme hacia donde se encuentra mirando y comenzará su misión")
    while True:
        angulo_introducido = input ("Ángulo: ").strip ()
        nums = re.findall(r"-?\d+", angulo_introducido)
        if not nums:
            printt("Por favor, introduzca un ángulo válido")
            continue
        else: break
    angulo = int(nums[0])
    angulo = angulo%360
    cohete.ang = angulo
    n=4 # poner 4
    printt (f"\033[1m Etapa 1 de {nombre_expedicion}:\033[0m\033[38;2;0;255;120m alcanzar el {nombre_nave}")
    time.sleep (n)
    printt (f"\033[1m Posición inicial:\033[0m\033[38;2;0;255;120m ({p.x},{p.y})")
    time.sleep (n)
    printt (f"\033[1m Ángulo inicial:\033[0m\033[38;2;0;255;120m {angulo}º")
    time.sleep (n)
    printt (f"\033[1m Combustible del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.combustible}/{cohete.combustible+5*dificultad} (ha habido una revisión técnica que ha gastado parte del combustible que me dijo que había)")
    time.sleep (n)
    printt (f"\033[1m Oxígeno del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.oxigeno}/{cohete.oxigeno+5*dificultad} (ha habido una revisión técnica que ha gastado parte del oxígeno que me dijo que había)")
    time.sleep (n)
    printt (f"\033[1m Estado del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.vida}/200 (un accidente durante la revisión técnica ha dañado el escudo térmico, pero no supondrá un problema si pilota con cuidado)")
    time.sleep (n)
    printt (f" Se encuentra encerrado en un edificio, por lo que los límites del mundo van de (0,0) a (99,99), aunque hay paredes que le bloquearán el paso")
    time.sleep (n)
    printt (f" Para finalizar la Etapa 1 debe encontrar la tarjeta de acceso a la lanzadera e ir al andén de la misma para llegar hasta su nave. \033[1mSuerte!!!\033[0m\033[38;2;0;255;120m")
    time.sleep (n)
    bucle_principal ()
def crear_mapa (p):
    global habitaciones
    global cuadricula
    global guardias
    global cofres
    global botiquines
    global bloqueos
    global salida
    global muro_lateral,muro_frontal
    guardias = []
    cofres = []
    botiquines = []
    bloqueos = []
    habitaciones = []
    salida = []
    muro_lateral = []
    muro_frontal = []
    cuadricula = {}
    for x in range(-100, 101):
        for y in range(-100, 101):
            if x < 0 and y >= 0:
                cuadricula [x,y] = "cesped"
            elif x >= 0 and y < 0:
                cuadricula [x,y] = "mar"
            else:
                cuadricula [x,y] = "muro"
    #habitación principal
    w, h = 20, 20
    if not 90>p.x>10:
        x0 = max(0, p.x - 18)
    else: x0=p.x-10
    if not 90>p.y>10:
        y0 = max(0, p.y - 18)
    else: y0=p.y-10
    nuevas_habitaciones = []
    hab_0 = Habitacion (x0,y0,w,h,0,"","")
    habitaciones.append (hab_0)
    ultimax,ultimay,ultimaw,ultimah = int (x0),int (y0),int (w),int (h)
    valida = False
    n=0
    while True:
        for _ in range (40):
            tipo = random.choice (("x","y"))
            w = random.randint (10,20)
            h = random.randint (10,20)
            if tipo == "x":
                tipo1 = random.choice (("izquierda","derecha"))
                if tipo1 == "derecha":
                    x0 = ultimax + ultimaw + 1
                    tipo2 = random.choice (("arriba","abajo"))
                    if tipo2 == "arriba":
                        y0 = ultimay + ultimah - random.randint (h//2-1,h-3)
                    elif tipo2 == "abajo":
                        y0 = ultimay - random.randint (h//2-1,h-3)
                elif tipo1 == "izquierda":
                    x0 = ultimax - w - 1
                    tipo2 = random.choice (("arriba","abajo"))
                    if tipo2 == "arriba":
                        y0 = ultimay + ultimah - random.randint (h//2-1,h-3)
                    elif tipo2 == "abajo":
                        y0 = ultimay - random.randint (h//2-1,h-3)
            elif tipo == "y":
                tipo1 = random.choice (("arriba","abajo"))
                if tipo1 == "arriba":
                    y0 = ultimay + ultimah + 1
                    tipo2 = random.choice (("izquierda","derecha"))
                    if tipo2 == "derecha":
                        x0 = ultimax + ultimaw - random.randint (w//2-1,w-3)
                    elif tipo2 == "izquierda":
                        x0 = ultimax - random.randint (w//2-1,w-3)
                elif tipo1 == "abajo":
                    y0 = ultimay - h - 1
                    tipo2 = random.choice (("izquierda","derecha"))
                    if tipo2 == "derecha":
                        x0 = ultimax + ultimaw - random.randint (w//2-1,w-3)
                    elif tipo2 == "izquierda":
                        x0 = ultimax - random.randint (w//2-1,w-3)
            temporal = Habitacion (x0,y0,w,h,"","","")
            for hab in habitaciones:
                if hab.colisiona (temporal) == True or x0<0 or y0<0 or x0+w>100 or y0+h>100: 
                    valida = False
                    break
                valida = True
            if valida == True:
                nueva = Habitacion (x0,y0,w,h,n,"","")
                habitaciones.append (nueva)
                nuevas_habitaciones.append (nueva)
                valida = False
        if len (nuevas_habitaciones) == 0: break
        else: 
            habit= nuevas_habitaciones.pop (0)
            n = habitaciones.index (habit)
            ultimax,ultimay,ultimaw,ultimah = habit.x,habit.y,habit.w,habit.h
    for hab in habitaciones:
        for i in range(hab.w):
            for j in range(hab.h):
                if i == 0 or i == hab.w-1 or j == 0 or j == hab.h-1:
                    pass
                else:
                    cuadricula[(hab.x+i, hab.y+j)] = "suelo"
    for hab in habitaciones:
        pasillo = hab.unir (habitaciones[hab.anterior])
        for celda in pasillo:
            x,y = celda
            if cuadricula[(x, y)] == "muro": cuadricula[(x, y)] = "suelo_pasillo"
            else: cuadricula[(x, y)] = "suelo"
    cuadricula [(p.x, p.y)] = "jugador"
def rellenar_habitaciones ():
    imax = 0
    for hab in habitaciones:
        i=1
        habb = hab
        while True:
            if habb.anterior <= 0: break
            else:
                i+=1
                habb = habitaciones [habb.anterior]
        hab.i=i
        imax = max (i,imax)
    primera_maxed = True
    salida = False
    n=0
    spawn = True
    opciones = ["lanza granadas", "armadura", "totem inmortalidad", "escudo burbuja"]
    for hab in habitaciones:
        if hab.x < 8 and salida == False:
            hab.estado = "salida"
            salida = True
            if spawn == True: spawn=False
        elif spawn == True: spawn=False
        elif hab.i < 4:
            hab.estado = random.choice (["laberinto","guardias","llave"])
            if hab.estado == "llave" and n==0: n+=1
            elif n > 0 and hab.estado == "llave": 
                hab.estado = "puerta" 
                n-=1
        elif imax > hab.i >= 4:
            hab.estado = random.choice (["guardias_tech","laberinto","guardias","puerta"])
            if n == 0 and hab.estado == "puerta": random.choice (["guardias_tech","laberinto","guardias"])
            elif hab.estado == "puerta": n-=1
        elif hab.i == imax:
            if primera_maxed:
                hab.estado = "tarjeta de acceso"
                primera_maxed = False
            else: 
                try:hab.estado = opciones.pop (random.randrange (len (opciones)))
                except:
                    hab.estado = "falso"
def dibujar_mapa (p):
    global tamaño,tortuga,pantalla
    tamaño=7.2
    pantalla = Screen ()
    pantalla.title (nombre_expedicion)
    pantalla.setup (width=720,height=720)
    pantalla.tracer (0)
    tortuga = Turtle ()
    tortuga.hideturtle ()
    tortuga.speed (0)
    tortuga.width (1)
    for y in range(99, -1, -1):
        for x in range(0, 100):
            if cuadricula [(x, y)]=="muro": tortuga.fillcolor ("#000000")
            elif cuadricula [(x, y)]=="suelo" or cuadricula [(x, y)]=="suelo_pasillo": tortuga.fillcolor ("#FFE188")
            tortuga.begin_fill ()
            tortuga.up()
            tortuga.goto (-360+x*tamaño,-360+y*tamaño)
            tortuga.down ()
            for _ in range (4):
                tortuga.forward (tamaño)
                tortuga.left (90)
            tortuga.end_fill ()
    tortuga.pencolor ("#787878")
    for k in range (101):
        tortuga.up ()
        tortuga.goto (-360+tamaño*k,360)
        tortuga.setheading (270)
        tortuga.down ()
        tortuga.forward (720)
    for j in range (101):
        tortuga.up ()
        tortuga.goto (-360,-360+tamaño*j)
        tortuga.setheading (0)
        tortuga.down ()
        tortuga.forward (720)
        tortuga.pencolor("#555555")
    for hab in habitaciones:
        casillas = []
        casillas_elegidas = []
        for i in range (hab.w):
            for j in range (hab.h):
                if cuadricula [(hab.x+i,hab.y+j)] == "suelo" or cuadricula [(hab.x+i,hab.y+j)] == "suelo_pasillo":
                    casillas.append ((i+hab.x,j+hab.y))
        celdas_borde = []
        for i in range(hab.w):
            for j in range(hab.h):
                if (i == 0 or i == hab.w-1 or j == 0 or j == hab.h-1):
                    cx, cy = hab.x+i, hab.y+j
                    if cuadricula[(cx, cy)] == "suelo" or cuadricula[(cx, cy)] == "suelo_pasillo":
                        es_borde_real = any(
                            cuadricula.get((cx+dx, cy+dy), "muro") == "muro"
                            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]
                        )
                        if es_borde_real:
                            celdas_borde.append((cx, cy))
        tramos = []
        while celdas_borde:
            tramo = [celdas_borde.pop(0)]
            cambiado = True
            while cambiado:
                cambiado = False
                for celda in celdas_borde[:]:
                    cx, cy = celda
                    for tx, ty in tramo:
                        if abs(cx-tx) + abs(cy-ty) == 1:
                            tramo.append(celda)
                            celdas_borde.remove(celda)
                            cambiado = True
                            break
            tramos.append(tramo)
        vecinos_hab = [habitaciones[hab.anterior]]
        for habi in habitaciones:
            if habi.anterior == habitaciones.index(hab):
                vecinos_hab.append(habi)
        tramos_disponibles = tramos[:]
        for vecino in vecinos_hab:
            if not tramos_disponibles: break
            vcx, vcy = vecino.centro()
            mejor_tramo = min(tramos_disponibles, key=lambda t: min(abs(c[0]-vcx)+abs(c[1]-vcy) for c in t))
            mas_cercana = min(mejor_tramo, key=lambda c: abs(c[0]-vcx)+abs(c[1]-vcy))
            hab.puertas.append((mas_cercana, vecino))
            tramos_disponibles.remove(mejor_tramo)
        for puerta,_ in hab.puertas:
            x,y=puerta
            cambiar_color (x,y,"#6E5239")
        if hab.estado == "laberinto" and len (hab.puertas)==1: 
            hab.estado = "botiquin"
            x,y = hab.centro ()
            boti = Botiquines (x,y)
            botiquines.append (boti)
            id = cambiar_color (x,y,"#00B500")
            boti.id.append (id)
            id = cambiar_color (x+1,y,"#00B500")
            boti.id.append (id)
            id = cambiar_color (x-1,y,"#00B500")
            boti.id.append (id)
            id = cambiar_color (x,y+1,"#00B500")
            boti.id.append (id)
            id = cambiar_color (x,y-1,"#00B500")
            boti.id.append (id)
        elif hab.estado == "salida":
            salida.append ((hab.x,hab.y+(hab.h//2)))
            salida.append ((hab.x,hab.y+(hab.h//2)-1))
            salida.append ((hab.x,hab.y+(hab.h//2)-2))
            salida.append ((hab.x,hab.y+(hab.h//2)+1))
            salida.append ((hab.x,hab.y+(hab.h//2)+2))
        elif hab.estado == "laberinto":
            ultimas = [hab.puertas[0][0]]
            camino = set()
            camino.add (hab.puertas[0][0])
            conexiones = set ()
            while len(ultimas) > 0:
                posibles = []
                x,y = ultimas[-1]
                if (x+1,y) in casillas and ((x+1,y)not in camino):
                    posibles.append((x+1,y))
                if (x-1,y) in casillas and ((x-1,y)not in camino):
                    posibles.append((x-1,y))
                if (x,y+1) in casillas and ((x,y+1)not in camino):
                    posibles.append((x,y+1))
                if (x,y-1) in casillas and ((x,y-1)not in camino):
                    posibles.append((x,y-1))
                if len(posibles) == 0:
                    ultimas.pop()
                else:
                    nuevo_x, nuevo_y = random.choice(posibles)
                    nueva = (nuevo_x,nuevo_y)
                    conexiones.add(((x, y), nueva))
                    conexiones.add((nueva, (x, y))) 
                    camino.add(nueva)
                    ultimas.append(nueva)
            sin_visitar = set(casillas) - camino
            while sin_visitar:
                for (x, y) in sin_visitar:
                    vecinos_visitados = [(vx, vy) for vx, vy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if (vx, vy) in camino]
                    if vecinos_visitados:
                        vx, vy = random.choice(vecinos_visitados)
                        conexiones.add(((x, y), (vx, vy)))
                        conexiones.add(((vx, vy), (x, y)))
                        camino.add((x, y))
                        ultimas = [(x, y)]
                        while ultimas:
                            posibles = []
                            cx, cy = ultimas[-1]
                            for nx, ny in [(cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)]:
                                if (nx, ny) in casillas and (nx, ny) not in camino:
                                    posibles.append((nx, ny))
                            if not posibles:
                                ultimas.pop()
                            else:
                                nuevo_x, nuevo_y = random.choice(posibles)
                                nueva = (nuevo_x, nuevo_y)
                                conexiones.add(((cx, cy), nueva))
                                conexiones.add((nueva, (cx, cy)))
                                camino.add(nueva)
                                ultimas.append(nueva)
                        sin_visitar = set(casillas) - camino
                        break
            for (x, y) in casillas:
                if (x+1, y) in casillas and ((x, y), (x+1, y)) not in conexiones:
                    pared(x, y, "lateral")
                    muro_lateral.append((x, y))
                if (x, y+1) in casillas and ((x, y), (x, y+1)) not in conexiones:
                    pared(x, y, "frontal")
                    muro_frontal.append((x, y))
        elif hab.estado == "guardias" or hab.estado == "guardias_tech":
            casillas_elegidas = random.sample (casillas,k=dificultad)
            for casilla in casillas_elegidas:
                x,y = casilla
                if hab.estado == "guardias":
                    e = Enemigo (x,y,"1")
                    guardias.append (e)
                    id = cambiar_color (x,y,"#FF0000")
                    e.id.append (id)
                elif hab.estado == "guardias_tech":
                    e = Enemigo (x,y,"2")
                    guardias.append (e)
                    id = cambiar_color (x,y,"#0066FF")
                    e.id.append (id)
        elif hab.estado in ["llave","tarjeta de acceso","lanza granadas","armadura","boost de velocidad","totem inmortalidad","escudo burbuja"]:
            x,y = hab.centro ()
            cofre = Cofre (x,y,hab.estado)
            cofres.append (cofre)
            id = cambiar_color (x,y,"#D4AD00")
            cofre.id.append (id)
            id = cambiar_color (x-1,y,"#D4AD00")
            cofre.id.append (id)
            casillas.remove ((x,y))
            casillas.remove ((x-1,y))
            casillas_elegidas = random.sample (casillas,k=dificultad//2)
            for casilla in casillas_elegidas:
                x,y = casilla
                e = Enemigo (x,y,"1")
                guardias.append (e)
                id = cambiar_color (x,y,"#FF0000")
                e.id.append (id)
        elif hab.estado == "puerta":
            door = Puertas ()
            bloqueos.append ((door,habitaciones.index (hab)))
            for puerta,_ in hab.puertas:
                x,y = puerta
                id = cambiar_color (x,y,"#8000FF")
                door.id.append (id)
                if cuadricula [x+1,y] == "muro":
                    id = cambiar_color (x+1,y,"#8000FF")
                    door.id.append (id)
                    id = cambiar_color (x-1,y,"#8000FF")
                    door.id.append (id) 
                elif cuadricula [x,y+1] == "muro":
                    id = cambiar_color (x,y+1,"#8000FF")
                    door.id.append (id)
                    id = cambiar_color (x,y-1,"#8000FF")
                    door.id.append (id)
            if len (hab.puertas) < 2:
                x,y = hab.centro ()
                cofre = Cofre (x,y,"vacio")
                cofres.append (cofre)
                id = cambiar_color (x,y,"#D4AD00")
                cofre.id.append (id)
                id = cambiar_color (x-1,y,"#D4AD00")
                cofre.id.append (id)
                hab.estado = "puertafin"
        elif hab.estado == "falso":
            x,y = hab.centro ()
            cofre = Cofre (x,y,"vacio")
            cofres.append (cofre)
            id = cambiar_color (x,y,"#D4AD00")
            cofre.id.append (id)
            id = cambiar_color (x-1,y,"#D4AD00")
            cofre.id.append (id)
        x,y = hab.centro ()
        tortuga.up ()
        tortuga.pencolor ("#FFFFFF")
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            tortuga.goto(-360 + 7.2*x + 3.6 + dx, -360 + 7.2*y + 3.6 + dy)
            tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
        tortuga.goto(-360 + 7.2*x + 3.6, -360 + 7.2*y + 3.6)
        tortuga.pencolor("#000000")
        tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
    id = cambiar_color (p.x,p.y,"#FF8000")
    p.id.append (id)
    pantalla.update ()
def bucle_principal ():
    t = 0
    n = -1
    printt ("En el mapa de su móvil usted está simbolizado por un cuadrado naranja, los enemigos con el color rojo o azul, el morado simboliza una puerta bloqueada y el amarillo un cofre. Si ha recibido daño utilice los botiquines simbolizados con una cruz verde.")
    printt ("He marcado con marrón los extremos del pasillo, si seleccionas la opción (ir a la habitación x) te trasladarás de una puerta a otra. Si desea ir a otro lugar no señalizado, emplee (WASD)")
    while True:
        introducido = False
        actual = habitaciones [t]
        n+=1
        opciones = []
        if p.vida > 0: pass
        elif p.vida <= 0 and "totem inmortalidad" in p.inventario:
            p.vida = 100
            p.inventario.remove ("totem inmortalidad")
            informe (n,"Ha resucitado",(p.x,p.y),(p.x,p.y),"La muerte no es el final","Ha resucitado, pero ha gastado su totem, así que ten más cuidado a partir de ahora")
        else: muerte (n)
        opciones = fopciones (actual)
        hab = actual
        if hab.estado == "laberinto":
            casillas_hab = set()
            for i in range(hab.w):
                for j in range(hab.h):
                    if cuadricula.get((hab.x + i, hab.y + j)) in ("suelo", "suelo_pasillo"):
                        casillas_hab.add((hab.x + i, hab.y + j))
            x_min = min(c[0] for c in casillas_hab)
            x_max = max(c[0] for c in casillas_hab)
            y_min = min(c[1] for c in casillas_hab)
            y_max = max(c[1] for c in casillas_hab)
            print()
            for y in range(y_max, y_min - 1, -1):
                fila_top = ""
                for x in range(x_min, x_max + 1):
                    if (x, y) not in casillas_hab:
                        fila_top += "███"
                    else:
                        hay_pared_arriba = (x, y) in muro_frontal
                        fila_top += "█" + ("█" if hay_pared_arriba else " ") + "█"
                print(fila_top)
                fila_mid = ""
                for x in range(x_min, x_max + 1):
                    if (x, y) not in casillas_hab:
                        fila_mid += "███"
                    else:
                        pared_izq = (x - 1, y) in muro_lateral
                        contenido = "P" if (p.x, p.y) == (x, y) else " "
                        pared_der = (x, y) in muro_lateral
                        fila_mid += ("█" if pared_izq else " ") + contenido + ("█" if pared_der else " ")
                print(fila_mid)
            fila_bot = ""
            for x in range(x_min, x_max + 1):
                fila_bot += "███" if (x, y_min) not in casillas_hab else "███"
            print(fila_bot)
            print()
        printt ("Sus opciones son:")
        i=1
        for opcion in opciones:
            printt (f"{i}. {opcion}")
            i+=1
        while True:
            try: 
                eleccion= input ("Introduzca el número de la opción que desee elegir: ")
                e = int(re.search(r"\d", eleccion).group()) - 1
                if -1 < e < len (opciones):
                    break
                else: 
                    printt ("Opción no válida")
                    time.sleep (0.2)
            except:
                printt ("Opción no válida")
                time.sleep (0.2)
        eleccion = opciones [e]
        if eleccion != "Realizar las acciones que introduzca (WASD)":
            for guardia in guardias:
                moverse (guardia)
        for hab in habitaciones:
            x,y = hab.centro ()
            tortuga.up ()
            tortuga.pencolor ("#FFFFFF")
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                tortuga.goto(-360 + 7.2*x + 3.6 + dx, -360 + 7.2*y + 3.6 + dy)
                tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
            tortuga.goto(-360 + 7.2*x + 3.6, -360 + 7.2*y + 3.6)
            tortuga.pencolor("#000000")
            tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
        if eleccion == "Ir hacia el norte":
            p.y += 1
            informe (n,eleccion,(p.x,p.y-1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia adelante")
            actualizar ()
        if eleccion == "Ir hacia el sur":
            p.y -= 1
            informe (n,eleccion,(p.x,p.y+1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia atras")
            actualizar ()
        if eleccion == "Ir hacia el este":
            p.x += 1
            informe (n,eleccion,(p.x-1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la derecha")
            actualizar ()
        if eleccion == "Ir hacia el oeste":
            p.x -= 1
            informe (n,eleccion,(p.x+1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la izquierda")
            actualizar ()
        if "Desbloquear la habitación" in eleccion:
            idx = int(re.search(r"\d+", eleccion).group())
            hab = habitaciones [idx]
            if hab.estado == "puerta": hab.estado = "habitación segura"
            elif hab.estado == "puertafin": hab.estado = "cofre"
            casillas = []
            for i in range (hab.w):
                for j in range (hab.h):
                    if cuadricula [(hab.x+i,hab.y+j)] == "suelo" or cuadricula [(hab.x+i,hab.y+j)] == "suelo_pasillo":
                        casillas.append ((i+hab.x,j+hab.y))
            for bloqueo in bloqueos:
                puerta,num = bloqueo
                if num == idx:
                    for id in puerta.id:
                        tortuga.clearstamp (id)
                    puerta.id.clear ()
            p.inventario.remove ("llave")
            informe (n,eleccion,(p.x,p.y),(p.x,p.y),f"ha desbloqueado la habitación {idx}",f"ha gastado una llave para desbloquear la habitación {idx}")
        if "Ir a la habitación" in eleccion:
            romper = False
            hab = habitaciones [t]
            idx = int(re.search(r"\d+", eleccion).group())
            hab1 = habitaciones [idx]
            if habitaciones.index (hab) < habitaciones.index (hab1): camino = hab1.unir (hab)
            else: camino = hab.unir (hab1)
            j=0
            x, y = min(camino, key=lambda c: abs(p.x - c[0]) + abs(p.y - c[1]))
            fin = False
            if (abs(p.x - camino[0][0]) + abs(p.y - camino[0][1])) > (abs(p.x - camino[-1][0]) + abs(p.y - camino[-1][1])):
                camino = list(reversed(camino))
            while True:
                if p.vida <=0: muerte (n)
                fin = ir (x,y,n,eleccion,"largo")
                actualizar ()
                n+=1
                if fin == True:break
            try: j = camino.index ((p.x,p.y))
            except: j =0
            while j < (len(camino)-1):
                j+=1
                if p.vida <=0: muerte (n)
                x,y = camino [j]
                ir (x,y,n,eleccion,"corto")
                actualizar ()
                for puerta,_ in hab1.puertas:
                    if (p.x,p.y) == puerta:
                        print("Ha llegado a su destino",end="\n")
                        time.sleep (2)
                        t = idx
                        romper = True
                if romper:break 
                n+=1
        if eleccion == "Abrir cofre" or eleccion == "Utilizar botiquín":
            x,y=actual.centro ()
            while True:
                fin = ir (x,y,n,eleccion,"largo")
                actualizar ()
                if fin == True:break
                n+=1
            if eleccion == "Utilizar botiquín":
                p.vida +=20
                for b in botiquines:
                    if b.x == p.x and b.y == p.y:
                        for id in b.id:
                            tortuga.clearstamp (id)
                        b.id.clear ()
                        botiquines.remove (b)
                        actual.estado = "abierto"
                        break
                informe (n,eleccion,(p.x,p.y),(p.x,p.y),"Ha recuperado 20 de vida","Ha utilizado un botiquín para recuperar vida")
            if eleccion == "Abrir cofre":
                for c in cofres:
                    if c.x==p.x and c.y==p.y:
                        if c.contenido != "vacio":
                            p.inventario.append (c.contenido)
                            informe (n,eleccion,(p.x,p.y),(p.x,p.y),f"Se ha añadido {c.contenido} a su inventario",f"Ha abierto un cofre y ha encontrado {c.contenido}")
                        else: informe (n,eleccion,(p.x,p.y),(p.x,p.y),"Ha abierto un cofre vacío","Ha abierto un cofre, pero estaba vacío")
                        if c.contenido == "tarjeta de acceso":
                            eventos_destacados.append ("Ha encontrado la tarjeta de acceso a la lanzadera")
                            for s in salida:
                                x,y=s
                                cambiar_color (x,y,"#FFFFFF")
                        for id in c.id:
                            tortuga.clearstamp (id)
                        c.id.clear ()
                        cofres.remove (c)
                        actual.estado = "abierto"
                        break
        if eleccion == "Realizar las acciones que introduzca (WASD)":
            while not introducido:
                if p.vida <=0: muerte (n)
                acciones = input ("Introduzca una cadena de texto usando WASD siendo: W (ir hacia adelante) | S (ir hacia atrás) | A (Ir hacia la izquierda) | D (Ir hacia la derecha): ").lower()
                if acciones:introducido = True
                else: printt ("Instrucciones no válidas")
            for accion in acciones:
                if p.vida <=0: muerte (n)
                if accion == "w":
                    if cuadricula [(p.x, p.y+1)] != "muro":
                        p.y += 1
                        daño = sucesos (n)
                        if daño: informe (n,'Realizar las acciones que introduzca --> "W"',(p.x,p.y-1),(p.x,p.y),f"Ha perdido {daño} de vida","Ha avanzado un paso hacia delante, pero se ha encontrado a un guardia")
                        else: informe (n,'Realizar las acciones que introduzca --> "W"',(p.x,p.y-1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia delante")
                    else: informe (n,'Realizar las acciones que introduzca --> "W"',(p.x,p.y),(p.x,p.y),"No se ha podido realizar esa acción porque había una pared","Sigue en el mismo sitio")
                    actualizar ()
                    n+=1
                if accion == "s":
                    if cuadricula [(p.x, p.y-1)] != "muro":
                        p.y -= 1
                        daño = sucesos (n)
                        if daño: informe (n,'Realizar las acciones que introduzca --> "S"',(p.x,p.y+1),(p.x,p.y),f"Ha perdido {daño} de vida","Ha avanzado un paso hacia atrás, pero se ha encontrado a un guardia")
                        else: informe (n,'Realizar las acciones que introduzca --> "S"',(p.x,p.y+1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia atrás")
                    else: informe (n,'Realizar las acciones que introduzca --> "S"',(p.x,p.y),(p.x,p.y),"No se ha podido realizar esa acción porque había una pared","Sigue en el mismo sitio")
                    actualizar ()
                    n+=1
                if accion == "d":
                    if cuadricula [(p.x+1, p.y)] != "muro":
                        p.x += 1
                        daño = sucesos (n)
                        if daño: informe (n,'Realizar las acciones que introduzca --> "D"',(p.x-1,p.y),(p.x,p.y),f"Ha perdido {daño} de vida","Ha avanzado un paso hacia la derecha, pero se ha encontrado a un guardia")
                        else: informe (n,'Realizar las acciones que introduzca --> "D"',(p.x-1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la derecha")
                    else: informe (n,'Realizar las acciones que introduzca --> "D"',(p.x,p.y),(p.x,p.y),"No se ha podido realizar esa acción porque había una pared","Sigue en el mismo sitio")
                    actualizar ()
                    n+=1
                if accion == "a":
                    if cuadricula [(p.x-1, p.y)] != "muro":
                        p.x -= 1
                        daño = sucesos (n)
                        if daño: informe (n,'Realizar las acciones que introduzca --> "A"',(p.x+1,p.y),(p.x,p.y),f"Ha perdido {daño} de vida","Ha avanzado un paso hacia la izquierda, pero se ha encontrado a un guardia")
                        else: informe (n,'Realizar las acciones que introduzca --> "A"',(p.x+1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la izquierda")
                    else: informe (n,'Realizar las acciones que introduzca --> "A"',(p.x,p.y),(p.x,p.y),"No se ha podido realizar esa acción porque había una pared","Sigue en el mismo sitio")
                    actualizar ()
                    n+=1
        if eleccion == "Eliminar a todos los enemigos de la sala":
            hab = actual
            casillas = []
            for i in range (hab.w):
                for j in range (hab.h):
                    if cuadricula [(hab.x+i,hab.y+j)] == "suelo" or cuadricula [(hab.x+i,hab.y+j)] == "suelo_pasillo":
                        casillas.append ((i+hab.x,j+hab.y))
            for g in guardias[:]:
                if (g.x,g.y) in casillas:
                    guardias.remove (g)
                    tortuga.clearstamp(g.id[0])
            p.inventario.remove ("lanza granadas")
            informe (n,"Ha utilizado lanzagranadas",(p.x,p.y),(p.x,p.y),"John McClane: ¡Yippie-ki-yay hijos de puta!","Ha borrado a todos los enemigos de la sala gracias a ese lanzagranadas")
        if eleccion == "Acceder a la lanzadera":
            eventos_destacados.append ("Ha accedido a la lanzadera y se ha subido a su nave")
            ir (actual.x,actual.y+actual.h//2,n,eleccion,"largo")
            printt ("Ha completado la primera parte de la misión, ahora a por su nave")
            pantalla.clearscreen ()
            main2 (n)
            break
        for hab in habitaciones:
            casillas = []
            for i in range (hab.w):
                for j in range (hab.h):
                    if cuadricula [(hab.x+i,hab.y+j)] == "suelo" or cuadricula [(hab.x+i,hab.y+j)] == "suelo_pasillo":
                        casillas.append ((i+hab.x,j+hab.y))
            if (p.x,p.y) in casillas: t = habitaciones.index(hab)           
        pantalla.update()
def actualizar ():
    for guardia in guardias:
        moverse (guardia)
    for stamp in p.id:
        tortuga.clearstamp (stamp)
    p.id.clear ()
    id = cambiar_color (p.x,p.y,"#FF8000")
    p.id.append (id)
    for hab in habitaciones:
        x,y = hab.centro ()
        tortuga.up ()
        tortuga.pencolor ("#FFFFFF")
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            tortuga.goto(-360 + 7.2*x + 3.6 + dx, -360 + 7.2*y + 3.6 + dy)
            tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
        tortuga.goto(-360 + 7.2*x + 3.6, -360 + 7.2*y + 3.6)
        tortuga.pencolor("#000000")
        tortuga.write(f"{habitaciones.index(hab)}", False, "center", ("Arial", 12, "bold"))
    pantalla.update ()          
def pared (x,y,tipo):
    tortuga.up ()
    tortuga.color ("#000000")
    tortuga.pensize (2)
    if tipo == "lateral":
        tortuga.goto (-360+x*tamaño+tamaño,-360+y*tamaño)
        tortuga.setheading(90)
        tortuga.down ()
        tortuga.forward (tamaño)
    if tipo == "frontal":
        tortuga.goto (-360+x*tamaño,-360+y*tamaño+tamaño)
        tortuga.setheading(0)
        tortuga.down ()
        tortuga.forward (tamaño)
def cambiar_color (x,y,color):
    tortuga.up()
    tortuga.goto (-360+x*tamaño+tamaño/2,-360+y*tamaño+tamaño/2)
    tortuga.shape ("square")
    tortuga.shapesize ((tamaño-2)/20,(tamaño-2)/20)
    tortuga.color (color)
    return tortuga.stamp ()
def printt (texto):
    for letra in texto:
        print (letra, end="",flush=True)
        time.sleep (0.05) # escribir 0.05
    print (end="\n")
    time.sleep (0.15)
def nombre (n):
    if len (n)<2:return False
    elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", n): return False
    else: return True
def fopciones (hab):
    opciones = []
    if hab.estado in ["llave","tarjeta de acceso","lanza granadas","armadura","boost de velocidad","totem inmortalidad","escudo burbuja","falso","puertafin"]: 
        opciones.append (f"Abrir cofre")
    if hab.estado == "laberinto":
        if (p.x,p.y) not in muro_frontal and cuadricula [(p.x,p.y+1)] != "muro": opciones.append ("Ir hacia el norte")
        if (p.x,p.y) not in muro_lateral and cuadricula [(p.x+1,p.y)] != "muro": opciones.append ("Ir hacia el este")
        if (p.x-1,p.y) not in muro_lateral and cuadricula [(p.x-1,p.y)] != "muro": opciones.append ("Ir hacia el oeste")
        if (p.x,p.y-1) not in muro_frontal and cuadricula [(p.x,p.y-1)] != "muro": opciones.append ("Ir hacia el sur")
    if (hab.estado == "guardias" or hab.estado == "guardias_tech") and "lanza granadas" in p.inventario: opciones.append ("Eliminar a todos los enemigos de la sala")
    vecinos = []
    if hab.anterior != habitaciones.index (hab): vecinos.append (habitaciones[hab.anterior])
    for habi in habitaciones:
        if habi.anterior == habitaciones.index(hab) and habi is not hab:
            vecinos.append(habi)
    for vecino in vecinos:
        if vecino.estado in ["llave","tarjeta de acceso","lanza granadas","armadura","boost de velocidad","totem inmortalidad","escudo burbuja","falso","puertafin"]: tipo = "cofre"
        elif vecino.estado == "abierto": tipo = "habitación ya saqueada"
        else: tipo = vecino.estado
        idx = habitaciones.index(vecino)
        if vecino.estado == "puerta" or vecino.estado == "puertafin":
            if "llave" in p.inventario:
                opciones.append(f"Desbloquear la habitación {idx}")
        else:
            if hab.estado != "laberinto":
                opciones.append(f"Ir a la habitación {idx}: {tipo}")
            else:
                for puerta, v in hab.puertas:
                    if v is vecino and (p.x, p.y) == puerta:
                        opciones.append(f"Ir a la habitación {idx}: {tipo}")
    if hab.estado == "botiquin": 
        opciones.append (f"Utilizar botiquín")
    if hab.estado == "salida":
        if "tarjeta de acceso" in p.inventario:
            opciones.append("Acceder a la lanzadera")
    if hab.estado != "laberinto":opciones.append ("Realizar las acciones que introduzca (WASD)")
    return opciones
def informe (n, eleccion,coordenadas_anteriores,coordenadas_posteriores,evento,explicacion):
    print (f"Paso {n}")
    time.sleep (0.1)
    print (f"Vida: {p.vida}/{105-5*dificultad}")
    time.sleep (0.1)
    print (f"Inventario: {p.inventario}")
    time.sleep (0.1)
    print (eleccion)
    time.sleep (0.1)
    if coordenadas_anteriores != coordenadas_posteriores: print (f"Se ha trasladado de {coordenadas_anteriores} --> {coordenadas_posteriores}")
    elif coordenadas_anteriores == coordenadas_posteriores: print (f"Se ha trasladado de {coordenadas_anteriores} --> {coordenadas_posteriores} (no se ha movido)") 
    time.sleep (0.1)
    print (f"Eventos importantes: {evento}")
    time.sleep (0.1)
    print (f"Resumen: {explicacion}")
    time.sleep (0.1)
    print ("",end="\n")
def moverse (e):
    while True:
        m = random.choice (["N","S","E","O"])
        if m == "N" and cuadricula [e.x,e.y+1] == "suelo" and (e.x,e.y+1) not in [guardias,cofres,botiquines]: 
            e.y +=1
            break
        if m == "S" and cuadricula [e.x,e.y-1] == "suelo" and (e.x,e.y-1) not in [guardias,cofres,botiquines]: 
            e.y -=1
            break
        if m == "E" and cuadricula [e.x+1,e.y] == "suelo" and (e.x+1,e.y) not in [guardias,cofres,botiquines]: 
            e.x +=1
            break
        if m == "O" and cuadricula [e.x-1,e.y] == "suelo" and (e.x-1,e.y) not in [guardias,cofres,botiquines]: 
            e.x -=1
            break
        break
    tortuga.clearstamp (e.id[0])
    e.id.pop ()
    if e.tipo == "1": 
        id = cambiar_color (e.x,e.y,"#FF0000")
        e.id.append (id)
    if e.tipo == "2": 
        id = cambiar_color (e.x,e.y,"#0066FF")
        e.id.append (id)
def ir (x,y,n,eleccion,tipo):
    suceso = None
    if p.x - x < 0 and cuadricula [(p.x+1, p.y)]!="muro":
        p.x += 1
        suceso = sucesos (n)
        if suceso: informe (n,eleccion,(p.x-1,p.y),(p.x,p.y),f"Ha perdido {suceso} de vida","Ha avanzado un paso hacia la derecha para acercarse a su destino, pero se ha encontrado a un guardia")
        else: informe (n,eleccion,(p.x-1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la derecha para acercarse a su destino")
    elif p.x - x > 0 and cuadricula [(p.x-1, p.y)]!="muro":
        p.x -= 1
        suceso = sucesos (n)
        if suceso: informe (n,eleccion,(p.x+1,p.y),(p.x,p.y),f"Ha perdido {suceso} de vida","Ha avanzado un paso hacia la izquierda para acercarse a su destino, pero se ha encontrado a un guardia")
        else: informe (n,eleccion,(p.x+1,p.y),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia la izquierda para acercarse a su destino")
    elif p.y - y > 0 and cuadricula [(p.x, p.y-1)]!="muro":
        p.y -= 1
        suceso = sucesos (n)
        if suceso: informe (n,eleccion,(p.x,p.y+1),(p.x,p.y),f"Ha perdido {suceso} de vida","Ha avanzado un paso hacia atrás para acercarse a su destino, pero se ha encontrado a un guardia")
        else: informe (n,eleccion,(p.x,p.y+1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia atrás para acercarse a su destino")
    elif p.y - y < 0 and cuadricula [(p.x,p.y+1)]!="muro":
        p.y += 1
        suceso = sucesos (n)
        if suceso: informe (n,eleccion,(p.x,p.y-1),(p.x,p.y),f"Ha perdido {suceso} de vida","Ha avanzado un paso hacia delante para acercarse a su destino, pero se ha encontrado a un guardia")
        else: informe (n,eleccion,(p.x,p.y-1),(p.x,p.y),"Nada interesante por aquí","Ha avanzado un paso hacia delante para acercarse a su destino")
    elif tipo == "largo": return True
def sucesos (n):
    for e in guardias:
        if (e.x,e.y) == (p.x,p.y):
            if "escudo burbuja" in p.inventario: 
                p.inventario.remove ("escudo burbuja")
                daño = 0
                printt ("Ese escudo burbuja le acaba de librar de un buen golpe, que pena que se haya roto")
            elif "armadura" in p.inventario: 
                daño = 5
                p.vida -= daño
            else: 
                daño = 15 
                p.vida-=daño
            if e.tipo == "1":
                guardias.remove (e)
                tortuga.clearstamp (e.id[0])
            if p.vida<0: p.vida = 0
            if p.vida > 0: pass
            elif p.vida <= 0 and "totem inmortalidad" in p.inventario:
                p.vida = 100
                p.inventario.remove ("totem inmortalidad")
                informe (n,"Ha resucitado",(p.x,p.y),(p.x,p.y),"La muerte no es el final","Ha resucitado, pero ha gastado su totem, así que ten más cuidado a partir de ahora")
            else: muerte (n)
            return daño
def muerte (n):
    eventos_destacados.append ("Ha muerto")
    resumir ("fracaso",n)
def main2 (n):
    printt ("Tome asiento y póngase cómodo, porque esto llevará un rato")
    printt ("Ahora que tenemos tiempo, creo que le debo una explicación. Estaba hackeando a la NASA por diversión cuando he descubierto que la Tierra está en grave peligro. Una civilización desconocida se está dedicando a destruir planetas, y por lo que se sabe su próximo objetivo es Marte.")
    time.sleep (2)
    printt ("Si destruyen a nuestro vecino rojo todo estará perdido, ya que los fragmentos colisionarán contra nuestro planeta, provocando nuestra extinción con una probab...")
    print ("Siguiente parada: plataforma de lanzamiento")
    printt ("Esta es su parada, bájese del tren y suba a la nave, yo iré inicializando la secuencia de lanzamiento")
    time.sleep (2)
    for i in range (10):
        print (10-i)
        time.sleep (1) #poner 1
    print ("Ignición")
    printt ("¡Fshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!")
    printt ("Se me ha olvidado decirle que ya han destruido la Luna, por lo que tendrá que esquivar el campo de asteroides para salir de la órbita terrestre")
    generar_asteroides ()
    dibujar_asteroides ()
    bucle_secundario (n)
def generar_asteroides ():
    global carriles
    carriles = []
    n = 2
    carriles.append ("libre")
    for _ in range (max (20*dificultad//2,20)):
        temporal = random.choices (["peligro","seguro"],[100/(n//2),100-(100/(n//2))])
        if temporal [0] == "peligro":
            n+=1
            v = random.randint (-4,4)
            lista = []
            if abs (v) == 4:
                lista.append (Asteroide (-1 if v>0 else 20,v))
                lista.append (Asteroide (-10 if v>0 else 30,v))
            if abs (v) == 3:
                lista.append (Asteroide (-1 if v>0 else 20,v))
                lista.append (Asteroide (-6 if v>0 else 26,v))
                lista.append (Asteroide (-12 if v>0 else 32,v))
            if abs (v) == 2 or abs (v) == 1:
                lista.append (Asteroide (-1 if v>0 else 20,v))
                lista.append (Asteroide (-5 if v>0 else 25,v))
                lista.append (Asteroide (-10 if v>0 else 30,v))
                lista.append (Asteroide (-15 if v>0 else 35,v))
            if v == 0:
                lista.append (Asteroide (2,v))
                lista.append (Asteroide (8,v))
                lista.append (Asteroide (13,v))
                lista.append (Asteroide (17,v))
            carriles.append (lista)
        if temporal [0] == "seguro":
            n=2
            carriles.append ("libre")
    for _ in range (12): carriles.append ("libre")
    return carriles
def dibujar_asteroides ():
    pantalla.title (nombre_expedicion)
    pantalla.setup (width=880,height=370)
    pantalla.tracer (0)
    pantalla.bgcolor("#373737")
    tortuga = Turtle ()
    tortuga.hideturtle ()
    tortuga.speed (0)
    tortuga.width (2)
    tortuga.color ("#FFFFFF")
    registrar_flecha ()
    for i in range (11):
        tortuga.up()
        tortuga.goto (-350,-175+(35*(i)))
        tortuga.down ()
        tortuga.setheading(0)
        tortuga.forward (700)
        tortuga.up ()
    for j in range (21):
        tortuga.up ()
        tortuga.goto (-350+(35*(j)),-175)
        tortuga.down ()
        tortuga.setheading (90)
        tortuga.forward (350)
    pantalla.update ()
def bucle_secundario (n):
    global combustible_total, oxigeno_total, vida_total
    combustible_total, oxigeno_total, vida_total = cohete.combustible,cohete.oxigeno,cohete.vida
    flechas = []
    modificado = False
    r=4 # poner 4
    printt (f"\033[1m Etapa 2 de {nombre_expedicion}:\033[0m\033[38;2;0;255;120m atravesar el cinturón de asteroides")
    time.sleep (r)
    printt (f"\033[1m Posición inicial:\033[0m\033[38;2;0;255;120m ({cohete.x},{cohete.y})")
    time.sleep (r)
    printt (f"\033[1m Ángulo inicial:\033[0m\033[38;2;0;255;120m {cohete.ang}º")
    time.sleep (r)
    printt (f"\033[1m Combustible del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.combustible}/{cohete.combustible}")
    time.sleep (r)
    printt (f"\033[1m Oxígeno del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.oxigeno}/{cohete.oxigeno}")
    time.sleep (r)
    printt (f"\033[1m Estado del {nombre_nave}:\033[0m\033[38;2;0;255;120m {cohete.vida}/{cohete.vida}")
    printt (f" He ocultado su señal en una franja que va de x=0 a x=19, si se sale de esta zona su nave será atacada por los alienígenas, por lo que debe tener mucho cuidado")
    time.sleep (r)
    printt (f" Para finalizar la etapa 2 debe atravesar el cinturón de asteroides que rodean la Tierra. \033[1mSuerte!!!\033[0m\033[38;2;0;255;120m")
    time.sleep (r)
    printt ("Tenga en cuenta que su nave avanzará dos casillas en el eje x o en el eje y si su nave tiene por ángulo un múltiplo de 90º")
    time.sleep (r)
    printt ("Las flechas que aparecen al lado de su radar señalizan la velocidad y sentido de los asteroides")
    filas = []
    e=None
    print (cohete.x,cohete.y)
    while True:
        filas.clear ()
        colision = False
        for i in range (10):
            filas.append (carriles [cohete.y+i])
        actualizacion (filas)
        id = ""
        limpiar()
        for flecha in flechas:
            tortuga.clearstamp (flecha)
        flechas.clear ()
        print("#" * 42)
        for j in range(9, -1, -1):
            idx = cohete.y + j
            if idx < 0 or idx >= len(carriles):
                print("#|" + " |" * 20 + "#")
                print("-" * 42)
                continue         
            fila = carriles[idx]
            fila_str = "#|"
            for i in range(20):    
                if (cohete.x, cohete.y) == (i, idx):
                    ang = min([0,30,60,90,120,150,180,210,240,270,300,330],key=lambda c: abs(c - cohete.ang) % 360)
                    flecha = ("↑|" if ang==0 else "↖|" if ang in(30,60) else
                            "←|" if ang==90 else "↙|" if ang in(120,150) else
                            "↓|" if ang==180 else "↘|" if ang in(210,240) else
                            "→|" if ang==270 else "↗|")
                    fila_str += flecha 
                elif fila != "libre" and any(e.x == i for e in fila):
                    fila_str += "#|"
                else:
                    fila_str += " |"
            fila_str += "#"
            print(fila_str,end=" ")
            if fila != "libre":
                elemento = fila [0]
                h = abs(elemento.v)
                if elemento.v > 0:
                    tortuga.up ()
                    tortuga.goto(375+15+(10*h/2), -175 + j*35 + 35/2)
                    tortuga.setheading (0)
                    tortuga.shape (f"flecha_{h}")
                    tortuga.color ("#FFFFFF")
                    id = tortuga.stamp ()
                    print ("-"*h,end="")
                    print (">")
                elif elemento.v < 0:
                    tortuga.up ()
                    tortuga.goto(-375-15-(8*h/2), -175 + j*35 + 35/2)
                    tortuga.setheading (180)
                    tortuga.shape (f"flecha_{h}")
                    tortuga.color ("#FFFFFF")
                    id = tortuga.stamp ()
                    print ("<",end="")
                    print ("-"*h,end="")
                    print () 
                else: print ()
                if id: flechas.append (id)
            else: print ("Fila segura")
            print("-" * 42)
        print("#" * 42)
        print()
        if not modificado:
            if e == "Ir hacia delante":
                if perdida == False: 
                    informar (n,e,(prev_x,prev_y),(cohete.x,cohete.y),"Ha avanzado sin sufrir ningún altercado")
                else:
                    informar (n,e,(prev_x,prev_y),(cohete.x,cohete.y),"Ha colisionado contra un asteroide, perdiendo 10 de vida")
            elif e == "Ir hacia atrás":
                if perdida == False: 
                    informar (n,e,(prev_x,prev_y),(cohete.x,cohete.y),"Ha retrocedido sin sufrir ningún altercado")
                else:
                    informar (n,e,(prev_x,prev_y),(cohete.x,cohete.y),"Ha colisionado contra un asteroide, perdiendo 10 de vida")
        else:
            if e == "Ir hacia delante":
                    informar (n,e,(prev_x,prev_y),f"({antx},{anty}) --> ({cohete.x},{cohete.y})",f"¡¡¡Cuidado!!!, ese rayo ha estado muy cerca. He tomado el control de su nave y la he movido a ({cohete.x},{cohete.y}) para evitar otros ataques")
            elif e == "Ir hacia atrás":
                    informar (n,e,(prev_x,prev_y),f"({antx},{anty}) --> ({cohete.x},{cohete.y})",f"¡¡¡Cuidado!!!, ese rayo ha estado muy cerca. He tomado el control de su nave y la he movido a ({cohete.x},{cohete.y}) para evitar otros ataques")
        if e == "Permanecer en la misma posición":
            if perdida == False: 
                informar (n,e,(cohete.x,cohete.y),(cohete.x,cohete.y),"No ha sucedido ningún altercado durante la espera")
            else:
                informar (n,e,(cohete.x,cohete.y),(cohete.x,cohete.y),"Un asteroide ha colisionado contra su nave, haciéndole perder 10 de vida")
        elif e == "Introducir el ángulo de la nave":
            if perdida == False: 
                informar (n,f"Introducir el ángulo de la nave: {cohete.ang}",(cohete.x,cohete.y),(cohete.x,cohete.y),"No ha sucedido ningún altercado durante las maniobras de giro")
            else:
                informar (n,f"Introducir el ángulo de la nave: {cohete.ang}",(cohete.x,cohete.y),(cohete.x,cohete.y),"Un asteroide ha colisionado contra su nave, haciéndole perder 10 de vida")
        if cohete.vida == 0 or cohete.combustible == 0 or cohete.oxigeno == 0: 
            printt ("Ha muerto, pero puede retomar la Etapa 2 a costa de volver al (10,0)")
            while True:
                respuesta = input ("Desea volver a intentarlo (Sí/No): ")
                if respuesta.lower () in ["si","sí","no"]: break
                else: print ("Respuesta no válida")
            if respuesta.lower () in ["si","sí"]:
                cohete.x,cohete.y = 10,0
                cohete.combustible=combustible_total
                cohete.oxigeno = oxigeno_total
                cohete.vida = 100
                for i in range (10):
                    filas.append (carriles [cohete.y+i])
                actualizacion (filas)
            else: 
                eventos_destacados.append ("Se ha quedado sin oxígeno" if cohete.oxigeno == 0 else "Se ha quedado sin combustible"if cohete.combustible == 0 else "Su nave ha sido destruida por un asteroide")
                resumir ("fracaso2",n)
        if cohete.y >= max (20*dificultad//2,20) + 1:
            pantalla.bye ()
            main3 (n)
        if e: time.sleep (5) # poner 5
        print ("1. Ir hacia delante")
        print ("2. Ir hacia atrás")
        print ("3. Permanecer en la misma posición")
        print ("4. Introducir el ángulo de la nave")
        while True:
            try: 
                eleccion= input ("Introduzca el número de la opción que desee elegir: ")
                e = int(re.search(r"\d", eleccion).group())
                if e == 1: 
                    e = "Ir hacia delante"
                    break
                elif e == 2: 
                    e = "Ir hacia atrás"
                    break
                elif e == 3: 
                    e = "Permanecer en la misma posición"
                    break
                elif e == 4: 
                    e = "Introducir el ángulo de la nave"
                    break
                else: 
                    printt ("Opción no válida")
                    time.sleep (0.2)
            except:
                printt ("Opción no válida")
                time.sleep (0.2)
        if 20> cohete.x >= 0 and cohete.y>=0:
            modificado = False
            if e == "Ir hacia delante":
                prev_x, prev_y = cohete.x, cohete.y
                cohete.x += ceil(v) if abs(v := round(2 * cos(radians(cohete.ang + 90)), 4)) % 1 >= 0.8 else floor(v)
                cohete.y += ceil(v) if abs(v := round(2 * sin(radians(cohete.ang + 90)), 4)) % 1 >= 0.8 else floor(v)
            elif e == "Ir hacia atrás":
                prev_x, prev_y = cohete.x, cohete.y
                cohete.x -= ceil(v) if abs(v := round(2 * cos(radians(cohete.ang + 90)), 4)) % 1 >= 0.8 else floor(v)
                cohete.y -= ceil(v) if abs(v := round(2 * sin(radians(cohete.ang + 90)), 4)) % 1 >= 0.8 else floor(v)
            elif e == "Permanecer en la misma posición": pass
            elif e == "Introducir el ángulo de la nave":
                while True:
                    angulo_introducido = input ("Ángulo de la nave (0º->Norte|90º->Oeste|180º->Sur|270º->Este): ").strip ()
                    nums = re.findall(r"-?\d+", angulo_introducido)
                    if not nums:
                        printt("Por favor, introduzca un ángulo válido")
                    else: break
                angulo = int(nums[0])
                angulo = angulo%360
                cohete.ang = angulo
            if not (20> cohete.x >= 0 and cohete.y>=0):
                modificado = True
                antx, anty = cohete.x, cohete.y
                if cohete.x >= 20: cohete.x = 19
                if cohete.x < 0: cohete.x = 0
                if cohete.y < 0: cohete.y = 0
        for carril in carriles:
            if carril != "libre":
                for t in carril:
                    for _ in range (abs(t.v)):
                        if t.v > 0 and (t.x+t.v) >= 20 and t.x <10000:
                            t.x = t.x+1-19
                        elif t.v < 0 and (t.x+t.v) < 0:
                            t.x = t.x-1+19
                        elif t.v > 0: t.x += 1
                        else: t.x-=1
                        if (t.x,carriles.index (carril)) == (cohete.x,cohete.y): 
                            cohete.vida = max (cohete.vida-10,0)
                            perdida = True
                            colision = True
                            t.x = 10000
        if not colision: perdida = False
        if e != "Permanecer en la misma posición": 
            cohete.combustible -= 1
        cohete.oxigeno -= 1
        actualizacion (filas)
        n +=1
def actualizacion (filas):
    tortuga.clearstamps ()
    for y, fila in enumerate(filas):
        if fila != "libre":
            for elemento in fila:
                if 0 <= elemento.x < 20:
                    try:
                        tortuga.clearstamp(elemento.id[0])
                        elemento.id.clear()
                    except:pass
                    elemento.id.append(poner_asteroide(elemento.x, y))
    try:
        tortuga.clearstamp(cohete.id[0])
        cohete.id.clear()
    except:pass
    cohete.id.append(poner_cohete(cohete.x, cohete.y))
def poner_asteroide (x,y):
    tortuga.up()
    tortuga.goto (-350+x*35+35/2,-175+y*35+35/2)
    tortuga.shape ("circle")
    tortuga.shapesize (30/20,30/20)
    tortuga.color ("#001BA4")
    return tortuga.stamp ()
def poner_cohete (x,y):
    tortuga.up()
    tortuga.goto (-350+x*35+35/2,-175+30/2)
    tortuga.shape ("triangle")
    tortuga.setheading (cohete.ang+90)
    tortuga.shapesize (20/20,30/20)
    tortuga.color ("#FF0000")
    return tortuga.stamp ()
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
def registrar_flecha():
    for v in range(1, 5):
        largo = v * 8 
        forma = Shape("compound")
        forma.addcomponent(((0,15),(8,0),(-8,0)), "#FFFFFF", "#FFFFFF")
        forma.addcomponent(((3,0),(3,-largo),(-3,-largo),(-3,0)), "#FFFFFF", "#FFFFFF")
        Screen().addshape(f"flecha_{v}", forma)
def informar (n,e,coordenada_anterior,coordenada_posterior,r):
    printt (f"Paso {n}")
    printt (f"Vida: {cohete.vida}/{vida_total}")
    printt (f"Oxígeno: {cohete.oxigeno}/{oxigeno_total}")
    printt (f"Combustible: {cohete.combustible}/{combustible_total}")
    printt (f"Ángulo: {cohete.ang}º")
    printt (e)
    if coordenada_anterior != coordenada_posterior: printt (f"Se ha trasladado de {coordenada_anterior} --> {coordenada_posterior}")
    elif coordenada_anterior == coordenada_posterior: printt (f"Se ha trasladado de {coordenada_anterior} --> {coordenada_posterior} (no se ha movido)") 
    printt (f"Resumen: {r}")
    print ("",end="\n")
def main3 (n):
    eventos_destacados.append ("Ha salvado a la humanidad")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m Enhorabuena... Ha conseguido superar el cinturón de asteroides. Pero me temo que aún queda el último paso.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m Dime qué tengo que hacer.")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m La nave alienígena es demasiado resistente. La única forma de destruirla es detonar un misil nuclear en su interior.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m Entonces... lánzalo.")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m Ojalá pudiera. Desde que la Luna fue destruida, ningún misil puede mantener la trayectoria sin un piloto.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m ...")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m Lo siento. He conectado el piloto automático de su nave... y he armado los explosivos.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m ¿Me estás diciendo que... no voy a volver?")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m No. Si le hubiera contado la verdad desde el principio, jamás habría aceptado la misión.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m ...")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m ¿Con esto... se salvarán todos?")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m Sí. La humanidad sobrevivirá gracias a usted.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m Entonces... ha merecido la pena.")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m Dile a mi familia que pensé en ellos hasta el último segundo...")
    printt("\033[1m Hacker:\033[0m\033[38;2;0;255;120m Lo haré. Y también les diré que el héroe que salvó el mundo nunca pidió reconocimiento.")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m La nave acelera de forma automática.")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m La gigantesca nave alienígena ocupa todo el horizonte.")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m 5...")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m 4...")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m 3...")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m 2...")
    printt("\033[1m Tú:\033[0m\033[38;2;0;255;120m Adiós...")
    printt("\033[1m Sistema:\033[0m\033[38;2;0;255;120m 1...")
    print("\n\n\033[1;31m¡¡BOOOOOOOOM!!\033[0m")
    printt("\033[38;2;0;255;120m Un destello blanco envuelve el espacio.")
    printt("\033[38;2;0;255;120m La nave alienígena desaparece entre una inmensa explosión.")
    printt("\033[38;2;0;255;120m El silencio vuelve al universo.")
    printt("\033[38;2;0;255;120m La Tierra... está a salvo.")
    resumir ("exito",n)
def resumir (resultado,n):
    try: pantalla.bye ()
    except: pass
    print ("-"*60,end="")
    print ()
    print (f"\033[1m Nombre de la expedición:\033[0m\033[38;2;0;255;120m {nombre_expedicion}")
    print (f"\033[1m Número de pasos:\033[0m\033[38;2;0;255;120m {n}")
    try:print (f"\033[1m Oxígeno restante / Oxígeno inicial:\033[0m\033[38;2;0;255;120m {cohete.oxigeno}/{oxigeno_total}")
    except:print (f"\033[1m Oxígeno restante / Oxígeno inicial:\033[0m\033[38;2;0;255;120m {cohete.oxigeno}/{cohete.oxigeno}")
    try:print (f"\033[1m Combustible restante / Combustible inicial:\033[0m\033[38;2;0;255;120m {cohete.combustible}/{combustible_total}")
    except:print (f"\033[1m Combustible restante / Combustible inicial:\033[0m\033[38;2;0;255;120m {cohete.combustible}/{cohete.combustible}")
    try:print (f"\033[1m Vida restante de la nave / Vida inicial de la nave:\033[0m\033[38;2;0;255;120m {cohete.vida}/{vida_total}")
    except:print (f"\033[1m Vida restante de la nave / Vida inicial de la nave:\033[0m\033[38;2;0;255;120m {cohete.vida}/{cohete.vida}")
    print (f"\033[1m Vida restante / Vida inicial:\033[0m\033[38;2;0;255;120m {p.vida}/{105-5*dificultad}")
    if resultado != "fracaso": print (f"\033[1m Ángulo final / Ángulo inicial:\033[0m\033[38;2;0;255;120m {cohete.ang}º <-- {angulo}º")
    if resultado == "fracaso":
        print (f"\033[1m Posición final / Posición inicial:\033[0m\033[38;2;0;255;120m ({p.x},{p.y})/({xi},{yi})")
    else:
        print (f"\033[1m Posición final / Posición inicial:\033[0m\033[38;2;0;255;120m ({cohete.x},{cohete.y})/(10,0)")
    print (f"\033[1m Eventos destacados:\033[0m\033[38;2;0;255;120m {eventos_destacados}")
    if "Ha muerto" in eventos_destacados:
        print (f"\033[1m Causa de finalización:\033[0m\033[38;2;0;255;120m ha muerto en una pelea contra un guardia")
    elif "Se ha quedado sin combustible" in eventos_destacados:
        print (f"\033[1m Causa de finalización:\033[0m\033[38;2;0;255;120m se ha quedado sin combustible y por tanto no ha podido finalizar la misión")
    elif "Se ha quedado sin oxígeno" in eventos_destacados:
        print (f"\033[1m Causa de finalización:\033[0m\033[38;2;0;255;120m ha muerto asfixiado porque se ha quedado sin oxígeno")
    elif "Su nave ha sido destruida" in eventos_destacados:
        print (f"\033[1m Causa de finalización:\033[0m\033[38;2;0;255;120m ha colisionado con demasiados asteroides")
    elif "Ha salvado a" in eventos_destacados:
        print (f"\033[1m Causa de finalización:\033[0m\033[38;2;0;255;120m ha salvado a la humanidad a costa de su vida, por lo que ha muerto, pero como un héroe")
    if resultado == "exito":
        texto = "ha finalizado exitosamente la misión"
    else: texto = "ha fracasado"
    print (f"\033[1m Resultado de la misión:\033[0m\033[38;2;0;255;120m {texto}")
    print ("-"*60,end="")
    print ()
    while True:
        respuesta = input ("Desea volver a comenzar la misión (Sí/No): ")
        if respuesta.lower () in ["si","sí","no"]: break
        else: print ("Respuesta no válida")
    if respuesta.lower () in ["si","sí"]:
        subprocess.run([sys.executable, sys.argv[0], nombre_persona])
    else: printt ("Ha sido un honor trabajar con usted y espero volver a verle pronto")
    sys.exit ()
if __name__== "__main__":
    main()
