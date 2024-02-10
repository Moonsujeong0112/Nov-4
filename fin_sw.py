from gpiozero import Button, LED, RGBLED
from signal import pause
from time import sleep
#rom ras_result import trans_result


flag_trans = 0
led_trans = LED(9) 
button_trans = Button(2) 


flag_reset = 0
led_reset = LED(11)
button_reset = Button(3) 


flag_speed = 0
led_speed = RGBLED(red=14, green=15, blue=18)
button_speed = Button(4) 
led_speed.color=(0,0,0)


def trans(scan_text):
        global flag_trans
        if flag_trans == 0 :
                flag_trans = 1
                led_trans.on()
                #re = trans_result(scan_text)
        else :
                flag_trans = 0
                led_trans.off()
        pause()
        


def reset(scan_text):
        global flag_reset
        if flag_reset == 0 :
                flag_reset = 1
                led_reset.on()
                scan_text=""
               
                #camstart()
                print("open!!")
                sleep(1.0)
                led_reset.off()
                
        else :
                flag_reset = 0
                led_reset.off()
        pause()

def speed():
        global flag_speed
        
        if flag_speed == 0:
                flag_speed=1
                #dots_speed(0)
               
                led_speed.color=(0,0,1)
                sleep(1.5)
        elif flag_speed == 1:
                flag_speed=2
                #dots_speed(1)
                
                led_speed.color=(0,1,0)
                sleep(1)
        else:
                flag_speed=0
                
                #dots_speed(2)
                led_speed.color=(1,0,0)
                sleep(0.5)
        

#if __name__ == '__main__':
button_trans.when_pressed = trans
button_reset.when_pressed = reset
button_speed.when_pressed = speed
pause()
