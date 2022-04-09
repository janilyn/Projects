#!/usr/bin/python

import pyglet
from pyglet.window import mouse
from obj_1stpuzzle import p1, p2, p3, p4, p5, p6, p7, p8 ,p9, po_lvl1sprite, bg2sprite, gameoversprite, back_basesprite, back_hoversprite, back_presssprite, highscore_basesprite, highscore_hoversprite, highscore_presssprite
from obj_2ndpuzzle import p1a, p2a, p3a, p4a, p5a, p6a, p7a, p8a, p9a, p10a, p11a, p12a, p13a, p14a, p15a, p16a, p17a, p18a, p19a, p20a, bg3sprite, po_lvl2sprite, gfsprite
import subprocess

window = pyglet.window.Window(800, 600, 'hOnoR aNd ExCelLeNce')

@window.event
# mouse events
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:

        # when back button is pressed
        if x > 80 and x < 245 and y > 140 and y < 193:
            @window.event
            def on_draw():
                back_presssprite.draw()

        # when highscore button is pressed
        if x > 540 and x < 706 and y > 144 and y < 192:
            @window.event
            def on_draw():
                highscore_presssprite.draw()

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        # when back button is released
        if x > 80 and x < 245 and y > 140 and y < 193:
            @window.event
            def on_draw():
                back_hoversprite.draw()
            window.close()
            subprocess.call(['python', 'start.py'])

        elif x > 540 and x < 706 and y > 144 and y < 192:
            @window.event
            def on_draw():
                highscore_hoversprite.draw()
            window.close()
            subprocess.call(['python', 'start.py']) # changelater!!

        else:
            @window.event
            def on_draw():
                back_basesprite.draw()
                highscore_basesprite.draw()

@window.event
def on_mouse_motion(x, y, button, modifiers):

    # when mouse hovers over back button
    if x > 80 and x < 245 and y > 140 and y < 193:
        @window.event
        def on_draw():
            back_hoversprite.draw()

    elif x > 540 and x < 706 and y > 144 and y < 192:
        @window.event
        def on_draw():
            highscore_hoversprite.draw()

    else:
        @window.event
        def on_draw():
            gfsprite.draw()
            back_basesprite.draw()
            highscore_basesprite.draw()

@window.event
def on_draw():  #shows play again screen
    window.clear()
    gfsprite.draw()  #change later!!
    back_basesprite.draw()
    highscore_basesprite.draw()

pyglet.app.run()