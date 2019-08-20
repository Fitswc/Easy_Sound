import pygame
from pygame.locals import *
from playsound import playsound
from time import sleep

def playmp3 (sound):
    playsound(sound)

playmp3('test.mp3')

def play (sound,vol = 10):
    pygame