# This file was made with the intention of being used with a halloween costume of the character Jacket from Payday 2 which allows the person to 
# play voice lines of the character by pressing a button on their hand to play the corresponding voice lines
# the idea of the random module to randomize the files as well as putting the voice_lines into a list was made by https://github.com/Kostowniak
# The initial creator of this code is https://github.com/dellthePROgrammer
# The code was developed on windows then brought to a raspberry pi where 3 buttons are used to play a different voice line

import os
from pydub.playback import play
import pygame
from random import randint as rd
from time import sleep

# function for the playing of the 'Hi' voice lines
def hi():
    directory = 'hi' # Directory of the hi files
    voice_lines = os.listdir(directory) # Gets the files from the directory
    list(voice_lines) # Puts the files from the directory into a list
    hi = voice_lines[rd(0,len(voice_lines) - 1)] # Sets the files used equal to a random number
    file = os.path.join(directory, hi) # Sets the file path
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

def arms():
    directory = 'arms' # Directory of the arms sound file
    file = os.path.join(directory, 'arms_outstretched.mp3') # Sets the file to be played
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

def random():
    directory = 'mp3' # The main dirctory for storing guns
    voice_lines = os.listdir(directory) # Gets the files from the directory
    list(voice_lines) # Puts the files from the directory into a list
    random = voice_lines[rd(0, len(voice_lines) - 1)] # Sets the files used equal to a random number
    file = os.path.join(directory, random) # Sets the file path
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

def arrest():
    # This is where all the voice line after arms out strecthed will go
    for i in range(0,2):
        directory = 'arrest' # The main dirctory for storing guns
        voice_lines = os.listdir(directory) # Gets the files from the directory
        list(voice_lines) # Puts the files from the directory into a list
        hi = voice_lines[i] # Sets the files used equal to a random number
        file = os.path.join(directory, hi) # Sets the file path
        pygame.init()
        pygame.mixer.music.unload() # First unloads te file if there was one before
        pygame.mixer.music.load(file) # Loads the file that is wanted
        pygame.mixer.music.play() # Plays the file loaded
        sleep(1.5)


# Main function of the program that will be used to call the functions related to the buttons pressed
def main():
    while True:
        n = input('hi, arms, or random: ').lower()
        if n == 'w':
            hi()
        elif n == 'a':
            arms()
        elif n == 's':
            random()
        elif n == 'd':
            arrest()
        elif n == '':
            break

if __name__ == '__main__':
    main()