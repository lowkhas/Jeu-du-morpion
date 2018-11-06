# -*- coding: utf-8 -*-
# Module graphique

"""
Module graphique pour l'ISN
Auteurs : M. Boehm & P. Remy, Lycée Les Pierres Vives, Carrières-sur-Seine
Version 3.5


SOMMAIRE :
PARTIE 1 : CONSTANTES ET CLASSES
PARTIE 2 : COULEURS
PARTIE 3 : FENETRE GRAPHIQUE
PARTIE 4 : AFFICHAGE DE TEXTES
PARTIE 5 : TRACE DE FORMES
PARTIE 6 : GESTION D'IMAGES
PARTIE 7 : GESTION DES SONS ET MUSIQUES
PARTIE 8 : GESTION DE LA SOURIS
PARTIE 9 : GESTION DU CLAVIER
PARTIE 10 : GESTION DU TEMPS
PARTIE 11 : VALEURS ALEATOIRES
"""

from math import *
import cmath
import random
import pygame
from pygame.locals import *

pygame.init()


#--------------------------------------------------
# PARTIE 1 : CONSTANTES ET CLASSES
#--------------------------------------------------

# PARTIE 1.1 : CONSTANTES GLOBALES

PYGAME_SDL_WEIGHT=0            # largeur de la fenêtre graphique
PYGAME_SDL_HEIGHT=0            # hauteur de la fenêtre graphique
PYGAME_SDL_FONT="verdana"      # police par défaut
PYGAME_SDL_AFFICHAGE=1         # constante par défaut pour l'affichage



# PARTIE 1.2 : CLASSES PREDEFINIES

