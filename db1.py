# db1.py

import sqlite3

#연결객체(일단 메모리에서 작업)
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성(테이블 스키마)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name,phoneNumber))
#여러건 입력
datalist = (("전우치", "010-123"),("박문수","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색결과
cur.execute("select * from PhoneBook;")

print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())


#선택 블럭 주석 : ctrl + /
# for row in cur:
#     print(row)

