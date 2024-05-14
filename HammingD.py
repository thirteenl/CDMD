# 计算汉明距离
import time
def hmddistance(hash1, hash2):
    num = 0
    assert len(hash1) == len(hash2)
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            num += 1
    return num

hash1='1110001110000100100101000000100011000000011110001010000110001100'
hash2='1110001110000100100101000000100011000000011110001010000110001100'
S_time=time.time()
print(hmddistance(hash1,hash2))
time.sleep(0.1)
E_time=time.time()
print(E_time-S_time)