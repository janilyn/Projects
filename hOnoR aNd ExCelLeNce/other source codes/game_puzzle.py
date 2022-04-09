#!/usr/bin/python

import pyglet
from pyglet.window import mouse
from obj_1stpuzzle import p1, p2, p3, p4, p5, p6, p7, p8 ,p9, po_lvl1sprite, bg2sprite, gameoversprite, back_basesprite, back_hoversprite, back_presssprite, highscore_basesprite, highscore_hoversprite, highscore_presssprite
from obj_2ndpuzzle import p1a, p2a, p3a, p4a, p5a, p6a, p7a, p8a, p9a, p10a, p11a, p12a, p13a, p14a, p15a, p16a, p17a, p18a, p19a, p20a, bg3sprite, po_lvl2sprite, gfsprite
import subprocess

window = pyglet.window.Window(800, 600, 'hOnoR aNd ExCelLeNce')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:

        # for puzzle piece 1
        if x > 645 and x < 767 and y > 270 and y < 355:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p1.x = x-70
                p1.y = y-70
            if p1.position == (95,327):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p1.position = (95,327)

        #for puzzle piece 2
        if x > 520 and x < 650 and y > 160 and y < 245:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p2.x = x-70
                p2.y = y-70
            if p2.position == (229,323):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p2.position = (229,323)
        
        #for puzzle piece 3
        if x > 690 and x < 785 and y > 503 and y < 590:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p3.x = x-70
                p3.y = y-70
            if p3.position == (330,360):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p3.position = (330,360)
        
        #for puzzle piece 4
        if x > 495 and x < 615 and y > 460 and y < 595:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p4.x = x-70
                p4.y = y-70
            if p4.position == (95,212):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p4.position = (95,212)

        #for puzzle piece 5
        if x > 497 and x < 625 and y > 303 and y < 443:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p5.x = x-70
                p5.y = y-70
            if p5.position == (229,175):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p5.position = (229,175)

        #for puzzle piece 6
        if x > 680 and x < 775 and y > 40 and y < 180:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p6.x = x-70
                p6.y = y-70
            if p6.position == (363,213):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p6.position = (363,213)

        #for puzzle piece 7
        if x > 310 and x < 438 and y > 470 and y < 570:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p7.x = x-70
                p7.y = y-70
            if p7.position == (96,96):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p7.position = (96,96)
        
        #for puzzle piece 8
        if x > 515 and x < 643 and y > 30 and y < 132:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p8.x = x-70
                p8.y = y-70
            if p8.position == (230,95):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p8.position = (230,95)

        #for puzzle piece 9
        if x > 692 and x < 790 and y > 375 and y < 480:
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p9.x = x-70
                p9.y = y-70
            if p9.position == (332,95):
                @window.event
                def on_mouse_drag(x, y, dx, dy, button, modifiers):
                    p9.position = (332,95)
        
            
