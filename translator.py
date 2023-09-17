# 구글번역 라이브러리
import googletrans
import sys

# 영->한 번역
def transform_text(scan_text): 
    # 2. 번역기 객체 생성
    translator = googletrans.Translator()
    # 3. 번역할 단어
    inStr = scan_text
    # 4. 번역
    outStr = translator.translate(inStr, dest = 'ko', src = 'auto')
    # 5. 결과
    print(f"{inStr} => {outStr.text}")
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

result_eh=[]
h=[]
e=[]
if isHangul(text[0]):
  c=1
else:
  c=0
# 한글 부분과 영어부분으로 나눠서 리스트에 저장
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
print(result_eh)

# 최종결과물
rrrr=[]

for t in result_eh:
  rrrr.append(transform_text(t))

result = ' '.join(rrrr)
print(result)
