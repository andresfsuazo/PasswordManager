from PM.PMClient.user_interface import UserInterface
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


class GUI(UserInterface):

    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.Auth = QtWidgets.QWidget()
        self.Home = QtWidgets.QWidget()
        self.popup = QtWidgets.QMessageBox()
        self.accountNameTitle = QtWidgets.QLabel(self.Home)
        self.usernameInput = QtWidgets.QLineEdit(self.Auth)
        self.passwordInput = QtWidgets.QLineEdit(self.Auth)
        self.loginButton = QtWidgets.QPushButton(self.Auth)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Home)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Home)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.getCredentialsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getUsernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.getPasswordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.addCredentialsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addUsernameInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.addPasswordInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.newAccountButton = QtWidgets.QPushButton(self.Auth)
        self.comboBox = QtWidgets.QComboBox(self.Home)

    def setup_UI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.popup.setWindowTitle("Alert")
        # -------------------------------------------------------------------------
        MainWindow.resize(671, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # -------------------------------------------------------------------------
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 9, 661, 391))
        self.stackedWidget.setObjectName("stackedWidget")
        # -------------------------------------------------------------------------
        self.Auth.setObjectName("Auth")
        # -------------------------------------------------------------------------
        self.titleLabel = QtWidgets.QLabel(self.Auth)
        self.titleLabel.setGeometry(QtCore.QRect(189, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        # -------------------------------------------------------------------------
        # Username and Password Inputs
        self.loginButton.setGeometry(QtCore.QRect(230, 220, 221, 61))
        self.loginButton.clicked.connect(self.login)
        self.loginButton.setObjectName("loginButton")
        # -------------------------------------------------------------------------
        self.newAccountButton.setGeometry(QtCore.QRect(280, 300, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newAccountButton.setFont(font)
        self.newAccountButton.clicked.connect(self.create_account)
        self.newAccountButton.setObjectName("newAccountButton")
        # -------------------------------------------------------------------------
        self.usernameInput.setGeometry(QtCore.QRect(290, 120, 191, 30))
        self.usernameInput.setObjectName("usernameInput")
        # -------------------------------------------------------------------------
        self.passwordInput.setGeometry(QtCore.QRect(290, 160, 191, 30))
        self.passwordInput.setObjectName("passwordInput")
        # -------------------------------------------------------------------------
        self.label = QtWidgets.QLabel(self.Auth)
        self.label.setGeometry(QtCore.QRect(180, 120, 101, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # -------------------------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.Auth)
        self.label_2.setGeometry(QtCore.QRect(180, 160, 111, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # -------------------------------------------------------------------------
        self.stackedWidget.addWidget(self.Auth)
        self.Home.setObjectName("Home")
        # -------------------------------------------------------------------------
        # User Account Name
        self.accountNameTitle.setGeometry(QtCore.QRect(200, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.accountNameTitle.setFont(font)
        self.accountNameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.accountNameTitle.setObjectName("accountNameTitle")
        # -------------------------------------------------------------------------
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 180, 251, 204))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # -------------------------------------------------------------------------
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getCredentialsButton.setObjectName("getCredentialsButton")
        self.getCredentialsButton.clicked.connect(self.get_account)
        # -------------------------------------------------------------------------
        self.verticalLayout.addWidget(self.getCredentialsButton)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.getUsernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.getUsernameLabel.setObjectName("getUsernameLabel")
        self.verticalLayout.addWidget(self.getUsernameLabel)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.getPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.getPasswordLabel.setObjectName("getPasswordLabel")
        self.verticalLayout.addWidget(self.getPasswordLabel)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 180, 251, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addCredentialsButton.setObjectName("addCredentialsButton")
        self.addCredentialsButton.clicked.connect(self.add_account)
        self.verticalLayout_3.addWidget(self.addCredentialsButton)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.addUsernameInput.setObjectName("addUsernameInput")
        self.verticalLayout_3.addWidget(self.addUsernameInput)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.addPasswordInput.setObjectName("addPasswordInput")
        self.verticalLayout_3.addWidget(self.addPasswordInput)
        self.label_9 = QtWidgets.QLabel(self.Home)
        self.label_9.setGeometry(QtCore.QRect(300, 70, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        # -------------------------------------------------------------------------
        self.comboBox.setGeometry(QtCore.QRect(140, 100, 381, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        # -------------------------------------------------------------------------
        self.stackedWidget.addWidget(self.Home)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslate_UI(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_UI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.newAccountButton.setText(_translate("MainWindow", "Create Account"))
        self.titleLabel.setText(_translate("MainWindow", "Password Manager"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.accountNameTitle.setText(_translate("MainWindow", "Password Manager"))
        self.getCredentialsButton.setText(_translate("MainWindow", "Get Credentials"))
        self.label_7.setText(_translate("MainWindow", "Username"))
        self.getUsernameLabel.setText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.getPasswordLabel.setText(_translate("MainWindow", "..."))
        self.addCredentialsButton.setText(_translate("MainWindow", "Add credentials"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_9.setText(_translate("MainWindow", "Account Name"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def display_alert(self, text, type="warning"):
        self.popup.setText(text)
        self.popup.setGeometry(self.get_window_center()[0], self.get_window_center()[1], 100, 100)
        if type == "warning":
            self.popup.setIcon(QMessageBox.Warning)
        elif type == "success":
            self.popup.setIcon(QMessageBox.Information)
        self.popup.exec_()

    def display_menu(self):
        self.setup_UI(self.window)
        self.window.show()
        sys.exit(self.app.exec_())

    def get_window_center(self):
        """Get windows position and dimensions"""
        w = self.window.frameGeometry().width()
        h = self.window.frameGeometry().height()
        x,y = self.window.pos().x() + w/2, self.window.pos().y() + h/2

        return (x,y)

    def change_window(self, win_num):
        self.stackedWidget.setCurrentIndex(win_num)

    def login(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        args = {"user": self.username, "pwd": self.password}
        logged_in = self.client.send_command("login", **args)

        # If login credential accepted go to home menu
        if logged_in:
            self.change_window(1)
            # User Account Name
            self.accountNameTitle.setText(self.username)
            self.Load_Accounts()
        else:
            # Create popup window woth alerts
            self.display_alert("Invalid Credentials!")

    def Load_Accounts(self):
        args = {"user": self.username}
        response = self.client.send_command("getall", **args)

        if response:
            response = response.split("|^|")
            # Insert result in labesls
            self.updateAccountList(response)
        else:
            print("No accounts found!")

    def create_account(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        args = {"user": self.username, "pwd": self.password}
        logged_in = self.client.send_command("new", **args)

        # If login credential accepted go to home menu
        if logged_in != "0":
            self.change_window(1)
        else:
            # Create popup window with alerts
            self.display_alert("Username unavailable")

    def get_account(self):
        account = str(self.comboBox.currentText())
        args = {"user": self.username, "pwd": self.password, "account": account}
        response = self.client.send_command("getsub", **args)

        if response:
            response = response.split("|^|")
            # Insert result in labesls
            self.getUsernameLabel.setText(response[0])
            self.getPasswordLabel.setText(response[1])
        else:
            # Popup window indicating account not founf
            self.display_alert("Account not found!")

    def add_account(self):
        validated = False
        account = str(self.comboBox.currentText())
        if account != "":
            args = {"user": self.username, "pwd": self.password, "account": account,
                    "usersub": self.addUsernameInput.text(),
                    "pwdsub": self.addPasswordInput.text()}
            validated = self.client.send_command("newsub", **args)

        if validated:
            # Popup indicating success
            self.display_alert("Credentials Saved!", "success")
            self.clear_labels()
        else:
            # Popup indicating failure
            self.display_alert("Account already exists!")

        # Clean all labels
        self.clear_labels()

    def clear_labels(self):
        self.getPasswordLabel.clear()
        self.getUsernameLabel.clear()
        self.addPasswordInput.clear()
        self.addUsernameInput.clear()

    def updateAccountList(self, items):
        self.comboBox.clear()
        self.comboBox.addItems(items)