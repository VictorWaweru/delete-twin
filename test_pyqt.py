#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

print("Starting test PyQt5 app...")

app = QApplication(sys.argv)
print("QApplication created")

window = QMainWindow()
print("QMainWindow created")

window.setWindowTitle("Test Window")
window.setGeometry(100, 100, 300, 200)
label = QLabel("Hello PyQt5!")
window.setCentralWidget(label)
print("UI setup complete")

window.show()
print("Window shown")

print("Starting event loop...")
sys.exit(app.exec_())
