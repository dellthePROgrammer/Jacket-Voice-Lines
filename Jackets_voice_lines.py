import os
from winsound import PlaySound
from pydub.playback import play
import pygame


def hi():
    directory = 'hi'
    voice_lines = os.listdir(directory)
    while True:
        for hi in voice_lines:
            file = os.path.join(directory, hi)
            pygame.init()
            n = input('')
            if n == '':
                pygame.mixer.music.unload()
                pygame.mixer.music.load(file)
                print(file)
                pygame.mixer.music.play()
                # main()
            elif n != '':
                main()

def arms():
    directory = 'arms'
    file = os.path.join(directory, 'arms_outstretched.mp3')
    pygame.init()
    print(file)
    pygame.mixer.music.unload()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    main()

def random():
    directory = 'mp3'
    voice_lines = os.listdir(directory)
    while True:
        for hi in voice_lines:
            file = os.path.join(directory, hi)
            pygame.init()
            n = input('')
            if n == '':
                pygame.mixer.music.unload()
                pygame.mixer.music.load(file)
                print(file)
                pygame.mixer.music.play()
                # main()
            elif n != '':
                main()

def main():
    while True:
        n = input('hi, arms, or random: ').lower()
        if n == 'hi':
            hi()
        elif n == 'arms':
            arms()
        elif n == 'random':
            random()
            
# while True:
#     # for filename in voice_lines:
#     #         file = os.path.join(directory, filename)
#     #         pygame.init()
#     #         while True:
#                 n = input('')
#                 if n == 'hi':
#                     directory = 'mp3\\hi'
#                     voice_lines = os.listdir(directory)
#                     while True:
#                         for hi in voice_lines:
#                             file = os.path.join(directory, hi)
#                             pygame.init()
#                             n = input('')
#                             if n == '':
#                                 pygame.mixer.music.unload()
#                                 pygame.mixer.music.load(file)
#                                 print(file)
#                                 pygame.mixer.music.play()
#                             elif n == 'q':
#                                 break
#                 elif n == 'arms':
#                     directory = 'mp3\\arms'
#                     voice_lines = os.listdir(directory)
#                     file = os.path.join(directory, 'arms_outstretched.mp3')
#                     pygame.init()
#                     print(file)
#                     pygame.mixer.music.unload()
#                     pygame.mixer.music.load(file)
#                     pygame.mixer.music.play()
#                 else:
#                     directory = 'mp3'
#                     voice_lines = os.listdir(directory)
#                     for random in voice_lines:
#                         file = os.path.join(directory, voice_lines)
#                         pygame.init()
#                         print(file)
#                         pygame.mixer.music.unload()
#                         pygame.mixer.music.load(file)
#                         pygame.mixer.music.play()                    
                
#             # voice_line = AudioSegment.from_wav(file)
#             # play(voice_line)



if __name__ == '__main__':
    main()