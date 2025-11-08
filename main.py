import time
import pydirectinput
from fish import fish, sell_fish
from use_rune import *

fish_count = 0
time.sleep(3)


while pydirectinput.position()[1] > 200:
    fish()
    fish_count = fish_count + 1
    if fish_count >= 20:
        sucess = sell_fish()
        if sucess:
            fish_count = 0
    #use_rune()