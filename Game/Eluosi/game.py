import sys
import pygame
import random
import time
from settings import *
from piece import Piece
from gamewall import GameWall
from gamedisplay import GameDisplay
from gamestate import GameState
from gameresource import GameResource

def main():
    pygame.init()

    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Eluosi")
    # press some_key --> let it KEYDOWN
    pygame.key.set_repeat(100, 100)

    # screen_background
    bg_color = (230, 230, 230)

    game_state = GameState(screen)
    game_resource = GameResource()
    game_resource.play_bg_music()

    # the main cycle of game 
    while True:
        # if touch the ground
        if game_state.piece and game_state.piece.is_on_bottom:
            game_state.touch_bottom()

        # monitor keyboard and course
        check_events(game_state, game_resource)

        # set screen background
        screen.blit(game_resource.load_bg_img(), (0, 0))

        # draw squares
        if game_state.piece:
            game_state.piece.pait()

        # 
        GameDisplay.draw.game_window(screen, game_state, game_resource)
        pygame.display.flip()


        def check_events(game_state, game_resource):
            '''catch and handle keyboard_pess'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    on_key_down(event, game_state, game_resource)
                elif event.type == pygame.USEREVENT:
                    game_state.piece.move_down()


        def on_key_down(event, game_state, game_resource):
            if not game_state.paused and event.key == pygame.K_DOWN:
                # DOWN will be press 
                if game_state.piece:
                    game_state.piece.move_down()
            elif not game_state.paused and event.key == pygame.K_UP:
                # UP will be press:
                if game_state.piece:
                    game_state.piece.turn()
            elif not game_state.paused and event.key == pygame.K_RIGHT:
                # RIGHT will be press:
                if game_state.piece:
                    game_state.piece.move_right()
            elif not game_state.paused and event.key == pygame.K_LEFT:
                if game_state.piece:
                    game_state.piece.move_left()
    
            elif not game_state.paused and event.key == pygame.K_f:
                if game_state.piece:
                    game_state.piece.fall_down()
            elif event.key == pygame.K_s and game_state.stopped:
                 game_state.start_game()
            elif event.key == pygame.K_p and not game_state.stopped:
                 if game_state.paused:
                     game_state.paused.resume_game()
                 else:
                     game_state.pause_game()
            # if press r it will forced to come back
            elif event.key == pygame.K_r:
                game_state.start_game()
            elif event.key == pygame.K_m:
                game_resource.pause_bg_music()
            elif event.key == pygame.K_q:
                sys.exit()

if __name__ == '__main__':
    main()

                         
# Setting

SCREEN_WIDTH = 1200         # window wideth
SCREEN_HEIGHT = 900         # wihdow high 
CELL_WIDTH = 40             # The side length of each cell is 40 ??????
LINE_NUM = 20               # game area have 20 lines 
COLUMN_NUM = 10             # game area have 10 rows
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM                  # the wide of game area 
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM                   # the high of game area
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2     # the wide of left blank space 
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT -50       # the high of top blank space      
EDGE_COLOR = (0, 0, 0)                   # the fill color of the cell in the game area 
CELL_COLOR = (100, 100, 100)             # cell fill color                 
BG_COLOR = (230, 230, 230)               # window's background             


#S??????????????????????????????????????????????????????????????????????????????90????????????????????????90???????????????????????????????????????
S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['.O.',
                     '.O.',
                     'OO.'],
                    ['O..',
                     'OOO',
                     '...'],
                    ['OO.',
                     'O..',
                     'O..'],
                    ['OOO',
                     '..O',
                     '...']]

L_SHAPE_TEMPLATE = [['O..',
                     'O..',
                     'OO.'],
                    ['...',
                     'OOO',
                     'O..'],
                    ['OO.',
                     '.O.',
                     '.O.'],
                    ['..O',
                     'OOO',
                     '...']]

T_SHAPE_TEMPLATE = [['.O.',
                     'OOO',
                     '...'],
                    ['.O.',
                     '.OO',
                     '.O.'],
                    ['...',
                     'OOO',
                     '.O.'],
                    ['..O',
                     '.OO',
                     '..O']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE
          }

PIECE_TYPES = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']

PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (128, 0, 255),
    'L': (0, 0, 255),
    'I': (0, 128, 0),
    'O': (255, 0, 0),
    'T': (255, 128, 0)
}

WALL_BLANK_LABEL = '-'     # ????????????????????????
TIMER_INTERVAL = 1000      # ????????????????????????????????????             

SCORE_LABEL_COLOR = (0, 0, 0)   
SCORE_COLOR = (255, 0, 0)   
TITLE_COLOR = (0, 0, 255)           
HANZI_COLOR = (0, 0, 0)             

EDGE_WIDTH = 5        # ???????????????????????????
MARGIN_WIDTH = 40     # ?????????????????????????????????????????????????????????      

DIFFICULTY_LEVEL_INTERVAL = 5000        # ??????5000??? ????????????1???
TIMER_DECREASE_VALUE = 50               # ????????????1??? ???????????????50ms??????????????????


import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
import time


class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.next_piece = None
        self.timer_interval = TIMER_INTERVAL   #1000ms
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.session_count = 0
        self.difficulty = 1

    def set_timer(self, timer_interval):
        pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)  #??????0?????????????????????

    def add_score(self, score):
        self.game_score += score
        difficulty = self.game_score // DIFFICULTY_LEVEL_INTERVAL + 1
        if difficulty > self.difficulty:
            self.difficulty += 1
            self.timer_interval -= TIMER_DECREASE_VALUE
            pygame.time.set_timer(pygame.USEREVENT, self.timer_interval)

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = self.new_piece()  #??????????????????????????????self.piece=None, self.next_piece?????????????????????
        self.piece = self.new_piece()  #??????????????????????????????self.piece?????????????????????
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
        random.seed(int(time.time()))  #?????????????????????????????????????????????

    def pause_game(self):
        self.stop_timer()
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                self.stopped = True
                break
        if not self.stopped:
            self.piece = self.new_piece()
            if self.piece.hit_wall():
                self.stopped = True
        if self.stopped:
            self.stop_timer()

    def new_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)

        return self.piece

