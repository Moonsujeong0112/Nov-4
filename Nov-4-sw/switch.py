from gpiozero import Button, LED, RGBLED
from signal import pause
from time import sleep
from ras_result import trans_result


############# GPIO핀은 다 써서 버튼 핀은 SDA1과 같은 특수한 핀으로 사용했는데 괜찮을거 같은데 통신을 위해 색다른 기능을 넣은거니까 될거같은데 아무튼 그 핀으로 설정해놨어
#############led는 핀 있는거로 설정했엉


# 번역
flag_trans = 0
led_trans = LED(40) # LED는 3번핀
button_trans = Button(3) # 스위치는 2번핀

# 리셋
flag_reset = 0
button_reset = Button(5) 

# 3색 led- 속도제어
flag_speed = 0
led_speed = RGBLED(red=12, green=32, blue=33)
button_speed = Button(7) 


def trans(scan_text):
        global flag_trans
        if flag_trans == 0 :
                flag_trans = 1
                led_trans.on()
                re = trans_result(scan_text)
        else :
                flag_trans = 0
                led_trans.off()
        pause()
        


def reset(scan_text):
        global flag_reset
        if flag_reset == 0 :
                flag_reset = 1
                scan_text=""
                # 카메라 켜기 함수 넣으면 됩니당!!!!!!
                print("open!!")
        else :
                flag_reset = 0
        pause()

def speed():
        global flag_speed
        # 느렸다가 빨라지기
        if flag_speed == 0:
                flag_speed=1
                # led 점자 나오기!!!
                led_speed.color=(0,0,1)
                sleep(1.5)
        elif flag_speed == 1:
                flag_speed=2
                # led 점자 나오기!!!
                led_speed.color=(1,1,0)
                sleep(1)
        else:
                flag_speed=0
                # led 점자 나오기!!!
                led_speed.color=(1,0,0)
                sleep(0.5)
        

if __name__ == '__main__':
        button_trans.when_pressed = trans
        button_reset.when_pressed = reset
        button_speed.when_pressed = speed
