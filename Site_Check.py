import sys
import httpx
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMainWindow
s = 302
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("site checker")
        button = QPushButton("Click me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
      response = httpx.get("https://yandex.com")
      k = s == response.status_code
      print("status code:", response.status_code, k)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
