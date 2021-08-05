import KRENtype as kt
import time


def Tprint(string):
    disassembled_string = kt.disassemble(string)
    for i in range(len(disassembled_string)):
        print("\r" + kt.assemble(disassembled_string[:i+1]), end="")
        time.sleep(0.1)


if __name__ == "__main__":
    Tprint("왜 'ㄱ'왕밤빵을 밟고 갑니까?")
