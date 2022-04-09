import pyglet

# bg image
bg = pyglet.image.load('img/back3.jpg')

# bg position
bgsprite = pyglet.sprite.Sprite(bg)
bgsprite.scale = 0.34
bgsprite.position = (0, 0)

# back button
back_base = pyglet.resource.image('img/t0.png')
back_hover = pyglet.resource.image('img/t2.png')
back_press = pyglet.resource.image('img/t3.png')

# back button position
back_basesprite = pyglet.sprite.Sprite(back_base)
back_basesprite.scale = 0.5
back_basesprite.position = (300,85)

back_hoversprite = pyglet.sprite.Sprite(back_hover)
back_hoversprite.scale = 0.5
back_hoversprite.position = (300,85)

back_presssprite = pyglet.sprite.Sprite(back_press)
back_presssprite.scale = 0.5
back_presssprite.position = (300,85)

# bg for how to play
bg_howtoplay = pyglet.image.load('img/back_howtoplay.png')

# bg position
bg2sprite = pyglet.sprite.Sprite(bg_howtoplay)
bg2sprite.scale = 0.34
bg2sprite.position = (0, 0)



