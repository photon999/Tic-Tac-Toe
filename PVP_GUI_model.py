import pygame,sys
import numpy as np


# from sympy import true

pygame.init()

RED=(255,0,0)
BG_COLOR= (28,170,156)
LINE_COLOR=(23,145,135)
CIRCLE_COLOR=(239,231,200)
CROSS_COLOR=(66,66,66)


WIDTH=400
HEIGHT=WIDTH
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLS=3
SQUARE_SIZE=WIDTH//BOARD_COLS
CIRCLE_RADIUS= SQUARE_SIZE//3
CIRCLE_WIDTH=15
CROSS_WIDTH=25
SPACE=SQUARE_SIZE//4

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board 
board = np.zeros( (BOARD_ROWS,BOARD_COLS) )
print(board)

# pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_lines():
    #horizontal line 1
    pygame.draw.line(screen,LINE_COLOR,(0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)
     #horizontal line 2
    pygame.draw.line(screen,LINE_COLOR,(0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE),LINE_WIDTH)
    #vertical line 1
    pygame.draw.line(screen,LINE_COLOR,(SQUARE_SIZE,0),(SQUARE_SIZE,WIDTH),LINE_WIDTH)
    #vertical line 2
    pygame.draw.line(screen,LINE_COLOR,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,WIDTH),LINE_WIDTH)

draw_lines()
def mark_square(row,col,player):
    board[row][col]=player

def available_square(row,col):
    return board[row][col] ==0 

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if(board[row][col]==0):
                 return False
        
    return True

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*SQUARE_SIZE + SQUARE_SIZE/2),int(row*SQUARE_SIZE +SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2 :
                pygame.draw.line(screen,CROSS_COLOR,(int(col*SQUARE_SIZE +SPACE ),int(row*SQUARE_SIZE +SQUARE_SIZE-SPACE)),(int(col*SQUARE_SIZE+SQUARE_SIZE -SPACE),int(row*SQUARE_SIZE +SPACE)),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(int(col*SQUARE_SIZE +SPACE ),int(row*SQUARE_SIZE+ SPACE)),(int(col*SQUARE_SIZE +SQUARE_SIZE -SPACE),int(row*SQUARE_SIZE +SQUARE_SIZE-SPACE)),CROSS_WIDTH)

def check_win(player):
    #vertical win check
    for col  in range(BOARD_COLS):
        if(board[0][col]==player and board[1][col]==player and board[2][col]==player):
            draw_vertical_winning_line(col,player)
            return True
     #horizontal win check
    for row in range(BOARD_ROWS):
        if(board[row][0]==player and board[row][1]==player and board[row][2]==player):
            draw_horizontal_winning_line(row,player)
            return True
    #asc diag check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    #desc diag check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True
    
    return False
        

def draw_vertical_winning_line(col,player):
    posX=col*SQUARE_SIZE+SQUARE_SIZE//2
    if player==1:
        color=CIRCLE_COLOR
    if player ==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(posX,20),(posX,WIDTH-20),LINE_WIDTH)




def draw_horizontal_winning_line(row,player):
    posY=row*SQUARE_SIZE+SQUARE_SIZE//2
    if player==1:
        color=CIRCLE_COLOR
    if player ==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(20,posY),(WIDTH-20,posY),LINE_WIDTH)


def draw_asc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    if player ==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),LINE_WIDTH)


def draw_desc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    if player ==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0


#main loop
player =1
game_over=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type== pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX=event.pos[0] #X
            mouseY=event.pos[1] #Y

            clicked_row=mouseY//SQUARE_SIZE
            clicked_col=mouseX//SQUARE_SIZE

            # print(clicked_row)
            # print(clicked_col)
            if(available_square(clicked_row,clicked_col)):
                mark_square(clicked_row,clicked_col,player)
                draw_figures()
                game_over=check_win(player)
                player=player%2+1

        if event.type ==pygame.KEYDOWN:
             if event.key==pygame.K_r:
                restart()
                player=1
                game_over=False    
                
            # print(mouseX)
            # print(mouseY)
            # print(board)
    pygame.display.update()