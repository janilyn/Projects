import pyglet

#bg2 image
bg2 = pyglet.resource.image('img/back2.png')

#bg position
bg2sprite = pyglet.sprite.Sprite(bg2)
bg2sprite.scale = 0.34
bg2sprite.position = (0,0)

#puzzle outline
p_outline_lvl1 = pyglet.resource.image('img/sketchlayer1.png')

#puzzle outline position
po_lvl1sprite = pyglet.sprite.Sprite(p_outline_lvl1)
po_lvl1sprite.scale = 0.8
po_lvl1sprite.position = (90,90)

#puzzle pieces
p1 = pyglet.resource.image('img/p1.png')
p2 = pyglet.resource.image('img/p2.png')
p3 = pyglet.resource.image('img/p3.png')
p4 = pyglet.resource.image('img/p4.png')
p5 = pyglet.resource.image('img/p5.png')
p6 = pyglet.resource.image('img/p6.png')
p7 = pyglet.resource.image('img/p7.png')
p8 = pyglet.resource.image('img/p8.png')
p9 = pyglet.resource.image('img/p9.png')

#puzzle pieces position
p1 = pyglet.sprite.Sprite(p1)
p1.scale = 0.8
p1.position = (640,235)

p2 = pyglet.sprite.Sprite(p2)
p2.scale = 0.8
p2.position = (520,120)

p3 = pyglet.sprite.Sprite(p3)
p3.scale = 0.8
p3.position = (655,500)

p4 = pyglet.sprite.Sprite(p4)
p4.scale = 0.8
p4.position = (490,455)

p5 = pyglet.sprite.Sprite(p5)
p5.scale = 0.8
p5.position = (495,265)

p6 = pyglet.sprite.Sprite(p6)
p6.scale = 0.8
p6.position = (680,40)

p7 = pyglet.sprite.Sprite(p7)
p7.scale = 0.8
p7.position = (310,460)

p8 = pyglet.sprite.Sprite(p8)
p8.scale = 0.8
p8.position = (515,22)

p9 = pyglet.sprite.Sprite(p9)
p9.scale = 0.8
p9.position = (660,370)

#gameover screen
go = pyglet.resource.image('img/gameover.jpg')

#gameover screen position
gameoversprite = pyglet.sprite.Sprite(go)
gameoversprite.scale = 0.34
gameoversprite.position = (0,0)

#back button
back_base = pyglet.resource.image('img/t0.png')
back_hover = pyglet.resource.image('img/t2.png')
back_press = pyglet.resource.image('img/t3.png')

#back button position
back_basesprite = pyglet.sprite.Sprite(back_base)
back_basesprite.scale = 0.5
back_basesprite.position = (70, 110)

back_hoversprite = pyglet.sprite.Sprite(back_hover)
back_hoversprite.scale = 0.5
back_hoversprite.position = (70, 110)

back_presssprite = pyglet.sprite.Sprite(back_press)
back_presssprite.scale = 0.5
back_presssprite.position = (70, 110)

#highscore button
highscore_base = pyglet.resource.image('img/h0.png')
highscore_hover = pyglet.resource.image('img/h2.png')
highscore_press = pyglet.resource.image('img/h3.png')

#highscore button position
highscore_basesprite = pyglet.sprite.Sprite(highscore_base)
highscore_basesprite.scale = 0.5
highscore_basesprite.position = (530,110)

highscore_presssprite = pyglet.sprite.Sprite(highscore_press)
highscore_presssprite.scale = 0.5
highscore_presssprite.position = (530,110)

highscore_hoversprite = pyglet.sprite.Sprite(highscore_hover)
highscore_hoversprite.scale = 0.5
highscore_hoversprite.position = (530,110)