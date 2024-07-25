import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path

# DB 처리 클래스
class ProductDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self._connect_db()

    def _connect_db(self):
        if os.path.exists(self.db_name):
            self.con = sqlite3.connect(self.db_name)
        else:
            self.con = sqlite3.connect(self.db_name)
            self._create_table()

        self.cur = self.con.cursor()

    def _create_table(self):
        self.cur.execute(
            "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, product_id, name, price):
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, product_id))
        self.con.commit()

    def remove_product(self, product_id):
        self.cur.execute("DELETE FROM Products WHERE id=?;", (product_id,))
        self.con.commit()

    def get_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# GUI 클래스
class Window(QMainWindow, uic.loadUiType("ProductList3.ui")[0]):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.db = db
        
        # 초기값 셋팅
        self.id = 0
        self.name = ""
        self.price = 0
        
        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        
        # 시그널과 슬롯 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        
        # 버튼 시그널 연결
        self.btnAdd.clicked.connect(self.addProduct)
        self.btnUpdate.clicked.connect(self.updateProduct)
        self.btnDelete.clicked.connect(self.removeProduct)
        
        # 초기 데이터 로드
        self.getProduct()
        
    def addProduct(self):
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.add_product(self.name, self.price)
        self.getProduct()
        
    def updateProduct(self):
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.update_product(self.id, self.name, self.price)
        self.getProduct()
        
    def removeProduct(self):
        self.id = self.prodID.text()
        self.db.remove_product(self.id)
        self.getProduct()
        
    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.get_products()
        
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 데이터베이스 인스턴스를 생성한다.
    db = ProductDB("ProductList.db")
    
    # GUI 인스턴스를 생성한다.
    myWindow = Window(db)
    myWindow.show()
    
    app.exec_()
