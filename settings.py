import pygame as pg
from draw_menu import ImageButton

set = {
    "FPS" : 0,
    "INGAME" : False,
    "INMENU" : True,
    "INSETTINGS" : False,
    "ONPAUSE" : False,
    "OPENEDMAP" : False,
    "DISPLAY" : [1920, 1080],
    "MINIMAP" : [50, 300, 100],
    "WINNAME" : "GoblinsGold",
    "countrooms" : 0,
    "ceilSize" : 100,
    "playerSize": 40,
    "roomSize" : 7,
    "showCollisions" : False,
    "showCurCoords" : False,
    "cx" : 0,
    "cy" : 0,
    "player" : {
        "rotate" : False,
        "health": 100,
        "posx" : 0,
        "posy" : 0,
        "speedx" : 0,
        "speedy" : 0,
        "speed" : 10
    },
    "none_texture" : "dirt.png",
    "player_texture" : "playerstay.png",
    "animations":{
        "player":[
            "entity/playerwalk1.png",
            "entity/playerwalk2.png"
        ]
    },
    "textures": {
        "gui" : {

        },
        "animations":{

        },
        "structures" : {

        },"items" : {

        },"entity" : {

        }, "secondLayer": {

        }
    },
    "object": {
        "gui" :{
            "mainPicture" : "GoblinASS2.png",
            "settingsPicture" : "GoblinASS.png"
        },
        "structures": {
            "dirt" : "dirt.png",
            "dirtwithwall" : "dirtwithwall.png",
            "dirtwithcorner" : "dirtwithcorner.png",
            "dirtwithcorner2" : "dirtwithcorner2.png",
            "darkfade" : "darkfade.png",
            "darkfadewithcorner" : "darkfadewithcorner.png"
        }, "items": {

        }, "entity": {
            "frog" : "frog.jpg"
        }, "secondLayer": {
            "frog" : "frog.jpg"
        }
    }
}

WIDTH, HEIGHT = set["DISPLAY"]

buttons = {
    "start" : ImageButton(WIDTH/2-(252/2), 450, 302, 124, "НАЧАТЬ ИГРУ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "exit" : ImageButton(WIDTH/2-(252/2), 800, 302, 124, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "settings" : ImageButton(WIDTH/2-(252/2), 650, 302, 124, "НАСТРОЙКИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
}

buttonsSettings = {
    "exit_from_settings": ImageButton(WIDTH/2-(252/2), 450, 302, 124, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3")
}

ingamebuttons = {
    "exit_from_game" : ImageButton(WIDTH/2-(252/2), 450, 302, 124, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3")
}

def load():
    set["textures"]["none"] = pg.image.load("game/textures/structures/" + set["none_texture"]).convert()
    set["player"]["texture"] = pg.image.load("game/textures/entity/" + set["player_texture"])
    for i in set["animations"]:
        set["textures"]["animations"][i] = []
        for j in set["animations"][i]:
            set["textures"]["animations"][i].append(pg.image.load("game/textures/" + j))

    for i in set["object"]:
        for j in set["object"][i]:
            set["textures"][i][j] = pg.image.load("game/textures/" + i + "/" + set["object"][i][j]).convert_alpha()