import pygame
from game.hp_bar import HpBar
from .bullet import PlayerBullet


class Player(HpBar):
    def __init__(self):
        self.x = 300
        self.y = 600
        self.point_x_1 = 49
        self.point_x_2 = 74
        self.point_y_1 = 38
        self.point_y_2 = 63
        self.x_change = 0
        self.y_change = 0
        self.pos_change = 15
        self.animation_counter = 0
        self.hp = 200
        self.width = 120
        self.height = 120
        self.player_ship_imgs = []

        self.player_ship_imgs_state_still = []
        for i in range(11):
            self.player_ship_imgs_state_still.append(pygame.image.load(f"./images/player/player_{i + 1}.png"))

        self.player_ship_imgs_state_right = []
        for i in range(11):
            self.player_ship_imgs_state_right.append(pygame.image.load(f"./images/player/player_turn_right_test.png"))

        self.player_ship_imgs_state_left = []
        for i in range(11):
            self.player_ship_imgs_state_left.append(pygame.image.load(f"./images/player/player_turn_left_test.png"))

        self.player_ship_imgs = self.player_ship_imgs_state_still
        self.x_start = 10
        self.y_start = 700
        self.name = "GRACZ"
        self.x_end = 200
        self.y_end = 730
        self.boom = 0
        # self.lost_bullet = False

    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0 
        win.blit(self.player_ship_imgs[self.animation_counter // 3], (self.x, self.y))
        self.move()
        self.hp_bar(win)

    def move(self):
        self.fire_place_x = self.x + 47
        self.x += self.x_change
        self.y += self.y_change
        if self.x <= 0:
            self.x = 0
        if self.x >= 900:
            self.x = 900
        if self.y <= 0:
            self.y = 0
        if self.y >= 650:
            self.y = 650
    
    def get_keyboard_events(self, event, bullets):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.y_change -= self.pos_change
            if event.key == pygame.K_DOWN:
                self.y_change += self.pos_change
            if event.key == pygame.K_RIGHT:
                self.x_change += self.pos_change
                self.player_ship_imgs = self.player_ship_imgs_state_right
            if event.key == pygame.K_LEFT:
                self.x_change -= self.pos_change
                self.player_ship_imgs = self.player_ship_imgs_state_left
            if event.key == pygame.K_SPACE:
                bullets.append(PlayerBullet(self.fire_place_x, self.y))

        elif event.type == pygame.KEYUP:
            self.x_change = 0
            self.y_change = 0
            self.player_ship_imgs = self.player_ship_imgs_state_still
        return bullets
