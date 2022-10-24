# This file was made with the intention of being used with a halloween costume of the character Jacket from Payday 2 which allows the person to 
# play voice lines of the character by pressing a button on their hand to play the corresponding voice lines
# the idea of the random module to randomize the files as well as putting the voice_lines into a list was made by https://github.com/Kostowniak
# The initial creator of this code is https://github.com/dellthePROgrammer
# The code was developed on windows then brought to a raspberry pi where 3 buttons are used to play a different voice line

import os
from pydub.playback import play
import pygame
from random import randint as rd
import time
import RPI.GPIO as GPIO

hi_button = 8
arms_button = 10
random_button = 12

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(hi_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def hi(channel):
    directory = 'hi' # Directory of the hi files
    voice_lines = os.listdir(directory) # Gets the files from the directory
    list(voice_lines) # Puts the files from the directory into a list
    hi = voice_lines[rd(0,len(voice_lines) - 1)] # Sets the files used equal to a random number
    file = os.path.join(directory, hi) # Sets the file path
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# function for the playing of the 'Hi' voice lines
# def hi():
#     directory = 'hi' # Directory of the hi files
#     voice_lines = os.listdir(directory) # Gets the files from the directory
#     list(voice_lines) # Puts the files from the directory into a list
#     hi = voice_lines[rd(0,len(voice_lines) - 1)] # Sets the files used equal to a random number
#     file = os.path.join(directory, hi) # Sets the file path
#     pygame.init()
#     pygame.mixer.music.unload() # First unloads te file if there was one before
#     pygame.mixer.music.load(file) # Loads the file that is wanted
#     pygame.mixer.music.play() # Plays the file loaded

def arms(channel):
    directory = 'arms' # Directory of the arms sound file
    file = os.path.join(directory, 'arms_outstretched.mp3') # Sets the file to be played
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

def random(channel):
    directory = 'mp3' # The main dirctory for storing guns
    voice_lines = os.listdir(directory) # Gets the files from the directory
    list(voice_lines) # Puts the files from the directory into a list
    hi = voice_lines[rd(0, len(voice_lines) - 1)] # Sets the files used equal to a random number
    file = os.path.join(directory, hi) # Sets the file path
    pygame.init()
    pygame.mixer.music.unload() # First unloads te file if there was one before
    pygame.mixer.music.load(file) # Loads the file that is wanted
    pygame.mixer.music.play() # Plays the file loaded

def arrest(channel):
    # This is where all the voice line after arms out strecthed will go
    pass


# Main function of the program that will be used to call the functions related to the buttons pressed
def main():
        start_time = time.time()
        button_time = time.time() - start_time
        # n = input('hi, arms, or random: ').lower()
        # if n == 'hi':
        #     # hi()
        #     pass
        # elif n == 'arms':
        #     arms()
        # elif n == 'random':
        #     random()
        # elif n == 'arrest':
            # arrest()
        if GPIO.input(hi_button) == GPIO.HIGH:
            # hi()
            GPIO.add_event_detect(hi_button,GPIO.RISING,callback=hi) # Setup event on pin 10 rising edge
        if GPIO.input(arms_button) == GPIO.HIGH:
            if .1 <= button_time < 2:
                # arms()
                GPIO.add_event_detect(arms_button,GPIO.RISING,callback=arms)
            elif 2 <= button_time < 4:
                # arrest()
                GPIO.add_event_detect(arms_button,GPIO.RISING,callback=arrest)
        if GPIO.input(random_button) == GPIO.HIGH:
            GPIO.add_event_detect(random_button,GPIO.RISING,callback=random)
        # time.sleep(3)
        exit = input("Press enter to quit\n\n") # Run until someone presses enter
        if exit == '':
            GPIO.cleanup() # Clean up


if __name__ == '__main__':
    main()