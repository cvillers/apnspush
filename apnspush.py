# vim: set ft=python :

import notifications
import argparse
try:
	import json
except ImportError:
	import simplejson as json
import sys
import os

DEFAULT_CONFIG = "/etc/apnspush.conf"
EPILOG = "API keys must be put in the configuration file (default %s)." % DEFAULT_CONFIG

###############################################################################

parser = argparse.ArgumentParser(description = "Client for App Notifications (4push) for iOS", epilog = EPILOG)

parser.add_argument("--config", help="config file location", default=DEFAULT_CONFIG)
parser.add_argument("--debug", type=bool, default=False, metavar='')
parser.add_argument("-t", "--title", help="message title", type=str)
parser.add_argument("-s", "--subtitle", help="message subtitle", type=str)
parser.add_argument("-p", "--long-message-preview", help="long message preview", type=str)
parser.add_argument("-i", "--icon-url", help="icon URL", type=str)
parser.add_argument("-v", "--message-level", help="message severity", choices=range(-2, 3), type=int)
parser.add_argument("-b", "--button-text", help="text on the action button (only displays when mobile device is not locked)", type=str)
parser.add_argument("-c", "--command", help="command to run when the action button is invoked (in iOS URI format)", type=str)
parser.add_argument("-u", "--users", help="list of users defined in the configuration file to send the message to (default all)", type=str, default="all", dest="clients")

soundGroup = parser.add_mutually_exclusive_group()
soundGroup.add_argument("-q", "--silent-message", help="do not play a sound for the recipient", type=bool, default=False, metavar='')
soundGroup.add_argument("-n", "--sound", help="sound to play on the mobile device", choices=range(1, 8), type=int, default=1)

longGroup = parser.add_mutually_exclusive_group()
longGroup.add_argument("-l", "--long-message", help="long message displayed in application", type=str)
longGroup.add_argument("-r", "--read-long-message", help="read the long message from standard input", type=bool, metavar='')

parser.add_argument("message", help="message text displayed in notfication", type=str, action="store")

args = parser.parse_args()

###############################################################################

if not os.path.isfile(args.config):
	print("Could not load config file %s" % args.config)
	sys.exit(1)

f = open(args.config)
config = json.load(f)
f.close()

###############################################################################

longMessage = ""

if(args.read_long_message):
	longMessage = sys.stdin.read()
else:
	longMessage = args.long_message

###############################################################################

clients = []

if args.clients == "all":
	clients = config["keys"].keys()
else:
	clients = args.clients.split(',')

for key in clients:
	if not key in config["keys"]:
		print("Unknown client %s" % key)
		sys.exit(2)
	notifications.send(config["keys"][key], args.message, args.title, args.subtitle, longMessage, args.long_message_preview, args.icon_url, args.message_level, args.silent_message, args.button_text, args.command, args.sound, args.debug)
