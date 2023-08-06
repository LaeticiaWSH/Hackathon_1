import pygame
#import freetype
import numpy as np

class Emojis:
    def __init__(self):
        self. face = pygame.freetype("segoe-ui-symbol.ttf")
        self.face.set_char_size(int(self.face.available_sizes[-1].size)) 
    def create_surface(self, unicode):
        self.face.load_char(unicode, pygame.freetype.FT_LOAD_COLOR)
        ft_bitmap = self.face.glyph.bitmap
        bitmap = np.array(ft_bitmap.buffer, dtype=np.uint8).reshape((ft_bitmap.rows, ft_bitmap.width, 4))
        bitmap[:, :, [0, 2]] = bitmap[:, :, [2, 0]]
        return pygame.image.frombuffer(bitmap.flatten(), (ft_bitmap.width, ft_bitmap.rows), 'RGBA')

pygame.init()
window = pygame.display.set_mode((200, 200))
emojis = Emojis()

emoji = emojis.create_surface('😃')
#emoji = emojis.create_surface('\U0001F603')
rect = emoji.get_rect(center = window.get_rect().center)

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("lightgray")
    window.blit(emoji, rect)
    pygame.display.flip()

pygame.quit()