#! /usr/bin/env python
#-*- coding: utf-8 -*-



import os
import configparser
# load the configuration
config = configparser.SafeConfigParser()
try:
    config.read("./conf.cfg")
except:
    config.read("./conf.cfg-sample")

PATH = os.path.abspath(".")

NB_BITS = int(config.get('globals','nb_bits'))

IRC_CHANNEL = config.get('irc','channel')
IRKER_HOST = config.get('irc','host')
IRKER_PORT = int(config.get('irc','port'))

MAIL_ENABLED = bool(int(config.get('email','enabled')))
MAIL_FROM = config.get('email','mail_from')
MAIL_TO = [config.get('email','mail_to')]
SMTP_SERVER = config.get('email','smtp')
USERNAME =  config.get('email','username')
PASSWORD =  config.get('email','password')

BITMESSAGE_ENABLED = bool(int(config.get('bitmessage','enabled')))
BITMESSAGE_FROM = config.get('bitmessage','from')
BITMESSAGE_TO = config.get('bitmessage','to')
API_PORT = int(config.get('bitmessage','apiport'))
API_INTERFACE = config.get('bitmessage','apiinterface')
BITMESSAGE_USERNAME =  config.get('bitmessage','apiusername')
BITMESSAGE_PASSWORD =  config.get('bitmessage','apipassword')

# address of the log file :
LOGS = os.path.join(PATH, "log")
# address of the database of hash values :
DATABASE = os.path.join(PATH, "base")
# address of the signature of the database:
DATABASE_SIG = os.path.join(PATH, "database.sig")

# path of the private key (to sign the database of hash values) :
PRIVATE_KEY = os.path.join(PATH, "pyhids_rsa")
# path of the public key (to check the integrity of the database) :
PUBLIC_KEY = os.path.join(PATH, "pyhids_rsa.pub")


# specific files to scan :
SPECIFIC_FILES_TO_SCAN = [ \
        os.path.join(PATH, "pyHIDS.py"),
        os.path.join(PATH, "conf.py"),
        os.path.join(PATH, "conf.cfg")]
for name, current_file in config.items("files"):
    SPECIFIC_FILES_TO_SCAN.append(current_file)

# rules to scan folders : ]
FOLDER_RULES = []
for name, rule in config.items("rules"):
    pattern, folfer = rule.split(' ')
    FOLDER_RULES.append((pattern, folfer))

# Output of commands :
COMMANDS = []
for name, command in config.items("commands"):
    COMMANDS.append(tuple(command.split(' ')))
