pip install kivy
python -m pip install --upgrade pip
pip install kivymd
pip install buildozer
pip install Cython

For APK with KivyMD
buildozer init
some changes in file "buildozer.spec":
*
  # (list) Application requirements
  # comma separated e.g. requirements = sqlite3,kivy
  requirements = python3,kivy  
  ---------------->
  # (list) Application requirements
  # comma separated e.g. requirements = sqlite3,kivy
  #requirements = python3,kivy
  requirements = python3,kivy==2.0.0,https://github.com/kivymd/KivyMD/archive/master.zip,pygments, sdl2_ttf==2.0.15,pillow
*
  # (str) Custom source folders for requirements  
  # Sets custom source for any requirements with recipes
  #requirements.source.kivy =../../kivy 
  ---------------->
  requirements.source.kivymd =../../kivymd
*
  # Kivy version to use
  osx.kivy_version = 2.0.0   ## current version
