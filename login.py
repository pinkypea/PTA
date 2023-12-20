from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6 import uic
import sys

#Lớp chứa giao diện đăng nhập
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)

        #Bắt sự kiện click chuột vào nút login
        self.btnLogin.clicked.connect(self.check_login)

    def check_login(self):
        #Lấy thông tin email và mật khẩu từ người dùng
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        #Kiểm tra email và mật khẩu có được nhập hay không
        if not email:
            msg_box.setText("Vui lòng nhập email!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return

        #Kiểm tra email và mật khẩu có được nhập đúng hay không
        if email == "admin@example.com" and password == "admin":
            #Nếu đăng nhập thành công
            msg_box.setText("Đăng nhập thành công!")
            msg_box.exec()
            return
        else:
            #Nếu đăng nhập không thành công
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
            return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()

    #Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    app.exec()