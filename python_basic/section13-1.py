# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

# 사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime

# DB 생성 & Auto Commit
# 본인 db 경로
conn = sqlite3.connect('./resource/record.db', isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)')

words = []  # 영어 단어 리스트(1000개 로드)

n = 1
cor_cnt = 0

with open('./resource/word.txt','r') as f:
    for c in f:
        words.append(c.strip())     # 양쪽 공백 제거
    # print(words)

    a = input("Ready? Press Enter Key!")    # Enter Game Start!
    print(a)
    start = time.time() # 시작시간 기록

    while n <= 5 :
        random.shuffle(words)   # words 섞기
        q = random.choice(words)# 한 단어 뽑기

        print()

        print("Question # {}".format(n))
        print(q)

        x = input() # 타이핑 입력

        print()

        if str(q).strip() == str(x).strip():
            print("Pass!")
            # 정답 소리 재생
            winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
            cor_cnt += 1
        else:
            print("Wrong!")
            # 오답 소리 재생
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        n += 1  # 다음 문제 전환
    
end = time.time()   # End Time
et = end - start    # 총 게임시간
et = format(et, ".3f")  # 소수 3자리 출력

if cor_cnt >= 3:
    print('합격!')
else:
    print('불합격!')


# 기록 DB 삽입
# cursor.execute("INSERT INTO records('cor_cnt','record','regdate') VALUES(?,?,?)",(cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%D %H:%M:%S'))

# 수행 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))


# 시작 지점
if __name__ == '__main__':
    pass