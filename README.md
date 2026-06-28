# 🖼️ Image Duplicate Scanner v2.2

**Professional Image Duplicate Detection Tool**  
Built by **GamEGanG** | © 2026 - All Rights Reserved

---

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [How to Use](#how-to-use)
- [Theme Settings](#theme-settings)
- [Troubleshooting](#troubleshooting)
- [Supported Formats](#supported-formats)
- [Version History](#version-history)
- [Tips & Best Practices](#tips--best-practices)

---

## ✨ Features

### 🔍 **Core Features**
- **Fast Image Scanning** - Quickly scans entire folders for duplicate images
- **Smart Detection** - Uses MD5 hashing of image thumbnails for accurate duplicate detection
- **Batch Operations** - Delete or move multiple duplicates at once
- **Export Reports** - Generate detailed CSV/TXT reports of findings

### 🎨 **UI/UX Features**
- **Dark/Light Mode** - Toggle between beautiful themes (View → Theme)
- **Professional Interface** - Modern PyQt5-based GUI
- **Real-time Progress** - Live progress bar during scanning
- **Interactive Results** - Tree view showing original vs duplicate files
- **Double-click Navigation** - Open file locations directly from results

### 🚀 **Performance**
- **Standalone Executable** - No Python installation required
- **Optimized Scanning** - Efficient image comparison algorithm
- **Low Memory Usage** - Thumbnail-based processing
- **Responsive UI** - Non-blocking scan operations

---

## 💾 Installation

### Option 1: Standalone Executable (Recommended - No Installation!)
Simply download and run:
```
ImageDuplicateScanner.exe
```
**No Python or dependencies needed!**

### Option 2: From Python Source
Requirements:
- Python 3.7+
- PyQt5
- Pillow (PIL)

Install dependencies:
```powershell
pip install PyQt5 Pillow
```

---

## 🚀 Quick Start

### **Method 1: Run Executable (Easiest)**
Double-click: `dist/ImageDuplicateScanner.exe`

### **Method 2: Run from Python**
```powershell
cd "path\to\double copy"
python delete.py
```

### **Method 3: Using Batch File**
```powershell
run_scanner.bat
```

### **Method 4: Using VBS (No Console Window)**
```powershell
run_scanner.vbs
```

---

## 📖 How to Use

### Step-by-Step Guide

1. **Start the Application**
   - Launch using one of the methods above
   - Window opens in center of screen

2. **Select a Folder**
   - Click "📂 Browse..." button
   - Choose a folder containing images
   - Quick image count appears

3. **Start Scanning**
   - Click "🔍 Start Scan"
   - Watch the progress bar
   - Scan runs in background (UI stays responsive)

4. **Review Results**
   - Results appear in tree view
   - ✅ Green = Original (kept)
   - ❌ Red = Duplicate (marked for removal)
   - Double-click file to open location

5. **Take Action**
   - **🗑️ Delete Duplicates** - Permanently delete duplicate files
   - **📦 Move Duplicates** - Move to backup folder (safer option)
   - **📝 Export Report** - Save detailed report as TXT file

### Example Workflow
```
1. Select: C:\Users\YourName\Pictures
2. Scan: 150 images found → 3 duplicate groups detected
3. Review: Check original vs duplicates
4. Action: Move duplicates to backup (keep originals safe)
5. Result: 45 MB freed, organized collection!
```

---

## 🎨 Theme Settings

### Switching Themes
1. Open the app
2. Go to **View** menu
3. Choose **☀️ Light Mode** or **🌙 Dark Mode**

### Theme Details
- **Light Mode**: Clean bright interface, good for daytime use
- **Dark Mode**: Easy on eyes, recommended for extended use
- **Persistent**: Theme preference is saved and restored on restart
- **Full Coverage**: All UI elements (buttons, menus, dialogs) are themed

### Storage
Theme preference saved in: `theme_config.txt`

---

## 🔧 Troubleshooting

### **App Won't Start**
```powershell
# Check Python syntax
python -m py_compile delete.py

# Run with error output
python delete.py
```

### **Window Doesn't Appear**
- Make sure your monitor is connected
- Try running: `python test_gui_simple.py` (test app)
- Check for conflicting programs

### **Scanning Issues**
- Ensure image files are readable
- Check disk space (need ~500MB free)
- Try with smaller folder first

### **Missing Dependencies**
```powershell
# Install PyQt5
pip install PyQt5

# Install Pillow
pip install Pillow
```

### **Slow Performance**
- Exclude large video libraries
- Scan smaller folders first
- Close other applications

---

## 📸 Supported Image Formats
- ✅ JPG / JPEG
- ✅ PNG
- ✅ GIF
- ✅ BMP
- ✅ TIFF
- ✅ WebP
- ✅ ICO
- ✅ SVG

---

## 📦 File Structure
```
Image Duplicate Scanner/
│
├── delete.py                      # Main application (v2.2)
├── dist/
│   └── ImageDuplicateScanner.exe  # Standalone executable
├── README.md                      # This file
├── CHANGELOG.md                   # Version history
├── theme_config.txt               # Theme preference (auto-created)
│
├── Launchers/
├── run_scanner.bat               # Batch launcher
├── run_scanner.vbs               # VBS launcher (no console)
├── launcher.py                   # Python launcher
│
└── versions/                      # Version backups
    ├── delete_v2.2.py            # Current version
    ├── delete_v2.1.py
    └── delete_v2.0.py
```

---

## 📜 Version History

### **v2.2 (Current) - 2026-06-28** 🎨
- ✨ **NEW: Dark/Light Theme System**
  - Toggle between themes in View menu
  - Persistent theme preference
  - Fully themed UI elements
- Added ThemeManager class
- Enhanced visual customization

### **v2.1.1 - 2026-06-28** 🐛
- Fixed syntax errors
- Removed console window on launch
- Rebuilt standalone executable
- Better window management

### **v2.1 - 2026-06-28** 🚀
- Fixed window display issues
- Added missing GUI imports
- Improved window positioning
- Better error handling

### **v2.0 - Initial Release**
- Full duplicate detection
- PyQt5 GUI interface
- Delete/Move/Export functions

---

## 💡 Tips & Best Practices

### ✅ Do's
- ✅ Use "Move Duplicates" first if unsure (safer than delete)
- ✅ Review results carefully before taking action
- ✅ Keep original of best quality image
- ✅ Export reports before bulk operations
- ✅ Backup important folders first
- ✅ Start with small test folders

### ❌ Don'ts
- ❌ Don't delete without reviewing results
- ❌ Don't run on system folders (C:\Windows, etc.)
- ❌ Don't interrupt scan while running
- ❌ Don't process very large folders (100k+ images) at once
- ❌ Don't ignore warnings

### 🎯 Optimization Tips
- Close other applications to speed up scanning
- Use SSD drives for faster processing
- Exclude network drives (slow)
- Scan organized folders (by date/type)
- Process medium-sized folders (500-5000 images) for best results

---

## 🎯 Common Questions

**Q: Is it safe to use?**  
A: Yes! The app always keeps the original and only removes duplicates. Use "Move" instead of "Delete" for extra safety.

**Q: Does it need Python installed?**  
A: No! The `.exe` file works standalone. Python only needed if running from source.

**Q: Can I recover deleted files?**  
A: If using "Move" option, files are in the backup folder. For "Delete", use Windows Recovery or third-party tools.

**Q: How accurate is duplicate detection?**  
A: Very accurate (99%+). Uses image hashing, not just filename comparison.

**Q: Can I run multiple scans?**  
A: Yes, just select a different folder and scan again.

**Q: Will it work on Mac/Linux?**  
A: Source code will, but `.exe` is Windows-only. Install Python and run `python delete.py` on Mac/Linux.

---

## 🔐 Privacy & Security
- ✅ All processing done locally (no cloud)
- ✅ No data collection or telemetry
- ✅ No internet connection required
- ✅ Safe to use on any computer

---

## 🤝 Support & Feedback
- Report bugs or request features
- Suggest improvements
- Share your experience

---

## 📄 License
© 2026 GamEGanG - All Rights Reserved

---

**Made with ❤️ by GamEGanG** | Version 2.2 | Last Updated: 2026-06-28
