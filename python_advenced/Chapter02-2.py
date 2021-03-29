# Chapter02-2
# 파이썬 심화
# Special  Method(Magic Method)

# 매직 메소드 실습

# 매직메소드 기초 설명

# 기본형

print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n = 100
# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n)) # True, True
print('EX1-5 -', n * 100, n.__mul__(100))

print()
print()

