# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재선언
class Student():
    """
    Student Class
    Author : Kim
    Date : 2021.03.26
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade ,details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)
    
    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


# Self 의미
studt1 = Student('Cho',2 ,3, {'gender': 'Male', 'score1' : 65,'score2':44})
studt2 = Student('Chang',4 ,1, {'gender': 'Female', 'score1' : 85,'score2':74})

print(id(studt1))
print(id(studt2))

print(studt1 == studt2)
print(studt1._name == studt2._name)
print(studt1 is studt2) # id값이 같냐고 묻는 것.

# ex
a = 'ABC'
b = a
# id값이 같은지?
print(a is b)

# 값이 같은지?
print(a == b)


# dir & dict 확인 (dir이 더 자세한 정보, 먼저 dict으로 검색 후 dir로 검색)
print(dir(studt1))
print(dir(studt2))

# 값까지 출력
print(studt1.__dict__)  
print(studt2.__dict__)


# Doctring (클래스의 주석을 확인)
print(Student.__doc__)

# 실행
studt1.detail_info()
studt2.detail_info()

# 에러
# Student.detail_info()

Student.detail_info(studt1)

# 비교
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) == id(studt2.__class__))


# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장x)

# studt1._name = 'Lee'

print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()

# 클래스 변수

# 접근
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)


print()
print()


# 공유 확인
print(Student.__dict__)
print(studt1.__dict__)
print(studt2.__dict__)

# 인스턴스 네임스페이스 없으면 자동으로 상위(클래스)에서 검색
# 즉, 동일한 이름으로 변수 생성(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del studt2
# 1
print(studt1.student_count) # 자동으로 상위에서 검색
print(Student.student_count)


