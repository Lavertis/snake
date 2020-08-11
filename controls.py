from time import sleep

import pygame

from snake import Move
from vector import Vector2D


def manage_controls(world):
    while True:
        check_for_user_interaction(world)
        sleep(0.002)


def check_for_user_interaction(world):
    direction_keys = {
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_RIGHT,
        pygame.K_LEFT,
    }
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if world.paused or event.key == pygame.K_p:
                pause(world)
            if len(world.pushedKeys) < 3 and event.key in direction_keys and not world.paused:
                world.pushedKeys.append(event.key)
        if event.type == pygame.QUIT:
            import sys
            sys.exit()


def check_for_direction_change(world):
    switcher = {
        pygame.K_UP: go_up,
        pygame.K_DOWN: go_down,
        pygame.K_RIGHT: go_right,
        pygame.K_LEFT: go_left,
    }
    if world.pushedKeys:
        event_key = world.pushedKeys.pop(0)
        switcher.get(event_key)(world)


def go_up(world):
    element_iterator = iter(world.snakeElements)
    head = next(element_iterator)
    if head.velocity.y == 0:
        change_position_cords = head.position
        head.velocity.set_values(0, -1)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(0, -1)))


def go_down(world):
    element_iterator = iter(world.snakeElements)
    head = next(element_iterator)
    if head.velocity.y == 0:
        change_position_cords = head.position
        head.velocity.set_values(0, 1)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(0, 1)))


def go_right(world):
    element_iterator = iter(world.snakeElements)
    head = next(element_iterator)
    if head.velocity.x == 0:
        change_position_cords = head.position
        head.velocity.set_values(1, 0)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(1, 0)))


def go_left(world):
    element_iterator = iter(world.snakeElements)
    head = next(element_iterator)
    if head.velocity.x == 0:
        change_position_cords = head.position
        head.velocity.set_values(-1, 0)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(-1, 0)))


def pause(world):
    world.paused = not world.paused
