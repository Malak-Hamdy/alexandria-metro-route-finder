import pygame as gm
from sys import exit  # closes any kind of code to make sure my pygame shutsdown correctly
from bfs import bfs
from data import *

gm.init()  # Runs pygame like starting an engine z
WIDTH, HEIGHT = 1400, 820
screen = gm.display.set_mode((WIDTH, HEIGHT))  # shows the screen
gm.display.set_caption("Metro Route Finder [BFS]")
icon = gm.image.load("D:\Introduction to AI\Metro Route Finder [BFS]\icon.png")
gm.display.set_icon(icon)

mv_object = gm.image.load("D:\Introduction to AI\Metro Route Finder [BFS]\myMetro.png")
mv_object = gm.transform.scale(mv_object, (70, 70))

map_surface = gm.image.load("D:\Introduction to AI\Metro Route Finder [BFS]\pygame_map (1).png")

path = []
visited = []
path_positions = []
visited_positions = []

FONT_PATH = r"D:\Introduction to AI\Metro Route Finder [BFS]\MaskingRenta-MAxjJ.otf"
title_font = gm.font.Font(FONT_PATH, 70)
font = gm.font.Font(FONT_PATH, 40)

#MENU VARIABLES
current_text = ""
destination_text = ""
active = "current"
error_message = ""

state = "menu"

metro_pos = None
target_index = 1
speed = 3


# Ceaning the input
def clean_input(text):
    return text.lower().replace(" ", "")


def handle_menu_event(event):
    global current_text, destination_text, active, error_message
    global state, path, visited, path_positions, visited_positions
    global metro_pos, target_index

    if event.type != gm.KEYDOWN:
        return  # Only care about key press

    # TAB:switch which box is active
    if event.key == gm.K_TAB:
        active = "destination" if active == "current" else "current"

    #delete last character
    elif event.key == gm.K_BACKSPACE:
        if active == "current":
            current_text = current_text[:-1]
        else:
            destination_text = destination_text[:-1]

    # try to run BFS
    elif event.key == gm.K_RETURN:
        start = clean_input(current_text)
        goal = clean_input(destination_text)

        if start in graph and goal in graph:

            path, visited = bfs(graph, start, goal)
            path_positions = [positions[i] for i in path]
            visited_positions = [positions[i] for i in visited]
            metro_pos = list(path_positions[0])
            target_index = 1
            state = "map"
        else:
            error_message = "Invalid station name!"  # show error on screen

    #add character to the active box
    else:
        if active == "current":
            current_text += event.unicode
        else:
            destination_text += event.unicode


def draw_menu():
    screen.fill((30, 0, 60))

    title = title_font.render("Metro Route Finder", True, (255, 255, 255))
    screen.blit(title, (400, 100))

    label1 = font.render("Current:", True, (255, 255, 255))
    label2 = font.render("Destination:", True, (255, 255, 255))

    screen.blit(label1, (200, 250))
    screen.blit(label2, (200, 370))

    box1 = gm.Rect(500, 250, 600, 60)
    box2 = gm.Rect(500, 370, 600, 60)

    gm.draw.rect(screen, (255, 255, 255), box1, 2)
    gm.draw.rect(screen, (255, 255, 255), box2, 2)

    txt1 = font.render(current_text, True, (255, 255, 255))
    txt2 = font.render(destination_text, True, (255, 255, 255))

    screen.blit(txt1, (box1.x + 15, box1.y + 10))
    screen.blit(txt2, (box2.x + 15, box2.y + 10))

    instruction = font.render("TAB to switch | ENTER to run BFS", True, (255, 255, 255))
    screen.blit(instruction, (350, 520))

    if error_message:
        err = font.render(error_message, True, (255, 220, 70))
        screen.blit(err, (400, 600))


def draw_path():
    NEON_GREEN = (57, 255, 20)
    for i in range(len(path_positions) - 1):
        gm.draw.line(
            screen,
            NEON_GREEN,
            path_positions[i],
            path_positions[i + 1],
            5
        )


def draw_visited():
    for pos in visited_positions:
        gm.draw.circle(screen, (255, 220, 70), pos, 6)


def move_metro():
    global metro_pos, target_index

    if target_index >= len(path_positions):
        return

    target = path_positions[target_index]

    dx = target[0] - metro_pos[0]
    dy = target[1] - metro_pos[1]

    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance <= speed:
        metro_pos[0] = target[0]
        metro_pos[1] = target[1]
        target_index += 1
    else:
        metro_pos[0] += speed * dx / distance
        metro_pos[1] += speed * dy / distance


def draw_results():
    screen.fill((30, 0, 60))

    title = font.render("Results", True, (255, 255, 255))
    screen.blit(title, (600, 40))

    # Total stops
    stops = font.render(f"Total Stops: {len(path) - 1}", True, (57, 255, 20))
    screen.blit(stops, (100, 120))

    # Full path
    path_label = font.render("Path:", True, (255, 220, 70))
    screen.blit(path_label, (100, 180))
    path_str = " -> ".join(path)
    # Split into multiple lines if too long
    words = path_str.split(" -> ")
    line, y = "", 230
    for word in words:
        test = line + " -> " + word if line else word
        if font.size(test)[0] > 1200:
            rendered = font.render(line, True, (255, 255, 255))
            screen.blit(rendered, (100, y))
            y += 50
            line = word
        else:
            line = test
    if line:
        screen.blit(font.render(line, True, (255, 255, 255)), (100, y))
        y += 60

    # Visited order
    visited_label = font.render("BFS Visited Order:", True, (255, 220, 70))
    screen.blit(visited_label, (100, y))
    y += 50
    line = ""
    for word in visited:
        test = line + ", " + word if line else word
        if font.size(test)[0] > 1200:
            screen.blit(font.render(line, True, (255, 255, 255)), (100, y))
            y += 45
            line = word
        else:
            line = test
    if line:
        screen.blit(font.render(line, True, (255, 255, 255)), (100, y))

    hint = font.render("Press any key to go back", True, (180, 180, 180))
    screen.blit(hint, (450, 760))


clock = gm.time.Clock()
while True:
    for event in gm.event.get():
        if event.type == gm.QUIT:
            gm.quit()
            exit()
        if state == "menu":
            handle_menu_event(event)
        # any keypress on results screen resets to menu
        elif state == "results" and event.type == gm.KEYDOWN:
            state = "menu"
            current_text = ""
            destination_text = ""
            error_message = ""

    if state == "menu":
        draw_menu()

    elif state == "map":
        screen.blit(map_surface, (0, 0))

        draw_visited()
        draw_path()

        move_metro()
        screen.blit(mv_object, metro_pos)


        if target_index >= len(path_positions):
            print("Path:", " -> ".join(path))
            print("Visited:", ", ".join(visited))
            print(f"Total Stops: {len(path) - 1}")
            state = "results"
    elif state == "results":
        draw_results()

    gm.display.update()
    clock.tick(60)
