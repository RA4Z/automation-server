import win32com.client
import pyautogui
import time
import subprocess

class SAP():
    def __init__(self, language:str, credential):
        self.language = language
        self.credential = credential
        self.connection = self.__verify_sap_open()
        
    def __verify_sap_open(self):
        try:
            sapguiauto = win32com.client.GetObject('SAPGUI')
            application = sapguiauto.GetScriptingEngine
            return application.Children(0)
        except:
            return self.__open_sap()

    def __open_sap(self):
        path = "C:/Program Files (x86)/SAP/FrontEnd/SapGui/saplgpad.exe"
        subprocess.Popen(path)
        while not pyautogui.getActiveWindowTitle().startswith("SAP Logon"):
            time.sleep(1)

        sapguiauto = win32com.client.GetObject('SAPGUI')
        application = sapguiauto.GetScriptingEngine
        connection = application.OpenConnection("EP0 - ECC Produção", True)
        session = connection.Children(0)
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/usr/txtRSYST-MANDT").Text = self.credential['principal']
        session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = self.credential['username']
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = self.credential['password']
        session.findById("wnd[0]/usr/txtRSYST-LANGU").text = self.language
        session.findById("wnd[0]").sendVKey(0)

        if session.activewindow.name == 'wnd[1]':
            session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").Select
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            
        return application.Children(0)
