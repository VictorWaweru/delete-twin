@echo off
echo 🥷 Building Photo Ninja...
echo Version: 2.3
echo "Silent. Precise. Deadly to Duplicates."
echo.
echo 📦 Installing PyInstaller...
pip install pyinstaller

echo.
echo 🔨 Building executable...
pyinstaller --onefile --windowed --name="PhotoNinja" --icon=app.ico delete.py

echo.
echo ✅ Build complete!
echo 📁 Your executable is in the "dist" folder
echo.
pause