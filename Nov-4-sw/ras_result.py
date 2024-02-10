# 글자 교정 라이브러리
from re import findall, sub
# 구글번역 라이브러리
import googletrans
#텍스트 추출 라이브러리
import easyocr
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import random

import sys, re

# 영->한 번역
def transform_texttoko(scan_text): 
    # 2. 번역기 객체 생성
    translator = googletrans.Translator()
    # 3. 번역할 단어
    inStr = scan_text
    # 4. 번역
    outStr = translator.translate(inStr, dest = 'ko', src = 'auto')
    
    return outStr.text

# 한->영 번역
def transform_texttoen(scan_text): 
    # 2. 번역기 객체 생성
    translator = googletrans.Translator()
    # 3. 번역할 단어
    inStr = scan_text
    # 4. 번역
    outStr = translator.translate(inStr, dest = 'en', src = 'auto')
    
    return outStr.text
# 한글인지 확인하기
def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0

def clean_text(text) : # 여기서 사용되는 text는 'string' 기준이여야 함. list 말고 그 안에 하나, string 형태로!
# 1~6단계
    texts_re = text.lower() # 소문자화
    texts_re3 = sub('[,?!;:]', '', texts_re) # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) # 특수문자 제거
    texts_re6 = ' '.join(texts_re4.split()) # white space 제거(단어 구분)
    return texts_re6 # 반환값

#텍스트 추출
reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext("test_image/test1.png")
img    = cv2.imread("test_image/test1.png")
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
print("사진에서 추출된 글자: ",scan_text)

# 입력 문장
def trans_result(scan_text):
  text = scan_text.split()
  result_eh=[]
  h=[]
  e=[]
  if isHangul(text[0]):
    c=1
  else:
    c=0
  for t in text:
    if c==1:
      if isHangul(t):
        c=1
        h.append(t)
      else:
        c=0
        result = ' '.join(h)
        result_eh.append(result)
        h.clear()
        e.append(t)
    elif c==0:
      if isHangul(t):
        c=1
        result = ' '.join(e)
        result_eh.append(result)
        e.clear()
        h.append(t)
      else:
        c=0
        e.append(t)
  if len(e)>0:
    result = ' '.join(e)
    result_eh.append(result)
  if len(h)>0:
    result = ' '.join(h)
    result_eh.append(result)

  rrrr=[]

  for t in result_eh:
    rrrr.append(transform_texttoko(t))

  result = ' '.join(rrrr)
  print("한글로 번역한 글자: ", result)
  return result




result = trans_result(scan_text)
print(result)
re_result=[]
# 교정 과정
for sent in result:
    
    checked_sent=clean_text(sent)
    
    print("교정된 글자: ", checked_sent) # 최종 교정 결과
    re_result.append(checked_sent)
    
    

result = ''.join(re_result)
print(result)
