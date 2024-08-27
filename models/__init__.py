#!/usr/bin/pyhton3
"""program initialization"""

from models.engine import TheStorage

storage = TheStorage()
storage.reload()
