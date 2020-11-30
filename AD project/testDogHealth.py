import unittest
import sys
from Dog_health import DogHealth
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QComboBox,
                             QTextEdit, QLineEdit, QGridLayout, QToolButton, QRadioButton)

app = QApplication(sys.argv)

class testDogHealth(unittest.TestCase):

    def setUp(self):
        self.g = DogHealth()

    def tearDown(self):
        pass

    def testInitUI(self):
        self.assertTrue(self.g.smallSize)
        self.assertEqual(self.g.foodKindEdit.currentText(), '1 (ANF 전연령 유기농 6Free 연어 애견사료)')
        self.assertEqual(self.g.gPerCup, self.g.gPerCupList[self.g.foodKindEdit.currentIndex()])
        self.g.bigSize.setChecked(True)
        self.assertFalse(self.g.smallSize.isChecked())
        self.assertTrue(self.g.bigSize.isChecked())

    def testGramDisplay(self):
        pass

    def testCalculate(self):
        self.g.submit.click()
        self.assertEqual(self.g.resultEdit.toPlainText(), '체중이 입력되지 않았습니다.')
        self.g.weightEdit.setText('2')
        self.g.submit.click()
        self.assertEqual(self.g.resultEdit.toPlainText(), '사료의 양이 입력되지 않았습니다.')
        self.g.foodAmountEdit.setText('60')
        self.g.submit.click()
        self.assertEqual(self.g.resultEdit.toPlainText(), '산책 시간이 입력되지 않았습니다.')
        self.g.walkingTimeEdit.setText('30')
        self.g.submit.click()
        self.assertNotEqual(self.g.resultEdit.toPlainText(), '체중이 입력되지 않았습니다.')
        self.assertNotEqual(self.g.resultEdit.toPlainText(), '사료의 양이 입력되지 않았습니다.')
        self.assertNotEqual(self.g.resultEdit.toPlainText(), '산책 시간이 입력되지 않았습니다.')

if __name__ == '__main__':
    unittest.main()
