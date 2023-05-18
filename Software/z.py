import tkinter as tk
import os
import pygame
import numpy as np
pygame.mixer.init()

global current_song
global song_list
global directory

directory = 'Music'
song_list = os.listdir(directory)
current_song = 0

song_path = os.path.join(directory, song_list[current_song])
np.random.shuffle(song_list)

def play_song():
    global current_song
    if song_list:
        print('Now Playing', song_list[current_song])
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
    else:
        print('No songs found in the directory.')

def pause_song():
    if pygame.mixer.music.get_busy():
       pygame.mixer.music.pause()
    else:
       pygame.mixer.music.unpause()   

def play_next():
    global current_song
    if current_song < len(song_list) - 1:
        current_song += 1
        
        play_song()
    else:
        quit()

def play_previous():
    global current_song
    if current_song > 0:
        current_song -= 1
        play_song()
    else:
        quit()

window = tk.Tk()
window.title('Music Player')
window.geometry('200x145')



play_button = tk.Button(window, text='Play', command=play_song)
pause_button = tk.Button(window, text='Pause', command=pause_song)
next_button = tk.Button(window, text='Next', command=play_next)
previous_button = tk.Button(window, text='Previous', command=play_previous)
stop_button = tk.Button(window, text='Stop', command=window.quit)

play_button.pack()
pause_button.pack()
previous_button.pack()
next_button.pack()
stop_button.pack()

window.mainloop()
