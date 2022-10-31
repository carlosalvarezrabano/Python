#Programa para descargar vídeos de YouTube en formato mp4

#Importante instalar módulos para que el programa funcione
import tkinter as tk
import pytube as YouTube

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised', bg='black')
canvas1.pack()

label1 = tk.Label(root, text='YouTube Video Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200,25, window=label1)

label2 = tk.Label(root, text='Enter Video URL for download')
label2.config(font=('helvetica', 10))
canvas1.create_window(200,100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200,140, window=entry1)

def download():
    ytd_url = entry1.get()
    try:
        obj = YouTube(ytd_url)
        filter = obj.streams.filter(progressive=True, file_extension='mp4')
        #En filename se puede cambiar el nombre del video generado por el que se prefiera
        filter.get_highest_resolution().download(filename='myvideo.mp4')
        label3 = tk.Label(root, text='Downloading started...', font=('helvetica', 10))
        canvas1.create_window(200,210, window=label3)
    except Exception as e:
        label4 = tk.Label(root, text='Downloading Failed :(', font=('helvetica', 10))
        canvas1.create_window(200,210, window=label4)


button1 = tk.Button(text='Download', command=download, bg='black', fg= 'white, 
font='helvetica', 9, 'bold')
canvas1.create_window(200,130, window=button1)

root.mainloop()
