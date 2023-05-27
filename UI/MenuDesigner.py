import json
from SerializationJson import SerializationJson
import pygame.sprite
import os

class MenuDesigner:
    def __init__(self, game):
        self.ui_elements = pygame.sprite.Group()
        self.spacing = 20
        self.orientatio = "vertical"
        self.background_color = (33, 174, 234)
        self.game = game
        self.Initialize()

    def Initialize(self):
        button = self.GetButtonByName("StartButton")
        button.rect.center = self.game.screen.get_rect().center

        self.ui_elements.add(button)
        self.GetLevelButtons()

    def GetButtonByName(self, name):
        with open("UI/menu.json", "r") as file:
            data = json.load(file)
            buttons = data["Buttons"]

            for btn in buttons:
                if btn["Name"] == name:
                    button = SerializationJson.SerializeButton(btn, self.game)
                    return button

        return None

    def Blitme(self):
        for el in self.ui_elements.sprites():
            el.blitme()

    def Update(self):
        self.game.screen.fill(self.background_color)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for el in self.ui_elements.sprites():
                    el.CheckButtonClick()

    def GetLevelButtons(self):
        json_files = [f for f in os.listdir("maps") if f.endswith('.json')]
        print(json_files)

        json_files = []
        for f in os.listdir("maps"):
            if f.endswith('.json'):
                json_files.append(f)
        print(json_files)

        count = len(json_files)

        for i in range(count):
            button = self.GetButtonByName("LevelButton")
            button.SetText('levl_ '+str(i+1))
            button.rect.x += i * 100
            button.name += f"_{i+1}"
            self.ui_elements.add(button)
        