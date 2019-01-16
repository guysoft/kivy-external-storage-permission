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
        while permission_status is None or not permission_status:
            print("permission status:")
            print(status)
            time.sleep(1)
        
        print("should have permission")

        
        uri = os.environ["SECONDARY_STORAGE"]
        test_path = os.path.join(uri, "test_yay")
        os.makedirs(test_path)
            

    def callback(self, data):
        print("Pushed button, running")
        """
        if not check_permission(Permission.WRITE_EXTERNAL_STORAGE):
            print("granding permission")
            print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        else:
            print("claims to have, trying anyway")
            print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        """
        print("request permission")
        print(request_permission(Permission.WRITE_EXTERNAL_STORAGE))
        Clock.schedule_once(self.second_thread, 5)
        

        



    def build(self):

        return Button(text='Tuch to test writing to ' + os.environ["SECONDARY_STORAGE"], on_press=self.callback)


if __name__ == '__main__':
    MyApp().run()
