@echo off
echo 🚀 Building Image Duplicate Scanner...
echo.

REM Install PyInstaller if not installed
pip install pyinstaller

REM Build the executable
pyinstaller --onefile --windowed --name="ImageCleaner" image_cleaner.py

echo.
echo ✅ Build complete!
echo 📁 Your executable is in the "dist" folder
echo.
pause