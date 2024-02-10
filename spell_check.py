from re import findall, sub
import kss
from hanspell import spell_checker

def clean_text(text) : # 여기서 사용되는 text는 'string' 기준이여야 함. list 말고 그 안에 하나, string 형태로!
# 1~6단계
    texts_re = text.lower() # 소문자화
    texts_re3 = sub('[,.?!;:]', '', texts_re) # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) # 특수문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4) # 영문자 제거
    texts_re6 = ' '.join(texts_re5.split()) # white space 제거(단어 구분)
    return texts_re6 # 반환값

# 입력 문장
t = "김형호      %%$$$ 영화시장분석가는'1987'의네이버영화정보네티즌10점평에서언급된단어들을지난해12월27일부터올해1월10일까지통계프로그램R과KoNLP패키지로텍스트마이닝하여분석했다"

# 교정 과정
for sent in kss.split_sentences(t):
    sent=clean_text(sent)
    spelled_sent = spell_checker.check(sent)
    checked_sent = spelled_sent.checked
    print(checked_sent) # 최종 교정 결과