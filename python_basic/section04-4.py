# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json과 비슷한 형태)
# 선언

a = {'name' : 'Kim', 'phone' : '010-0000-0000', 'birth' : 920819}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('address'))     #None
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,2,4]
a['rank2'] = (1,2,3)
print(a)

# key, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print(2 in b)
print('name2' not in a)


# 집합 (Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)    #[1, 4, 5, 6]
#형변환
t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합(intersection)
print(s1.intersection(s2))
print(s1 & s2)
#합집합(union)
print(s1 | s2)
print(s1.union(s2))
#차집합(difference)
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))