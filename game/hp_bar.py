import pygame

class HpBar:
    def hp_bar(self, win):
        self.x_hp = self.hp + self.x_start - 10
         
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(self.name, True, (0, 0, 0))
        win.blit(text, (self.x_start, self.y_start))
        pygame.draw.line(win, (0, 0, 0), (self.x_start, self.y_start + 30), (self.x_end + 5, self.y_end), 20)
        pygame.draw.line(win, (255, 0, 0), (self.x_start + 5, self.y_start + 30), (self.x_end, self.y_end), 7) # red
        if self.hp > 0:
            pygame.draw.line(win, (0, 255, 0), (self.x_start + 5, self.y_start + 30), (self.x_hp, self.y_end), 7) # green   
    
    def boom_after_collision(self, win):
        if self.boom <= 10:
            pygame.draw.circle(win, (255, 255, 0), (self.x + 50, self.y + 50), 40)

            pygame.draw.circle(win, (255, 100, 0), (self.x + 50, self.y + 50), 60)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 50, self.y + 50), 40)
                
            pygame.draw.circle(win, (255, 0, 0), (self.x + 50, self.y + 50), 80)
            pygame.draw.circle(win, (255, 100, 0), (self.x + 50, self.y + 50), 60)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 50, self.y + 50), 40)
                    
            pygame.draw.circle(win, (0, 0, 0), (self.x + 50, self.y + 50), 100)
            pygame.draw.circle(win, (255, 0, 0), (self.x + 50, self.y + 50), 80)
            pygame.draw.circle(win, (255, 100, 0), (self.x + 50, self.y + 50), 60)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 50, self.y + 50), 40) 
            self.boom += 1