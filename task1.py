import os
import sys

import pygame
import requests

http_proxy = "http://s2021010026:Mba23042006@proxy.volgatech.net:3128"
https_proxy = "http://s2021010026:Mba23042006@proxy.volgatech.net:3128"

proxyDict = {
    "http": http_proxy,
    "https": https_proxy
}

map_request = "https://static-maps.yandex.ru/1.x/?ll=134.217653,-25.058957&spn=20,20&l=map"
response = requests.get(map_request, proxies=proxyDict)


map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)