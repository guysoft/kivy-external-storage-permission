import kivy

from kivy.app import App
from kivy.uix.button import Button
import android
import os
import time
from android.permissions import Permission, request_permission, check_permission
from kivy.clock import Clock



class MyApp(App):
    def second_thread(self, data):
        print("starting second thread")
        permission_status = check_permission(Permission.WRITE_EXTERNAL_STORAGE)
        print(permission_status)
        
        if permission_status is not None and permission_status:
            print("got permission")
            path = os.environ["SECONDARY_STORAGE"]
            test_path = os.path.join(path, "test_yay")
            os.makedirs(test_path)
        else:
            Clock.schedule_once(self.second_thread, 1)

        

            

    def callback(self, data):
        print("Pushed button, running")
        print("request permission")
        print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        Clock.schedule_once(self.second_thread, 5)



    def build(self):

        return Button(text='Touch to test writing to ' + os.environ["SECONDARY_STORAGE"], on_press=self.callback)


if __name__ == '__main__':
    MyApp().run()
