import pygame
import os


def load_image(file_name, useColorKey=False):
    if os.path.isfile(file_name):
        image = pygame.image.load(file_name)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + file_name + " - Check filename and path?")


def load_list(file_name):
    print(os.path.isdir(file_name))
    if os.path.isdir(file_name):
        list = []
        for name in os.listdir(file_name):
            list.append(load_image(file_name + '/' + name))
        # image = image.convert_alpha()
        # Return the image
        return list
    else:
        raise Exception("Error loading list: " + file_name + " - Check filename and path?")


def change_to(self, image_list, index):
    self.image = image_list[index]


def next_image(self, image_list):
    self.current_nb += 1
    if self.current_nb > len(image_list) - 1:
        self.current_nb = 0
        #self.is_shooting = False # obligatoire sinon shoot à l'infini, probleme avec monster sans doute
    change_to(self, image_list, int(self.current_nb))


def clock():
    current_time = pygame.time.get_ticks()
    return current_time


