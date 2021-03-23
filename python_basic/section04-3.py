# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])  
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'h1')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)   # index 2 자리에 7을 입력
print(y)
y.remove(2)
y.remove(7)
print(y)    
y.pop()     # LIFO
print(y)
ex = [88,77]
# y.append(ex)
y.extend(ex)
print(y)

# 삭제 : del, remove, pop


# 튜플 (순서o, 중복o, 수정x, 삭제x)
# 수정을 하지 않는 중요 값을 저장할 때 사용

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])
print(c + d)
print(c * 3)
print()
print()
print()

# 튜플 함수

z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)   # z 안에 3이 있는가? True
print(z.index(5))   # 5의 인덱스는 몇인가? 0
print(z.count(1))   # 튜플 안에 1이 몇 개가 있는가? 2



