from sys import exit
from random import randint
from textwrap import dedent

class Cena(object):
    def entrada(self):
        print("Essa cena ainda não foi configurada.")
        exit(1)

class Engine(object):
    def __init__(self, cena.mapa):
        self.cena.mapa = cena.mapa

    def