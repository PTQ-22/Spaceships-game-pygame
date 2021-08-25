import pygame

class PlayerBullet:

    def __init__(self, x, y):
        self.img = pygame.image.load("./images/bullets/bullet_green.png")
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        self.move()

    def move(self):
        self.y -= 10

    def out_of_game(self):
        if self.y <= 0:
            return True
        return False
    
    def hit(self, opponent, win):
        if self.x > (opponent.x + opponent.point_x_1) and (self.x + 5) < (opponent.x + opponent.point_x_2 ):
            if self.y > opponent.y and (self.y + 5) < (opponent.y + opponent.height):
                self.draw_hit(win)
                return True
        elif self.x > opponent.x and (self.x + 5) < (opponent.x + opponent.width):
            if self.y > (opponent.y + opponent.point_y_1) and (self.y + 5) < (opponent.y + opponent.point_y_2):
                self.draw_hit(win)
                return True
        return False
        
        """ if self.x > opponent.x and (self.x + 5) < (opponent.x + opponent.width):
                if self.y > opponent.y and (self.y + 5) < (opponent.y + opponent.height):
                    self.draw_hit(win)
                    return True"""
    def draw_hit(self, win):
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)

        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)                    
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 9)
        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)
                        
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 20)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 9)
        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3) 