@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        # for puzzle piece 1
        if p1.x > 65 and p1.x < 140 and p1.y > 290 and p1.y < 380:
            p1.position = (95,327)
        else:
            p1.position = (640,235)
            
        #for puzzle piece 2
        if p2.x > 180 and p2.x < 290 and p2.y > 290 and p2.y < 400:
            p2.position = (229,323)
        else:
            p2.position = (520,120)

        #for puzzle piece 3
        if p3.x > 300 and p3.x < 385 and p3.y > 340 and p3.y < 420:
            p3.position = (330,360)
        else:
            p3.position = (655,500)

        #for puzzle piece 4
        if p4.x > 50 and p4.x < 160 and p4.y > 180 and p4.y < 280:
            p4.position = (95,212)
        else:
            p4.position = (490,455)

        #for puzzle piece 5
        if p5.x > 190 and p5.x < 290 and p5.y > 145 and p5.y < 255:
            p5.position = (229,175)
        else:
            p5.position = (495,265)
        
        #for puzzle piece 6
        if p6.x > 330 and p6.x < 415 and p6.y > 180 and p6.y < 290:
            p6.position = (363,213)
        else:
            p6.position = (680,40)

        #for puzzle piece 7
        if p7.x > 50 and p7.x < 135 and p7.y > 65 and p7.y < 150:
            p7.position = (96,96)
        else:
            p7.position = (310,460)
        
        #for puzzle piece 8
        if p8.x > 190 and p8.x < 290 and p8.y > 60 and p8.y < 140:
            p8.position = (230,95)
        else:
            p8.position = (515,22)

        #for puzzle piece 9
        if p9.x > 300 and p9.x < 410 and p9.y > 65 and p9.y < 135:
            p9.position = (332,95)
        else:
            p9.position = (660,370)

        
        #to make the pieces stay in position once put in their correct places
        if p1.position == (95,327):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p1.position = (95,327)
                    
        if p2.position == (229,323):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p2.position = (229,323)
        
        if p3.position == (330,360):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p3.position = (330,360)

        if p4.position == (95,212):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p4.position = (95,212)

        if p5.position == (229,175):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p5.position = (229,175)
        
        if p6.position == (363,213):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p6.position = (363,213)

        if p7.position == (96,96):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p7.position = (96,96)

        if p8.position == (230,95):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p8.position = (230,95)

        if p9.position == (332,95):
            @window.event
            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                p9.position = (332,95)

        #if puzzle is complete, move to next puzzle
        if p1.position == (95,327) and p2.position == (229,323) and p3.position == (330,360) and p4.position == (95,212) and p5.position == (229,175) and p6.position == (363,213) and p7.position == (96,96) and p8.position == (230,95) and p9.position == (332,95):
            @window.event
            def on_mouse_press(x, y, button, modifiers):
                if button == mouse.LEFT:

                    #for puzzle piece 1
                    if x > 692 and x < 777 and y > 286 and y < 343:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p1a.x = x-45
                            p1a.y = y-45
                        if p1a.position == (94,374):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p1a.position = (94,374)

                    #for puzzle piece 2
                    if x > 486 and x < 578 and y > 246 and y < 304:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p2a.x = x-45
                            p2a.y = y-45
                        if p2a.position == (185,377):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p2a.position = (185,377)

                    #for puzzle piece 3
                    if x > 561 and x < 658 and y > 537 and y < 594:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p3a.x = x-45
                            p3a.y = y-45
                        if p3a.position == (285,377):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p3a.position = (285,377)

                    #for puzzle piece 4
                    if x > 702 and x < 786 and y > 18 and y < 75:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p4a.x = x-45
                            p4a.y = y-45
                        if p4a.position == (373,392):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p4a.position = (373,392)

                    #for puzzle piece 5
                    if x > 477 and x < 565 and y > 463 and y < 527:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p5a.x = x-45
                            p5a.y = y-45
                        if p5a.position == (93,320):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p5a.position = (93,320)

                    #for puzzle piece 6
                    if x > 685 and x < 780 and y > 528 and y < 593:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p6a.x = x-45
                            p6a.y = y-45
                        if p6a.position == (171,320):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p6a.position = (171,320)

                    #for puzzle piece 7
                    if x > 456 and x < 555 and y > 11 and y < 76:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p7a.x = x-45
                            p7a.y = y-45
                        if p7a.position == (285,320):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p7a.position = (285,320)

                    #for puzzle piece 8
                    if x > 600 and x < 686 and y > 354 and y < 419:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p8a.x = x-45
                            p8a.y = y-45
                        if p8a.position == (389,305):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p8a.position = (389,305)

                    #for puzzle piece 9
                    if x > 689 and x < 777 and y > 455 and y < 516:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p9a.x = x-45
                            p9a.y = y-45
                        if p9a.position == (93,240):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p9a.position = (93,240)

                    #for puzzle piece 10
                    if x > 329 and x < 422 and y > 8 and y < 66:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p10a.x = x-45
                            p10a.y = y-45
                        if p10a.position == (186,256):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p10a.position = (186,256)

                    #for puzzle piece 11
                    if x > 691 and x < 789 and y > 93 and y < 151:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p11a.x = x-45
                            p11a.y = y-45
                        if p11a.position == (285,256):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p11a.position = (285,256)

                    #for puzzle piece 12
                    if x > 465 and x < 551 and y > 537 and y < 596:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p12a.x = x-45
                            p12a.y = y-45
                        if p12a.position == (373,256):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p12a.position = (373,256)

                    #for puzzle piece 13
                    if x > 597 and x < 683 and y > 262 and y < 331:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p13a.x = x-45
                            p13a.y = y-45
                        if p13a.position == (93,166):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p13a.position = (93,166)

                    #for puzzle piece 14
                    if x > 685 and x < 780 and y > 173 and y < 242:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p14a.x = x-45
                            p14a.y = y-45
                        if p14a.position == (171,184):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p14a.position = (171,184)

                    #for puzzle piece 15
                    if x > 583 and x < 682 and y > 441 and y < 509:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p15a.x = x-45
                            p15a.y = y-45
                        if p15a.position == (285,184):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p15a.position = (285,184)

                    #for puzzle piece 16
                    if x > 591 and x < 677 and y > 29 and y < 95:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p16a.x = x-45
                            p16a.y = y-45
                        if p16a.position == (372,167):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p16a.position = (372,167)

                    #for puzzle piece 17
                    if x > 694 and x < 781 and y > 356 and y < 438:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p17a.x = x-45
                            p17a.y = y-45
                        if p17a.position == (93,94):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p17a.position = (93,94)

                    #for puzzle piece 18
                    if x > 486 and x < 579 and y > 332 and y < 415:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p18a.x = x-45
                            p18a.y = y-45
                        if p18a.position == (186,93):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p18a.position = (186,93)

                    #for puzzle piece 19
                    if x > 568 and x < 668 and y > 135 and y < 220:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p19a.x = x-45
                            p19a.y = y-45
                        if p19a.position == (285,94):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p19a.position = (285,94)
                    
                    #for puzzle piece 20
                    if x > 373 and x < 458 and y > 466 and y < 547:
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p20a.x = x-45
                            p20a.y = y-45
                        if p20a.position == (372,93):
                            @window.event
                            def on_mouse_drag(x, y, dx, dy, button, modifiers):
                                p20a.position = (372,93)

            @window.event
            def on_mouse_release(x, y, button, modifiers):
                if button == mouse.LEFT:
                    # for puzzle piece 1
                    if p1a.x > 60 and p1a.x < 134 and p1a.y > 357 and p1a.y < 408:
                        p1a.position = (94,374)
                    else:
                        p1a.position = (690,267)

                    # for puzzle piece 2
                    if p2a.x > 158 and p2a.x < 230 and p2a.y > 356 and p2a.y < 412:
                        p2a.position = (185,377)
                    else:
                        p2a.position = (484,230)

                    # for puzzle piece 3
                    if p3a.x > 256 and p3a.x < 332 and p3a.y > 355 and p3a.y < 411:
                        p3a.position = (285,377)
                    else:
                        p3a.position = (560,520)

                    # for puzzle piece 4
                    if p4a.x > 349 and p4a.x < 436 and p4a.y > 372 and p4a.y < 425:
                        p4a.position = (373,392)
                    else:
                        p4a.position = (685,17)

                    # for puzzle piece 5
                    if p5a.x > 69 and p5a.x < 133 and p5a.y > 302 and p5a.y < 353:
                        p5a.position = (93,320)
                    else:
                        p5a.position = (477,461)

                    # for puzzle piece 6
                    if p6a.x > 145 and p6a.x < 231 and p6a.y > 300 and p6a.y < 352:
                        p6a.position = (171,320)
                    else:
                        p6a.position = (670,526)

                    # for puzzle piece 7
                    if p7a.x > 263 and p7a.x < 334 and p7a.y > 303 and p7a.y < 351:
                        p7a.position = (285,320)
                    else:
                        p7a.position = (455,10)

                    # for puzzle piece 8
                    if p8a.x > 366 and p8a.x < 435 and p8a.y > 288 and p8a.y < 340:
                        p8a.position = (389,305)
                    else:
                        p8a.position = (600,338)

                    # for puzzle piece 9
                    if p9a.x > 68 and p9a.x < 134 and p9a.y > 218 and p9a.y < 275:
                        p9a.position = (93,240)
                    else:
                        p9a.position = (689,438)

                    # for puzzle piece 10
                    if p10a.x > 162 and p10a.x < 238 and p10a.y > 237 and p10a.y < 290:
                        p10a.position = (186,256)
                    else:
                        p10a.position = (328,7)

                    # for puzzle piece 11
                    if p11a.x > 260 and p11a.x < 332 and p11a.y > 238 and p11a.y < 288:
                        p11a.position = (285,256)
                    else:
                        p11a.position = (690,92)

                    # for puzzle piece 12
                    if p12a.x > 350 and p12a.x < 432 and p12a.y > 238 and p12a.y < 288:
                        p12a.position = (373,256)
                    else:
                        p12a.position = (449,536)

                    # for puzzle piece 13
                    if p13a.x > 67 and p13a.x < 135 and p13a.y > 143 and p13a.y < 205:
                        p13a.position = (93,166)
                    else:
                        p13a.position = (597,245)

                    # for puzzle piece 14
                    if p14a.x > 148 and p14a.x < 220 and p14a.y > 162 and p14a.y < 216:
                        p14a.position = (171,184)
                    else:
                        p14a.position = (670,173)

                    # for puzzle piece 15
                    if p15a.x > 262 and p15a.x < 335 and p15a.y > 164 and p15a.y < 220:
                        p15a.position = (285,184)
                    else:
                        p15a.position = (583,440)

                    # for puzzle piece 16
                    if p16a.x > 347 and p16a.x < 415 and p16a.y > 145 and p16a.y < 206:
                        p16a.position = (372,167)
                    else:
                        p16a.position = (574,10)

                    # for puzzle piece 17
                    if p17a.x > 66 and p17a.x < 134 and p17a.y > 71 and p17a.y < 124:
                        p17a.position = (93,94)
                    else:
                        p17a.position = (692,354)

                    # for puzzle piece 18
                    if p18a.x > 157 and p18a.x < 235 and p18a.y > 61 and p18a.y < 135:
                        p18a.position = (186,93)
                    else:
                        p18a.position = (485,330)

                    # for puzzle piece 19
                    if p19a.x > 252 and p19a.x < 336 and p19a.y > 68 and p19a.y < 131:
                        p19a.position = (285,94)
                    else:
                        p19a.position = (568,135)

                    # for puzzle piece 20
                    if p20a.x > 347 and p20a.x < 417 and p20a.y > 60 and p20a.y < 127:
                        p20a.position = (372,93)
                    else:
                        p20a.position = (355,462)

                #to make the pieces stay in position once put in their correct places
                    if p1a.position == (94,374):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p1a.position = (94,374)

                    if p2a.position == (185,377):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p2a.position = (185,377)

                    if p3a.position == (285,377):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p3a.position = (285,377)

                    if p4a.position == (373,392):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p4a.position = (373,392)

                    if p5a.position == (93,320):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p5a.position = (93,320)

                    if p6a.position == (171,320):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p6a.position = (171,320)

                    if p7a.position == (285,320):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p7a.position = (285,320)

                    if p8a.position == (389,305):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p8a.position = (389,305)
                    
                    if p9a.position == (93,240):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p9a.position = (93,240)

                    if p10a.position == (186,256):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p10a.position = (186,256)

                    if p11a.position == (285,256):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p11a.position = (285,256)

                    if p12a.position == (373,256):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p12a.position = (373,256)

                    if p13a.position == (93,166):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p13a.position = (93,166)

                    if p14a.position == (171,184):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p14a.position = (171,184)

                    if p15a.position == (285,184):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p15a.position = (285,184)

                    if p16a.position == (372,167):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p16a.position = (372,167)

                    if p17a.position == (93,94):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p17a.position = (93,94)

                    if p18a.position == (186,93):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p18a.position = (186,93)

                    if p19a.position == (285,94):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p19a.position = (285,94)

                    if p20a.position == (372,93):
                        @window.event
                        def on_mouse_drag(x, y, dx, dy, button, modifiers):
                            p20a.position = (372,93)

                    #if puzzle is complete
                    if p1a.position == (94,374) and p2a.position == (185,377) and p3a.position == (285,377) and p4a.position == (373,392) and p5a.position == (93,320) and p6a.position == (171,320) and p7a.position == (285,320) and p8a.position == (389,305) and p9a.position == (93,240) and p10a.position == (186,256) and p11a.position == (285,256) and p12a.position == (373,256) and p13a.position == (93,166) and p14a.position == (171,184) and p15a.position == (285,184) and p16a.position == (372,167) and p17a.position == (93,94) and p18a.position == (186,93) and p19a.position == (285,94) and p20a.position == (372,93):
                        timer.running = False  #stop timer

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
                                    subprocess.call(['python', 'highscore.py'])

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
                            gfsprite.draw()
                            back_basesprite.draw()
                            highscore_basesprite.draw()
                            timer.label.draw()
                        
                        #saves time to user_score textfile
                        with open('user_score.txt', 'r') as f:
                            data = f.readlines()
                            data[1] = str(timer.label.text)+"\n"
                        with open('user_score.txt', 'w') as f:
                            f.writelines(data)
                        f.close()

            @window.event
            def on_draw():
                window.clear()
                bg3sprite.draw()
                po_lvl2sprite.draw()
                p1a.draw()
                p2a.draw()
                p3a.draw()
                p4a.draw()
                p5a.draw()
                p6a.draw()
                p7a.draw()
                p8a.draw()
                p9a.draw()
                p10a.draw()
                p11a.draw()
                p12a.draw()
                p13a.draw()
                p14a.draw()
                p15a.draw()
                p16a.draw()
                p17a.draw()
                p18a.draw()
                p19a.draw()
                p20a.draw()
                timer.label.draw()


