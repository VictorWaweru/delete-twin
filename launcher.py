#!/usr/bin/env python3
"""
Clean launcher for Image Duplicate Scanner - runs without console window
"""
import os
import sys
import subprocess

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
delete_py = os.path.join(script_dir, "delete.py")

# Run using pythonw to hide console window
subprocess.Popen([sys.executable.replace("python.exe", "pythonw.exe"), delete_py])
