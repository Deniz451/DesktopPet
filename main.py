import pygame
import time
import win32api
import win32con
import win32gui

pygame.init()

screen_width = 900
screen_height = 500

#screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Desktop Pet')

sprite_sheet_image = pygame.image.load('photos/sprite_sheet_cropped.png').convert_alpha()
bg = (50, 50, 50)
black = (0, 0, 0)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*bg), 0, win32con.LWA_COLORKEY)

def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(color)

    return image

run = True
while run:

    for x in range(12):
        screen.fill(bg)
        frame = get_image(sprite_sheet_image, x, 160, 315, 0.5, black)
        screen.blit(frame, (0, 0))
        pygame.display.flip()
        time.sleep(0.15) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
