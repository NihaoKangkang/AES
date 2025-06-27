from algorithm import *
from algorithm.aes import *

if __name__ == "__main__":

    inputData = input('Input text,hex data or file location need to calculate aes(press ENTER to abort): ')
    inputKey = input(
        'Input 128/192/256 bits secret key in hex (like \'0123456789abcdef0123456789abcdef\', input nothing to abort): ')
    # 因为示例为16进制字符串，所以这边进行了byte流输出，实际输入应当为string
    # inputData = b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
    # inputData = "681edf34d206965e86b3e94f536e4246"
    # Same Key
    # inputData = './LICENSE'
    # inputData = 'nihao woshi wang'
    # inputKey = "2b7e151628aed2a6abf7158809cf4f3c"
    # inputKey = '8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
    # inputKey = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'
    # inputData = '3243f6a8885a308d313198a2e0370734'
    # inputData = '3925841d02dc09fbdc118597196a0b32'
    # print(aes_str_decode(inputData,inputKey).hex())
    # print(aes_encode(inputData, int(inputKey, 16), len(inputKey)).hex())
    # inputData = 'Hello, world~! I\'m Kyi Wong'
    # inputData = '11c7e6219e8ad5e29646dd1fae642b6ec426e9d001ba71cb67cedeae00cd2b0e'
    try:
        if inputData and len(inputKey) in [32, 48, 64]:
            encodeFlag = input("Do you want to encode(y)/decode(n) this data?(Y/n): ")
            if encodeFlag == 'y' or encodeFlag == 'Y' or encodeFlag == '':
                result = aes_encode(inputData, int(inputKey, 16), len(inputKey))
                print('AES encode result: ', result.hex() if isinstance(result, bytes) else result)
            else:
                print('AES decode result: ', aes_decode(inputData, int(inputKey, 16), len(inputKey)))
        else:
            print("Check input data.")
    except ValueError:
        print("Check input data.")
