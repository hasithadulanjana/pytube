from __future__ import unicode_literals
import PySimpleGUI as sg
import youtube_dl

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter your youtube link'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Close Window')]]


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
# Create the Window
window = sg.Window('Youtube downloader', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
event, values = window.read()
link = values['textbox']
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
         }],
        }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
 ydl.download([link])
    
window.close()
