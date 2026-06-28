# Image Duplicate Scanner - Version History

## Version 2.1 (Current) - 2026-06-28
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
├── delete.py                    # Current version (v2.1)
├── run_scanner.bat              # Batch file launcher
├── run_scanner.vbs              # VBS launcher
├── launcher.py                  # Python launcher
├── CHANGELOG.md                 # This file
└── versions/
    └── delete_v2.0.py           # Previous version backup
```
