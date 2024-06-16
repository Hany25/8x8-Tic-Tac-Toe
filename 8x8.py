from microbit import*
import neopixel
gz_led = neopixel.NeoPixel(pin0,64)
border_colour = (0,5,0)
x_mark_colour = (10,0,0)
x_temp_colour = (5,0,0)
o_mark_colour = (0,0,10)
o_temp_colour = (0,0,5)
no_colour = (0,0,0)
player = ""
part = 0
place = 0
pin_press = 0
stop =0 
score_count = 0
list = [[0,1,9,8], [3,4,12,11], [6,7,15,14], [24,25,33,32],
       [27,28,36,35], [30,31,39,38], [48,49,57,56], [51,52,60,59],
       [54,55,63,62]]
win_list = [[1,2,3],
           [1,5,9],
           [1,4,7],
           [2,5,8],
           [3,6,9],
           [3,5,7],
           [4,5,6],
           [7,8,9]]
win_list_index = 0
o_list = []
x_list = []
c = (0,0,0)
def select():
    global player, part, temp, pin_press
    if button_a.get_presses():
        player = "x"
        temp = player
        display.show(Image.NO)
        pin_press +=1
    elif button_b.get_presses():
        player = "o"
        temp = player
        display.show(Image("09990:"
                               "90009:"
                               "90009:"
                               "90009:"
                               "09990"))
        pin_press+=1
    if pin_logo.is_touched():
        part += 1

def draw_border(border_colour):
    for i in range(8):
        gz_led[2 +8*i] = border_colour
        gz_led[5 +8*i] = border_colour  
        gz_led[16 + i] = border_colour  
        gz_led[40 + i] = border_colour  
        gz_led.write()

def rotate():
    global place, list, x_temp_colour, o_temp_colour, c, current,stop
    if place == 0:
        return
    elif player == "x" and stop == 0:
       for i in range(4):
            current = gz_led[list[place-1][i]]
            gz_led[list[place-1][i]] = x_temp_colour
            gz_led.write()
            sleep(75)
            gz_led[list[place-1][i]] = current
    elif player == "o" and stop == 0:
        for i in range(4):
            current = gz_led[list[place-1][i]]
            gz_led[list[place-1][i]] = o_temp_colour
            gz_led.write()
            sleep(75)
            gz_led[list[place-1][i]] = current
        
    
    
def placement():
    global place, x_mark_colour, gz_led, player, has
    if pin13.read_digital() == 0 and place < 9:
        place += 1
        display.show(place)
        sleep(500)
    elif pin13.read_digital() == 1:
        display.clear()
    if pin12.read_digital() == 0 and place >1:
        place -= 1
        display.show(place)
        sleep(500)
    elif pin12.read_digital() == 1:
        display.clear()
    if pin16.read_digital() == 0 and player == "x":
        has = 0
        for g in range(len(o_list)):
            if place == o_list[g]:
                has = 1
        if has == 0 :
            for j in range (9):
                for i in range(4):
                    if (place-1) == j:
                        gz_led[list[j][i]] = x_mark_colour
                        gz_led.write()
                        x_list.append(place)
            player = "o"
            display.show(Image("09990:"
                                   "90009:"
                                   "90009:"
                                   "90009:"
                                   "09990"))
            sleep(1000)
            display.clear()
    if pin16.read_digital() == 0 and player == "o" :
        has = 0
        for u in range(len(x_list)):
            if place == x_list[u]:
                has = 1
        if has == 0 :
            for j in range (9):
                for i in range(4):
                    if (place-1) == j:
                        gz_led[list[j][i]] = o_mark_colour
                        gz_led.write()
                        o_list.append(place)
            player = "x"
            display.show(Image.NO)
            sleep(1000)
            display.clear()


def winx():
    global x_list,list, win_list,o_list, win_list_index,score_count,stop
    if len(x_list) >= 3:
        k = 0
        for i in range(8):
            score_count = 0
            for j in range(3):
                for k in range(len(x_list)):
                    if win_list[i][j] == x_list[k] and score_count != 3: 
                        score_count += 1
                        break
                if score_count == 3:
                    win_list_index = i
                    break
            if score_count== 3:
                break    
    if score_count == 3:
        for i in range(9):
            if (i+1) != win_list[win_list_index][0] and (i+1) != win_list[win_list_index][1] and (i+1) != win_list[win_list_index][2]:
                for m in range (4):
                    gz_led[list[i][m]] = no_colour
                    gz_led.write()
                    display.show(Image.NO)
        stop = 1
    if (score_count == 3) and (pin8.read_digital() == 0 or pin12.read_digital() == 0 or pin13.read_digital() == 0 or pin14.read_digital() == 0 or pin15.read_digital() == 0 or pin16.read_digital() == 0):
        for i in range(64):
            gz_led[i] = no_colour


def wino():
    global list, win_list,o_list, win_list_index,score_count,stop
    if len(o_list) >= 3:
        k = 0
        for i in range(8):
            score_count = 0
            for j in range(3):
                for k in range(len(o_list)):
                    if win_list[i][j] == o_list[k] and score_count != 3: 
                        score_count += 1
                        break
                if score_count == 3:
                    win_list_index = i
                    break
            if score_count == 3:
                break
    if score_count == 3:
        for i in range(9):
            if (i+1) != win_list[win_list_index][0] and (i+1) != win_list[win_list_index][1] and (i+1) != win_list[win_list_index][2]:
                for m in range (4):
                    gz_led[list[i][m]] = no_colour
                    gz_led.write()
                    display.show(Image("09990:"
                                   "90009:"
                                   "90009:"
                                   "90009:"
                                   "09990"))
        stop = 1
    if (score_count == 3) and (pin8.read_digital() == 0 or pin12.read_digital() == 0 or pin13.read_digital() == 0 or pin14.read_digital() == 0 or pin15.read_digital() == 0 or pin16.read_digital() == 0):
        for i in range(64):
            gz_led[i] = no_colour
    

display.show("?")
while part == 0:
    select()
draw_border(border_colour)
while part == 1:
    placement()
    rotate()
    winx()
    wino()
