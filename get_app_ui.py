# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AppointmentFinder(object):
    def setupUi(self, AppointmentFinder):
        AppointmentFinder.setObjectName("AppointmentFinder")
        AppointmentFinder.resize(597, 474)
        self.labelPick = QtWidgets.QLabel(AppointmentFinder)
        self.labelPick.setGeometry(QtCore.QRect(9, 39, 77, 16))
        self.labelPick.setObjectName("labelPick")
        self.cboCenter = QtWidgets.QComboBox(AppointmentFinder)
        self.cboCenter.setGeometry(QtCore.QRect(170, 39, 401, 21))
        self.cboCenter.setObjectName("cboCenter")
        self.cboCenter.addItem("")
        self.cboCenter.addItem("")
        self.cboCenter.addItem("")
        self.cboCenter.addItem("")
        self.cboCenter.addItem("")
        self.cboCenter.addItem("")
        self.labelDOB = QtWidgets.QLabel(AppointmentFinder)
        self.labelDOB.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.labelDOB.setObjectName("labelDOB")
        self.labelDay = QtWidgets.QLabel(AppointmentFinder)
        self.labelDay.setGeometry(QtCore.QRect(170, 70, 21, 16))
        self.labelDay.setObjectName("labelDay")
        self.cboMonth = QtWidgets.QComboBox(AppointmentFinder)
        self.cboMonth.setGeometry(QtCore.QRect(350, 70, 61, 21))
        self.cboMonth.setObjectName("cboMonth")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.cboMonth.addItem("")
        self.labelMonth = QtWidgets.QLabel(AppointmentFinder)
        self.labelMonth.setGeometry(QtCore.QRect(300, 70, 36, 16))
        self.labelMonth.setObjectName("labelMonth")
        self.labelYear = QtWidgets.QLabel(AppointmentFinder)
        self.labelYear.setGeometry(QtCore.QRect(430, 70, 23, 16))
        self.labelYear.setObjectName("labelYear")
        self.labelEmail = QtWidgets.QLabel(AppointmentFinder)
        self.labelEmail.setGeometry(QtCore.QRect(10, 100, 49, 16))
        self.labelEmail.setObjectName("labelEmail")
        self.labelFirstname = QtWidgets.QLabel(AppointmentFinder)
        self.labelFirstname.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.labelFirstname.setObjectName("labelFirstname")
        self.entryFirstName = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryFirstName.setGeometry(QtCore.QRect(170, 130, 401, 21))
        self.entryFirstName.setObjectName("entryFirstName")
        self.entryEmail = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryEmail.setGeometry(QtCore.QRect(170, 100, 401, 21))
        self.entryEmail.setObjectName("entryEmail")
        self.labelLastName = QtWidgets.QLabel(AppointmentFinder)
        self.labelLastName.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.labelLastName.setObjectName("labelLastName")
        self.entryLastName = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryLastName.setGeometry(QtCore.QRect(170, 160, 401, 21))
        self.entryLastName.setObjectName("entryLastName")
        self.labelAddress = QtWidgets.QLabel(AppointmentFinder)
        self.labelAddress.setGeometry(QtCore.QRect(10, 190, 49, 16))
        self.labelAddress.setObjectName("labelAddress")
        self.labelStreet = QtWidgets.QLabel(AppointmentFinder)
        self.labelStreet.setGeometry(QtCore.QRect(170, 190, 49, 16))
        self.labelStreet.setObjectName("labelStreet")
        self.entryStreet = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryStreet.setGeometry(QtCore.QRect(210, 190, 191, 21))
        self.entryStreet.setObjectName("entryStreet")
        self.labelPostCode = QtWidgets.QLabel(AppointmentFinder)
        self.labelPostCode.setGeometry(QtCore.QRect(430, 190, 61, 16))
        self.labelPostCode.setObjectName("labelPostCode")
        self.entryPostCode = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryPostCode.setGeometry(QtCore.QRect(490, 190, 81, 21))
        self.entryPostCode.setObjectName("entryPostCode")
        self.labelHouseNum = QtWidgets.QLabel(AppointmentFinder)
        self.labelHouseNum.setGeometry(QtCore.QRect(170, 220, 91, 16))
        self.labelHouseNum.setObjectName("labelHouseNum")
        self.entryHouseNum = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryHouseNum.setGeometry(QtCore.QRect(260, 220, 91, 21))
        self.entryHouseNum.setObjectName("entryHouseNum")
        self.labelCity = QtWidgets.QLabel(AppointmentFinder)
        self.labelCity.setGeometry(QtCore.QRect(370, 220, 49, 16))
        self.labelCity.setObjectName("labelCity")
        self.entryCity = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryCity.setGeometry(QtCore.QRect(410, 220, 161, 21))
        self.entryCity.setObjectName("entryCity")
        self.labelPhoneNum = QtWidgets.QLabel(AppointmentFinder)
        self.labelPhoneNum.setGeometry(QtCore.QRect(10, 260, 91, 16))
        self.labelPhoneNum.setObjectName("labelPhoneNum")
        self.labelWithout = QtWidgets.QLabel(AppointmentFinder)
        self.labelWithout.setGeometry(QtCore.QRect(10, 280, 131, 16))
        self.labelWithout.setObjectName("labelWithout")
        self.entryPhoneNum = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryPhoneNum.setGeometry(QtCore.QRect(170, 260, 401, 21))
        self.entryPhoneNum.setObjectName("entryPhoneNum")
        self.labelCode = QtWidgets.QLabel(AppointmentFinder)
        self.labelCode.setGeometry(QtCore.QRect(10, 320, 101, 16))
        self.labelCode.setObjectName("labelCode")
        self.entryCode = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryCode.setGeometry(QtCore.QRect(170, 310, 391, 21))
        self.entryCode.setObjectName("entryCode")
        self.cmdGetCode = QtWidgets.QPushButton(AppointmentFinder)
        self.cmdGetCode.setGeometry(QtCore.QRect(170, 390, 151, 24))
        self.cmdGetCode.setObjectName("cmdGetCode")
        self.cmdUseCode = QtWidgets.QPushButton(AppointmentFinder)
        self.cmdUseCode.setGeometry(QtCore.QRect(340, 390, 221, 24))
        self.cmdUseCode.setObjectName("cmdUseCode")
        self.cmdExit = QtWidgets.QPushButton(AppointmentFinder)
        self.cmdExit.setGeometry(QtCore.QRect(290, 430, 75, 24))
        self.cmdExit.setObjectName("cmdExit")
        self.cboDay = QtWidgets.QComboBox(AppointmentFinder)
        self.cboDay.setGeometry(QtCore.QRect(200, 70, 68, 22))
        self.cboDay.setObjectName("cboDay")
        self.cboYear = QtWidgets.QComboBox(AppointmentFinder)
        self.cboYear.setGeometry(QtCore.QRect(480, 70, 68, 22))
        self.cboYear.setObjectName("cboYear")
        self.labelDriverPath = QtWidgets.QLabel(AppointmentFinder)
        self.labelDriverPath.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.labelDriverPath.setObjectName("labelDriverPath")
        self.entryPath = QtWidgets.QLineEdit(AppointmentFinder)
        self.entryPath.setGeometry(QtCore.QRect(170, 10, 271, 21))
        self.entryPath.setObjectName("entryPath")
        self.cmdGetPath = QtWidgets.QPushButton(AppointmentFinder)
        self.cmdGetPath.setGeometry(QtCore.QRect(460, 10, 111, 24))
        self.cmdGetPath.setObjectName("cmdGetPath")
        self.checkBoxCode = QtWidgets.QCheckBox(AppointmentFinder)
        self.checkBoxCode.setGeometry(QtCore.QRect(171, 351, 80, 20))
        self.checkBoxCode.setChecked(False)
        self.checkBoxCode.setObjectName("checkBoxCode")
        self.checkBoxApp = QtWidgets.QCheckBox(AppointmentFinder)
        self.checkBoxApp.setGeometry(QtCore.QRect(340, 351, 122, 20))
        self.checkBoxApp.setChecked(False)
        self.checkBoxApp.setObjectName("checkBoxApp")

        self.retranslateUi(AppointmentFinder)
        QtCore.QMetaObject.connectSlotsByName(AppointmentFinder)

    def retranslateUi(self, AppointmentFinder):
        _translate = QtCore.QCoreApplication.translate
        AppointmentFinder.setWindowTitle(_translate("AppointmentFinder", "Form"))
        self.labelPick.setText(_translate("AppointmentFinder", "Pick a website:"))
        self.cboCenter.setItemText(0, _translate("AppointmentFinder", "20259 Hamburg, Impfzentrum AGAPLESION DIAKONIEKLINIKUM"))
        self.cboCenter.setItemText(1, _translate("AppointmentFinder", "20357 Hamburg, Corona-Impfzentrum Hamburg"))
        self.cboCenter.setItemText(2, _translate("AppointmentFinder", "20537 Hamburg, Institut f??r Hygiene und Umwelt Hamburg, Impfzentrum"))
        self.cboCenter.setItemText(3, _translate("AppointmentFinder", "21029 Hamburg, Bergedorf - IZ im Bethesda Krankenhaus"))
        self.cboCenter.setItemText(4, _translate("AppointmentFinder", "21075 Hamburg, Asklepios Klinikum Harburg"))
        self.cboCenter.setItemText(5, _translate("AppointmentFinder", "22417 Hamburg, AK Nord-Heidberg HH Langenhorn"))
        self.labelDOB.setText(_translate("AppointmentFinder", "Date of birth:"))
        self.labelDay.setText(_translate("AppointmentFinder", "Day"))
        self.cboMonth.setItemText(0, _translate("AppointmentFinder", "Jan"))
        self.cboMonth.setItemText(1, _translate("AppointmentFinder", "Feb"))
        self.cboMonth.setItemText(2, _translate("AppointmentFinder", "Mar"))
        self.cboMonth.setItemText(3, _translate("AppointmentFinder", "Apr"))
        self.cboMonth.setItemText(4, _translate("AppointmentFinder", "May"))
        self.cboMonth.setItemText(5, _translate("AppointmentFinder", "Jun"))
        self.cboMonth.setItemText(6, _translate("AppointmentFinder", "Jul"))
        self.cboMonth.setItemText(7, _translate("AppointmentFinder", "Aug"))
        self.cboMonth.setItemText(8, _translate("AppointmentFinder", "Sep"))
        self.cboMonth.setItemText(9, _translate("AppointmentFinder", "Oct"))
        self.cboMonth.setItemText(10, _translate("AppointmentFinder", "Nov"))
        self.cboMonth.setItemText(11, _translate("AppointmentFinder", "Dec"))
        self.labelMonth.setText(_translate("AppointmentFinder", "Month"))
        self.labelYear.setText(_translate("AppointmentFinder", "Year"))
        self.labelEmail.setText(_translate("AppointmentFinder", "Email:"))
        self.labelFirstname.setText(_translate("AppointmentFinder", "First name:"))
        self.labelLastName.setText(_translate("AppointmentFinder", "Last name:"))
        self.labelAddress.setText(_translate("AppointmentFinder", "Address:"))
        self.labelStreet.setText(_translate("AppointmentFinder", "Street:"))
        self.labelPostCode.setText(_translate("AppointmentFinder", "Post code:"))
        self.labelHouseNum.setText(_translate("AppointmentFinder", "House number:"))
        self.labelCity.setText(_translate("AppointmentFinder", "City:"))
        self.labelPhoneNum.setText(_translate("AppointmentFinder", "Phone number:"))
        self.labelWithout.setText(_translate("AppointmentFinder", "(without country code)"))
        self.labelCode.setText(_translate("AppointmentFinder", "Vermittlungscode:"))
        self.cmdGetCode.setText(_translate("AppointmentFinder", "Get Vermittlungscode"))
        self.cmdUseCode.setText(_translate("AppointmentFinder", "Get appointment with Vermittlungscode"))
        self.cmdExit.setText(_translate("AppointmentFinder", "Exit"))
        self.labelDriverPath.setText(_translate("AppointmentFinder", "Chromedriver path:"))
        self.cmdGetPath.setText(_translate("AppointmentFinder", "Select path"))
        self.checkBoxCode.setToolTip(_translate("AppointmentFinder", "If checked, it will proceed with getting the code else it will stop just before it clicks \'book\'"))
        self.checkBoxCode.setText(_translate("AppointmentFinder", "Book code"))
        self.checkBoxApp.setToolTip(_translate("AppointmentFinder", "If checked, it will proceed with booking the appointment else it will stop just before it clicks \'book\'"))
        self.checkBoxApp.setText(_translate("AppointmentFinder", "Book appointment"))
