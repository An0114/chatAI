# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtCore import Qt
from PySide6.QtGui import (QFont, QIcon,
                           QKeyEvent)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QPushButton,
                               QTextBrowser, QTextEdit, QWidget, QMainWindow)

import client
from chatAI.serve.server import start_server
import time
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(470, 450)
        Form.setMinimumSize(QSize(470, 450))
        Form.setMaximumSize(QSize(470, 450))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioCard))
        Form.setWindowIcon(icon)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 0, 480, 460))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.msframe = QFrame(self.widget)
        self.msframe.setObjectName(u"msframe")
        self.msframe.setMinimumSize(QSize(471, 261))
        self.msframe.setMaximumSize(QSize(471, 261))
        self.msframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.msframe.setFrameShadow(QFrame.Shadow.Raised)
        self.getmessage = QTextBrowser(self.msframe)
        self.getmessage.setObjectName(u"getmessage")
        self.getmessage.setGeometry(QRect(10, 11, 451, 241))
        self.getmessage.setMinimumSize(QSize(451, 241))
        self.getmessage.setMaximumSize(QSize(451, 241))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.msframe)

        self.messageframe = QFrame(self.widget)
        self.messageframe.setObjectName(u"messageframe")
        self.messageframe.setMinimumSize(QSize(381, 191))
        self.messageframe.setMaximumSize(QSize(381, 191))
        self.messageframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.messageframe.setFrameShadow(QFrame.Shadow.Raised)
        self.messageEdit = QTextEdit(self.messageframe)
        self.messageEdit.setObjectName(u"messageEdit")
        self.messageEdit.setGeometry(QRect(10, 10, 361, 171))
        self.messageEdit.setMinimumSize(QSize(361, 171))
        self.messageEdit.setMaximumSize(QSize(361, 171))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.messageframe)

        self.puframe = QFrame(self.widget)
        self.puframe.setObjectName(u"puframe")
        self.puframe.setMinimumSize(QSize(91, 191))
        self.puframe.setMaximumSize(QSize(91, 191))
        self.puframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.puframe.setFrameShadow(QFrame.Shadow.Raised)
        self.pubtn = QPushButton(self.puframe)
        self.pubtn.setObjectName(u"pubtn")
        self.pubtn.setGeometry(QRect(10, 10, 71, 171))
        self.pubtn.setMinimumSize(QSize(71, 171))
        self.pubtn.setMaximumSize(QSize(71, 171))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pubtn.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.puframe)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"chatAI", None))
        self.pubtn.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
    # retranslateUi

class chat_ui(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # start_serve()

        # 对按键进行事件绑定
        self.pubtn.clicked.connect(self.show_msg)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Qt.Key_Return:
            self.show_msg()

    def show_msg(self):
        msg = self.messageEdit.toPlainText().strip()
        msg = 'user:' + msg
        self.getmessage.append(msg)
        self.messageEdit.clear()
        rev_msg = client.run_client(msg)

        if rev_msg:
            self.getmessage.append(rev_msg)
        else:
            self.messageEdit.clear()


def start_app():
    app = QApplication(sys.argv)
    window = chat_ui()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server, daemon=True)
    chat_thead = threading.Thread(target=start_app)
    server_thread.start()
    chat_thead.start()
    server_thread.join()









