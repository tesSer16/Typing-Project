# KRENtype_v1.0 made by tesSer16

cho_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ',
             'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

double_vowels_dict2 = {'ㅗㅏ': 'ㅘ', 'ㅗㅐ': 'ㅙ', 'ㅗㅣ': 'ㅚ',
                       'ㅜㅓ': 'ㅝ', 'ㅜㅔ': 'ㅞ', 'ㅜㅣ': 'ㅟ',
                       'ㅡㅣ': 'ㅢ'}
double_consonants_dict2 = {'ㄱㅅ': 'ㄳ', 'ㄴㅈ': 'ㄵ', 'ㄴㅎ': 'ㄶ',
                           'ㄹㄱ': 'ㄺ', 'ㄹㅁ': 'ㄻ', 'ㄹㅂ': 'ㄼ',
                           'ㄹㅅ': 'ㄽ', 'ㄹㅌ': 'ㄾ', 'ㄹㅍ': 'ㄿ',
                           'ㄹㅎ': 'ㅀ', 'ㅂㅅ': 'ㅄ'}

double_vowels_dict1 = {v: k for k, v in double_vowels_dict2.items()}
double_consonants_dict1 = {v: k for k, v in double_consonants_dict2.items()}


def disassemble(string):  # 문자열을 분리
    result = ''

    for s in string:
        if 44032 <= ord(s) <= 55203:  # chr(44032) -> 가, chr(55203) -> 힣
            pre_char = ord(s) - 44032

            int_char1 = int(pre_char / 588)  # 초성 추출
            char1 = cho_list[int_char1]
            result += char1

            int_char2 = int((pre_char - 588 * int_char1) / 28)  # 중성 추출
            char2 = jung_list[int_char2]
            if char2 in double_vowels_dict1:
                char2 = char2.replace(char2, double_vowels_dict1[char2])
            result += char2

            int_char3 = int((pre_char - (588 * int_char1) - (28 * int_char2)))  # 종성 추출
            if not int_char3:  # 공백일 경우(받침이 없을 경우) 건너뜀
                continue
            char3 = jong_list[int_char3]
            if char3 in double_consonants_dict1:
                char3 = char3.replace(char3, double_consonants_dict1[char3])
            result += char3

        elif 12593 <= ord(s) <= 12643:  # chr(44032) -> ㄱ, chr(55203) -> ㅣ
            if s in double_vowels_dict1:
                s = s.replace(s, double_vowels_dict1[s])
            if s in double_consonants_dict1:
                s = s.replace(s, double_consonants_dict1[s])
            result += s

        else:
            result += s

    return result


def combination(string):  # 완성된 글쇠들을 조합
    result = 44032
    for i, s in enumerate(string):
        if i == 0:
            result += 21 * 28 * cho_list.index(s)
        elif i == 1:
            result += 28 * jung_list.index(s)
        else:
            result += jong_list.index(s)

    return chr(result)


def assemble(result):  # 분해된 한글을 조합
    string = ''
    temp = ''
    counter, i = 0, 0
    while True:
        print(counter, string, temp)
        if i >= len(result):
            if len(temp) == 1:
                string += temp
            elif temp:
                string += combination(temp)
            break

        temp += result[i]

        if counter == 0:
            i += 1
            if temp[0] in cho_list:
                counter = 1
            else:
                string += temp
                temp = ''
            continue

        elif counter == 1:
            if temp[1] in jung_list:
                i += 1
                counter = 1.5
            elif temp in double_consonants_dict2:
                i += 1
                counter = 1.414
            else:
                counter = 0
                string += temp[:-1]
                temp = ''
            continue

        elif counter == 1.414:
            if temp[2] in jung_list:
                i += 1
                counter = 1.5
                string += temp[0]
                temp = temp[1:]
            else:
                counter = 0
                string += double_consonants_dict2[temp[:-1]]
                temp = ''
            continue

        elif counter == 1.5:
            if temp[1:3] in double_vowels_dict2:
                i += 1
                temp = temp.replace(temp[1:3], double_vowels_dict2[temp[1:3]])
                counter = 2
            elif temp[2] not in jong_list or temp[2] == ' ':
                counter = 0
                string += combination(temp[:-1])
                temp = ''
            else:  # temp[2] in jong_list
                temp = temp[:-1]
                counter = 2
            continue

        elif counter == 2:
            if temp[2] not in jong_list or temp[2] == ' ':
                counter = 0
                string += combination(temp[:-1])
                temp = ''
            else:  # temp[2] in jong_list
                i += 1
                counter = 2.5
            continue

        elif counter == 2.5:
            if temp[2:4] in double_consonants_dict2:
                i += 1
                counter = 3
            elif temp[3] in jung_list:
                i += 1
                string += combination(temp[:2])
                temp = temp[2:]
                counter = 1.5
            else:
                counter = 0
                string += combination(temp[:-1])
                temp = ''
            continue

        else:  # counter == 3
            if temp[4] in jung_list:
                i += 1
                string += combination(temp[:3])
                temp = temp[3:]
                counter = 1.5
            else:
                temp = temp.replace(temp[2:4], double_consonants_dict2[temp[2:4]])
                counter = 0
                string += combination(temp[:-1])
                temp = ''
            continue

    return string


if __name__ == "__main__":
    data = disassemble(input(">>> "))
    print("Disassembled:", data)
    print("Assembled:", assemble(data))
