import os

links = open('links.txt')

for i in links:
    os.system('youtube-dl -o music/%(title)s-%(id)s.%(ext)s --extract-audio --audio-format mp3 {}'.format(i))
    

