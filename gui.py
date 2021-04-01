import tkinter as tk
import pafy
import os
from PIL import Image, ImageTk
from tkinter import Canvas
import urllib.request


def thumbnail():
    link = video.get()
    thmb = link[17:]
    canvas = Canvas(
        master=frame4,
        width=300,
        height=300
    )
    urllib.request.urlretrieve(f"http://i.ytimg.com/vi/{thmb}/default.jpg", "local-filename.jpg")
    filename = ImageTk.PhotoImage(Image.open('local-filename.jpg'))
    im1 = Image.open(r'local-filename.jpg')
    im1.save(r'localf.gif')
    filename = ImageTk.PhotoImage(Image.open('localf.gif'))
    Image.open('localf.gif').resize((20, 20))
    canvas.create_image(20, 20, image=filename)
    canvas.pack()
    l1 = tk.Label(master = frame4, image = 'localf.gif')
    l1.pack()
def save():
    beginning = tk.Label(
        master=frame2,
        text="Processing...",
        foreground='black'
    )
    beginning.pack()
    link = video.get()
    singlevid = pafy.new(link)
    res = singlevid.getbest()
    size = res.get_filesize()
    print(f'Size is {size} and resolution is {res}')
    vid = res.download(filepath=f"{file_path}")
    interactive = tk.Label(
        master=frame2,
        text="Done!",
        foreground='black'
    )
    interactive.pack()


homedir = os.path.expanduser("~")
file_path = os.path.join(homedir, 'Desktop')


window = tk.Tk()

frame4 = tk.Frame(master=window, width=50, bg="white")
frame4.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


title = tk.Label(
    master = frame1,
    text = 'Youtube Downloader',
    foreground = 'white',
    background = 'red',
)
title.pack()


video = tk.Entry(
    master = frame2,
)
video.pack()


download = tk.Button(
    master = frame3,
    text = 'Download',
    width = 25,
    height = 5,
    foreground = 'orange',
    command = thumbnail
)

download.pack()

window.mainloop()