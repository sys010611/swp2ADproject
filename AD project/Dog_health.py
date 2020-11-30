import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QComboBox,
                             QTextEdit, QLineEdit, QGridLayout, QToolButton, QRadioButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class DogHealth(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # widgets
        weight = QLabel('체중:')
        self.weightEdit = QLineEdit()
        self.weightEdit.setAlignment(Qt.AlignRight)
        kg = QLabel('kg')
        size = QLabel("크기:")
        self.smallSize = QRadioButton('소형', self)
        self.smallSize.setChecked(True)
        self.mediumSize = QRadioButton('중형', self)
        self.bigSize = QRadioButton('대형', self)
        foodKind = QLabel("사료 종류:")
        self.foodKindEdit = QComboBox()
        self.foodKindEdit.addItems(['1 (ANF 전연령 유기농 6Free 연어 애견사료)',
                                    '2 (탐사 6free 애완견 사료 연어 레시피)',
                                    '3 (나우프레쉬 그레인프리 스몰브리드 어덜트 사료)',
                                    '4 (탐사 유기농 6free 전연령 애완견사료, 연어)',
                                    '5 (닥터독 3개월 이상 연어 피부모질 닥터독 사료)'])
        foodCalorie = QLabel('사료 kg당 kcal 직접 입력: ')
        self.foodCalorieEdit = QLineEdit()
        self.foodCalorieEdit.setAlignment(Qt.AlignRight)
        kcal = QLabel("kcal")
        self.gPerCupList = [75, 80, 90, 80, 80]
        self.gPerCup = self.gPerCupList[self.foodKindEdit.currentIndex()]
        self.gPerCupLabel = QLabel('      (종이컵 1컵: ' + str(self.gPerCup) + 'g)')
        font = self.gPerCupLabel.font() #폰트 설정
        font.setPointSize(12)
        self.gPerCupLabel.setFont(font)

        self.foodKindEdit.activated[str].connect(self.gramDisplay)  # 사료를 선택할 때마다 1컵당 g 표시 변화

        foodAmount = QLabel("하루 사료 섭취량:")
        self.foodAmountEdit = QLineEdit()
        self.foodAmountEdit.setAlignment(Qt.AlignRight)
        g = QLabel('g')
        walkingTime = QLabel("하루 산책 시간:")
        self.walkingTimeEdit = QLineEdit()
        self.walkingTimeEdit.setAlignment(Qt.AlignRight)
        minute = QLabel('분')
        result = QLabel("칼로리 측정 결과:")
        self.resultEdit = QTextEdit()
        self.submit = QToolButton()
        self.submit.setText('Submit')
        self.submit.setFixedSize(200, 50)
        self.submit.clicked.connect(self.calculate)

        picture1 = QLabel()
        picture1.setPixmap(QPixmap('/home/seop/바탕화면/1.jpg'))
        picture2 = QLabel()
        picture2.setPixmap(QPixmap('/home/seop/바탕화면/2.jpg'))
        picture3 = QLabel()
        picture3.setPixmap(QPixmap('/home/seop/바탕화면/3.jpg'))
        picture4 = QLabel()
        picture4.setPixmap(QPixmap('/home/seop/바탕화면/4.jpg'))
        picture5 = QLabel()
        picture5.setPixmap(QPixmap('/home/seop/바탕화면/5.jpg'))

        # layout
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(weight, 0, 0)
        self.grid.addWidget(self.weightEdit, 0, 1, 1, 4)
        self.grid.addWidget(kg, 0, 5)
        self.grid.addWidget(size, 1, 0)
        self.grid.addWidget(self.smallSize, 1, 1)
        self.grid.addWidget(self.mediumSize, 1, 2)
        self.grid.addWidget(self.bigSize, 1, 3)
        self.grid.addWidget(picture1, 2, 1)
        self.grid.addWidget(picture2, 2, 2)
        self.grid.addWidget(picture3, 2, 3)
        self.grid.addWidget(picture4, 2, 4)
        self.grid.addWidget(picture5, 2, 5)
        self.grid.addWidget(foodKind, 3, 0)
        self.grid.addWidget(self.foodKindEdit, 3, 1, 1, 4)
        self.grid.addWidget(foodCalorie, 4, 0)
        self.grid.addWidget(self.foodCalorieEdit, 4, 1, 1, 4)
        self.grid.addWidget(kcal, 4, 5)
        self.grid.addWidget(self.gPerCupLabel, 5, 5)
        self.grid.addWidget(foodAmount, 5, 0)
        self.grid.addWidget(self.foodAmountEdit, 5, 1, 1, 4)
        self.grid.addWidget(g, 5, 5)
        self.grid.addWidget(walkingTime, 6, 0)
        self.grid.addWidget(self.walkingTimeEdit, 6, 1, 1, 3)
        self.grid.addWidget(minute, 6, 4)
        self.grid.addWidget(self.submit, 6, 5)
        self.grid.addWidget(result, 7, 0)
        self.grid.addWidget(self.resultEdit, 8, 0, 1, 6)

        self.setLayout(self.grid)
        self.setGeometry(300, 100, 500, 800)
        self.setWindowTitle("애완견 건강관리 프로그램")
        self.show()

    def gramDisplay(self):
        self.gPerCupLabel.deleteLater()
        self.gPerCup = self.gPerCupList[self.foodKindEdit.currentIndex()]
        self.gPerCupLabel = QLabel('      (종이컵 1컵: ' + str(self.gPerCup) + 'g)')
        font = self.gPerCupLabel.font()  # 폰트 설정
        font.setPointSize(12)
        self.gPerCupLabel.setFont(font)
        self.grid.addWidget(self.gPerCupLabel, 5, 5)

    def calculate(self):
        if self.weightEdit.text() == '':
            self.resultEdit.setText('체중이 입력되지 않았습니다.')
            return
        if self.foodAmountEdit.text() == '':
            self.resultEdit.setText('사료의 양이 입력되지 않았습니다.')
            return
        if self.walkingTimeEdit.text() == '':
            self.resultEdit.setText('산책 시간이 입력되지 않았습니다.')
            return
        calories = [3.577, 3.5, 3.733, 3.5, 4.2]
        calorie = calories[self.foodKindEdit.currentIndex()]
        if self.foodCalorieEdit.text() != '':
            calorie = float(self.foodCalorieEdit.text()) / 1000
        calorieGain = round(calorie * float(self.foodAmountEdit.text()))
        calorieLoss = round(1.78 * float(self.weightEdit.text()) * 1 / 15 * float(self.walkingTimeEdit.text()))
        basicCalorieLoss = round(110 * float(self.weightEdit.text()) ** 0.75)
        totalCalorie = calorieGain - calorieLoss - basicCalorieLoss
        resultText = '섭취 칼로리: '+ str(calorieGain) + '\n산책에 의한 소모 칼로리: '+ str(calorieLoss) +\
                     '\n기초 대사에 의한 소모 칼로리: ' + str(basicCalorieLoss) + '\n최종 칼로리: '+ str(totalCalorie)
        self.resultEdit.setText(str(resultText))
        if totalCalorie > calorieGain*0.25:
            self.resultEdit.append('칼로리 과잉입니다.')
            if self.smallSize.isChecked() and int(self.walkingTimeEdit.text()) < 15:
                self.resultEdit.append('산책 시간을 더 늘리기를 권장합니다.')
            elif self.mediumSize.isChecked() and int(self.walkingTimeEdit.text()) < 40:
                self.resultEdit.append('산책 시간을 더 늘리기를 권장합니다.')
            elif self.bigSize.isChecked() and int(self.walkingTimeEdit.text()) < 90:
                self.resultEdit.append('산책 시간을 더 늘리기를 권장합니다.')
            else:
                self.resultEdit.append('사료의 양을 줄이기를 권장합니다.')
        elif totalCalorie < -calorieGain*0.25:
            self.resultEdit.append('칼로리 부족입니다.')
            if self.smallSize.isChecked() and int(self.walkingTimeEdit.text()) > 45:
                self.resultEdit.append('산책 시간을 조금 줄이기를 권장합니다.')
            elif self.mediumSize.isChecked() and int(self.walkingTimeEdit.text()) > 80:
                self.resultEdit.append('산책 시간을 조금 줄이기를 권장합니다.')
            elif self.bigSize.isChecked() and int(self.walkingTimeEdit.text()) > 150:
                self.resultEdit.append('산책 시간을 조금 줄이기를 권장합니다.')
            else:
                self.resultEdit.append('사료의 양을 조금 늘리기를 권장합니다.')
        else:
            self.resultEdit.append('건강 상태가 좋습니다.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DogHealth()
    sys.exit(app.exec_())
