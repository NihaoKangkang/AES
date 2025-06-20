# import algorithm.aes
# from algorithm import *


# a = b'\x123'
# # algorithm.aes.padding_zero(a)
# print(int.from_bytes(a))
# print([j for j in a])

b = 74
d = 75
print(b.to_bytes())
print(d.to_bytes())
c = b.to_bytes() + d.to_bytes()
print(c)
print(hex(int.from_bytes(c)))