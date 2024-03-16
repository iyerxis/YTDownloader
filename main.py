##############################$
#$ // (:Made By Iyerxis:) // $#
##############################$

import yt_dlp
from tkinter import *
from tkinter import ttk, filedialog

#  Скачивание видоса
def download(link, output_path):
        with yt_dlp.YoutubeDL({'outtmpl': f"{output_path}/%(title)s.%(ext)s"}) as ydl:
            info = ydl.extract_info(link, download=True)
            title = info.get('title', '')
            return title

#  Только Аудио
def download_audio(link, output_path):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': f"{output_path}/%(title)s.mp3"}) as ydl:
        info = ydl.extract_info(link, download=True)
        title = info.get('title', '')
        return title

#  Получение ссылки и выбор директории
def sk():
    link = entr1.get()
    output = filedialog.askdirectory()
    if output:
        title = download(link, output)
        if title:
            string.set('Downloaded Successfully: ' + '"' + title + '"')
        else:
            string.set('Select a directory!')    

def sk_audio():
    link = entr1.get()
    output = filedialog.askdirectory()
    if output:
        title = download_audio(link, output)
        if title:
            string.set('Downloaded Successfully: ' + '"' + title + '"')
   
#  Проверка галОчки "Only audio"
def check_flag():
    if check_audio.get() == 1:
        command = sk_audio()
    else:
        command = sk()
    return command

#  Окно
root = Tk()
root.geometry("450x250")
root.resizable(width=False, height=False)
root.title('YouTube Downloader 1.1')
root.attributes("-alpha", 0.86)
root.config(bg='gray19')

#  Текст перед полем ввода
text1 = StringVar()
text1.set('Enter link to video:')
label = ttk.Label(foreground='white', background='gray19', textvariable=text1, font='sans')
label.pack(anchor=NW, padx=3)

#  Поле Ввода
entr1 = ttk.Entry(width=200, font='sans', )
entr1.pack(padx=5, pady=5)

#  ГалОчка онли аудио
check_audio = IntVar()
audio = ttk.Checkbutton(text="Only audio", variable=check_audio)
audio.pack(padx=6, pady=6, anchor=NW)

#  Кнопка загрузки
btn1 = ttk.Button(text='Go', command=check_flag) 
btn1.pack(anchor='s', expand=True, fill=X, ipadx=10, ipady=10)

#  Status
string = StringVar()
status = ttk.Label(foreground="gray18", textvariable=string, wraplength=250)
status.pack(padx=5, pady=5, anchor=NW)

#  Цикл окна
root.mainloop()