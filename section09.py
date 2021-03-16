# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# **반드시 close 리소스 반환
f.close()

print("--------------------------")
print("--------------------------")

# 예제2
with open('./resource/review.txt', 'r') as f:
# f = open('./resource/review.txt', 'r')와 같지만 close()를 하지 않아도 된다.
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("--------------------------")
print("--------------------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("--------------------------")
print("--------------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 이미 위에서 불러왔기 때문에 '내용없음'
    print(">", content) 

print("--------------------------")
print("--------------------------")

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='###')
        line = f.readline()

print("--------------------------")
print("--------------------------")

# 예제6
with open('./resource/review.txt', 'r') as f:
    # 문장을 enter 기준으로 list로 반환
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end='***')

print("--------------------------")
print("--------------------------")
print()

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Niceman!\n')


# 예제2
with open('./resource/text1.txt','a') as f:
    f.write('Goodman!\n')


# 예제3
from random import randint

with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['Kim\n','Park\n',"Cho\n"]
    f.writelines(list)


# 예제5
with open('./resource/text4.txt','w') as f:
    # 콘솔에 찍히는 것이 아니라 연결된 파일에 찍힘
    print('Test Contents1!', file=f)
    print('Test Contents2!', file=f)
