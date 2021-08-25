import pygame
pygame.init()

class Button(object):
    def __init__(self, x, y, width, height, color, text='', font_color=(0, 0, 0), font_size=30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.uses = 5
        self.font_color = font_color
        self.font_size = font_size
        self.border_size = 5
        self.big_text = False
        self._1star_x_pos = self.x + 150
        self._1star_y_pos = self.y + 10
        self._2star_x_pos = self.x + 200
        self._2star_y_pos = self.y + 10
        self._3star_x_pos = self.x + 250
        self._3star_y_pos = self.y + 10

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.border_size, self.y - self.border_size, self.width + self.border_size*2, self.height + self.border_size*2), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', self.font_size)
            text = font.render(self.text, True, self.font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2 ), self.y + (self.height / 2 - text.get_height() /2 )))
        if self.big_text:
            f = pygame.font.Font('freesansbold.ttf', 30)
            t = f.render(self.big_text, True, (255, 0, 0))
            win.blit(t, (self.x + 7, self.y - (self.height / 2 - text.get_height() /2 )))

    def is_mouse(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def center_and_draw_big_text(self, text):
        self.x = 400
        self.y = 250
        self.width = 200
        self.height = 100 
        self.font_size = 30
        self.big_text = text

    def draw_with_stars(self, win, s_1, s_2, s_3):
        if s_1:
            self._1star_color = (255, 255, 0)
        else:    
            self._1star_color = (0, 0, 50)
        if s_2:
            self._2star_color = (255, 255, 0)
        else:
            self._2star_color = (0, 0, 50) #(255, 255, 0)
        if s_3:
            self._3star_color = (255, 255, 0)
        else:
            self._3star_color = (0, 0, 50)

        pygame.draw.rect(win, (0, 0, 0), (self.x - self.border_size, self.y - self.border_size, self.width + self.border_size*2, self.height + self.border_size*2), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', self.font_size)
            text = font.render(self.text, True, self.font_color)
            win.blit(text, (self.x + (self.width/4 - text.get_width()/2 ), self.y + (self.height / 2 - text.get_height() /2 )))
            pygame.draw.polygon(win, self._1star_color, [(self._1star_x_pos, self._1star_y_pos), # 1
                                                         (self._1star_x_pos + 4, self._1star_y_pos + 8), # 2
                                                         (self._1star_x_pos + 12, self._1star_y_pos + 10), # 3
                                                         (self._1star_x_pos + 6, self._1star_y_pos + 16), # 4
                                                         (self._1star_x_pos + 8, self._1star_y_pos + 24), # 5
                                                         (self._1star_x_pos, self._1star_y_pos + 20), # 6
                                                         (self._1star_x_pos - 8, self._1star_y_pos + 24), # 7
                                                         (self._1star_x_pos - 6, self._1star_y_pos + 16), # 8
                                                         (self._1star_x_pos - 12, self._1star_y_pos + 10), # 9
                                                         (self._1star_x_pos - 4, self._1star_y_pos + 8)  # 10
                                                         ])
            pygame.draw.polygon(win, self._2star_color, [(self._2star_x_pos, self._2star_y_pos), # 1
                                                         (self._2star_x_pos + 4, self._2star_y_pos + 8), # 2
                                                         (self._2star_x_pos + 12, self._2star_y_pos + 10), # 3
                                                         (self._2star_x_pos + 6, self._2star_y_pos + 16), # 4
                                                         (self._2star_x_pos + 8, self._2star_y_pos + 24), # 5
                                                         (self._2star_x_pos, self._2star_y_pos + 20), # 6
                                                         (self._2star_x_pos - 8, self._2star_y_pos + 24), # 7
                                                         (self._2star_x_pos - 6, self._2star_y_pos + 16), # 8
                                                         (self._2star_x_pos - 12, self._2star_y_pos + 10), # 9
                                                         (self._2star_x_pos - 4, self._2star_y_pos + 8)  # 10
                                                         ])
            pygame.draw.polygon(win, self._3star_color, [(self._3star_x_pos, self._3star_y_pos), # 1
                                                         (self._3star_x_pos + 4, self._3star_y_pos + 8), # 2
                                                         (self._3star_x_pos + 12, self._3star_y_pos + 10), # 3
                                                         (self._3star_x_pos + 6, self._3star_y_pos + 16), # 4
                                                         (self._3star_x_pos + 8, self._3star_y_pos + 24), # 5
                                                         (self._3star_x_pos, self._3star_y_pos + 20), # 6
                                                         (self._3star_x_pos - 8, self._3star_y_pos + 24), # 7
                                                         (self._3star_x_pos - 6, self._3star_y_pos + 16), # 8
                                                         (self._3star_x_pos - 12, self._3star_y_pos + 10), # 9
                                                         (self._3star_x_pos - 4, self._3star_y_pos + 8)  # 10
                                                         ])