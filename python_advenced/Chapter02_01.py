# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)

# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type => value
# 파이썬 => 일관성

# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
# x가 [0]이고, y는 [1]이라는걸 알아야 사용 가능하다. (단점)
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('EX1-1 -', line_leng1)


# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언 - 튜플의 성질 + 클래스와 비슷한 접근방식
Point = namedtuple('Point', 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX -2 -', line_leng2)
print('EX -3 -', line_leng1 == line_leng2)



# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # 튜플 중복 (Default = False)

# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)


# Dict to Unpacking
temp_dict = {'x' : 75, 'y': 55}


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20,40)
p3 = Point3(45, y=20)    # x,y를 선언해도 안해도 ok
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)


print('EX2-2 -', p1, p2, p3, p4, p5)

print()
print()


