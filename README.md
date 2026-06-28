# Image Duplicate Scanner - Quick Start Guide

## What I Fixed

I've made the following improvements to fix the window closing issue:

1. **Better Error Handling**: Added comprehensive error handling in the `scan_finished()` method to catch and display any errors
2. **Window Management**: Improved window positioning and focus management to ensure it displays properly
3. **Center Screen Positioning**: Window now opens in the center of your screen instead of a fixed position

## How to Use

### Method 1: Run from Terminal (Recommended for Testing)
```powershell
cd "c:\Users\GaMEgGAnG\Desktop\double copy"
python delete.py
```

### Method 2: Double-Click (Easier for Regular Use)
1. Right-click on `delete.py`
2. Select "Open with" → "Python"
3. Or create a shortcut that runs: `pythonw delete.py`

### Method 3: Using the Batch File
```
run_scanner.bat
```

## How It Works

1. **Start the Application**: Run the script using one of the methods above
2. **Select a Folder**: Click the "📂 Browse..." button to select a folder with images
3. **Start Scanning**: Click "🔍 Start Scan"
4. **Review Results**: Wait for the scan to complete, then review the duplicate groups
5. **Take Action**: 
   - Delete duplicates (🗑️)
   - Move duplicates to a backup folder (📦)
   - Export a detailed report (📝)

## Troubleshooting

### If the window doesn't appear:
1. Make sure PyQt5 is installed:
   ```powershell
   pip install PyQt5
   ```
2. Make sure Pillow is installed:
   ```powershell
   pip install Pillow
   ```
3. Test with the simple GUI test:
   ```powershell
   python test_gui_simple.py
   ```

### If you see errors:
- The error message will display in a dialog box
- Check the terminal for detailed error information
- Make sure your folder path has valid image files

## Supported Image Formats
- JPG / JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP
- ICO
- SVG

## Tips
- **Start with Move**: If unsure, use "Move Duplicates" instead of "Delete" to backup files first
- **Review Results**: Always review the duplicate groups before taking action
- **Large Folders**: For folders with many images, the scan may take a few seconds
