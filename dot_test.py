#word list 
first_word_list = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ'
                   , 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ'
                   , 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ'
                   , 'ㅄ']

middle_word_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ'
                    , 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

num_word_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

abc_word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
                 , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
                 , 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
                 , 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'
                 , 'W', 'X', 'Y', 'Z']

#종성 제어
def print_jong(sentance):
    print('종성' + sentance)



#초성 중성 영어 숫자 제어
def print_dot(sentance):
    print(sentance)


#초성 종성 분리 led제어
def com_len(sentance):
    com = sentance
    com_len = len(com) 
    com.append(" ")
    for i in range(com_len):
        if any(str in com[i+1] for str in '/'):
            if any(str in com[i] for str in first_word_list):
                print_jong(com[i])
        else:
            print_dot(com[i])



#input
#sentance = ['1', '1', 'ㅇ', 'ㅝ', 'ㄹ', '4', 'ㅇ', 'ㅣ', 'ㄹ'
#           , 'ㅇ', 'ㅡ', 'ㄴ', 'ㅈ', 'ㅓ', 'ㅁ', 'ㅈ', 'ㅏ', 'ㅇ', 'ㅢ', 'ㄴ', 'ㅏ', 'ㄹ'
#           , 'ㅇ', 'ㅣ', 'ㅂ', 'ㄴ', 'ㅣ', 'ㄷ', 'ㅏ']
#sentance = ['ㅈ', 'ㅓ', 'ㅁ', 'ㅈ', 'ㅏ', 'ㅇ', 'ㅢ', 'ㄴ', 'ㅏ', 'ㄹ'
#           , 'ㅇ', 'ㅣ', 'ㅂ', 'ㄴ', 'ㅣ', 'ㄷ', 'ㅏ']
sentance = ['ㅊ', 'ㅗ', 'ㄹ', 'ㅗ', 'ㄱ', 'ㅁ', 'ㅐ', 'ㅅ', 'ㅣ', 'ㄹ']


cnt = len(sentance)+1 #count sentence len
sentance.append("")
sentance.append("")

for i in range(cnt):
    #종성 구분
    if any(str in sentance[i] for str in first_word_list):
        if any(str in sentance[i-1] for str in middle_word_list):
            if any(str in sentance[i+1] for str in first_word_list):
                sentance.insert(i+1, '/')
            if any(str in sentance[i+1] for str in ""):
                sentance.insert(i+1, '/')
        #앞에 숫자 있을 때 초성 종성 구분
        if any(str in sentance[i+1] for str in num_word_list):
            if any(str in sentance[i-1] for str in middle_word_list):
                if any(str in sentance[i-2] for str in first_word_list):
                    sentance.insert(i+1, '/')
        #앞에 영어 있을 때 초성 종성 구분
        if any(str in sentance[i+1] for str in abc_word_list):
            if any(str in sentance[i-1] for str in middle_word_list):
                if any(str in sentance[i-2] for str in first_word_list):
                    sentance.insert(i+1, '/')
        
print(sentance)
#cnt = len(sentance) #count sentence len
com_len(sentance)
    






