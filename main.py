import kivy

from kivy.app import App
from kivy.uix.button import Button
import android
import os


class MyApp(App):

    def callback(self, data):
        print("Pushed button, running")
        from android.permissions import Permission, request_permission, check_permission

        if not check_permission(Permission.WRITE_EXTERNAL_STORAGE):
            print("granding permission")
            print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        else:
            print("claims to have, trying anyway")
            print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        
        print("should have permission")

        
        uri = os.environ["SECONDARY_STORAGE"]
        test_path = os.path.join(uri, "test_yay")
        os.makedirs(test_path)
            
        



    def build(self):

        return Button(text='Tuch to test writing to ' + os.environ["SECONDARY_STORAGE"], on_press=self.callback)


if __name__ == '__main__':
    MyApp().run()
