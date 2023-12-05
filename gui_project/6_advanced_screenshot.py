# 스크린샷 프로그램 작성

# keyboard install 필요
import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # 2023.12.05 10:30:15 -> _20231205_103015
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save(f"image{curr_time}.png")    # image_20231205_103015.png


# 사용자가 F9를 누르면 스크린샷 저장
keyboard.add_hotkey("F9", screenshot)
# 조합키 사용 가능 >> ex) ctrl+shift+s

# 사용자가 esc를 누를 때까지 프로그램 수행
keyboard.wait("esc")