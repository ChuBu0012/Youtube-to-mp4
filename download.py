from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Functions
    #เลือกโฟลเดอร์ที่จะเก็บ Video
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #รับ Url ที่กรอกเข้ามา
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')

    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    #ย้ายไฟล์ไปในโฟลเดอร์ที่เลือกไว้
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="เลือกโฟลเดอร์", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Download btns
download_btn = Button(screen, text="ดาวน์โหลดวีดีโอ",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
# add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
