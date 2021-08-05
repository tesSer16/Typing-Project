cho_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
            'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

jung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
             'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

jong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
             'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
             'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


double_vowels_dict = {'ㅗㅏ': 'ㅘ', 'ㅗㅐ': 'ㅙ', 'ㅗㅣ': 'ㅚ',
                      'ㅜㅓ': 'ㅝ', 'ㅜㅔ': 'ㅞ', 'ㅜㅣ': 'ㅟ',
                      'ㅡㅣ': 'ㅢ'}
double_consonants_dict = {'ㄱㅅ': 'ㄳ', 'ㄴㅈ': 'ㄵ', 'ㄴㅎ': 'ㄶ',
                          'ㄹㄱ': 'ㄺ', 'ㄹㅁ': 'ㄻ', 'ㄹㅂ': 'ㄼ',
                          'ㄹㅅ': 'ㄽ', 'ㄹㅌ': 'ㄾ', 'ㄹㅍ': 'ㄿ',
                          'ㄹㅎ': 'ㅀ', 'ㅂㅅ': 'ㅄ'}

inv_double_vowels_dict = {v: k for k, v in double_vowels_dict.items()}
inv_double_consonants_dict = {v: k for k, v in double_consonants_dict.items()}


def disassemble(s):
    result = ""  # 결과를 저장할 변수
    
    n = ord(s) - 44032

    a = n // 588  # 초성 추출
    result += cho_list[a]

    b = (n % 588) // 28  # 중성 추출
    jung = jung_list[b]
    if jung in inv_double_vowels_dict:  # 모음 결합 여부 확인
        jung = jung.replace(jung, inv_double_vowels_dict[jung])
    result += jung

    c = n % 28  # 종성 추출
    if not c:  # 공백일 경우(받침이 없을 경우) 건너뜀
        return result
    jong = jong_list[c]
    if jong in inv_double_consonants_dict:  # 모음 결합 여부 확인
        jong = jong.replace(jong, inv_double_consonants_dict[jong])
    result += jong

    return result
