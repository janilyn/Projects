import pyglet

# bg image
bg = pyglet.image.load('img/back_user_input.png')

key_label = pyglet.text.Label('',
                              font_name='Arial Rounded MT Bold',
                              font_size=40,
                              color=(130,0,0,255),
                              x = 543, y = 275,
                              anchor_x='center')

# buttons
back_base = pyglet.resource.image('img/t0.png')
back_hover = pyglet.resource.image('img/t2.png')
back_press = pyglet.resource.image('img/t3.png')

continue_base = pyglet.resource.image('img/j0.png')
continue_hover = pyglet.resource.image('img/j2.png')
continue_press = pyglet.resource.image('img/j3.png')


# bg position
bgsprite = pyglet.sprite.Sprite(bg)
bgsprite.scale = 0.34
bgsprite.position = (0, 0)

# button positions
back_basesprite = pyglet.sprite.Sprite(back_base)
back_basesprite.scale = 0.5
back_basesprite.position = (340, 165)

back_hoversprite = pyglet.sprite.Sprite(back_hover)
back_hoversprite.scale = 0.5
back_hoversprite.position = (340, 165)

back_presssprite = pyglet.sprite.Sprite(back_press)
back_presssprite.scale = 0.5
back_presssprite.position = (340, 165)

continue_basesprite = pyglet.sprite.Sprite(continue_base)
continue_basesprite.scale = 0.5
continue_basesprite.position = (550, 165)

continue_hoversprite = pyglet.sprite.Sprite(continue_hover)
continue_hoversprite.scale = 0.5
continue_hoversprite.position = (550, 165)

continue_presssprite = pyglet.sprite.Sprite(continue_press)
continue_presssprite.scale = 0.5
continue_presssprite.position = (550, 165)