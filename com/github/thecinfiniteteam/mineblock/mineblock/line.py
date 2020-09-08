#encoding:utf-8
import pygame,os,sys,easygui
from pygame import locals

def init():
    pygame.init()
def cre_window(title,icontitle,ico):
    global window
    window = pygame.display.set_mode(size=(512,512))
    pygame.display.set_caption(title,icontitle)
    pygame.display.set_icon(ico);
def window_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # 判断鼠标是否按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判断是否是鼠标左键被按下
            if event.button == 1:
                print("鼠标左键被点击")
                # 获取鼠标坐标位置
                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]
                # 判断设定好的点击区域
                if 432 <= mouseX <= 432+72 and 432 <= mouseY <= 432+72:
                    global command
                    command = easygui.enterbox(title="Command", msg="Input Command",default="/");



def window_display_img(window_,image,x,y):
    window_.blit(image,(x,y))
"""
def window_click(x,y,x2,y2):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               mousePos = pygame.mouse.get_pos()
               mouseX,mouseY = mousePos[0],mousePos[1]
               print(mouseX,mouseY)
               #if mouseX == x and mouseX <= x2 and mouseY == y and mouseY <= y2:
               if x <= mouseX <= x2 and y >= mouseY <= y2:
                   #if window_click(432, 504, 432, 504):
                    return easygui.enterbox(title="Command", msg="Input Command",default="/");
               else:
                   return False;
"""
def getInputCommand():
    return command
def window_DisplayFont(window_,text,r,g,b,x,y):
    font = pygame.font.Font("./fonts/def_HYBeiKeHeiW.ttf",16)
    window_text = font.render(text,True,(r,g,b))
    window_.blit(window_text,(x,y))

init()
while True:
    cre_window("Terminal","",pygame.image.load("./images/terminal.ico"))
    window_display_img(window, pygame.image.load("./images/terminal_line.png"), 0, 0)
    window_display_img(window,pygame.image.load("./images/terminal_line_button.png"),432,432)
    window_DisplayFont(window,"[MineBlock](info) Loader Python Lib",255,255,255,10,0)
    window_DisplayFont(window, "[MineBlock](info) Loader 3D", 255, 255, 255, 10, 15)
    window_DisplayFont(window, "[MineBlock](info) Reg Api", 255, 255, 255, 10, 30)
    #window_click(432, 432+72, 432, 432+72)
    window_event()
    pygame.display.update()
