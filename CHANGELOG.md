# Photo Ninja - Version History

## Version 2.3 (Current) - 2026-06-29
- **NEW: Zero-Byte File Detection** 🗑️
  - Detect and display empty (0-byte) image files
  - Dedicated "Delete Zero-Byte Files" button
  - Zero-byte files shown in red in results
  - Option to disable zero-byte detection
  - "Clean Zero-Byte Files" tool in Tools menu
  - Zero-byte files included in export reports
- Enhanced summary with zero-byte file count
- Updated UI with new controls
- Improved status messages

## Version 2.2 - 2026-06-28
- **NEW: Dark/Light Theme System** 🎨
  - Added ThemeManager class for theme management
  - Light mode (bright, clean interface)
  - Dark mode (easy on the eyes)
  - View menu with theme switcher
  - Theme preference saved and persists across sessions
- Added theme configuration file (`theme_config.txt`)
- Fully themed UI elements (buttons, menus, tree view, status bar)
- Application renamed to **Photo Ninja**

## Version 2.1.1 - 2026-06-28
- Fixed syntax error in main() function
- Removed accidental documentation text from code
- Fixed exe launcher issue (removed console window)
- Created standalone executable

## Version 2.1 - 2026-06-28
- Fixed window management and display issues
- Added missing PyQt5 GUI imports
- Improved window positioning
- Better error handling

## Version 2.0
- Initial working version with full duplicate detection
- PyQt5 GUI interface
- Delete, move, and export functionality