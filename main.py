import tkinter as tk
import random

root = tk.Tk()
root.configure(background='black')
root.geometry(f"150x320")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

frameCount = 9
anim_right = './gif/right.gif'
anim_left = './gif/left.gif'
anim_up = './gif/up.gif'
anim_down = './gif/down.gif'
frames = [tk.PhotoImage(file=anim_up, format='gif -index %i' % (i)) for i in range(frameCount)]

x = 0
y = 0

def update_animation(index):
    frame = frames[index]
    index += 1
    if index == frameCount:
        index = 0
    label.configure(image=frame)
    root.after(100, update_animation, index)

def change_position(targetX, targetY):
    global x, y

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

label = tk.Label(root, bd=0, bg='black')
label.pack()

root.after(0, update_animation, 0)
get_random_pos()

root.mainloop()
