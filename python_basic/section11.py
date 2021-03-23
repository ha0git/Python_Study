# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제 1
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    next(reader)    # 열 이름 생략가능 (header skip)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)



# 예제 2
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)    # 열 이름 생략가능 (header skip)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)



# 예제 3
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k,v in c.items:
            print(k, v)
        print('--------------')


# 예제 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    # 순회하여 list를 작성 => 순회하면서 조건을 걸어야 하거나 할 때 사용
    for v in w:
        wt.writerow(v)



# 예제 5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # 순회하지 않고 한 번에 list를 작성해준다.
    wt.writerows(w)


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용 (openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas


import pandas as pd
# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자 (생략할 row 번호)
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # (행, 열) (20, 7)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)