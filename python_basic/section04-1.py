# 데이터 타입
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "kim",
    "age" : "25"
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 타입 출력
print(type(v_tuple))
print(type(v_float))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2) # 제곱
print(f3 + i2)  # 실수 + 정수 = 실수 (자동 캐스팅)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2) # 9.0 (실수)


# 형변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))   # (3+0j)
print(int(True))    # 1
print(int(False))   # 0
print(int('3'))     # 3 (int)
print(complex(False))   # 0j


# 단항 연산자
y = 100
y += 100
print(y)


# 수치 연산 함수

# 절대값
print(abs(-7))

# 몫, 나머지
n, m = divmod(100, 8)
print(n, m)     # 12, 4

import math

print(math.ceil(5.1))   # 올림
print(math.floor(3.874))# 내림