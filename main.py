import pygame
import random
import win32api
import win32con
import win32gui

pygame.init()

#screen_width = 900
#screen_height = 500
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

spawn_x = random.randint(0, screen_width)
spawn_y = random.randint(0, screen_height)

screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#sprite_sheet_image = pygame.image.load('photos/sprite_sheet_cropped.png').convert_alpha()
sprite_sheet_image = pygame.image.load('photos/sprite_sheet.png').convert_alpha()
bg = (50, 50, 50)
black = (0, 0, 0)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*bg), 0, win32con.LWA_COLORKEY)


def get_image(sheet, frame, row, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), (row * height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image


clock = pygame.time.Clock()

x, y = spawn_x, spawn_y
move_speed = 5
column = 0
row = 0
column_count = sprite_sheet_image.get_width() // 160

run = True
while run:

    # Determine movement direction
    if random.randint(0, 1) == 0:
        rand_x = random.randint(0, screen_width)
        rand_y = y

        if rand_x > x:
            dir = 'right'
        elif rand_x < x:
            dir = 'left'
    else:
        rand_y = random.randint(0, screen_height)
        rand_x = x 

        if rand_y > y:
            dir = 'top'
        elif rand_y < y:
            dir = 'down'

    match dir:
        case 'right':
            row = 0
        case 'left':
            row = 1
        case 'down':
            row = 3
        case 'top':
            row = 2
        
    while (x, y) != (rand_x, rand_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if x < rand_x:
            x += min(move_speed, rand_x - x)
        elif x > rand_x:
            x -= min(move_speed, x - rand_x)
        if y < rand_y:
            y += min(move_speed, rand_y - y)
        elif y > rand_y:
            y -= min(move_speed, y - rand_y)

        
        screen.fill(bg)
        frame_image = get_image(sprite_sheet_image, column, row, 160, 360, 0.5, black)
        #frame_image = get_image(sprite_sheet_image, frame, 0, 160, 160, 0.5, black)
        screen.blit(frame_image, (x, y))
        pygame.display.flip()

        column = (column + 1) % column_count

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


pygame.quit()
