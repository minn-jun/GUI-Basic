# 자동 스크린샷 프로그램 작성

# Pillow install 필요
from PIL import ImageGrab
import time

time.sleep(5)    # 5초 대기 : 사용자가 준비하는 시간

for i in range(1, 11):    # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()    # 현재 스크린 이미지를 가져옴
    img.save(f"image{i}.png")    # 파일로 저장
    time.sleep(2)    # 2초 단위