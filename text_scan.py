#텍스트 추출 라이브러리
import easyocr
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import random
import matplotlib.pyplot as plt
# 문장 교정 라이브러리
from re import findall, sub
import kss
from hanspell import spell_checker


#텍스트 추출
reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext("test08.png")
img    = cv2.imread("test08.png")
print("[INFO] OCR'ing input image...")
img = Image.fromarray(img)
font = ImageFont.truetype("HMKMRHD.TTF",20)
draw = ImageDraw.Draw(img)
scan_text = ""
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(255, 3),dtype="uint8")
for i in result :
    x = i[0][0][0]
    y = i[0][0][1]
    w = i[0][1][0] - i[0][0][0]
    h = i[0][2][1] - i[0][1][1]

    color_idx = random.randint(0,255)
    color = [int(c) for c in COLORS[color_idx]]
    draw.rectangle(((x, y), (x+w, y+h)), outline=tuple(color), width=2)
    draw.text((int((x + x + w) / 2) , y-2),str(i[1]), font=font, fill=tuple(color),)
    scan_text += i[1]
    scan_text += " "

#문장 교정
def clean_text(scan_text) : # 여기서 사용되는 text는 'string' 기준이여야 함. list 말고 그 안에 하나, string 형태로!
# 1~6단계
    texts_re = text.lower() # 소문자화
    texts_re3 = sub('[,.?!;:]', '', texts_re) # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) # 특수문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4) # 영문자 제거
    texts_re6 = ' '.join(texts_re5.split()) # white space 제거(단어 구분)
    return texts_re6 # 반환값

# 입력 문장
t = clean_text(scan_text)

# 교정 과정
for sent in kss.split_sentences(t):
    sent=clean_text(sent)
    spelled_sent = spell_checker.check(sent)
    checked_sent = spelled_sent.checked
    print(checked_sent) # 최종 교정 결과

plt.imshow(img)
plt.show()