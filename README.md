kivy-external-storage-permission
================================

Requirements:

* Docker
* tested on Ubuntu
* Adnroid device connected to push the created apk
* Time, the initial build can take a while

Run:
```
mkdir reproduce
cd reproduce
git clone https://github.com/guysoft/kivy-external-storage-permission.git
git clone https://github.com/guysoft/python-for-android.git
cd kivy-external-storage-permission
sudo docker-compose up -d 
# Waiting for merge of https://github.com/JonasT/p4a-build-spaces/pull/8
sudo docker exec -it -u 0 buildozer-test pip3 install https://github.com/kivy/buildozer/archive/master.zip
./docker_build
./docker_debug
```

