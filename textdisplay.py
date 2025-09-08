import pygame


class TextDisplay():
    def __init__(self,label,value,font,antialising,text_color,x,y):
        self.label = label
        self.value = value
        self.font = font
        self.antialising = antialising
        self.text_color = text_color
        self.x = x
        self.y = y
        self.update_surface()

    def update_surface(self):
        self.text_to_display = f"{self.label}{self.value}"
        self.surface = self.font.render(self.text_to_display, self.antialising,self.text_color)

    def update_value(self,new_value):
        self.value = new_value
        self.update_surface()


    def draw(self, screen):
        screen.blit(self.surface,(self.x, self.y))

    def update(self):
        pass
