import logging
from tkinter import messagebox

import ui
import gamemodes
import link

logging.basicConfig(format='[main.py] %(levelname)s: %(message)s', level=logging.INFO)


def setup():
    ui.init()

    ui.root.title(ui.lang.software_name)
    ui.root.bind('<F11>', toggleFullscreen)
    ui.root.protocol("WM_DELETE_WINDOW", close)
    ui.root.after(100,loop)
    ui.root.after(100,link.link.refresh_serial)
    ui.root.mainloop()

#Functions
    
def loop():
    global network_change
    link.link.readSerial()
    ui.root.after(100,loop)

fullscreen = False
def toggleFullscreen(n): #toggles fullscreen
    global fullscreen
    fullscreen = not fullscreen
    ui.root.attributes("-fullscreen", fullscreen)

def close(): #prompts user for confirmation when closing window
    if messagebox.askyesno(title=ui.lang.quit, message=ui.lang.quitmessage):
        ui.root.destroy()
        print("End")

if __name__ == "__main__":
    setup()
