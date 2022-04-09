#!/usr/bin/python

import pyglet
from pyglet.window import key
from pyglet.window import mouse
import obj_input_name
import subprocess

window = pyglet.window.Window(800, 600, 'hOnoR aNd ExCelLeNce')

# button actions
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        # when back button is pressed
        if x > 348 and x < 520 and y < 235 and y > 180:
            @window.event
            def on_draw():
                obj_input_name.back_presssprite.draw()

        # when continue button is pressed
        if x > 435 and x < 730 and y < 205 and y > 155:
            @window.event
            def on_draw():
                obj_input_name.continue_presssprite.draw()


@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        # when back button is released
        if x > 348 and x < 520 and y < 235 and y > 180:
            @window.event
            def on_draw():
                obj_input_name.back_hoversprite.draw()
            window.close()
            subprocess.call(['python', 'start.py'])

        # when continue button is released
        elif x > 558 and x < 730 and y < 205 and y > 155:
            @window.event
            def on_draw():
                obj_input_name.continue_hoversprite.draw()

            #saves username to user_score textfile
            f = open('user_score.txt', 'w')
            if obj_input_name.key_label.text == "":
                f.write("no_name\n")
            else:
                f.write(str(obj_input_name.key_label.text)+"\n")
                f.write("xxx\n")
            f.close()

            window.close()
            subprocess.call(['python', 'game_puzzle.py'])
   

        else:
            @window.event
            def on_draw():
                obj_input_name.back_basesprite.draw()
                obj_input_name.continue_basesprite.draw()


@window.event
def on_mouse_motion(x, y, button, modifiers):
    # when mouse hovers over back button
    if x > 348 and x < 520 and y < 235 and y > 180:
        @window.event
        def on_draw():
            obj_input_name.back_hoversprite.draw()

    # when mouse hovers over continue button
    elif x > 558 and x < 730 and y < 235 and y > 180:
        @window.event
        def on_draw():
            obj_input_name.continue_hoversprite.draw()

    else:
        @window.event
        def on_draw():
            window.clear()
            obj_input_name.bgsprite.draw()
            obj_input_name.back_basesprite.draw()
            obj_input_name.continue_basesprite.draw()
            obj_input_name.key_label.draw()

#username input
@window.event
def on_key_press(symbol,modifier):
    if symbol == key.BACKSPACE:
        obj_input_name.key_label.text = ''

@window.event
def on_text(text):
    if text != key.BACKSPACE and len(obj_input_name.key_label.text)<12:
        obj_input_name.key_label.text += text

@window.event
def on_draw():
    window.clear()
    obj_input_name.bgsprite.draw()
    obj_input_name.back_basesprite.draw()
    obj_input_name.continue_basesprite.draw()
    obj_input_name.key_label.draw()

window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()