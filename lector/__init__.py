"""
Lector
~~~~~~~~~~

Interface for Amazon Kindle Data
"""

__version__ = '0.0.3a1'

from .reader import Error, APIError, ConnectionError, LoginError, BrowserError,\
        KindleBook, ReadingProgress, KindleCloudReaderAPI
