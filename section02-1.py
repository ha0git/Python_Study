# Section02-1
# 파이썬 기초 코등
# Print 구문의 이해

# 02. 파이썬 기초 코딩

# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python''')

# Separator 옵션 사용
print('T','E','S','T', sep='')          # TEST
print('2019','02','19', sep='-')        # 2019-02-19
print('niceman', 'google.com', sep='@') # niceman@google.com  
  
# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
print('testtest')   # end 옵션 없기 때문에 줄바꿈 일어남

# Welcome To the black parade piano notes
# testtest
# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
# You and Me

print('{0} and {1} and {0}'.format('You','Me'))
# You and Me and You

print("{a} and {b}".format(a='You',b='Me'))
# You and Me 

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('ha0', 7))

# number 자릿수 정하기
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))
# Test1: 776, Price: 6534.12

# Escape 코드
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백스페이스
\000 : 널 문자
"""

# Escape 예제
print("'you'")
print('\'you\'')
print('"you"')
print(""'you'"")
print('\\you\\\n')  # 줄바꿈
print('\t\t\ttest') # 들여쓰기

print("""you""") # error