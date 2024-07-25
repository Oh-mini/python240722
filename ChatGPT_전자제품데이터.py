
import openpyxl
import random

# 새 워크북을 만들고 활성 워크시트를 선택합니다.
wb = openpyxl.Workbook()
ws = wb.active

# 헤더 행 설정
headers = ["제품 ID", "제품명", "수량", "가격"]
ws.append(headers)

# 샘플 제품명 리스트
product_names = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "헤드폰",
    "블루투스 스피커", "게임 콘솔", "스마트 TV", "카메라", "모니터",
    "프린터", "키보드", "마우스", "외장 하드 드라이브", "USB 플래시 드라이브",
    "라우터", "드론", "스마트 홈 허브", "피트니스 트래커", "전동 스쿠터"
]

# 100개의 제품 데이터를 생성합니다.
for i in range(1, 101):
    product_id = f"P{i:03d}"  # 제품 ID를 P001, P002 등의 형식으로 생성
    product_name = random.choice(product_names)
    quantity = random.randint(1, 100)
    price = round(random.uniform(50, 1000), 2)  # 50에서 1000 사이의 무작위 가격 (소수점 2자리)
    ws.append([product_id, product_name, quantity, price])

# 워크북을 파일로 저장합니다.
wb.save("products.xlsx")

print("products.xlsx 파일이 성공적으로 생성되었습니다.")