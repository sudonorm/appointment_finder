import sys
import numpy as np
import time

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)

from get_app_ui import Ui_AppointmentFinder

class Window(QMainWindow, Ui_AppointmentFinder):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        days = [str(x) for x in np.arange(1, 32)]
        years = reversed([str(x) for x in np.arange(1901, int(time.strftime("%Y")) + 1)])
        self.cboDay.addItems(days)
        self.cboYear.addItems(years)
        self.connectSignalsSlots()
        
    def connectSignalsSlots(self):
        self.cmdGetPath.clicked.connect(self.dir_pop_up)
        #self.cmdGetCode.clicked.connect(self.get_values)
        self.cmdGetCode.clicked.connect(self.find_code)
        self.cmdUseCode.clicked.connect(self.find_appointment)
        self.cmdExit.clicked.connect(QApplication.instance().quit)
        
    def dir_pop_up(self):
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        folder = folder + "//chromedriver.exe"
        self.entryPath.setText(folder)

    def get_values(self):
        print(self.cboCenter.currentText())
        print(self.cboDay.currentText())
        print(self.cboMonth.currentText())
        print(self.cboYear.currentText())

        print(self.entryPhoneNum.text())
        print(self.entryEmail.text())

        if self.checkBoxCode.isChecked():
            print("code is checked!")

        if self.checkBoxApp.isChecked():
            print("app is checked!")
        

    def find_code(self):
        import requests
        import pandas as pd
        import os
        import time
        import random
        from bs4 import BeautifulSoup as bs
        from selenium import webdriver
        import re
        import numpy as np
        import warnings
        import itertools
        import winsound
        warnings.filterwarnings("ignore")
        from selenium.webdriver.common.keys import Keys

        option = webdriver.ChromeOptions()
        #option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--incognito')
        option.add_argument('--disable-infobars')
        option.add_argument("--disable-notifications")
        #option.add_argument('disable-infobars')
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

        driver = webdriver.Chrome(executable_path=self.entryPath.text(), options=option)
        driver.implicitly_wait(10)

        cnt = 0
        urlDict = {"20259 Hamburg, Impfzentrum AGAPLESION DIAKONIEKLINIKUM":"https://226-iz.impfterminservice.de/impftermine/service?plz=20259", "20357 Hamburg, Corona-Impfzentrum Hamburg": "https://353-iz.impfterminservice.de/impftermine/service?plz=20357",
        "20537 Hamburg, Institut für Hygiene und Umwelt Hamburg, Impfzentrum": "https://226-iz.impfterminservice.de/impftermine/service?plz=20537",
        "21029 Hamburg, Bergedorf - IZ im Bethesda Krankenhaus":"https://226-iz.impfterminservice.de/impftermine/service?plz=21029",
        "21075 Hamburg, Asklepios Klinikum Harburg":"https://226-iz.impfterminservice.de/impftermine/service?plz=21075",
         "22417 Hamburg, AK Nord-Heidberg HH Langenhorn":"https://226-iz.impfterminservice.de/impftermine/service?plz=22417"}

        url = urlDict[self.cboCenter.currentText()]

        driver.get(url)
        time.sleep(3)

        found = False
        unAvail = 'Es wurden keine freien Termine in Ihrer Region gefunden'

        nein = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]/span")
        nein.click()

        cnt += 1
        print(f'{"Number of tries: "}{str(cnt)}', end="\r")

        time.sleep(5)

        try:
            msg = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/div/div").text.strip()
            msg = msg.split(".")[0]

        except:
            msg = "different"
            
        if not msg == unAvail:
                print("appointment found!")

                try:
                    ja = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[1]/div/div/label[1]/span")
                    ja.click()

                    dob = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[3]/div/div/input")

                    dob.send_keys(self.cboDay.currentText())
                    dob.send_keys(Keys.RIGHT)
                    dob.send_keys(self.cboMonth.currentText())
                    dob.send_keys(Keys.RIGHT)
                    dob.send_keys(self.cboYear.currentText())

                    dob.send_keys(self.cboYear.currentText())
                    dob.send_keys(Keys.LEFT)
                    dob.send_keys(self.cboMonth.currentText())
                    dob.send_keys(Keys.LEFT)
                    dob.send_keys(self.cboDay.currentText())
                    dob.send_keys(Keys.LEFT)

                    continueF = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[4]/button")
                    continueF.click()

                except:
                    pass

                try:
                    msg2 = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[2]/span").text.strip()
                    msg2 = msg2.split(".")[0]
                except:
                    msg2 = ""
                    
                if not msg2 == unAvail:
                    
                    try:
                        e_mail = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[1]/label/input")

                        e_mail.send_keys(self.entryEmail.text())

                        phoneNumber = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[2]/label/div/input")

                        phoneNumber.send_keys(self.entryPhoneNum.text())

                        if self.checkBoxCode.isChecked():
                            get_code = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[3]/button")

                            get_code.click()
                    except:
                        pass

                    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

                    found = True
                else:
                    print("false alarm. Retrying...")

        while not found:

            nein = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]/span")
            nein.click()

            time.sleep(5)
            
            try:
                msg = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/div/div").text.strip()
                msg = msg.split(".")[0]
            except:
                msg = "different"

            cnt += 1
            print(f'{"Number of tries: "}{str(cnt)}', end="\r")

            if not msg == unAvail:
                print("appointment found!")
                try:
                    ja = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[1]/div/div/label[1]/span")
                    ja.click()

                    dob = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[3]/div/div/input")

                    dob.send_keys(self.cboDay.currentText())
                    dob.send_keys(Keys.RIGHT)
                    dob.send_keys(self.cboMonth.currentText())
                    dob.send_keys(Keys.RIGHT)
                    dob.send_keys(self.cboYear.currentText())

                    dob.send_keys(self.cboYear.currentText())
                    dob.send_keys(Keys.LEFT)
                    dob.send_keys(self.cboMonth.currentText())
                    dob.send_keys(Keys.LEFT)
                    dob.send_keys(self.cboDay.currentText())
                    dob.send_keys(Keys.LEFT)

                    continueF = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[4]/button")
                    continueF.click()

                except:
                    pass

                try:
                    msg2 = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[2]/span").text.strip()
                    msg2 = msg2.split(".")[0]
                except:
                    msg2 = ""
                    
                if not msg2 == unAvail:
                    
                    try:
                        e_mail = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[1]/label/input")

                        e_mail.send_keys(self.entryEmail.text())

                        phoneNumber = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[2]/label/div/input")

                        phoneNumber.send_keys(self.entryPhoneNum.text())
                        
                        if self.checkBoxCode.isChecked():
                            get_code = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-check-result/div/div/div[2]/div/div/div/div/app-its-check-success/div/form/div[3]/button")

                            get_code.click()
                    except:
                        pass

                    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

                    found = True
                else:
                    print("false alarm. Retrying...")
                
            time.sleep(random.randint(4, 9))

    def find_appointment(self):
        import requests
        import pandas as pd
        import os
        import time
        import random
        from bs4 import BeautifulSoup as bs
        from selenium import webdriver
        import re
        import numpy as np
        import warnings
        import itertools
        import winsound
        warnings.filterwarnings("ignore")
        from selenium.webdriver.common.keys import Keys

        option = webdriver.ChromeOptions()
        #option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--incognito')
        option.add_argument('--disable-infobars')
        option.add_argument("--disable-notifications")
        #option.add_argument('disable-infobars')
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

        driver = webdriver.Chrome(executable_path=self.entryPath.text(), options=option)
        driver.implicitly_wait(10)

        urlDict = {"20259 Hamburg, Impfzentrum AGAPLESION DIAKONIEKLINIKUM":"https://226-iz.impfterminservice.de/impftermine/service?plz=20259", "20357 Hamburg, Corona-Impfzentrum Hamburg": "https://353-iz.impfterminservice.de/impftermine/service?plz=20357",
        "20537 Hamburg, Institut für Hygiene und Umwelt Hamburg, Impfzentrum": "https://226-iz.impfterminservice.de/impftermine/service?plz=20537",
        "21029 Hamburg, Bergedorf - IZ im Bethesda Krankenhaus":"https://226-iz.impfterminservice.de/impftermine/service?plz=21029",
        "21075 Hamburg, Asklepios Klinikum Harburg":"https://226-iz.impfterminservice.de/impftermine/service?plz=21075",
         "22417 Hamburg, AK Nord-Heidberg HH Langenhorn":"https://226-iz.impfterminservice.de/impftermine/service?plz=22417"}

        url = urlDict[self.cboCenter.currentText()]
        code = self.entryCode.text()
        
        unAvail = 'Derzeit stehen leider keine Termine zur Verfügung'
        cnt = 0
        found = False

        #print(self.entryFirstName.text(), self.entryLastName.text(), self.entryPostCode.text(), self.entryCity.text(), self.entryStreet.text(), self.entryHouseNum.text(), self.entryPhoneNum.text(), self.entryEmail.text())

        driver.get(url)

        time.sleep(random.randint(4, 10))
        yes = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[1]/span")

        yes.click()
        time.sleep(random.randint(4, 10))
        HH_input = driver.find_element_by_name("ets-input-code-0")

        HH_input.send_keys(code)
        time.sleep(random.randint(4, 10))
        search = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[2]/button")

        search.click()
        time.sleep(random.randint(4, 10))

        loc20357 = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[2]/div[2]/button")
        loc20357.click()

        time.sleep(random.randint(4, 10))

        try:
            msg = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[1]/span")

            msg = msg.text.strip().split(".")[0].strip()
        except:
            msg = "different"

        cnt += 1
        print(f'{"Checking for free appointments. Number of tries: "}{str(cnt)}', end="\r")
            
        if not msg == unAvail:
            print("appointment found!")
            
            appt = driver.find_element_by_class_name("its-slot-pair-search-radio-btn")
            appt.click()
            time.sleep(2)
            acptVacDate = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[2]/button[1]")
            acptVacDate.click()
            time.sleep(2)

            enterData = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[2]/div[2]/div[2]/button")
            enterData.click()
            gender = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[1]/div/div/div/label[1]/span")
            gender.click()
            #
            firstName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[1]/div/label/input")
            lastName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[2]/div/label/input")
            postPlz = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[1]/div/label/input")
            place = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[2]/div/label/input")
            streetName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[1]/div/label/input")
            streetNum = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[2]/div/label/input")
            phnNum = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[3]/div/label/div/input")
            emailAdd = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[5]/div/div/label/input")

            fName = self.entryFirstName.text()
            lName = self.entryLastName.text()
            Plz = self.entryPostCode.text()
            city = self.entryCity.text()
            street = self.entryStreet.text()
            nmbr = self.entryHouseNum.text()
            phone = self.entryPhoneNum.text()
            email = self.entryEmail.text()

            firstName.send_keys(fName)
            lastName.send_keys(lName)
            postPlz.send_keys(Plz)
            place.send_keys(city)
            streetName.send_keys(street)
            streetNum.send_keys(nmbr)
            phnNum.send_keys(phone)
            emailAdd.send_keys(email)

            acptAppDate = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[2]/button[1]")
            acptAppDate.click()
            time.sleep(2)

            if self.checkBoxApp.isChecked():
                bookApp = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[3]/div[2]/div[2]/button")
                bookApp.click()

            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

            found = True
        else:
            cancel = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[2]/button[2]")
            cancel.click()
            
        while not found:
            time.sleep(random.randint(5, 10))
            
            loc20357 = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[2]/div[2]/button")
            loc20357.click()
            
            time.sleep(random.randint(4, 10))
            
            try:
                msg = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[1]/span")

                msg = msg.text.strip().split(".")[0].strip()
            except:
                msg = "different"

            cnt += 1
            print(f'{"Checking for free appointments. Number of tries: "}{str(cnt)}', end="\r")

            if not msg == unAvail:
                print("appointment found!")

                appt = driver.find_element_by_class_name("its-slot-pair-search-radio-btn")
                appt.click()
                time.sleep(2)
                acptVacDate = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[2]/button[1]")
                acptVacDate.click()
                time.sleep(2)

                enterData = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[2]/div[2]/div[2]/button")
                enterData.click()
                gender = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[1]/div/div/div/label[1]/span")
                gender.click()
                #
                firstName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[1]/div/label/input")
                lastName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[2]/div/label/input")
                postPlz = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[1]/div/label/input")
                place = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[2]/div/label/input")
                streetName = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[1]/div/label/input")
                streetNum = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[2]/div/label/input")
                phnNum = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[3]/div/label/div/input")
                emailAdd = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[5]/div/div/label/input")

                fName = self.entryFirstName.text()
                lName = self.entryLastName.text()
                Plz = self.entryPostCode.text()
                city = self.entryCity.text()
                street = self.entryStreet.text()
                nmbr = self.entryHouseNum.text()
                phone = self.entryPhoneNum.text()
                email = self.entryEmail.text()

                firstName.send_keys(fName)
                lastName.send_keys(lName)
                postPlz.send_keys(Plz)
                place.send_keys(city)
                streetName.send_keys(street)
                streetNum.send_keys(nmbr)
                phnNum.send_keys(phone)
                emailAdd.send_keys(email)

                acptAppDate = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-contact-modal/div/div/div/div[2]/div/form/div[2]/button[1]")
                acptAppDate.click()
                time.sleep(2)

                if self.checkBoxApp.isChecked():
                    bookApp = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[3]/div[2]/div[2]/button")
                    bookApp.click()

                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

                found = True

            else:
                cancel = driver.find_element_by_xpath("/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[2]/button[2]")
                cancel.click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())