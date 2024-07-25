# DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#폼 클래스 정의 (다중 상속)
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모")

#해당 모듈을 직접 실행했는지 여부를 체크
#JAVA, c언어 main()함수가 진입점(Entry point)
if __name__ == "__main__":
    #실행프로세스 생성
    app = QApplication(sys.argv)
    #인스턴스 생성
    demoForm = DemoForm()
    #화면 보여주기
    demoForm.show()
    #이벤트 처리 대기
    app.exec_()
