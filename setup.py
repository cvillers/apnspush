import os
import sys
from setuptools import setup

if sys.version < (2, 6):
	REQUIRES = ["simplejson", "argparse", "notifications"]
else:
	REQUIRES = ["json", "argparse", "notifications"]


setup(
	name = "apnspush",
	version = "0.3.3",
	author = "Cameron Villers",
	author_email = "cameron@ville.rs",
	description = ("A client for the App Notifications service for Apple mobile devices."),
	license = "zlib",
	keywords = "iOS push",
	url = "https://github.com/cvillers/apnspush",
	scripts = ["apnspush.py"],
	install_requires = REQUIRES,
	classifiers = [
		"Development Status :: 4 - Beta"
	]
)
