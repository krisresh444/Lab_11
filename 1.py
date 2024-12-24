import pygame
import sys

#Проверка победителя
def check_win(mas,znak):
    zero = 0
    for stroki in mas:
        zero += stroki.count(0)
        if stroki.count(znak) == 3:
            return znak
    for colonki in range(3):
        if mas[0][colonki]==znak and mas[1][colonki]==znak and mas[2][colonki]==znak:
            return znak
    if mas[0][0]==znak and mas[1][1]==znak and mas[2][2]==znak:
            return znak
    if mas[0][2]==znak and mas[1][1]==znak and mas[2][0]==znak:
            return znak
    if zero == 0:
        return 'Ничья('
    return False

pygame.init()

size_block = 100
otstup = 15
dlin = height = size_block*3 + otstup*4 #длина высота квадратика

size_window = (dlin,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

pink = (255,194,204)
green = (168,255,171)
orange = (255,199,102)
blue =(102,102,255)
black = (0,0,0)
white = (255,255,255)
mas = [[0]*3 for i in range(3)]
query = 0 # 1 2 3 4 5 6 7
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:#координаты мышки
            x_mouse,y_mouse = pygame.mouse.get_pos()
            colonki = x_mouse//(otstup+size_block)
            stroki = y_mouse//(otstup+size_block)
            if mas[stroki][colonki] == 0:
                if query%2 ==0:
                    mas[stroki][colonki] = 'x'
                else:
                    mas[stroki][colonki] = 'o'
                query+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query =0 
            screen.fill(black)      
    if not game_over:
        for stroki in range(3):
            for colonki in range(3):
                if mas[stroki][colonki]=='x':
                    color = pink
                elif mas[stroki][colonki]=='o':
                    color = blue
                else:
                    color = white
                x = colonki*size_block+(colonki+1)*otstup
                y = stroki*size_block+(stroki+1)*otstup
                pygame.draw.rect(screen,color,(x,y,size_block,size_block))
                if color == pink:
                    pygame.draw.line(screen,green,(x+4,y+4),(x+size_block-4,y+size_block-4),4)
                    pygame.draw.line(screen,green,(x+size_block-4,y+4),(x+4,y+size_block-4),4)
                elif color == blue:
                    pygame.draw.circle(screen,orange,(x+size_block//2,y+size_block//2),size_block//2-1,4)

    if (query-1)%2 ==0:#x
        game_over = check_win(mas,'x')
    else:#o
        game_over = check_win(mas,'o')

    if game_over:
        screen.fill(pink)#черный экран
        font = pygame.font.SysFont('stxingkai',80)#шрифт,размер
        text1 = font.render(game_over,True,blue)#либо крестик либо нолик либо ничья белым цветом
        text_rect = text1.get_rect() #его координаты
        #центр экрана
        text_x = screen.get_width() / 2-text_rect.width/2
        text_y = screen.get_height() / 2-text_rect.height/2
        screen.blit(text1,(text_x,text_y))#прикрепляет текст
    pygame.display.update()