from PIL import ImageGrab
import time
import pydirectinput
from utils import *

def wait_for_fish():
    start_time = time.perf_counter()
    fishing_start_color = (0, 0, 0)
    while not fishing_start_color == (255, 255, 255):
        px = ImageGrab.grab().load()
        fishing_start_color = px[1573, 982]
        if fishing_start_color == (255, 255, 255):
            break
        time.sleep(1)
        if time.perf_counter() - start_time > 120:
            break
    time.sleep(1)

def click_on_fish():
    click_delay = 0.2

    pydirectinput.press('\\')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('a')
    time.sleep(click_delay)
    pydirectinput.press('w')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('\\')

def find_you(image):
    divisions = 50
    bar_start = 1060
    bar_end = 1490
    # 33, 154, 167
    for i in range(bar_start, bar_end, int((bar_end - bar_start)/divisions)):
        red = image[i, 1025][0]
        green = image[i, 1025][1]
        blue = image[i, 1025][2]
        if about_equals(red, 0xF6, 20) and about_equals(green, 0xF6, 20) and about_equals(blue, 0xF6, 20):
            return i
    return 1490

def find_bar(image):
    divisions = 50
    bar_start = 1490
    bar_end = 1060
    # 33, 154, 167
    for i in range(bar_start, bar_end, int((bar_end - bar_start)/divisions)):
        red = image[i, 1034][0]
        green = image[i, 1034][1]
        blue = image[i, 1034][2]
        if blue > 0x40 or green > 0x40:
            return i
    return 1060


def fish_time():
    start_time = time.perf_counter()
    while 1:
        px = ImageGrab.grab().load()
        you_pos = find_you(px)
        you_pos = (you_pos - 1060)/(1490-1060)
        bar_pos = find_bar(px)
        bar_pos = (bar_pos - 1060)/(1490-1060)

        if bar_pos > you_pos and not about_equals(bar_pos, you_pos, 0.10):
            pydirectinput.click()

        if px[1486, 462] == (255, 255, 255):
            break
        
        if time.perf_counter() - start_time > 20:
            return True
    return False
        
def exit_fish():
    click_delay = 0.2

    time.sleep(.5)
    pydirectinput.press('\\')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('w')
    time.sleep(click_delay)
    pydirectinput.press('w')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('\\')

def fish():
    click_on_fish()
    wait_for_fish()
    fullError = fish_time()
    if not fullError:
        exit_fish()

def walk_shop():
    pydirectinput.keyDown('s')
    time.sleep(.4)
    pydirectinput.press('space')
    time.sleep(1)
    pydirectinput.keyUp('s')
    time.sleep(.3)
    pydirectinput.press('e')
    time.sleep(3)
    px = ImageGrab.grab().load()
    if not px[1867, 908] == (255, 255, 255):
        px = ImageGrab.grab().load()
        if not px[1867, 908] == (255, 255, 255):
            return False
    pydirectinput.press('\\')
    time.sleep(.2)
    pydirectinput.press('s')
    time.sleep(.2)
    pydirectinput.press('enter')
    time.sleep(.2)
    pydirectinput.press('\\')
    time.sleep(1)
    return True

def shop_error():
    px = ImageGrab.grab().load()
    error_counter = 0
    while not px[1533, 982] == (255, 255, 255) and not px[1536, 982] == (255, 255, 255) and error_counter < 25:
        pydirectinput.press('w')
        error_counter += 1
        px = ImageGrab.grab().load()
        time.sleep(.5)


def walk_back():
    pydirectinput.keyDown('w')
    time.sleep(1.6)
    pydirectinput.keyUp('w')
    time.sleep(.3)

def sell_fish():
    sucess = walk_shop()
    if not sucess:
        shop_error()
        return False

    click_delay = 0.5
    for i in range(20):
        pydirectinput.press('\\')
        time.sleep(click_delay)
        pydirectinput.press('a')
        time.sleep(click_delay)
        pydirectinput.press('a')
        time.sleep(click_delay)
        pydirectinput.press('a')
        time.sleep(click_delay)

        px = ImageGrab.grab().load()
        if px[1192, 532] == (255, 255, 255):

            pydirectinput.press('enter')
            time.sleep(click_delay)
            pydirectinput.press('w')
            time.sleep(click_delay)
            pydirectinput.press('s')
            time.sleep(click_delay)
            pydirectinput.press('a')
            time.sleep(click_delay)
            pydirectinput.press('enter')
            time.sleep(click_delay)
            pydirectinput.press('w')
            time.sleep(click_delay)
            pydirectinput.press('w')
            time.sleep(click_delay)
            pydirectinput.press('enter')
            time.sleep(click_delay)
            pydirectinput.press('\\')
            time.sleep(click_delay)
        else: 
            pydirectinput.press('\\')
            time.sleep(click_delay)
            pydirectinput.press('\\')
            time.sleep(click_delay)
            pydirectinput.press('a')
            time.sleep(click_delay)
            pydirectinput.press('enter')
            time.sleep(click_delay)
            pydirectinput.press('\\')
            break

    walk_back()

    return True

    

