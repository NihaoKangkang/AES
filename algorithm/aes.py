from os.path import isfile

S_box = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
         0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
         0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
         0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
         0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
         0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
         0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
         0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
         0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
         0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
         0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
         0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
         0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
         0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
         0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
         0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
RS_box = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
          0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
          0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
          0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
          0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
          0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
          0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
          0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
          0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
          0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
          0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
          0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
          0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
          0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
          0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
          0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
shift_rows_list = [1, 6, 11, 16,
                   5, 10, 15 ,4,
                   9, 14, 3, 8,
                   13, 2, 7, 12]
shift_rows_list_r = [1, 14, 11, 8,
                     5, 2, 15, 12,
                     9, 6, 3, 16,
                     13, 10, 7, 4]
mix_array = [0x02, 0x03, 0x01, 0x01,
             0x01, 0x02, 0x03, 0x01,
             0x01, 0x01, 0x02, 0x03,
             0x03, 0x01, 0x01, 0x02]
mix_array_r = [0x0e, 0x0b, 0x0d, 0x09,
               0x09, 0x0e, 0x0b, 0x0d,
               0x0d, 0x09, 0x0e, 0x0b,
               0x0b, 0x0d, 0x09, 0x0e]
Rcon = [0x01, 0x02, 0x04, 0x08, 0x10,
        0x20, 0x40, 0x80, 0x1b, 0x36,
        0x6c, 0xd8, 0xab, 0x4d, 0x9a]


# 字节代换
# 输入 data: bytes table:int list
# 输出 bytes
def subBytes(data, table):
    sub_bytes = b''
    # 是否需要table[int(j)]?!
    sub_bytes += b''.join([table[j].to_bytes(1, 'big') for j in data])
    return sub_bytes


# input: data: byte string; table:int list
# output: permute_result: byte string
def shift_rows(data, table):
    # 注意：table 中的数字从 1 开始计数，而 Python 索引从 0 开始
    permute_result = b''
    permute_result += b''.join([data[j - 1 : j] for j in table])
    return permute_result

# input: a: int; b: byte
# output: int
def galois_multiplication(a, b):
    # print(a, hex(int.from_bytes(b)))
    multi_result = 0
    # print(f"mix_array: {a}, shift_rows: {b}")
    b = int.from_bytes(b)
    while a:
        if a & 0x01:
            multi_result ^= b
            # print('b: ',b)
            # print(multi_result)
        a >>= 1
        # 如果最高位是1
        if b & 0x80:
            b <<= 1
            b &= 0xff
            b ^= 0x1b
        else:
            b <<= 1
            b &= 0xff
    return multi_result


# input: data: byte string; table:int list
# output: bytes
def mix_columns(data, table):
    mix_result = b''
    # for column in range(0, 4):
    #     for row in range(0, 4):
    # print(hex(int.from_bytes(data)))
    # aes数据块排序，先列后行
    for column in range(0, 4):
        for row in range(0, 4):
            temp_result = (galois_multiplication(table[row * 4 + 0], data[0 + column * 4 : 1 + column * 4]) ^
                           galois_multiplication(table[row * 4 + 1], data[1 + column * 4 : 2 + column * 4]) ^
                           galois_multiplication(table[row * 4 + 2], data[2 + column * 4 : 3 + column * 4]) ^
                           galois_multiplication(table[row * 4 + 3], data[3 + column * 4 : 4 + column * 4]))
            # print(hex(temp_result))
            # print(format(temp_result, f'02x'))
            mix_result += bytes.fromhex(format(temp_result, f'02x'))
    return mix_result


# input: data : byte
# output: data : byte
def padding_zero(data):
    if len(data) % 16 != 0:
        data += b'\x00' * (16 - len(data) % 16)
    return data


def remove_padding_zeros(data):
    length = len(data)
    while length > 0 and data[length - 1] == 0x00:
        length -= 1
    return data[:length]


def G(w: int, i):
    w = format(w, f"032b")
    # 字循环
    w_list = [int(w[8:16], 2), int(w[16:24], 2), int(w[24:], 2), int(w[:8], 2)]
    # 字节替换
    w_subBytes = int.from_bytes(subBytes(w_list, S_box))
    # 轮常量异或(与第一个字节进行异或)
    w_xor = w_subBytes ^ (Rcon[i] << 24)
    return w_xor


