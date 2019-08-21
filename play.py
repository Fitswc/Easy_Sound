from playsound import playsound
from time import sleep
import pygame as game
#import library

game.mixer.init()

def play (endswith,sound,vol):
    if endswith == "wav":
        play = game.mixer.Sound(sound)
        play.set_volume(vol)
        play.play()
    else:
        game .mixer.load(sound)



