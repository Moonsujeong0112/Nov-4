# 구글번역 라이브러리
import googletrans
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

