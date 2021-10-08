import KRtype as kt
import time


def Tprint(string):
    disassembled_string = kt.disassemble(string)
    for i in range(len(disassembled_string)):
        print("\r" + kt.assemble(list(disassembled_string[:i+1])), end="")
        time.sleep(0.2)


if __name__ == "__main__":
    input()
    Tprint("ㅘ! 'ㄲ', 'ㅠ', 'ㄺ'의 합성인 굴국(뀱) 먹으러 ㄱㄱ싱~")
    input()
