from playsound import playsound
from time import sleep
import pygame as game
#import library

game.mixer.init()

def play (endswith,sound,time):
    if endswith == "wav":
        play = game.mixer.Sound(sound)
        play.play()
    if endswith == "mp3":
        playsound(sound)

play("ogg","test.ogg",100)




