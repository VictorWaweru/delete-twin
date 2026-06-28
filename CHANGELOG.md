# Image Duplicate Scanner - Version History

## Version 2.2 (Current) - 2026-06-28
- **NEW: Dark/Light Theme System** 🎨
  - Added ThemeManager class for theme management
  - Light mode (bright, clean interface)
  - Dark mode (easy on the eyes)
  - View menu with theme switcher
  - Theme preference saved and persists across sessions
- Added theme configuration file (`theme_config.txt`)
- Fully themed UI elements (buttons, menus, tree view, status bar)
- Backup file: `versions/delete_v2.2.py`

## Version 2.1.1 - 2026-06-28
- Fixed syntax error in main() function
- Removed accidental documentation text from code
- Fixed exe launcher issue (removed console window)
- Created standalone executable (ImageDuplicateScanner.exe)
- Files: `delete.py`, `dist/ImageDuplicateScanner.exe`, `run_scanner.bat`, `run_scanner.vbs`, `launcher.py`
- Backup file: `versions/delete_v2.1.py`

## Version 2.1 - 2026-06-28
- Fixed window management and display issues
- Added missing PyQt5 GUI imports (QFont, QColor, QIcon, QDesktopServices)
- Improved window positioning (centers on screen)
- Updated copyright year to 2026
- Better error handling in scan_finished() method
- Files: `delete.py`, `run_scanner.bat`, `run_scanner.vbs`, `launcher.py`

## Version 2.0
- Initial working version with full duplicate detection
- PyQt5 GUI interface
- Delete, move, and export functionality
- Backup file: `versions/delete_v2.0.py`

---

## How to Use Version History

1. **Latest Version**: Use `delete.py` in the main folder
2. **Previous Versions**: Check the `versions/` folder for backups
3. **Rolling Back**: Copy the old version from `versions/` to the main folder

## File Structure
```
double copy/
├── delete.py                    # Current version (v2.2)
├── dist/ImageDuplicateScanner.exe  # Standalone executable
├── theme_config.txt             # Theme preference storage
├── run_scanner.bat              # Batch file launcher
├── run_scanner.vbs              # VBS launcher
├── launcher.py                  # Python launcher
├── CHANGELOG.md                 # This file
└── versions/
    ├── delete_v2.2.py           # Version 2.2 backup (current)
    ├── delete_v2.1.py           # Version 2.1 backup
    └── delete_v2.0.py           # Version 2.0 backup
```
