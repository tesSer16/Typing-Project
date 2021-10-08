# KRKRtype_v3.1 made by tesSer16

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


def disassemble(string):
    result = ""  # 결과를 저장할 변수

    for s in string:
        if ord('가') <= ord(s) <= ord('힣'):  # 44032 <= ord(s) <= 55203
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
                continue
            jong = jong_list[c]
            if jong in inv_double_consonants_dict:  # 자음 결합 여부 확인
                jong = jong.replace(jong, inv_double_consonants_dict[jong])
            result += jong

        elif ord('ㄱ') <= ord(s) <= ord('ㅣ'):  # 12593 <= ord(s) <= 12643
            if s in inv_double_vowels_dict:  # 모음 결합 여부 확인
                s = s.replace(s, inv_double_vowels_dict[s])
            elif s in inv_double_consonants_dict:  # 자음 결합 여부 확인
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
        self.state = 1

    def B1C(self, state):
        if not self.string:
            return 0
        else:
            self.temp += self.string.pop(0)
            return state

    def end(self):
        self.state = 1
        self.result += combination(self.temp[:-1])
        self.temp = self.temp[-1]

    def state1(self):
        if self.temp[0] in cho_list:
            self.state = self.B1C(4)
        else:
            self.state = 2

    def state2(self):
        if self.temp[0] in jung_list:
            self.state = self.B1C(3)
        else:  # single end
            self.result += self.temp
            self.temp = ""
            self.state = self.B1C(1)

    def state3(self):
        if self.temp in double_vowels_dict:
            self.temp = double_vowels_dict[self.temp]
            self.result += self.temp  # single end
            self.temp = ""
            self.state = self.B1C(1)
        else:
            self.end()

    def state4(self):
        if self.temp[1] in jung_list:
            self.state = self.B1C(5)
        else:
            self.state = 6

    def state5(self):
        if self.temp[1:3] in double_vowels_dict:
            self.temp = self.temp.replace(self.temp[1:3], double_vowels_dict[self.temp[1:3]])
            self.state = self.B1C(8)
        else:
            self.state = 8

    def state6(self):
        if self.temp in double_consonants_dict:
            self.temp = double_consonants_dict[self.temp]
            self.state = self.B1C(7)
        else:
            self.end()

    def state7(self):
        if self.temp[1] in jung_list:
            # 이중자음 분리
            self.temp = self.temp.replace(self.temp[-2], inv_double_consonants_dict[self.temp[-2]])
            self.result += self.temp[0]  # partial end
            self.temp = self.temp[1:]
            self.state = self.B1C(5)
        else:
            self.end()

    def state8(self):
        if self.temp[2] in jong_list and self.temp[2] != ' ':
            self.state = self.B1C(9)
        else:
            self.end()

    def state9(self):
        if self.temp[2:4] in double_consonants_dict:
            self.temp = self.temp.replace(self.temp[2:4], double_consonants_dict[self.temp[2:4]])
            self.state = self.B1C(10)
        else:
            self.state = 10

    def state10(self):
        if self.temp[-1] in jung_list:
            if self.temp[-2] in inv_double_consonants_dict:
                # 이중자음 분리
                self.temp = self.temp.replace(self.temp[-2], inv_double_consonants_dict[self.temp[-2]])
            self.result += combination(self.temp[:-2])  # partial end
            self.temp = self.temp[-2:]
            self.state = self.B1C(5)
        else:
            self.end()

    states = [None, state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]


def assemble(string):  # 분해된 한글을 조합
    out = Assembler(string)
    while out.state:
        # print(f"{out.state}, result: {out.result}, temp: {out.temp}")  # for debug
        Assembler.states[out.state](out)

    if out.temp:
        out.result += combination(out.temp)

    return out.result


if __name__ == "__main__":
    data = disassemble(input(">>> "))
    print("Disassembled:", data)
    print("Assembled:", assemble(list(data)))
