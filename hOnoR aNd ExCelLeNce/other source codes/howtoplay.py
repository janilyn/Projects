#!/usr/bin/python
import pyglet
from pyglet.window import mouse
import obj_highscore
import subprocess

window = pyglet.window.Window(800, 600, 'hOnoR aNd ExCelLeNce')

howtoplay_label = pyglet.text.Label('How to play:',
                            font_name='Arial Rounded MT Bold',
                            font_size=30,
                            color=(130,0,0,255),
                            x=21, y=440)

description_label = pyglet.text.Label('Use your skills to help the Iska pass her subjects! Click. Drag. Drop. Kung di ka pa marunong bumuo ng puzzle, kawawa ka naman!',
                            font_name='Arial Rounded MT Bold',
                            font_size=20,
                            color=(130,0,0,255),
                            x=window.width//2, y=355,
                            anchor_x='center',
                            width = 650,
                            multiline = True,
                            align = 'center')

description2_label = pyglet.text.Label('(Click on each piece by left-clicking on it once and dragging it to its correct position.)',
                            font_name='Arial Rounded MT Bold',
                            font_size=10,
                            color=(130,0,0,255),
                            x=window.width//2, y=270,
                            anchor_x='center',
                            width = 650,
                            multiline = True,
                            align = 'center')

@window.event
# mouse events
def on_mouse_press(x, y, button, modifiers):

    if button == mouse.LEFT:

        # when back button is pressed
        if x > 311 and x < 475 and y > 100 and y < 152:
            @window.event
            def on_draw():
                obj_highscore.back_presssprite.draw()

@window.event
def on_mouse_release(x, y, button, modifiers):

    if button == mouse.LEFT:
        # when back button is released
        if x > 311 and x < 475 and y > 100 and y < 152:
            def on_draw():
                obj_highscore.back_hoversprite.draw()
            window.close()
            subprocess.call(['python', 'start.py'])

        else:
            @window.event
            def on_draw():
                obj_highscore.back_basesprite.draw()

@window.event
def on_mouse_motion(x, y, button, modifiers):

    # when mouse hovers over back button
    if x > 311 and x < 475 and y > 100 and y < 152:
        @window.event
        def on_draw():
            obj_highscore.back_hoversprite.draw()

    else:
        @window.event
        def on_draw():
            obj_highscore.bg2sprite.draw()
            obj_highscore.back_basesprite.draw()
            howtoplay_label.draw()
            description_label.draw()
            description2_label.draw()

@window.event
def on_draw():
    window.clear()
    obj_highscore.bg2sprite.draw()
    obj_highscore.back_basesprite.draw()
    howtoplay_label.draw()
    description_label.draw()
    description2_label.draw()

pyglet.app.run()