class Point:
    """
    Cette classe définit un point prenant deux champs x et y.
    P.x est l'abscisse du point P.
    P.y est l'ordonnée du point P.
    On écrira P=Point(10,50) pour définir le point P de coordonnées (10,50).
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y



#--------------------------------------------------
# PARTIE 2 : COULEURS
#--------------------------------------------------

# PARTIE 2.1 : COULEURS PREDEFINIES

black=pygame.Color(0,0,0)
blue=pygame.Color(0,0,255)
brown=pygame.Color(88,41,0)
cyan=pygame.Color(0,255,255)
gold=pygame.Color(255,215,0)
gray=pygame.Color(128,128,128)
green=pygame.Color(0,255,0)
magenta=pygame.Color(255,0,255)
orange=pygame.Color(255,127,0)
pink=pygame.Color(253,108,158)
purple=pygame.Color(127,0,255)
red=pygame.Color(255,0,0)
salmon=pygame.Color(248,142,85)
silver=pygame.Color(206,206,206)
turquoise=pygame.Color(37,253,233)
white=pygame.Color(255,255,255)
yellow=pygame.Color(255,255,0)


# PARTIE 2.2 CREATION DE COULEURS RGB

def couleur_RGB(r,g,b):
    """
    Renvoie une couleur RGB
    r (compris entre 0 et 255) est la quantité de rouge
    g (compris entre 0 et 255) est la quantité de vert
    b (compris entre 0 et 255) est la quantité de bleu
    """
    return pygame.Color(r,g,b)




#--------------------------------------------------
# PARTIE 3 : FENETRE GRAPHIQUE
#--------------------------------------------------

# Initialisation de la fenêtre graphique
def init_graphic(W,H,name="Fenêtre ISN",bg_color=black,fullscreen=0):
    """
    Initialise la fenêtre graphique
    W est la largeur
    H est la hauteur
    name est le nom de la fenêtre (par défaut Fenêtre ISN)
    bg_color est la couleur de l'arrière-plan (par défaut noir)
    fullscreen affiche la fenêtre de taille W*H si la valeur est 0 (par défaut)
    et en plein écran pour une autre valeur
    L'origine (0,0) de la fenêtre graphique est situé en haut à gauche
    """
    global PYGAME_SDL_WINDOW,PYGAME_SDL_WEIGHT,PYGAME_SDL_HEIGHT
    PYGAME_SDL_WEIGHT=W; PYGAME_SDL_HEIGHT=H
    if fullscreen==0:
        PYGAME_SDL_WINDOW=pygame.display.set_mode((int(W),int(H)))
    else:
        PYGAME_SDL_WINDOW=pygame.display.set_mode((int(W),int(H)),FULLSCREEN)
    pygame.display.set_caption(name)
    pygame.draw.rect(PYGAME_SDL_WINDOW,bg_color,(0,0,int(W),int(H)),0)
    pygame.display.flip()



# Fermeture de la fenêtre graphique
def wait_escape(text="Appuyer sur Echap pour terminer",size=20,color=gray,text_bold=False,text_italic=False):
    """
    Attend que l'on tape Echap et quitte
    Instruction bloquante
    Les arguments text (chaîne de caractères), size (entier), color (couleur),
    text_bold (gras) et text_italic (italique) sont optionnels
    """
    if text!="":
        a=PYGAME_SDL_WEIGHT/2-largeur_texte(text,int(size),text_bold,text_italic)/2
        b=PYGAME_SDL_HEIGHT-hauteur_texte(text,int(size),text_bold,text_italic)
        P=Point(a,b)
        aff_pol(text,int(size),P,color,text_bold,text_italic)
    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0
    pygame.quit()


# Désactivation de l'affichage automatique
def affiche_auto_off():
    """
    Désactive l'affichage automatique
    """
    global PYGAME_SDL_AFFICHAGE
    PYGAME_SDL_AFFICHAGE=0


# Activation de l'affichage automatique
def affiche_auto_on():
    """
    Active l'affichage automatique
    """
    global PYGAME_SDL_AFFICHAGE
    PYGAME_SDL_AFFICHAGE=1


# Affichage des formes construites
def affiche_all():
    """
    Permet d'afficher les tracés de formes
    """
    pygame.display.flip()




#--------------------------------------------------
# PARTIE 4 : AFFICHAGE DE TEXTES
#--------------------------------------------------

def largeur_texte(T,t,text_bold=False,text_italic=False):
    """
    Calcule la largeur d'un texte T écrit en taille t
    Les arguments text_bold (gras) et text_italic (italique) sont optionnels
    """
    font=pygame.font.SysFont(PYGAME_SDL_FONT,t,bold=text_bold,italic=text_italic)
    text=font.render(T,1,black)
    text_coordinates=text.get_rect()
    return tuple(text_coordinates)[2]


def hauteur_texte(T,t,text_bold=False,text_italic=False):
    """
    Calcule la hauteur d'un texte T écrit en taille t
    Les arguments text_bold (gras) et text_italic (italique) sont optionnels
    """
    font=pygame.font.SysFont(PYGAME_SDL_FONT,t,bold=text_bold,italic=text_italic)
    text=font.render(T,1,black)
    text_coordinates=text.get_rect()
    return tuple(text_coordinates)[3]



def aff_pol(T,t,P,C,text_bold=False,text_italic=False):
    """
    Affiche une chaîne de caractère T en police Verdana à la taille t
    P est le point en haut à gauche
    C est la couleur d'affichage
    Les arguments text_bold (gras) et text_italic (italique) sont optionnels
    """
    P.x=int(P.x); P.y=int(P.y)
    font=pygame.font.SysFont(PYGAME_SDL_FONT,t,bold=text_bold,italic=text_italic)
    text=font.render(T,1,C)
    PYGAME_SDL_WINDOW.blit(text,(P.x,P.y))
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()



def list_fonts():
    """
    Renvoie la liste des polices disponibles
    """
    return pygame.font.get_fonts()



def test_font(S):
    """
    S est une chaîne de caractères
    Renvoie 1 si S est une police disponible et 0 sinon
    """
    if S in pygame.font.get_fonts():
        return 1
    return 0



def change_font(S):
    """
    S est une chaîne de caractères
    Change la police initiale en la police S si elle est disponible
    """
    global PYGAME_SDL_FONT

    if S in pygame.font.get_fonts():
        PYGAME_SDL_FONT=S



#--------------------------------------------------
# PARTIE 5 : TRACE DE FORMES
#--------------------------------------------------

def draw_pixel(P,C):
    """
    Affiche un pixel de couleur C au point P
    """
    P.x=int(P.x); P.y=int(P.y)
    pygame.draw.line(PYGAME_SDL_WINDOW,C,(P.x,P.y),(P.x,P.y),1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_line(P,Q,C):
    """
    Trace un segment de couleur C entre les points P et Q
    """
    P.x=int(P.x); P.y=int(P.y); Q.x=int(Q.x); Q.y=int(Q.y)
    pygame.draw.line(PYGAME_SDL_WINDOW,C,(P.x,P.y),(Q.x,Q.y),1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_triangle(P,Q,R,C):
    """
    Trace un triangle de couleur C et de sommets P, Q et R
    """
    P.x=int(P.x); P.y=int(P.y); Q.x=int(Q.x); Q.y=int(Q.y); R.x=int(R.x); R.y=int(R.y)
    pygame.draw.polygon(PYGAME_SDL_WINDOW,C,([P.x,P.y],[Q.x,Q.y],[R.x,R.y]),1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_fill_triangle(P,Q,R,C):
    """
    Trace un triangle de couleur C et de sommets P, Q et R
    """
    P.x=int(P.x); P.y=int(P.y); Q.x=int(Q.x); Q.y=int(Q.y); R.x=int(R.x); R.y=int(R.y)
    pygame.draw.polygon(PYGAME_SDL_WINDOW,C,([P.x,P.y],[Q.x,Q.y],[R.x,R.y]),0)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_rectangle(P,l,h,C):
    """
    Trace un rectangle de couleur C, de centre P, de largeur l et de hauteur h
    """
    pygame.draw.rect(PYGAME_SDL_WINDOW,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_fill_rectangle(P,l,h,C):
    """
    Trace un rectangle plein de couleur C, de centre P, de largeur l et de hauteur h
    """
    pygame.draw.rect(PYGAME_SDL_WINDOW,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),0)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_circle(P,r,C):
    """
    Trace un cercle de couleur C, de centre P et de rayon r
    """
    P.x=int(P.x); P.y=int(P.y); r=int(r)
    pygame.draw.circle(PYGAME_SDL_WINDOW,C,(P.x,P.y),r,1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_fill_circle(P,r,C):
    """
    Trace un cercle plein de couleur C, de centre P et de rayon r
    """
    P.x=int(P.x); P.y=int(P.y); r=int(r)
    pygame.draw.circle(PYGAME_SDL_WINDOW,C,(P.x,P.y),r,0)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_ellipse(P,l,h,C):
    """
    Trace une ellipse de couleur C inscrite dans un rectangle de centre P, de
    largeur l et de hauteur h
    """
    pygame.draw.ellipse(PYGAME_SDL_WINDOW,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_fill_ellipse(P,l,h,C):
    """
    Trace une ellipse pleine de couleur C inscrite dans un rectangle de centre P,
    de largeur l et de hauteur h
    """
    pygame.draw.ellipse(PYGAME_SDL_WINDOW,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),0)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_arc(P,l,h,start,end,C):
    """
    Trace une portion d'ellipse de couleur C inscrite dans un rectangle de centre P,
    de largeur l et de hauteur h.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[
    """
    pygame.draw.arc(PYGAME_SDL_WINDOW,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),start,end,1)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_sector(P,r,start,end,C):
    """
    Trace un secteur angulaire d'origine P, de rayon r, d'angle end-start et
    de couleur C.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[
    """
    draw_arc(P,2*r,2*r,start,end,C)
    draw_line(P,Point(P.x+r*cos(start),P.y-r*sin(start)),C)
    draw_line(P,Point(P.x+r*cos(end),P.y-r*sin(end)),C)
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()


def draw_fill_sector(P,r,start,end,C):
    """
    Trace un secteur angulaire plein d'origine P, de rayon r, d'angle end-start et
    de couleur C.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[
    """
    affiche_auto_off()
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            z=complex(x,y)
            arg=cmath.phase(z)
            if arg<0:
                arg+=2*pi
            if(abs(z)<=r and start<=arg<=end):
                draw_pixel(Point(P.x+x,P.y-y),C)
    affiche_auto_on()
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()



#--------------------------------------------------
# PARTIE 6 : GESTION D'IMAGES
#--------------------------------------------------

def load_image(titre,P):
    """
    Affiche une image
    Titre est une chaîne de caractère donnant le titre de l'image
    P est le point en haut à gauche de l'image
    Renvoie l'image sous forme de surface pygame
    """
    P.x=int(P.x); P.y=int(P.y)
    fond = pygame.image.load(titre).convert()
    PYGAME_SDL_WINDOW.blit(fond,(P.x,P.y))
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()
    return fond


def load_image_transp(titre,P):
    """
    Affiche une image à transparence
    Titre est une chaîne de caractère donnant le titre de l'image
    P est le point en haut à gauche de l'image
    Renvoie l'image sous forme de surface pygame
    """
    P.x=int(P.x); P.y=int(P.y)
    fond = pygame.image.load(titre).convert_alpha()
    PYGAME_SDL_WINDOW.blit(fond,(P.x,P.y))
    if PYGAME_SDL_AFFICHAGE==1:
        pygame.display.flip()
    return fond


def transfer_image(titre):
    """
    Renvoie la surface pygame correspondant à l'image
    Attention, l'image n'est pas affichée à l'écran ; cette fonction est
    utile pour obtenir les dimensions de l'image, la redimensionner ou la
    sauvegarder
    """
    return pygame.image.load(titre)


def save_image(I,F):
    """
    I est une surface pygame
    F est une chaîne de caractères
    Permet de sauvegarder la surface I dans un fichier F
    """
    pygame.image.save(I,F)


def get_size_image(I):
    """
    Renvoie les dimensions de la surface pygame I
    """
    return pygame.Surface.get_size(I)


def resize_image(I,W,H):
    """
    I est une surface pygame
    W et H sont des entiers supérieurs à 1
    Permet de redimensionner I avec la largeur W et la hauteur H
    Renvoie la nouvelle surface pygame
    """
    return pygame.transform.scale(I,(W,H))



#--------------------------------------------------
# PARTIE 7 : GESTION DES SONS ET MUSIQUES
#--------------------------------------------------


# PARTIE 7.1 : SONS

def play_sound(S):
    """
    S est une chaîne de caractères
    Joue le son S
    """
    pygame.mixer.Sound(S).play()


def stop_sound(S):
    """
    S est une chaîne de caractères
    Arrête le son S
    """
    pygame.mixer.Sound(S).stop()


def set_volume_sound(S,v):
    """
    S est une chaîne de caractères
    v est un flottant entre 0.0 et 1.0
    Permet de régler le volume du son S
    """
    pygame.mixer.Sound(S).set_volume(v)


def get_volume_sound(S):
    """
    S est une chaîne de caractères
    Renvoie le volume du son S
    """
    return pygame.mixer.Sound(S).get_volume()


# PARTIE 7.2 : MUSIQUES

def load_music(M):
    """
    M est une chaîne de caractères
    Charge la musique M dans la playlist
    Utiliser de préférence des .wav
    """
    pygame.mixer.music.load(M)


def play_music(loop=0):
    """
    Lance la playlist
    L'argument optionnel loop prend les valeurs 0 ou 1. Si loop vaut 1, alors la
    musique est jouée en boucle.
    """
    if loop==1:
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.play()


def restart_music():
    """
    Relance la playlist au début
    """
    pygame.mixer.music.rewind()


def stop_music():
    """
    Arrête la playlist
    """
    pygame.mixer.music.stop()


def pause_music():
    """
    Met la playlist en pause
    """
    pygame.mixer.music.pause()


def unpause_music():
    """
    Reprend la playlist
    """
    pygame.mixer.music.unpause()


def set_volume_music(v):
    """
    v est un flottant entre 0.0 et 1.0
    Permet de régler le volume de la musique
    """
    pygame.mixer.music.set_volume(v)


def get_volume_music():
    """
    Renvoie le volume de la musique
    """
    return pygame.mixer.music.get_volume()


def get_busy_music():
    """
    Renvoie 1 si la playlist est jouée et 0 sinon
    """
    return pygame.mixer.music.get_busy()




#--------------------------------------------------
# PARTIE 8 : GESTION DE LA SOURIS
#--------------------------------------------------

def wait_clic():
    """
    Attend que l'on clique gauche avec la souris
    Renvoie les coordonnées du point cliqué
    Instruction bloquante
    """
    pygame.event.clear()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                return Point(event.pos[0],event.pos[1])


def wait_clic_LR():
    """
    Attend que l'on clique avec la souris
    Renvoie une liste contenant une chaîne de caractère indiquant le bouton
    cliqué (G pour gauche et D pour droit) et les coordonnées du point cliqué
    Instruction bloquante
    """
    pygame.event.clear()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    return ["G",Point(event.pos[0],event.pos[1])]
                if event.button == 3:
                    return ["D",Point(event.pos[0],event.pos[1])]


def device_mouse_off():
    """
    Supprime le curseur de la souris dans la fenêtre graphique
    """
    pygame.mouse.set_visible(0)


def device_mouse_on():
    """
    Affiche le curseur de la souris dans la fenêtre graphique
    """
    pygame.mouse.set_visible(1)


def get_mouse():
    """
    Renvoie la position de la souris
    Instruction non bloquante
    """
    pygame.event.clear()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == MOUSEMOTION:
                return Point(event.pos[0],event.pos[1])



#--------------------------------------------------
# PARTIE 9 : GESTION DU CLAVIER
#--------------------------------------------------

def wait_key():
    """
    Attend que l'on tape sur une touche du clavier(y compris avec une combinaison
    de touches) et retourne le code ascii correspond. Instruction bloquante
    """
    pygame.event.clear()
    caractere=""
    while caractere=="":
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                caractere=event.dict['unicode']
                if caractere!="":
                    return ord(caractere)


def wait_space_letter():
    """
    Attend que l'on tape sur une touche du clavier
    Si la touche est une lettre, renvoie la lettre correspondante en majuscule
    Si la touche est la barre d'espace, renvoie la chaîne de caractère espace
    Sinon, renvoie une chaîne vide
    Instruction bloquante
    """
    key=wait_key()
    if 96<key<123:
        return chr(key-32)
    if key==32:
        return " "
    return ""


def wait_arrow():
    """
    Attend que l'on tape sur une touche du clavier
    Renvoie up, down, left, right suivant que l'on a tapé sur la flèche du
    haut, du bas, de gauche ou de droite
    Renvoie une chaîne vide sinon
    Instruction bloquante
    """
    pygame.event.clear()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return "up"
                elif event.key == K_DOWN:
                    return "down"
                elif event.key == K_LEFT:
                    return "left"
                elif event.key == K_RIGHT:
                    return "right"



# Les fonctions ci-dessous sont à combiner en général avec la fonction wait_key()
def get_space_letter(key):
    """
    key est un nombre code ascii (nombre entier entre 0 et 255)
    Si key est le code d'une lettre minuscule (valeur entre 97 et 122) ou
    majuscule (valeur entre 65 et 90), renvoie la lettre majuscule correspondante
    Si key est le code de l'espace (valeur 32), renvoie la chaîne de caractère espace
    Renvoie une chaîne vide dans les autres cas

    """
    if 64<key<91:
        return chr(key)
    if 96<key<123:
        return chr(key-32)
    if key==32:
        return " "
    return ""


def is_letter(key):
    """
    Teste si key est le code ascii d'une lettre minuscule (valeur entre 97 et
    122) ou d'une lettre majuscule (valeur entre 65 et 90)
    Retourne 1 si vrai et 0 sinon
    """
    if (64<key<91 or 96<key<123):
        return 1
    return 0


def is_space(key):
    """
    Teste si key est le code ascii de l'espace (valeur 32)
    Retourne 1 si vrai et 0 sinon
    """
    if key==32:
        return 1
    return 0


def is_return(key):
    """
    Teste si key est le code ascii de la touche return  (valeur 13)
    Retourne 1 si vrai et 0 sinon
    """
    if key==13:
        return 1
    return 0



#--------------------------------------------------
# PARTIE 10 : GESTION DU TEMPS
#--------------------------------------------------

def attendre(millisecondes):
    """
    Attend le nombre de millisecondes passé en argument
    """
    pygame.time.delay(millisecondes)


def chrono_start():
    """
    Démarre un chronomètre
    """
    global CHRONO
    CHRONO=pygame.time.get_ticks()


def chrono_val():
    """
    Affiche le temps écoulé en millisecondes depuis le lancement du chronomètre
    """
    global CHRONO
    return pygame.time.get_ticks()-CHRONO



#--------------------------------------------------
# PARTIE 11 : VALEURS ALEATOIRES
#--------------------------------------------------

def alea():
    """
    Renvoie un flottant dans l'intervalle [0,1[
    """
    return random.random()


def alea_int(a,b):
    """
    a et b sont des entiers
    Renvoie un entier dans l'intervalle [a,b]
    """
    return int(floor((b-a+1)*random.random()))+a

