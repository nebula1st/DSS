from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from admin.admin import DSSWindow
from login.login import SigninWindow

class MainWindow(BoxLayout):

    DSS_widget = DSSWindow()
    login_widget = SigninWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_log.add_widget(self.login_widget)
        self.ids.scrn_dss.add_widget(self.DSS_widget)

class MainApp(App):
    def build(self):

        return MainWindow()

if __name__=='__main__':
    MainApp().run()