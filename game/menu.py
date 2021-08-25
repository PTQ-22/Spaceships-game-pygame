import pygame
from buttons.button import Button
from levels.level_1 import Level_1  # V
from levels.level_2 import Level_2  # V
from levels.level_3 import Level_3  # V
from levels.level_4 import Level_4  # V
from levels.level_5 import Level_5  # V
from levels.level_6 import Level_6  # V
from levels.level_7 import Level_7  # x
from levels.level_8 import Level_8
from levels.level_9 import Level_9

class Menu:

    def __init__(self, num_of_levels):
        self.animation_counter = 0
        self.background_start_imgs = []
        for i in range(11):
            self.background_start_imgs.append(pygame.image.load(f"./images/menu_background/background_start_{i + 1}.png"))
        self.buttons = []
        self.buttons_list_counter = 60
        self.del_button = Button(820, 12, 150, 25, (255, 0, 0), 'Usuń postępy', font_size=20)
        for b in range(num_of_levels):
            self.buttons.append(Button(700, self.buttons_list_counter, 280, 50, (0, 0, 150), f"LEVEL {b + 1}"))
            self.buttons_list_counter += 70

    def draw(self, win, star_data):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0 
        win.blit(self.background_start_imgs[self.animation_counter // 3], (0, 0))
        self.del_button.draw(win)
        for b, button in enumerate(self.buttons):
            button.draw_with_stars(win,
                                   s_1=star_data[f"level_{b+1}"]['star_1'],
                                   s_2=star_data[f"level_{b+1}"]['star_2'],
                                   s_3=star_data[f"level_{b+1}"]['star_3'])

    def buttons_events(self, level):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    if button.is_mouse(pos):
                        button.color = (0, 0, 100)
                    else:
                        button.color = (0, 0, 150)
                if self.del_button.is_mouse(pos):
                    self.del_button.color = (200, 0, 0)
                else:
                    self.del_button.color = (255, 0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons[0].is_mouse(pos):
                    return Level_1()
                if self.buttons[1].is_mouse(pos):
                    return Level_2()
                if self.buttons[2].is_mouse(pos):
                    return Level_3()
                if self.buttons[3].is_mouse(pos):
                    return Level_4()
                if self.buttons[4].is_mouse(pos):
                    return Level_5()
                if self.buttons[5].is_mouse(pos):
                    return Level_6()
                if self.buttons[6].is_mouse(pos):
                    return Level_7()
                if self.buttons[7].is_mouse(pos):
                    return Level_8()
                if self.buttons[8].is_mouse(pos):
                    return Level_9()
                if self.del_button.is_mouse(pos):
                    return 777
        return 0
