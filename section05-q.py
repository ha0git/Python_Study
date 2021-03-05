# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for s in q1:
     if s == '가을':
        print(q1[s])

# join을 왜 쓴건지 모르겠다..
print(''.join([q1[s] for s in q1 if s == '가을']))

print()
print()


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for q in q2.values():
    if q == '사과':
        print(True)


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

s3 = 55

if s3 > 80 :
    print("A학점")
elif s3 > 60 :
    print("B학점")
elif s3 > 40 :
    print("C학점")
elif s3 > 20 :
    print("D학점")
elif s3 >= 0 :
    print("E학점")
else:
    print("과락")


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
best = 0

best = a
if b > a:
    best = b
elif c > b:
    best = c

print(best)



# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
i = '920819-1234567'

if int(i[7]) % 2 == 0:
    print("여자")
else:
    print("남자")



# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
q3.remove("정")
print(q3)


print(''.join([s for s in q3 if s != '정']))


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

# for문의 s는 int형이 아닌가..?
print(''.join([str(s) for s in range(1,100) if int(s) % 2 == 1 ]))


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for q in q4:
    if len(q) >= 5 :
        print(q)


# 한 줄로 작성
print([q for q in q4 if len(q) >= 5])



# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print([q for q in q5 if q.islower()])


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for q in q6:
    if q.islower():
        q.upper()
    else:
        q.lower()

print(q6)

print([s.upper() if s.islower() else s.lower() for s in q5])
