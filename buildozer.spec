[app]
title = VoidPAK Toolkit
package.name = voidpaktoolkit
package.domain = org.voidpak
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,so,jar
source.include_patterns = assets/*,*.py
source.exclude_exts = spec
version = 3.5
requirements = python3,kivy,pycryptodome,gmalg,zstandard
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
