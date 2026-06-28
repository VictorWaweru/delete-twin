#!/usr/bin/env python3
"""
Quick test to verify the GUI window opens and stays open
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget

app = QApplication(sys.argv)

# Create main window
window = QMainWindow()
window.setWindowTitle("✓ Window Test - If you see this, the GUI is working!")
window.setGeometry(200, 200, 600, 400)

# Center window
desktop = QDesktopWidget()
screen_rect = desktop.screenGeometry()
x = (screen_rect.width() - 600) // 2
y = (screen_rect.height() - 400) // 2
window.move(x, y)

# Create simple content
central = QWidget()
window.setCentralWidget(central)
layout = QVBoxLayout(central)
label = QLabel("✓ GUI Window is Working!\n\nIf you can see this, PyQt5 is working correctly.\nYou can close this window.")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

# Ensure window is visible
window.setWindowState(window.windowState() | Qt.WindowActive)
window.raise_()
window.activateWindow()

print("Window opened - showing GUI...")
window.show()

# Run event loop
sys.exit(app.exec_())
