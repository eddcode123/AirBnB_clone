#!/usr/bin/python3
"""__init__ majic method for models directory"""
from .file_storage import FileStorage


storage = FileStorage()
storage.reload()
