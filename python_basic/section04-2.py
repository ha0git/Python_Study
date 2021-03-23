# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4)) # 9, 7, 0, 0


escape_str1 = "Do you have a \"big collection\""
print(escape_str1)  # Do you have a "big collection"

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)  # Tab     Tab     Tab

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

raw_s2 = r'\\a\\a'
print(raw_s2)

# 멀티 라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
# 'a'가 str_o4에 포함되어 있는가?
print('a' in str_o4)        # True
print('f' in str_o4)        # False
print('z' not in str_o4)    # True

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수

# a = "Niceman"
# b = "orange"

# # 소문자?
# print(a.islower())      # False
# # 끝나는 글자가 e?
# print(b.endswith('e'))  # True
# # 첫글자를 대문자로
# print(a.capitalize())   # Niceman
# # 글자 대체
# print(a.replace('nice', 'good'))    # goodman
# # 글자의 역순을 배열로
# print(list(reversed(b)))    # ['e', 'g', 'n', 'a', 'r', 'o']


# 문자열 슬라이싱

a = "niceman"
b = "orange"

print(a[0:3])       # nic
print(a[0:4])       # nice
print(a[0:len(a)])  # niceman
print(a[:4])        # nice
print(a[:])         # niceman

# index 0~4 문자를 2씩 띄어서 출력
print(b[0:4:2])     # oa
print(b[1:-2])      # ran
# 처음부터 끝까지 출력인데 index -1 부터
print(b[::-1])      # egnaro
