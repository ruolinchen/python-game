# Ruolin Chen, rlc8my
# Christine Li, cjl4ev

import pygame
import gamebox

camera = gamebox.Camera(1142, 636)
background = gamebox.from_image(camera.x, camera.y, "night_time.png")
creators = gamebox.from_text(280, 20, "Creators: Christine Li (cjl4ev), Ruolin Chen (rlc8my)", "Snap ITC", 18, "white")
game_name = gamebox.from_text(camera.x, 280, "Counting Sheep", "Snap ITC", 60, "white")
description = gamebox.from_text(camera.x, 340, "How long can you jump fences for?", "Snap ITC", 24, "white")
rules1 = gamebox.from_text(camera.x, 370, "Jump fences without touching them or you lose a life!", "Snap ITC", 24,
                           "white")
rules2 = gamebox.from_text(camera.x, 400, "You get three lives, collect clovers to recover lives.", "Snap ITC", 24,
                           "white")
p1_instructions = gamebox.from_text(camera.x, 440, "Press SPACE to Jump", "Snap ITC", 24, "white")
to_start = gamebox.from_text(camera.x, 480, "Press ENTER to Start", "Snap ITC", 32, "white")
music = gamebox.load_sound('crickets_compressed.wav')
music_player = music.play(-1)

ground = gamebox.from_color(600, 634, "black", 1200, 50)

fence = gamebox.from_image(1000, 550, "fence.png")
fence.scale_by(.50)

character = gamebox.from_image(350, 545, "sheep.png")
character.scale_by(.20)

lives = gamebox.from_text(950, 40, "Lives left:", "Snap ITC", 24, "white")

health3 = gamebox.from_image(1075, 100, "sheep.png")
health3.scale_by(.1)
health2 = gamebox.from_image(990, 100, "sheep.png")
health2.scale_by(.1)
health1 = gamebox.from_image(905, 100, "sheep.png")
health1.scale_by(.1)

health = [health1, health2, health3]

clover = gamebox.from_image(900, 580, "clover.png")
clovers = [clover]

game_on = False

camera.draw(background)
camera.draw(creators)
camera.draw(game_name)
camera.draw(description)
camera.draw(rules1)
camera.draw(rules2)
camera.draw(p1_instructions)
camera.draw(to_start)

count = 0
time = 0
score = 0


def tick(keys):
    global game_on, background, count, time, score
    if pygame.K_RETURN in keys:
        game_on = True
    if game_on:

        character.yspeed += 10

        if pygame.K_SPACE in keys:
            character.yspeed -= 310

        character.y = character.y + character.yspeed
        if character.y < 0:
            character.y = 0
        keys.clear()

        if character.touches(ground):
            character.move_to_stop_overlapping(ground)
            camera.draw(ground)
        camera.draw(background)

        time += 1
        seconds = str(int((time / ticks_per_second))).zfill(1)
        timer = gamebox.from_text(120, 40, "Time: " + seconds + "s", "Snap ITC", 24, "white")
        camera.draw(timer)

        fence.x -= 20
        if fence.right < camera.left:
            fence.x = 1200
        character.yspeed = 0

        if character.right_touches(fence):
            character.move_to_stop_overlapping(fence)
            character.yspeed -= 290
            count += 1
            music1 = gamebox.load_sound('baa.wav')
            music1.play()
        if character.bottom_touches(fence):
            character.move_to_stop_overlapping(fence)
            character.yspeed -= 160
            count += 1
            music1 = gamebox.load_sound('baa.wav')
            music1.play()
        for clove in clovers:
            clove.x -= 20
            if character.touches(clove):
                clovers.remove(clove)
                if count != 0:
                    count -= 1
            camera.draw(clove)
        if time % 300 == 0 and time != 0:
            new_clover = gamebox.from_image(900, 580, "clover.png")
            clovers.append(new_clover)
        camera.draw(fence)
        camera.draw(character)
        camera.draw(lives)

        for healths in health:
            if count == 0:
                camera.draw(healths)
            if count == 1:
                camera.draw(health[1])
                camera.draw(health[2])
            if count == 2:
                camera.draw(health[2])
            if count == 3:
                gamebox.pause()
                score = seconds
                game_over = gamebox.from_text(camera.x, 300, "GAME OVER!", "Snap ITC", 80, 'white')
                scorer = gamebox.from_text(camera.x, 375, "Score: " + str(score), "Snap ITC", 90, "white")
                camera.draw(game_over)
                camera.draw(scorer)

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)