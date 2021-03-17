# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크


# syntaxError : 잘못된 문법

# print('Test)

# if True
#     pass

# x => y

# NameError : 참조변수 없음

a = 10
b = 15

# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) # 없는 index 호출 => 예외 발생


# keyError

dic = {'name': 'Kim', 'Age': 33, 'city': 'Seoul'}

# print(dic['hobby'])
print(dic.get('hobby'))


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month())   # 없는 메소드


# ValueError : 참조 값이 없을 때 발생

x = [1, 5, 9]

# x.remove(10)
# x.index(10)


# FileNotFoundError

# f = open('test.txt', 'r')     # 존재하지 않는 파일 호출


# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)

# print(x + list(y))


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행



# 예제 1

name = ["kim",  'Lee', 'Park']

try:
    z = 'Kim'   # 'Cho' => 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z. x+1))
except ValueError:
    print('Not Found it! - Occurred ValueError!')
else:
    print('Ok! else!')



# 예제 2

try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z. x+1))
except:     # 에러 내용을 정확히 쓰지 않아도 가능.
    print('Not Found it! - Occurred ValueError!')
else:       # 성공했을 때만 실행
    print('Ok! else!')
finally:    # 무조건 실행
    print('finally ok!')


# 예제 3
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!')

# 예제 4
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z. x+1))
except ValueError as l:
    print('Not Found it! - ValueError!')
except IndexError:
    print('Not Found it! - IndexError!')
except Exception:
    print('Not Found it! - Occurred Error!')
else:       # 성공했을 때만 실행
    print('Ok! else!')
finally:    # 무조건 실행
    print('finally ok!')


# 예제 5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == "Kim":
        print('허가!')
    else:   # 작성자가 에러 종류를 직접 규정할 수 있음
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('ok!')