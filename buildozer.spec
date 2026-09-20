[app]
title = MyTools
package.name = mytools
package.domain = org.mytools
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,qrcode,pypng,psutil
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_NETWORK_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CHANGE_WIFI_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,REQUEST_INSTALL_PACKAGES
android.api = 34
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.enable_androidx = True
android.res_xml = provider_paths.xml
android.extra_manifest_application_arguments = extra_manifest_application_arguments.xml

[buildozer]
log_level = 2
warn_on_root = 1
