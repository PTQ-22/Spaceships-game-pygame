import pygame
import json
from game.menu import Menu


class Main:

    def __init__(self):
        self.width = 1000
        self.height = 750
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.level = 0 # numer poziomu 0 -> menu, 1 -> level_1 ...
        self.num_of_levels = 9
        with open("star_data/data.json") as json_file:
            self.star_data = json.loads(json_file.read())
        if len(self.star_data) != self.num_of_levels:
            self.star_data.setdefault(f"level_{self.num_of_levels}", {"star_1": False, "star_2": False, "star_3": False})
            with open("star_data/data.json", 'w') as main_json_file:
                str_json_data = json.dumps(self.star_data)
                main_json_file.write(str_json_data)
            with open("star_data/data.json") as json_file:
                self.star_data = json.loads(json_file.read())
        self.menu = Menu(self.num_of_levels)
        pygame.display.set_caption("STATKI")
        pygame.display.set_icon(pygame.image.load("./images/icon/icon.png"))

    def main(self):
        while self.level != -1:
            self.clock.tick(30)
            pygame.display.update()
            self.draw_level()

    def draw_level(self):
        if self.level == 0:
            self.menu.draw(self.window, self.star_data)
            self.level = self.menu.buttons_events(self.level)        
        elif self.level == 777:
            with open("star_data/no_stars.json") as no_stars_file:
                self.star_data = json.loads(no_stars_file.read()) 

            with open("star_data/data.json", 'w') as main_json_file:
                str_json_data = json.dumps(self.star_data)
                main_json_file.write(str_json_data)
            self.level = 0
        else:
            self.level.draw(self.window)
            if self.level.is_star_data:
                self.star_data = self.level.pass_star_data()
                with open("star_data/data.json", 'w') as main_json_file:
                    str_json_data = json.dumps(self.star_data)
                    main_json_file.write(str_json_data)
            self.level = self.level.events()
    
    def __del__(self):
        with open("star_data/data.json", 'w') as main_json_file:
            str_json_data = json.dumps(self.star_data)
            main_json_file.write(str_json_data)
