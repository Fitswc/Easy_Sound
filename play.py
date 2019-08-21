from playsound import playsound
from time import sleep
import pygame as game
import os
#import library

game.mixer.init()

def play(sound):
    playsound(sound)
def ui_play(sound):
    os.system(sound)