# input: key: int
# output: rk: int list
# 以AES128为例，要将初始密钥设置为rk[0]
def rk_generator(key, length_of_key):
    # 计算密钥长度 单位：bit 128/192/256
    length_of_key = (length_of_key // 2) * 8
    # 将key转化为2进制
    key = format(key, f'0{length_of_key}b')
    # 计算需要加密轮数
    Nk = length_of_key // 32
    Nr = {128: 10, 192:12, 256: 14}[length_of_key]
    # 将密钥按列导入W数组，每组32bit = 4byte = 1word.
    W = [int(key[i: i + 32], 2) for i in range(0, length_of_key, 32)]
    # 密钥扩展
    for i in range(len(W), (Nr + 1) * 4):
        if i % Nk == 0:
            W.append(W[i - Nk] ^ G(W[i - 1], i // Nk - 1))
        elif Nk > 6 and i % 4 == 0:
            W.append(W[i - Nk] ^
                     int.from_bytes(subBytes(W[i - 1].to_bytes(4, 'big'), S_box)))
        else:
            W.append(W[i - Nk] ^ W[i - 1])
    # 将密钥填充到rk中
    rk = []
    # print(len(W))
    for i in range(0, len(W), 4):
        rk.append(int.from_bytes(W[i].to_bytes(4, 'big') +
                                 W[i + 1].to_bytes(4, 'big') +
                                 W[i + 2].to_bytes(4, 'big') +
                                 W[i + 3].to_bytes(4, 'big'), 'big'))
    return rk, Nr


# AES 核心实现代码
# input: data : byte  rk: int list
# output: byte
# 待改进：AES 192/256 尚未实现
def data_encryption_standard(data, rk, Nr):
    blockNumber = len(data) // 16
    # print(blockNumber)

    result = b''
    for block in range(0, blockNumber):
        blockData = data[block * 16: (block + 1) * 16]
        # 初始变换
        # print(hex(int.from_bytes(blockData)))
        # print(hex(rk[0]))
        result_t = int.from_bytes(blockData) ^ rk[0]
        result_t = result_t.to_bytes(16, 'big')
        # print(hex(int.from_bytes(result_t)))
        # 前n-1循环运算
        for i in range(1, Nr):
            # 字节代换
            result_t = subBytes(result_t, S_box)
            # print(hex(int.from_bytes(result_t)))
            # 行移位
            result_t = shift_rows(result_t, shift_rows_list)
            # print(hex(int.from_bytes(result_t)))
            # 列混合
            result_t = mix_columns(result_t, mix_array)
            # print(':', hex(int.from_bytes(result_t)))
            # 轮密钥加
            result_t = int.from_bytes(result_t) ^ rk[i]
            result_t = result_t.to_bytes(16, 'big')
        # 最后一轮
        result_t = subBytes(result_t, S_box)
        result_t = shift_rows(result_t, shift_rows_list)
        result_t = int.from_bytes(result_t) ^ rk[Nr]
        result += result_t.to_bytes(16, 'big')
    return result


def data_decryption_standard(data, rk, Nr):
    blockNumber = len(data) // 16
    result = b''
    for block in range(0, blockNumber):
        blockData = data[block * 16: (block + 1) * 16]
        # 初始变换
        # print(hex(int.from_bytes(blockData)))
        # print(hex(rk[0]))
        result_t = int.from_bytes(blockData) ^ rk[0]
        result_t = result_t.to_bytes(16, 'big')
        # print(hex(int.from_bytes(result_t)))
        # 前n-1循环运算
        for i in range(1, Nr):
            # 行移位
            result_t = shift_rows(result_t, shift_rows_list_r)
            # print(hex(int.from_bytes(result_t)))
            # 字节代换
            result_t = subBytes(result_t, RS_box)
            # print(hex(int.from_bytes(result_t)))
            # 轮密钥加
            result_t = int.from_bytes(result_t) ^ rk[i]
            result_t = result_t.to_bytes(16, 'big')
            # 列混合
            result_t = mix_columns(result_t, mix_array_r)
            # print(':', hex(int.from_bytes(result_t)))
        # 最后一轮
        result_t = shift_rows(result_t, shift_rows_list_r)
        result_t = subBytes(result_t, RS_box)
        result_t = int.from_bytes(result_t) ^ rk[Nr]
        result += result_t.to_bytes(16, 'big')
    return result


def aes_str_encode(data, rk, Nr):
    # 测试，加密16进制数据，非字符串
    b_messages = padding_zero(bytes.fromhex(data))
    # b_messages = padding_zero(data.encode())
    return data_encryption_standard(b_messages, rk, Nr)


def aes_str_decode(data, rk, Nr):
    b_messages = bytes.fromhex(data)
    return remove_padding_zeros(data_decryption_standard(b_messages, rk, Nr))


# 输入：data：string or file location; key：int
# 输出: hex string
def aes_file_encode(filename, rk, Nr):
    # 文件读写部分
    file_count = 0
    c_fname = filename + '_encoded' + format(file_count, '02d')
    while isfile(c_fname):
        file_count += 1
        c_fname = filename + '_encoded' + format(file_count, '02d')
    # 加密后文件名c_fname
    with open(filename, 'rb') as text_file:
        byte_file = text_file.read()
    byte_file = padding_zero(byte_file)
    encodeMessage = data_encryption_standard(byte_file, rk, Nr)
    with open(c_fname, 'wb') as out_file:
        out_file.write(encodeMessage)
    return c_fname


# 输入: data: hex string; key: int
# 输出： byte string or file
def aes_file_decode(filename, rk, Nr):

    # 文件读写部分
    file_count = 0
    c_fname = filename + '_decoded' + format(file_count, '02d')
    while isfile(c_fname):
        file_count += 1
        c_fname = filename + '_decoded' + format(file_count, '02d')
    # 加密后文件名c_fname
    with open(filename, 'rb') as text_file:
        byte_file = text_file.read()
    decodeMessage = data_decryption_standard(byte_file, rk, Nr)
    with open(c_fname, 'wb') as out_file:
        out_file.write(remove_padding_zeros(decodeMessage))
    return c_fname



def aes_encode(data, key, length_of_key):
    rk, Nr = rk_generator(key, length_of_key)

    if isfile(data):
        file_location = aes_file_encode(data, rk, Nr)
        return f"File encode success! File location: {file_location}"
    else:
        return aes_str_encode(data, rk, Nr)


def aes_decode(data, key, length_of_key):
    rk, Nr = rk_generator(key, length_of_key)
    rk.reverse()
    if isfile(data):
        return aes_file_decode(data, rk, Nr)
    else:
        return aes_str_decode(data, rk, Nr)
