from PIL import ImageGrab
import time
import pydirectinput
from utils import *

def is_blood():
    px = ImageGrab.grab().load()
    red = px[164, 1223][0]
    green = px[164, 1223][1]
    blue = px[164, 1223][2]
    blood = False
    if about_equals(red, 0x46, 5) and about_equals(green, 0x0F, 3) and about_equals(blue, 0x0F, 3):
        blood = True
    return True

def use_rune():
    click_delay = 0.1

    pydirectinput.press('\\')
    time.sleep(click_delay)
    pydirectinput.press('a')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('a')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('a')
    time.sleep(click_delay)
    pydirectinput.press('s')
    time.sleep(click_delay)
    pydirectinput.press('a')
    time.sleep(click_delay)
    pydirectinput.press('w')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    pydirectinput.press('d')
    time.sleep(click_delay)
    for i in range(5):
        pydirectinput.press('w')
        time.sleep(click_delay)
    pydirectinput.press('enter')
    time.sleep(click_delay)
    pydirectinput.press('\\')