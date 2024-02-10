from gpiozero import LED, Button
from time import sleep
#from switch import speed 
from signal import pause
from time import sleep
#rom ras_result import trans_resul


flag_reset = 0
led_reset = LED(11)
button_reset = Button(3) 
#led 
#dot 1 pin
dot1 = LED(17)
dot2 = LED(27)
dot3 = LED(22)
dot4 = LED(23)
dot5 = LED(24)
dot6 = LED(25)
#dot 2
dot1_1 = LED(5)
dot1_2 = LED(6)
dot1_3 = LED(19)
dot1_4 = LED(16)
dot1_5 = LED(20)
dot1_6 = LED(21)



abc_word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
                 , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
                 , 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
                 , 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'
                 , 'W', 'X', 'Y', 'Z']

def dot2_off():
    #if any(str in len for str in dot2_word_list):
        dot1_1.off()
        dot1_2.off()
        dot1_3.off()
        dot1_4.off()
        dot1_5.off()
        dot1_6.off()

def com_len(sen):
    if sen == 'a':
            dot1.off()
            dot2.on()
            dot3.off()
            dot4.off()
            dot5.on()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot2.off()
            dot5.off()
            dot6.off()
    if sen == 'b':
            dot1.on()
            dot2.off()
            dot3.on()
            dot4.on()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot3.off()
            dot4.off()
            dot5.off()
    if sen == 'c':
            dot1.on()
            dot2.off()
            dot3.on()
            dot4.on()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot3.off()
            dot4.off()
            dot5.off()
    if sen == 'd':
            dot1.off()
            dot2.off()
            dot3.off()
            dot4.off()
            dot5.off()
            dot6.on()
            sleep(1.5)
            dot6.off()
    if sen == 'e':
            dot1.off()
            dot2.off()
            dot3.on()
            dot4.on()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot4.off()
            dot5.off()
            dot3.off()
    if sen == 'f':
            dot1.off()
            dot2.off()
            dot3.off()
            dot4.on()
            dot5.off()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot4.off()
            dot6.off()
    if sen == 'g':
            dot1.on()
            dot2.off()
            dot3.on()
            dot4.on()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot3.off()
            dot4.off()
            dot5.off()
    if sen == 'h':
            dot1.off()
            dot2.off()
            dot3.off()
            dot4.off()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot5.off()
    if sen == 'i':
            dot1.on()
            dot2.off()
            dot3.on()
            dot4.off()
            dot5.off()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot3.off()
            dot6.off()
    ##
    if sen == 'j':
            dot1.off()
            dot2.on()
            dot3.on()
            dot4.on()
            dot5.off()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot2.off()
            dot3.off()
            dot4.off()
    if sen == 'k':
            dot1.on()
            dot2.on()
            dot3.off()
            dot4.off()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot2.off()
            dot5.off()
    if sen == 'l':
            dot1.on()
            dot2.on()
            dot3.off()
            dot4.off()
            dot5.off()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot2.off()
            dot6.off()
    if sen == 'm':
            dot1.off()
            dot2.on()
            dot3.on()
            dot4.off()
            dot5.on()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot2.off()
            dot3.off()
            dot5.off()
            dot6.off()
    if sen == 'n':
            dot1.off()
            dot2.on()
            dot3.on()
            dot4.off()
            dot5.on()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot2.off()
            dot3.off()
            dot5.off()
            dot6.off()
    if sen == 'o':
            dot1.off()
            dot2.on()
            dot3.off()
            dot4.off()
            dot5.off()
            dot6.on()
            dot2_off()
            sleep(1.5)
            dot2.off()
            dot6.off()
    if sen == 'p':
            dot1.on()
            dot2.off()
            dot3.off()
            dot4.off()
            dot5.on()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot1.off()
            dot5.off()
    if sen == 'q':
            dot1.off()
            dot2.off()
            dot3.on()
            dot4.off()
            dot5.off()
            dot6.off()
            dot2_off()
            sleep(1.5)
            dot3.off()

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
        
sen = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'd', 'j', 'h', 'k', 'l', 'm'
        , 'h', 'l', 'n', 'e', 'o', 'p', 'l', 'q']

#button_reset.when_pressed = reset
#pause()
print('open!!')

for i in range(len(sen)):
    com_len(sen[i])
    
print('finished work')
