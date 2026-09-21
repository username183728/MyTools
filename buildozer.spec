[app]
title = MyTools
package.name = mytools
package.domain = org.mytools
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.exclude_dirs = __pycache__,.github,bin,.buildozer
version = 1.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,qrcode,pypng,psutil,certifi
orientation = portrait
fullscreen = 0

# MANAGE_EXTERNAL_STORAGE: File Manager / Editor / ZIP di Android 11+ (pengguna harus
#   mengaktifkan "Akses semua file"; aplikasi mengarahkan ke pengaturannya saat pertama dibuka).
#   Catatan: izin ini dibatasi kebijakan Google Play; untuk sideload/APK langsung tidak masalah.
# NEARBY_WIFI_DEVICES: membaca info Wi-Fi di Android 13+.
android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_NETWORK_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,NEARBY_WIFI_DEVICES,CHANGE_WIFI_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,REQUEST_INSTALL_PACKAGES
android.api = 34
android.minapi = 24
android.ndk = 28c
android.ndk_api = 24
# Ingin build lebih cepat? Cukup arm64-v8a (hampir semua HP modern).
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.enable_androidx = True
android.res_xml = provider_paths.xml
android.extra_manifest_application_arguments = extra_manifest_application_arguments.xml

[buildozer]
log_level = 2
warn_on_root = 1
