# KRtype_v3.0 made by tesSer16

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
            if char2 in inv_double_vowels_dict:
                char2 = char2.replace(char2, inv_double_vowels_dict[char2])
            result += char2

            int_char3 = int((pre_char - (588 * int_char1) - (28 * int_char2)))  # 종성 추출
            if not int_char3:  # 공백일 경우(받침이 없을 경우) 건너뜀
                continue
            char3 = jong_list[int_char3]
            if char3 in inv_double_consonants_dict:
                char3 = char3.replace(char3, inv_double_consonants_dict[char3])
            result += char3

        elif 12593 <= ord(s) <= 12643:  # chr(44032) -> ㄱ, chr(55203) -> ㅣ
            if s in inv_double_vowels_dict:
                s = s.replace(s, inv_double_vowels_dict[s])
            if s in inv_double_consonants_dict:
                s = s.replace(s, inv_double_consonants_dict[s])
            result += s

        else:
            result += s

    return result


def combination(string):  # 완성된 글쇠들을 조합
    if len(string) == 1:
        return string

    result = 44032  # 가
    for i, s in enumerate(string):
        if i == 0:
            result += 21 * 28 * cho_list.index(s)
        elif i == 1:
            result += 28 * jung_list.index(s)
        elif i == 2:
            result += jong_list.index(s)

    return chr(result)


class Assembler:
    def __init__(self, string):
        self.string = string[1:]
        self.result = ""
        self.temp = string[0]
        self.counter = 1

    def B1C(self, counter):
        if not self.string:
            return 0
        else:
            self.temp += self.string.pop(0)
            return counter

    def end(self):
        self.counter = 1
        self.result += combination(self.temp[:-1])
        self.temp = self.temp[-1]

    def state1(self):
        if self.temp[0] in cho_list:
            self.counter = self.B1C(2)
        else:  # single end
            self.result += self.temp
            self.temp = ""
            self.counter = self.B1C(1)

    def state2(self):
        if self.temp[1] in jung_list:
            self.counter = self.B1C(3)
        else:
            self.counter = 4

    def state3(self):
        if self.temp[1:3] in double_vowels_dict:
            self.temp = self.temp.replace(self.temp[1:3], double_vowels_dict[self.temp[1:3]])
            self.counter = self.B1C(6)
        else:
            self.counter = 6

    def state4(self):
        if self.temp in double_consonants_dict:
            self.temp = double_consonants_dict[self.temp]
            self.counter = self.B1C(5)
        else:
            self.end()

    def state5(self):
        if self.temp[2] in jung_list:
            self.temp = inv_double_consonants_dict[self.temp]  # 이중자음 분리
            self.result += self.temp[0]  # partial end
            self.temp = self.temp[1:]
            self.counter = self.B1C(3)
        else:
            self.end()

    def state6(self):
        if self.temp[2] in jong_list and self.temp[2] != ' ':
            self.counter = self.B1C(7)
        else:
            self.end()

    def state7(self):
        if self.temp[2:4] in double_consonants_dict:
            self.temp = self.temp.replace(self.temp[2:4], double_consonants_dict[self.temp[2:4]])
            self.counter = self.B1C(8)
        else:
            self.counter = 8

    def state8(self):
        if self.temp[-1] in jung_list:
            if self.temp[-2] in inv_double_consonants_dict:
                self.temp = self.temp.replace(self.temp[-2], inv_double_consonants_dict[self.temp[-2]])
            self.result += combination(self.temp[:-2])  # partial end
            self.temp = self.temp[-2:]
            self.counter = self.B1C(3)
        else:
            self.end()

    states = [None, state1, state2, state3, state4, state5, state6, state7, state8]


def assemble(string):  # 분해된 한글을 조합
    out = Assembler(string)
    while out.counter:
        print(out.counter, out.result, out.temp)
        Assembler.states[out.counter](out)

    if out.temp:
        if len(out.temp) == 1:
            out.result += out.temp
        else:
            out.result += combination(out.temp)

    return out.result


if __name__ == "__main__":
    data = disassemble(input(">>> "))
    print("Disassembled:", data)
    print("Assembled:", assemble(list(data)))
