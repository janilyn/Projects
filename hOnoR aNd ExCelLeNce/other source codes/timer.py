import sys
import pyglet

window = pyglet.window.Window()


countdown = int(1)

class Timer(object):
    def __init__(self):
        self.start = '00:45'
        self.label = pyglet.text.Label(self.start, font_name='Arial Rounded MT Bold', font_size=20,
                                       x = 10, y = 10)
        self.reset()

    def reset(self):
        self.time = (countdown * 45) + 1
        self.running = True
        self.label.text = self.start
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time -= dt
            m, s = divmod(self.time, 45)
            self.label.text = '%02d:%02d' % (m, s)
            if m < 5:
                self.label.color = (255, 255, 255, 255)
            if m < 0:
                self.running = False
                self.label.text = 'STOP'

@window.event
def on_draw():
    window.clear()
    timer.label.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run()