#timer
countdown = int(1)

class Timer(object):
    def __init__(self):
        self.start = '01:00'
        self.label = pyglet.text.Label(self.start, font_name='Arial Rounded MT Bold', font_size=20,
                                       x = 10, y = 10)
        self.reset()

    def reset(self):
        self.time = (countdown * 60) + 1
        self.running = True
        self.label.text = self.start
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time -= dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m < 0:
                self.running = False
                @window.event
                # mouse events
                def on_mouse_press(x, y, button, modifiers):
                    if button == mouse.LEFT:
                        # when back button is pressed
                        if x > 80 and x < 245 and y > 140 and y < 193:
                            @window.event
                            def on_draw():
                                back_presssprite.draw()

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
                        else:
                            @window.event
                            def on_draw():
                                back_basesprite.draw()

                @window.event
                def on_mouse_motion(x, y, button, modifiers):
                    # when mouse hovers over back button
                    if x > 80 and x < 245 and y > 140 and y < 193:
                        @window.event
                        def on_draw():
                            back_hoversprite.draw()
                    else:
                        @window.event
                        def on_draw():
                            gameoversprite.draw()
                            back_basesprite.draw()

                @window.event
                def on_draw():
                    window.clear()
                    gameoversprite.draw()
                    back_basesprite.draw()

@window.event
def on_draw():
    window.clear()
    bg2sprite.draw()
    po_lvl1sprite.draw()
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    p5.draw()
    p6.draw()
    p7.draw()
    p8.draw()
    p9.draw()
    timer.label.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run()