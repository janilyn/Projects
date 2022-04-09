import pyglet

#bg image
bg = pyglet.image.load('img/back.png')

#buttons
start_base = pyglet.resource.image('img/s0.png')
start_hover = pyglet.resource.image('img/s2.png')
start_press = pyglet.resource.image('img/s3.png')

howtoplay_base = pyglet.resource.image('img/i0.png')
howtoplay_hover = pyglet.resource.image('img/i2.png')
howtoplay_press = pyglet.resource.image('img/i3.png')

highscore_base = pyglet.resource.image('img/h0.png')
highscore_hover = pyglet.resource.image('img/h2.png')
highscore_press = pyglet.resource.image('img/h3.png')

#bg position
bgsprite = pyglet.sprite.Sprite(bg)
bgsprite.scale = 0.34
bgsprite.position = (0,0)

# button positions
start_basesprite = pyglet.sprite.Sprite(start_base)
start_basesprite.scale = 0.32
start_basesprite.position = (315,155)

start_hoversprite = pyglet.sprite.Sprite(start_hover)
start_hoversprite.scale = 0.32
start_hoversprite.position = (315,155)

start_presssprite = pyglet.sprite.Sprite(start_press)
start_presssprite.scale = 0.32
start_presssprite.position = (315,155)

howtoplay_basesprite = pyglet.sprite.Sprite(howtoplay_base)
howtoplay_basesprite.scale = 0.32
howtoplay_basesprite.position = (435,155)

howtoplay_hoversprite = pyglet.sprite.Sprite(howtoplay_hover)
howtoplay_hoversprite.scale = 0.32
howtoplay_hoversprite.position = (435,155)

howtoplay_presssprite = pyglet.sprite.Sprite(howtoplay_press)
howtoplay_presssprite.scale = 0.32
howtoplay_presssprite.position = (435,155)

highscore_basesprite = pyglet.sprite.Sprite(highscore_base)
highscore_basesprite.scale = 0.32
highscore_basesprite.position = (555,155)

highscore_presssprite = pyglet.sprite.Sprite(highscore_press)
highscore_presssprite.scale = 0.32
highscore_presssprite.position = (555,155)

highscore_hoversprite = pyglet.sprite.Sprite(highscore_hover)
highscore_hoversprite.scale = 0.32
highscore_hoversprite.position = (555,155)