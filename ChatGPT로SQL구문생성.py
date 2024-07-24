import sqlite3
import random
import string

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        self.cursor.execute('''
            INSERT INTO electronics (product_name, price) VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        if product_name and price:
            self.cursor.execute('''
                UPDATE electronics SET product_name = ?, price = ? WHERE product_id = ?
            ''', (product_name, price, product_id))
        elif product_name:
            self.cursor.execute('''
                UPDATE electronics SET product_name = ? WHERE product_id = ?
            ''', (product_name, product_id))
        elif price:
            self.cursor.execute('''
                UPDATE electronics SET price = ? WHERE product_id = ?
            ''', (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM electronics WHERE product_id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''
            SELECT * FROM electronics WHERE product_id = ?
        ''', (product_id,))
        return self.cursor.fetchone()

    def select_all_products(self):
        self.cursor.execute('''
            SELECT * FROM electronics
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


# 샘플 데이터 생성 함수
def generate_sample_data():
    sample_data = []
    for _ in range(100):
        product_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        price = round(random.uniform(10.0, 1000.0), 2)
        sample_data.append((product_name, price))
    return sample_data


# 데이터베이스 초기화 및 샘플 데이터 삽입
db = ElectronicsDatabase()

sample_data = generate_sample_data()
for product_name, price in sample_data:
    db.insert_product(product_name, price)

# 테스트 코드
print(db.select_all_products())

db.update_product(1, product_name="UPDATED_PRODUCT", price=999.99)
print(db.select_product(1))

db.delete_product(2)
print(db.select_all_products())

db.close()
