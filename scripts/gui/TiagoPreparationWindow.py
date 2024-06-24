# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TiagoPreparationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

PLAYCHESS_PKG_DIR = "/home/pal/tiago_public_ws/src/playchess"
GUI_SCRIPTS_DIR   = PLAYCHESS_PKG_DIR + "/scripts/gui"

class Ui_TiagoPreparation(object):
    def setupUi(self, TiagoPreparation):
        TiagoPreparation.setObjectName("TiagoPreparation")
        TiagoPreparation.resize(518, 354)
        self.verticalLayout = QtWidgets.QVBoxLayout(TiagoPreparation)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(TiagoPreparation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 210))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 478, 212))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SearchLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchLabel.setObjectName("SearchLabel")
        self.verticalLayout_2.addWidget(self.SearchLabel)
        self.ExplanationLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ExplanationLabel.setFont(font)
        self.ExplanationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExplanationLabel.setWordWrap(True)
        self.ExplanationLabel.setObjectName("ExplanationLabel")
        self.verticalLayout_2.addWidget(self.ExplanationLabel)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.WarningSignLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WarningSignLabel.sizePolicy().hasHeightForWidth())
        self.WarningSignLabel.setSizePolicy(sizePolicy)
        self.WarningSignLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.WarningSignLabel.setText("")
        self.WarningSignLabel.setPixmap(QtGui.QPixmap(GUI_SCRIPTS_DIR + "/images/warning.png"))
        self.WarningSignLabel.setScaledContents(True)
        self.WarningSignLabel.setObjectName("WarningSignLabel")
        self.horizontalLayout_2.addWidget(self.WarningSignLabel)
        self.WarningLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WarningLabel.sizePolicy().hasHeightForWidth())
        self.WarningLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.WarningLabel.setFont(font)
        self.WarningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WarningLabel.setWordWrap(True)
        self.WarningLabel.setObjectName("WarningLabel")
        self.horizontalLayout_2.addWidget(self.WarningLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.SuggestionLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SuggestionLabel.setFont(font)
        self.SuggestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SuggestionLabel.setWordWrap(True)
        self.SuggestionLabel.setObjectName("SuggestionLabel")
        self.verticalLayout_2.addWidget(self.SuggestionLabel)
        self.horizontalLayout_1.addLayout(self.verticalLayout_2)
        self.ImageLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMaximumSize(QtCore.QSize(200, 200))
        self.ImageLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ImageLabel.setText("")
        self.ImageLabel.setPixmap(QtGui.QPixmap(GUI_SCRIPTS_DIR + "/images/tiago_chess.jpg"))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setOpenExternalLinks(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.horizontalLayout_1.addWidget(self.ImageLabel)
        self.verticalLayout.addWidget(self.frame)
        self.ProgressGifLabel = QtWidgets.QLabel(TiagoPreparation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressGifLabel.sizePolicy().hasHeightForWidth())
        self.ProgressGifLabel.setSizePolicy(sizePolicy)
        self.ProgressGifLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.ProgressGifLabel.setMaximumSize(QtCore.QSize(50, 50))
        self.ProgressGifLabel.setText("")
        self.movie = QtGui.QMovie(GUI_SCRIPTS_DIR + "/images/ElaborationGif.gif")
        self.ProgressGifLabel.setMovie(self.movie)
        self.movie.start()
        #self.ProgressGifLabel.setPixmap(QtGui.QPixmap("images/Pulse-1s-211px.gif"))
        self.ProgressGifLabel.setScaledContents(True)
        self.ProgressGifLabel.setObjectName("ProgressGifLabel")
        self.verticalLayout.addWidget(self.ProgressGifLabel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OperationCompletedLabel = QtWidgets.QLabel(TiagoPreparation)
        self.OperationCompletedLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OperationCompletedLabel.sizePolicy().hasHeightForWidth())
        self.OperationCompletedLabel.setSizePolicy(sizePolicy)
        self.OperationCompletedLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.OperationCompletedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OperationCompletedLabel.setObjectName("OperationCompletedLabel")
        self.horizontalLayout.addWidget(self.OperationCompletedLabel)
        self.StartGamePushButton = QtWidgets.QPushButton(TiagoPreparation)
        self.StartGamePushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartGamePushButton.sizePolicy().hasHeightForWidth())
        self.StartGamePushButton.setSizePolicy(sizePolicy)
        self.StartGamePushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.StartGamePushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.StartGamePushButton.setObjectName("StartGamePushButton")
        self.horizontalLayout.addWidget(self.StartGamePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TiagoPreparation)
        QtCore.QMetaObject.connectSlotsByName(TiagoPreparation)

    def retranslateUi(self, TiagoPreparation):
        _translate = QtCore.QCoreApplication.translate
        TiagoPreparation.setWindowTitle(_translate("TiagoPreparation", "Form"))
        self.SearchLabel.setText(_translate("TiagoPreparation", " TIAGo preparation in progress..."))
        self.ExplanationLabel.setText(_translate("TiagoPreparation", "The operation consists in TIAGo opening the arm and positioning it over the clock, ready to catch pieces."))
        self.WarningLabel.setText(_translate("TiagoPreparation", "WARNING!"))
        self.SuggestionLabel.setText(_translate("TiagoPreparation", " Step away from TIAGo, to avoid collisions."))
        self.OperationCompletedLabel.setText(_translate("TiagoPreparation", "Preparation Completed!"))
        self.StartGamePushButton.setText(_translate("TiagoPreparation", "Start the game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TiagoPreparation = QtWidgets.QWidget()
    ui = Ui_TiagoPreparation()
    ui.setupUi(TiagoPreparation)
    TiagoPreparation.show()
    sys.exit(app.exec_())

