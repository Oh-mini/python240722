# db2.py

import sqlite3

#연결객체(파일에 저장)
con = sqlite3.connect(r"c:\work\sample.db")
#커서객체
cur = con.cursor()
#테이블 구조 생성(테이블 스키마)
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")
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

#완료
con.commit()

#선택 블럭 주석 : ctrl + /
# for row in cur:
#     print(row)

