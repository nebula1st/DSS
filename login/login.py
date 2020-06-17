from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from utils.connectdb import ConnectDB

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        nik = user.text
        passw = pwd.text
        
        conn = ConnectDB().Connect()
        cursor = conn.cursor()
        find_user = ("SELECT * FROM karyawan WHERE IDKaryawan = %s AND No_Telpon = %s")
        cursor.execute(find_user,[(nik),(passw)])
        results = cursor.fetchall()
        if results:
            for i in results:
                if i[2]!='hr':
                    #label = self.ids.success
                    info.text = "[color=#FF0000]Anda tidak punya wewenang untuk membuka aplikasi ini[/color]"
                else:
                    self.parent.parent.current = 'scrn_dss'
                    info.text = ""
                    self.ids.username_field.text = ''
                    self.ids.pwd_field.text = ''
        else:
            info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'
                   

        #if uname == '' or passw == '':
        #    info.text = '[color=#FF0000]username and/ or password required[/color]'
        #else:
        #    if uname == 'admin' and passw == 'admin':
        #        info.text = '[color=#00FF00]Logged In successfully!!![/color]'
        #    else:
        #        info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'

kv = Builder.load_file("login/login.kv")

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__=="__main__":
    sa = SigninApp()
    sa.run()
