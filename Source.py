import tkinter as tk
import tkinter.font as tkFont
from datetime import datetime
import time
import mouse

past=time.time()
gui=False

print("Sleep Screen up and running")
def main():
    root = tk.Tk()
    root.geometry("1920x1080")
    root.config(bg="black")
    root.attributes('-fullscreen',True)

    fontObj=tkFont.Font(size=40)
    txtstr=tk.StringVar()
    txtstr.set("test")

    labeltxt=tk.Label(root,font=fontObj,textvariable=txtstr,fg="white",bg="black",height=20,width=70)
    labeltxt.pack()
    labeltxt.place(anchor="center",relx=0.5,rely=0.5)

    while True:
        if mouse.is_pressed(button="left"):
            root.destroy()
            gui=False
            break
        else:
            time.sleep(0.1)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            txtstr.set(current_time)
            root.update()
            
while True:
    if mouse.is_pressed(button="left"):
        past=time.time()
    else:
        time.sleep(0.1)
        now=time.time()
        if now-past>=450 and gui==False:
            gui=True
            main()
        
