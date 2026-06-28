#!/usr/bin/env python3
"""
Photo Ninja - Professional Edition
Version: 2.1.1
Built by GamEGanG
FIXES: Window management, GUI import errors, console window hiding
"""

import os
import sys
import hashlib
import shutil
from collections import defaultdict
from datetime import datetime

# Try to import PyQt5
try:
    from PyQt5 import QtWidgets, QtCore, QtGui
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QCoreApplication
    from PyQt5.QtGui import QFont, QColor, QIcon, QDesktopServices
except ImportError:
    print("PyQt5 not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])
    print("Please restart the script.")
    sys.exit(1)

# Try to import Pillow
try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    print("Please restart the script.")
    sys.exit(1)

class ScannerThread(QThread):
    progress = pyqtSignal(int, str)
    status = pyqtSignal(str)
    done = pyqtSignal(dict)
    error = pyqtSignal(str)
    
    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.running = True
        
    def stop(self):
        self.running = False
        
    def run(self):
        try:
            self.status.emit("🔍 Scanning for images...")
            files = []
            
            # Walk through folder
            for root, dirs, names in os.walk(self.folder):
                if not self.running:
                    return
                for name in names:
                    if not self.running:
                        return
                    ext = os.path.splitext(name)[1].lower()
                    if ext in {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico', '.svg'}:
                        files.append(os.path.join(root, name))
            
            if not files:
                self.status.emit("😕 No images found!")
                self.done.emit({})
                return
            
            self.status.emit(f"📸 Found {len(files)} images. Checking for duplicates...")
            hashes = defaultdict(list)
            
            for i, filepath in enumerate(files):
                if not self.running:
                    return
                try:
                    with Image.open(filepath) as img:
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        img.thumbnail((50, 50))
                        h = hashlib.md5(img.tobytes()).hexdigest()
                        hashes[h].append(filepath)
                except Exception as e:
                    # Skip files that can't be processed
                    continue
                    
                progress = int((i + 1) / len(files) * 100)
                self.progress.emit(progress, f"🔄 Processing {os.path.basename(filepath)}")
            
            duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
            self.status.emit(f"✅ Found {len(duplicates)} duplicate groups")
            self.done.emit(duplicates)
            
        except Exception as e:
            self.error.emit(str(e))

class ThemeManager:
    """Manages light and dark themes"""
    
    LIGHT_THEME = {
        "name": "Light",
        "bg_color": "#ffffff",
        "text_color": "#2c3e50",
        "header_bg": "#ecf0f1",
        "button_bg": "#3498db",
        "button_hover": "#2980b9",
        "danger_bg": "#e74c3c",
        "danger_hover": "#c0392b",
        "success_bg": "#27ae60",
        "success_hover": "#229954",
        "warning_bg": "#e67e22",
        "warning_hover": "#d35400",
        "info_bg": "#9b59b6",
        "info_hover": "#8e44ad",
        "border_color": "#bdc3c7",
        "tree_bg": "#ffffff",
        "tree_selected": "#3498db",
        "statusbar_bg": "#ecf0f1"
    }
    
    DARK_THEME = {
        "name": "Dark",
        "bg_color": "#1e1e1e",
        "text_color": "#e0e0e0",
        "header_bg": "#2d2d2d",
        "button_bg": "#0d47a1",
        "button_hover": "#1565c0",
        "danger_bg": "#c62828",
        "danger_hover": "#d32f2f",
        "success_bg": "#1b5e20",
        "success_hover": "#2e7d32",
        "warning_bg": "#e65100",
        "warning_hover": "#ef6c00",
        "info_bg": "#6a1b9a",
        "info_hover": "#7b1fa2",
        "border_color": "#424242",
        "tree_bg": "#2d2d2d",
        "tree_selected": "#0d47a1",
        "statusbar_bg": "#2d2d2d"
    }
    
    def __init__(self):
        self.current_theme = self.LIGHT_THEME
        self.load_theme()
    
    def load_theme(self):
        """Load saved theme preference"""
        theme_file = os.path.join(os.path.dirname(__file__), "theme_config.txt")
        try:
            if os.path.exists(theme_file):
                with open(theme_file, 'r') as f:
                    theme_name = f.read().strip()
                    if theme_name == "Dark":
                        self.current_theme = self.DARK_THEME
                    else:
                        self.current_theme = self.LIGHT_THEME
        except:
            pass
    
    def save_theme(self, theme_name):
        """Save theme preference"""
        theme_file = os.path.join(os.path.dirname(__file__), "theme_config.txt")
        try:
            with open(theme_file, 'w') as f:
                f.write(theme_name)
        except:
            pass
    
    def get_stylesheet(self, theme):
        """Generate stylesheet for given theme"""
        t = theme
        return f"""
            QMainWindow, QDialog {{ background-color: {t['bg_color']}; color: {t['text_color']}; }}
            QLabel {{ color: {t['text_color']}; }}
            QLineEdit {{ background-color: {t['header_bg']}; color: {t['text_color']}; border: 1px solid {t['border_color']}; padding: 5px; border-radius: 3px; }}
            QPushButton {{ background-color: {t['button_bg']}; color: white; padding: 5px 15px; border-radius: 4px; font-weight: bold; border: none; }}
            QPushButton:hover {{ background-color: {t['button_hover']}; }}
            QPushButton:pressed {{ background-color: {t['button_hover']}; }}
            QGroupBox {{ color: {t['text_color']}; border: 1px solid {t['border_color']}; border-radius: 4px; margin-top: 10px; padding-top: 10px; }}
            QGroupBox::title {{ subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }}
            QTreeWidget {{ background-color: {t['tree_bg']}; color: {t['text_color']}; border: 1px solid {t['border_color']}; alternate-background-color: {t['header_bg']}; }}
            QTreeWidget::item:selected {{ background-color: {t['tree_selected']}; color: white; }}
            QProgressBar {{ background-color: {t['header_bg']}; color: {t['text_color']}; border: 2px solid {t['border_color']}; border-radius: 5px; text-align: center; height: 25px; font-weight: bold; }}
            QProgressBar::chunk {{ background-color: {t['success_bg']}; border-radius: 5px; }}
            QStatusBar {{ background-color: {t['statusbar_bg']}; color: {t['text_color']}; border-top: 1px solid {t['border_color']}; }}
            QMenuBar {{ background-color: {t['header_bg']}; color: {t['text_color']}; }}
            QMenuBar::item:selected {{ background-color: {t['button_bg']}; }}
            QMenu {{ background-color: {t['header_bg']}; color: {t['text_color']}; }}
            QMenu::item:selected {{ background-color: {t['button_bg']}; }}
        """

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.duplicates = {}
        self.scanner = None
        self.theme_manager = ThemeManager()
        self.setup_ui()
        self.setup_menubar()
        self.apply_theme()
        
    def setup_ui(self):
        self.setWindowTitle("🥋 Photo Ninja")
        self.setGeometry(200, 200, 900, 650)
        
        # Center window on screen
        from PyQt5.QtWidgets import QDesktopWidget
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - 900) // 2
        y = (screen_rect.height() - 650) // 2
        self.move(x, y)
        
        # Make window stay on top and visible
        self.setWindowState(self.windowState() | Qt.WindowActive)
        self.raise_()
        self.activateWindow()
        
        # Set window icon
        try:
            self.setWindowIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        except:
            pass
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        
        # Header
        header = QLabel("🥋 Photo Ninja")
        header.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; padding: 5px;")
        layout.addWidget(header)
        
        # Folder selection
        folder_group = QGroupBox("📁 Select Folder")
        folder_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        folder_layout = QHBoxLayout(folder_group)
        
        self.folder_edit = QLineEdit()
        self.folder_edit.setReadOnly(True)
        self.folder_edit.setPlaceholderText("Choose a folder with images...")
        folder_layout.addWidget(self.folder_edit)
        
        browse_btn = QPushButton("📂 Browse...")
        browse_btn.clicked.connect(self.browse_folder)
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 5px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        folder_layout.addWidget(browse_btn)
        
        layout.addWidget(folder_group)
        
        # Controls
        control_group = QGroupBox("🚀 Controls")
        control_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        control_layout = QVBoxLayout(control_group)
        
        button_layout = QHBoxLayout()
        
        self.scan_btn = QPushButton("🔍 Start Scan")
        self.scan_btn.clicked.connect(self.start_scan)
        self.scan_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        button_layout.addWidget(self.scan_btn)
        
        self.stop_btn = QPushButton("⏹️ Stop")
        self.stop_btn.clicked.connect(self.stop_scan)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        button_layout.addWidget(self.stop_btn)
        
        button_layout.addStretch()
        control_layout.addLayout(button_layout)
        
        # Progress
        self.progress = QProgressBar()
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                text-align: center;
                height: 25px;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #2ecc71;
                border-radius: 5px;
            }
        """)
        control_layout.addWidget(self.progress)
        
        self.status_label = QLabel("💡 Ready to scan. Select a folder and click 'Start Scan'")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("padding: 5px; color: #2c3e50;")
        control_layout.addWidget(self.status_label)
        
        layout.addWidget(control_group)
        
        # Results
        results_group = QGroupBox("📊 Results")
        results_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        results_layout = QVBoxLayout(results_group)
        
        # Summary
        self.summary_label = QLabel("No scan results yet")
        self.summary_label.setStyleSheet("padding: 5px; background-color: #ecf0f1; border-radius: 4px;")
        results_layout.addWidget(self.summary_label)
        
        # Tree
        self.results_tree = QTreeWidget()
        self.results_tree.setHeaderLabels(["📁 File", "📏 Size", "📂 Location"])
        self.results_tree.setAlternatingRowColors(True)
        self.results_tree.setStyleSheet("""
            QTreeWidget {
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 5px;
            }
            QTreeWidget::item {
                padding: 3px;
            }
            QTreeWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        self.results_tree.itemDoubleClicked.connect(self.open_file_location)
        results_layout.addWidget(self.results_tree)
        
        # Actions
        action_layout = QHBoxLayout()
        
        self.delete_btn = QPushButton("🗑️ Delete Duplicates")
        self.delete_btn.clicked.connect(self.delete_duplicates)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setStyleSheet("""
            QPushButton:enabled {
                background-color: #e67e22;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:enabled:hover {
                background-color: #d35400;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
                padding: 8px 15px;
                border-radius: 4px;
            }
        """)
        action_layout.addWidget(self.delete_btn)
        
        self.move_btn = QPushButton("📦 Move Duplicates")
        self.move_btn.clicked.connect(self.move_duplicates)
        self.move_btn.setEnabled(False)
        self.move_btn.setStyleSheet("""
            QPushButton:enabled {
                background-color: #3498db;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:enabled:hover {
                background-color: #2980b9;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
                padding: 8px 15px;
                border-radius: 4px;
            }
        """)
        action_layout.addWidget(self.move_btn)
        
        self.export_btn = QPushButton("📝 Export Report")
        self.export_btn.clicked.connect(self.export_report)
        self.export_btn.setEnabled(False)
        self.export_btn.setStyleSheet("""
            QPushButton:enabled {
                background-color: #9b59b6;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:enabled:hover {
                background-color: #8e44ad;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
                color: #7f8c8d;
                padding: 8px 15px;
                border-radius: 4px;
            }
        """)
        action_layout.addWidget(self.export_btn)
        
        action_layout.addStretch()
        results_layout.addLayout(action_layout)
        
        layout.addWidget(results_group)
        
        # Status bar
        self.status_bar = self.statusBar()
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #ecf0f1;
                padding: 3px;
                border-top: 1px solid #bdc3c7;
            }
        """)
        self.status_bar.showMessage("🟢 Ready")
        
        # Add permanent status
        self.status_progress = QProgressBar()
        self.status_progress.setMaximumWidth(150)
        self.status_progress.setVisible(False)
        self.status_bar.addPermanentWidget(self.status_progress)
        
        # Make sure window stays open
        self.setAttribute(Qt.WA_DeleteOnClose, False)
        
    def setup_menubar(self):
        """Setup menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        open_action = QAction("&Open Folder", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.browse_folder)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu (Theme)
        view_menu = menubar.addMenu("&View")
        
        light_theme_action = QAction("☀️ Light Mode", self)
        light_theme_action.triggered.connect(lambda: self.switch_theme("Light"))
        view_menu.addAction(light_theme_action)
        
        dark_theme_action = QAction("🌙 Dark Mode", self)
        dark_theme_action.triggered.connect(lambda: self.switch_theme("Dark"))
        view_menu.addAction(dark_theme_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        help_action = QAction("&Help", self)
        help_action.setShortcut("F1")
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "📁 Select Folder with Images",
            self.folder_edit.text() or os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        if folder:
            self.folder_edit.setText(folder)
            self.scan_btn.setEnabled(True)
            self.status_bar.showMessage(f"📁 Selected: {folder}")
            
            # Quick count
            try:
                count = 0
                for root, dirs, files in os.walk(folder):
                    for f in files:
                        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                            count += 1
                if count > 0:
                    self.status_label.setText(f"📸 Found {count} images in this folder")
            except:
                pass
    
    def start_scan(self):
        folder = self.folder_edit.text()
        if not folder or not os.path.exists(folder):
            QMessageBox.warning(
                self,
                "⚠️ No Folder Selected",
                "Please select a valid folder first.\nClick 'Browse...' to choose a folder."
            )
            return
        
        # Clear previous results
        self.results_tree.clear()
        self.duplicates = {}
        self.delete_btn.setEnabled(False)
        self.move_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.summary_label.setText("🔄 Scanning in progress...")
        
        # Create and start scanner thread
        self.scanner = ScannerThread(folder)
        self.scanner.progress.connect(self.update_progress)
        self.scanner.status.connect(self.update_status)
        self.scanner.done.connect(self.scan_finished)
        self.scanner.error.connect(self.scan_error)
        
        self.scan_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress.setValue(0)
        self.status_progress.setVisible(True)
        self.status_progress.setValue(0)
        
        self.scanner.start()
        self.status_bar.showMessage("🔄 Scanning...")
        self.status_label.setText("🔍 Starting scan...")
    
    def stop_scan(self):
        if self.scanner and self.scanner.isRunning():
            reply = QMessageBox.question(
                self,
                "⏹️ Stop Scan?",
                "Are you sure you want to stop the scan?\nProgress will be lost.",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.scanner.stop()
                self.scanner.wait()  # Wait for thread to finish
                self.status_label.setText("⏹️ Scan stopped by user")
                self.status_bar.showMessage("⏹️ Stopped")
                self.scan_btn.setEnabled(True)
                self.stop_btn.setEnabled(False)
                self.status_progress.setVisible(False)
                self.summary_label.setText("Scan was stopped by user")
    
    def update_progress(self, value, status):
        self.progress.setValue(value)
        self.status_progress.setValue(value)
        self.status_label.setText(status)
    
    def update_status(self, status):
        self.status_label.setText(status)
        self.status_bar.showMessage(status)
    
    def scan_finished(self, duplicates):
        """Handle scan completion - KEEP WINDOW OPEN"""
        try:
            self.duplicates = duplicates
            self.scan_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            self.status_progress.setVisible(False)
            
            if duplicates:
                total = sum(len(paths) - 1 for paths in duplicates.values())
                total_size = 0
                for paths in duplicates.values():
                    for path in paths[1:]:
                        try:
                            total_size += os.path.getsize(path)
                        except:
                            pass
                
                self.summary_label.setText(
                    f"🎉 Found {len(duplicates)} duplicate groups ({total} files, {total_size / (1024**2):.1f} MB)"
                )
                self.status_label.setText(f"✅ Complete! Found {total} duplicate files")
                self.status_bar.showMessage(f"✅ Complete! Found {total} duplicate files")
                self.delete_btn.setEnabled(True)
                self.move_btn.setEnabled(True)
                self.export_btn.setEnabled(True)
                self.display_results()
                
                # Show success message - WINDOW STAYS OPEN
                QMessageBox.information(
                    self,
                    "✅ Scan Complete",
                    f"Found {len(duplicates)} duplicate groups!\n"
                    f"Total duplicate files: {total}\n"
                    f"Space that can be freed: {total_size / (1024**2):.1f} MB\n\n"
                    "Review the results and choose an action below."
                )
            else:
                self.summary_label.setText("✅ No duplicates found! Your folder is clean.")
                self.status_label.setText("✅ No duplicates found")
                self.status_bar.showMessage("✅ No duplicates found")
                
                QMessageBox.information(
                    self,
                    "✅ Clean Folder",
                    "No duplicate images found in this folder!\n"
                    "Your photo collection is already organized."
                )
            
            # IMPORTANT: Don't close the window
            self.raise_()
            self.activateWindow()
        except Exception as e:
            print(f"ERROR in scan_finished: {e}")
            import traceback
            traceback.print_exc()
            self.status_label.setText(f"❌ Error in scan_finished: {e}")
            QMessageBox.critical(self, "Error", f"Error processing scan results:\n{e}")
    
    def scan_error(self, error):
        """Handle scan errors - KEEP WINDOW OPEN"""
        self.status_label.setText(f"❌ Error: {error}")
        self.status_bar.showMessage("❌ Error occurred")
        self.scan_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.status_progress.setVisible(False)
        self.summary_label.setText(f"❌ Error: {error}")
        
        QMessageBox.critical(
            self,
            "❌ Scan Error",
            f"An error occurred during scanning:\n\n{error}\n\n"
            "Please try again with a different folder."
        )
        
        # IMPORTANT: Don't close the window
        self.raise_()
        self.activateWindow()
    
    def display_results(self):
        self.results_tree.clear()
        
        for group_id, paths in enumerate(self.duplicates.values(), 1):
            # Group header
            group = QTreeWidgetItem(self.results_tree)
            group.setText(0, f"📁 Group {group_id} ({len(paths)} files)")
            font = QFont()
            font.setBold(True)
            group.setFont(0, font)
            group.setForeground(0, QColor(46, 125, 50))
            
            # Original (first/largest)
            orig = QTreeWidgetItem(group)
            orig.setText(0, f"✅ {os.path.basename(paths[0])} (original)")
            try:
                size = os.path.getsize(paths[0])
                orig.setText(1, f"{size / 1024:.1f} KB")
            except:
                orig.setText(1, "Unknown")
            orig.setText(2, os.path.dirname(paths[0]))
            orig.setForeground(0, QColor(46, 125, 50))
            
            # Duplicates
            for path in paths[1:]:
                dup = QTreeWidgetItem(group)
                dup.setText(0, f"❌ {os.path.basename(path)}")
                try:
                    size = os.path.getsize(path)
                    dup.setText(1, f"{size / 1024:.1f} KB")
                except:
                    dup.setText(1, "Unknown")
                dup.setText(2, os.path.dirname(path))
                dup.setForeground(0, QColor(200, 0, 0))
        
        self.results_tree.expandAll()
        for i in range(3):
            self.results_tree.resizeColumnToContents(i)
    
    def open_file_location(self, item, column):
        if item.parent():  # Only for file items
            path = item.text(2)
            if os.path.exists(path):
                QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(path))
    
    def delete_duplicates(self):
        if not self.duplicates:
            return
        
        total = sum(len(paths) - 1 for paths in self.duplicates.values())
        total_size = 0
        for paths in self.duplicates.values():
            for path in paths[1:]:
                try:
                    total_size += os.path.getsize(path)
                except:
                    pass
        
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("⚠️ Confirm Deletion")
        msg.setText(f"Delete {total} duplicate files?")
        msg.setInformativeText(
            f"This will free up {total_size / (1024**2):.1f} MB of space.\n\n"
            "⚠️ This action cannot be undone!\n"
            "The original files will be kept."
        )
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.button(QMessageBox.Yes).setText("🗑️ Yes, Delete")
        msg.button(QMessageBox.No).setText("❌ No, Cancel")
        
        if msg.exec_() != QMessageBox.Yes:
            return
        
        # Delete
        deleted = 0
        total_deleted = 0
        errors = []
        
        self.status_bar.showMessage("🗑️ Deleting duplicates...")
        self.status_label.setText("🗑️ Deleting duplicate files...")
        
        for paths in self.duplicates.values():
            for path in paths[1:]:
                try:
                    size = os.path.getsize(path)
                    os.remove(path)
                    deleted += 1
                    total_deleted += size
                except Exception as e:
                    errors.append(f"{os.path.basename(path)}: {str(e)}")
        
        # Refresh results
        self.duplicates = {h: [p for p in paths if os.path.exists(p)] 
                          for h, paths in self.duplicates.items() if any(os.path.exists(p) for p in paths)}
        self.duplicates = {h: paths for h, paths in self.duplicates.items() if len(paths) > 1}
        
        if self.duplicates:
            self.display_results()
        else:
            self.results_tree.clear()
            self.summary_label.setText("✅ All duplicates have been deleted!")
            self.delete_btn.setEnabled(False)
            self.move_btn.setEnabled(False)
            self.export_btn.setEnabled(False)
        
        if errors:
            QMessageBox.warning(
                self,
                "⚠️ Completed with Errors",
                f"Deleted {deleted} files.\n"
                f"Freed {total_deleted / (1024**2):.1f} MB.\n\n"
                f"Errors with {len(errors)} files."
            )
        else:
            QMessageBox.information(
                self,
                "✅ Deletion Complete",
                f"Deleted {deleted} duplicate files!\n"
                f"Freed {total_deleted / (1024**2):.1f} MB of space."
            )
        
        self.status_bar.showMessage(f"✅ Deleted {deleted} files, freed {total_deleted / (1024**2):.1f} MB")
    
    def move_duplicates(self):
        if not self.duplicates:
            return
        
        dest = QFileDialog.getExistingDirectory(
            self,
            "📦 Select Destination Folder for Duplicates",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if not dest:
            return
        
        # Create duplicates folder
        dup_folder = os.path.join(dest, "duplicates_backup")
        os.makedirs(dup_folder, exist_ok=True)
        
        total = sum(len(paths) - 1 for paths in self.duplicates.values())
        
        reply = QMessageBox.question(
            self,
            "📦 Confirm Move",
            f"Move {total} duplicate files to:\n{dup_folder}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.No:
            return
        
        moved = 0
        total_moved = 0
        errors = []
        
        self.status_bar.showMessage("📦 Moving duplicates...")
        self.status_label.setText("📦 Moving duplicate files...")
        
        for paths in self.duplicates.values():
            for path in paths[1:]:
                try:
                    # Preserve structure
                    rel_path = os.path.relpath(path, self.folder_edit.text())
                    dest_path = os.path.join(dup_folder, rel_path)
                    dest_dir = os.path.dirname(dest_path)
                    os.makedirs(dest_dir, exist_ok=True)
                    
                    # Handle duplicate names
                    if os.path.exists(dest_path):
                        base, ext = os.path.splitext(dest_path)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        dest_path = f"{base}_{timestamp}{ext}"
                    
                    size = os.path.getsize(path)
                    shutil.move(path, dest_path)
                    moved += 1
                    total_moved += size
                except Exception as e:
                    errors.append(f"{os.path.basename(path)}: {str(e)}")
        
        # Refresh results
        self.duplicates = {h: [p for p in paths if os.path.exists(p)] 
                          for h, paths in self.duplicates.items() if any(os.path.exists(p) for p in paths)}
        self.duplicates = {h: paths for h, paths in self.duplicates.items() if len(paths) > 1}
        
        if self.duplicates:
            self.display_results()
        else:
            self.results_tree.clear()
            self.summary_label.setText("✅ All duplicates have been moved!")
            self.delete_btn.setEnabled(False)
            self.move_btn.setEnabled(False)
            self.export_btn.setEnabled(False)
        
        if errors:
            QMessageBox.warning(
                self,
                "⚠️ Completed with Errors",
                f"Moved {moved} files.\n"
                f"Total size: {total_moved / (1024**2):.1f} MB.\n\n"
                f"Errors with {len(errors)} files."
            )
        else:
            QMessageBox.information(
                self,
                "✅ Move Complete",
                f"Moved {moved} duplicate files!\n"
                f"Total size: {total_moved / (1024**2):.1f} MB\n\n"
                f"Files are stored in:\n{dup_folder}"
            )
        
        self.status_bar.showMessage(f"✅ Moved {moved} files to backup folder")
    
    def export_report(self):
        if not self.duplicates:
            QMessageBox.information(self, "📝 No Report", "No duplicates to report.")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "💾 Save Report",
            f"duplicate_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "Text Files (*.txt)"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("🖼️ IMAGE DUPLICATE REPORT\n")
                f.write("=" * 80 + "\n")
                f.write(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"📁 Folder: {self.folder_edit.text()}\n")
                f.write("=" * 80 + "\n\n")
                
                total = sum(len(paths) - 1 for paths in self.duplicates.values())
                total_size = 0
                for paths in self.duplicates.values():
                    for path in paths[1:]:
                        try:
                            total_size += os.path.getsize(path)
                        except:
                            pass
                
                f.write("📊 SUMMARY\n")
                f.write("-" * 40 + "\n")
                f.write(f"Total duplicate groups: {len(self.duplicates)}\n")
                f.write(f"Total duplicate files: {total}\n")
                f.write(f"Total duplicate size: {total_size / (1024**2):.1f} MB\n\n")
                
                f.write("📋 DUPLICATE DETAILS\n")
                f.write("-" * 80 + "\n\n")
                
                for idx, (h, paths) in enumerate(self.duplicates.items(), 1):
                    f.write(f"Group {idx} (Hash: {h[:16]}...)\n")
                    f.write("  " + "-" * 76 + "\n")
                    f.write(f"  ✅ ORIGINAL: {paths[0]}\n")
                    try:
                        f.write(f"     Size: {os.path.getsize(paths[0]) / 1024:.1f} KB\n")
                    except:
                        pass
                    f.write(f"\n  ❌ DUPLICATES ({len(paths) - 1}):\n")
                    for path in paths[1:]:
                        f.write(f"    - {path}\n")
                        try:
                            f.write(f"      Size: {os.path.getsize(path) / 1024:.1f} KB\n")
                        except:
                            pass
                    f.write("\n")
                
                f.write("=" * 80 + "\n")
                f.write("📌 End of report\n")
            
            QMessageBox.information(
                self,
                "💾 Report Saved",
                f"Report saved to:\n{file_path}\n\n"
                f"Size: {os.path.getsize(file_path) / 1024:.1f} KB"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "❌ Export Error", f"Error exporting report:\n\n{e}")
    
    def show_about(self):
        QMessageBox.about(
            self,
            "About Photo Ninja",
            "🥋 Photo Ninja\n\n"
            "Version: 2.1.1\n"
            "Built by GamEGanG\n\n"
            "A simple tool to find and remove duplicate images.\n\n"
            "Features:\n"
            "• Fast scanning with image comparison\n"
            "• Delete or move duplicates\n"
            "• Export detailed reports\n"
            "• User-friendly interface\n"
            "• Fixed window management and GUI imports\n\n"
            "© 2026 GamEGanG - All Rights Reserved"
        )
    
    def show_help(self):
        help_text = """
        📖 How to Use Photo Ninja
        
        1. 📁 Select a Folder
           • Click "Browse..." or use File > Open Folder
           • Choose a folder with your images
        
        2. 🔍 Start Scanning
           • Click "Start Scan" to begin
           • Watch the progress bar
        
        3. 📊 Review Results
           • Green = Original (kept)
           • Red = Duplicate (to remove)
           • Double-click to open file location
        
        4. 🗑️ Take Action
           • Delete Duplicates: Permanently remove
           • Move Duplicates: Move to backup folder
           • Export Report: Save detailed list
        
        💡 Tips:
        • Use "Move Duplicates" first if unsure
        • Always review before deleting
        • The largest/highest quality version is kept
        """
        
        QMessageBox.information(self, "📖 Help", help_text)
    
    def apply_theme(self):
        """Apply the current theme to the window"""
        stylesheet = self.theme_manager.get_stylesheet(self.theme_manager.current_theme)
        self.setStyleSheet(stylesheet)
    
    def switch_theme(self, theme_name):
        """Switch between light and dark themes"""
        if theme_name == "Dark":
            self.theme_manager.current_theme = self.theme_manager.DARK_THEME
        else:
            self.theme_manager.current_theme = self.theme_manager.LIGHT_THEME
        
        self.theme_manager.save_theme(theme_name)
        self.apply_theme()
        
        QMessageBox.information(
            self,
            "Theme Changed",
            f"✅ Switched to {theme_name} Mode\n\nThe theme will persist when you restart the app."
        )
    
    def closeEvent(self, event):
        """Handle window close event - properly clean up"""
        if self.scanner and self.scanner.isRunning():
            reply = QMessageBox.question(
                self,
                "❓ Scan in Progress",
                "A scan is still running.\nDo you want to stop and exit?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.scanner.stop()
                self.scanner.wait()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

def main():
    try:
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        app.setApplicationName("Photo Ninja")
        
        # Set application icon
        try:
            app.setWindowIcon(QIcon())
        except:
            pass
        
        # Create and show main window
        window = MainWindow()
        window.show()
        
        # Start event loop - THIS KEEPS THE APP RUNNING
        exit_code = app.exec_()
        return exit_code
        
    except Exception as e:
        print(f"ERROR in main(): {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    main()