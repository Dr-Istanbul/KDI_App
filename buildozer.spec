[app]

# Title of your application
title = Khalifa Designs International

# Package name (unique identifier for your app)
package.name = kdi_app

# Package domain (used as a namespace for your app)
package.domain = org.kdi

# Source directory (where your main.py is located)
source.dir = .

# Source files to include (main.py and logo.png)
source.include_exts = py,png,jpg,kv,atlas

# Main entry point of your app
source.include_patterns = KDIlogo.png

# Application version (major.minor.revision)
version = 1.0

# Requirements for your app
requirements = python3,kivy,kivymd,pillow,cython,pyjnius

# Orientation (portrait or landscape)
orientation = portrait

# Android API level
android.api = 30

# Minimum Android SDK version
android.minapi = 21


android.ndk_api = 21



# Target Android SDK version
android.ndk = 25b
# Permissions required by your app
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icon for your app (must be in the source directory)
icon.filename = KDIlogo.png

# Presplash screen (optional)
presplash.filename = KDIlogo.png

# Log level for Buildozer (0 = minimal, 1 = verbose)
log_level = 1

# (Optional) Fullscreen mode
fullscreen = 0

# (Optional) Allow backup on Android
android.allow_backup = True

# (Optional) Debug mode
debug = 1
