import os
import tkinter as tk
import random
from threading import Thread
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.configure(background='black')
root.geometry(f"150x320")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

frameCount = 9
anim_right = os.path.join(basedir, 'gif', 'right.gif')
anim_left = os.path.join(basedir, 'gif', 'left.gif')
anim_up = os.path.join(basedir, 'gif', 'up.gif')
anim_down = os.path.join(basedir, 'gif', '/down.gif')

frames = [tk.PhotoImage(file=anim_up, format='gif -index %i' % (i)) for i in range(frameCount)]

x = 0
y = 0
is_animating = False

def update_animation(index):
    global is_animating
    if not is_animating:
        return
    frame = frames[index]
    index += 1
    if index == frameCount:
        index = 0
    label.configure(image=frame)
    root.after(100, update_animation, index)

def change_position(targetX, targetY):
    global x, y, is_animating

    if not is_animating:
        return

    if abs(x - targetX) > 5 or abs(y - targetY) > 5:
        if x < targetX:
            x += 1
        elif x > targetX:
            x -= 1 

        if y < targetY:
            y += 1 
        elif y > targetY:
            y -= 1
        
        root.geometry('+{}+{}'.format(x, y)) 
        root.after(10, change_position, targetX, targetY)
    else:
        get_random_pos()

def get_random_pos():
    randX = random.randint(170, screen_width - 170)
    randY = random.randint(320, screen_heigth - 320)

    if randX > x:
         load_animation(anim_right)
    elif randX < x:
         load_animation(anim_left)
    elif randY > y:
         load_animation(anim_down)
    elif randY < y:
         load_animation(anim_up)

    change_position(randX, randY)

def load_animation(animation_file):
    global frames
    frames = [tk.PhotoImage(file=animation_file, format='gif -index %i' % (i)) for i in range(frameCount)]

def start_window_animation():
    global is_animating
    is_animating = True
    root.after(0, update_animation, 0)
    get_random_pos()

def stop_window_animation():
    global is_animating
    is_animating = False
    root.geometry('+0+0')
    label.configure(image='')

label = tk.Label(root, bd=0, bg='black')
label.pack()

def create_image():
    width = 64
    height = 64
    color1 = "black"
    color2 = "white"

    image = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        (width // 4, height // 4, 3 * width // 4, 3 * height // 4),
        fill=color2,
    )
    return image

def quit_app(icon, item):
    icon.stop()
    root.destroy()

menu = Menu(
    MenuItem("Start", lambda: start_window_animation()),
    MenuItem("Stop", lambda: stop_window_animation()),
    MenuItem("Termiante", lambda icon, item: quit_app(icon, item))
)

icon = Icon("Test App", create_image(), "Test App", menu)

def run_tray():
    icon.run()

tray_thread = Thread(target=run_tray, daemon=True)
tray_thread.start()

root.mainloop()
