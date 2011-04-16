import os
from setuptools import setup

setup(
	name = "Client for App Notifications (4push) for iOS",
	version = "0.1",
	author = "Cameron Villers",
	author_email = "cameron@ville.rs",
	description = ("A client for the App Notifications service for Apple mobile devices."),
	license = "zlib",
	keywords = "iOS push",
	url = "https://github.com/cvillers/apnspush",
	scripts = ["apnspush.py"],
	install_requires = ["notifications"],
	classifiers = [
		"Development Status :: 4 - Beta"
	]
)
