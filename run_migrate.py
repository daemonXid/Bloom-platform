#!/usr/bin/env python
"""Migration wrapper with proper encoding settings"""
import os
import sys
import locale

# Force UTF-8 encoding
os.environ['PYTHONUTF8'] = '1'
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'
os.environ['LANG'] = 'en_US.UTF-8'

# Set locale
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except Exception:
    pass

# Import and run Django management command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.management import execute_from_command_line
execute_from_command_line([sys.argv[0], 'migrate', '--verbosity', '2'])
