#!/usr/bin/python
import pyglet
from pyglet.window import mouse
import obj_highscore
import subprocess

window = pyglet.window.Window(800, 600, 'hOnoR aNd ExCelLeNce')

# what this does is it compares the time in user_score file to time in highscore file
# and puts the higher value in the highscore file
with open('user_score.txt', 'r') as f:
    with open('highscore.txt', 'r') as g:
        data = f.readlines()
        data2 = g.readlines()
        if float(data[1][-3:-1]) > float(data2[1][-3:-1]) or "xxx" in data[1]:
            data2[0] = str(data[0])
            data2[1] = str(data[1])
        elif data2 == "":
            g.writelines(data)
        else:
            None
with open('highscore.txt', 'w') as g:
    g.writelines(data2)
f.close()
g.close()

with open('highscore.txt', 'r') as g:
    data2 = g.readlines()
    user = data2[0][:-1]
    score = 60 - int(data2[1][-3:-1])

g.close()

#displays username
username_label = pyglet.text.Label(str(user),
                            font_name='Arial Rounded MT Bold',
                            font_size=40,
                            color=(130,0,0,255),
                            x=window.width//2, y=270,
                            anchor_x='center')

#displays highscore
hs_label = pyglet.text.Label('Finished within '+ '\n' + str(score) + ' seconds!',
                            font_name='Arial Rounded MT Bold',
                            font_size=25,
                            color=(130,0,0,255),
                            x=window.width//2, y=210,
                            anchor_x='center',
                            width = 600,
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
            obj_highscore.bgsprite.draw()
            obj_highscore.back_basesprite.draw()
            username_label.draw()
            hs_label.draw()

@window.event
def on_draw():
    window.clear()
    obj_highscore.bgsprite.draw()
    username_label.draw()
    hs_label.draw()
    obj_highscore.back_basesprite.draw()

pyglet.app.run()