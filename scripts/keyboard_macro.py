import keyboard
import time
i = 0
recorded = keyboard.record(until='esc')
while i < 100:
    keyboard.play(recorded)

    i = i + 1
