#!/usr/bin/env python
"""
Migration script that sets proper environment to avoid encoding issues on Windows
"""
import os
import sys

# Set environment to avoid psycopg2 encoding issues
os.environ['PGCLIENTENCODING'] = 'UTF8'
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Prevent psycopg2 from trying to read system PostgreSQL config files
os.environ['PGSYSCONFDIR'] = ''
os.environ['PGSERVICEFILE'] = ''

# Now import Django and run migrate
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed?"
    ) from exc

execute_from_command_line([sys.argv[0], 'migrate'])
