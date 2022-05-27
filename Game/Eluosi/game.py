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

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
LINE_NUM = 20
COLUMN_NUM = 10 
# GAME_AREA_WIDTH = CELL_WIDTH * COULUMN_NUM
# GAME_AREA_HEIGHT = CELL_WIDTH * COULUMN_NUM
# GAME_AREA_LEFT  
