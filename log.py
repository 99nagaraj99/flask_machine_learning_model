"""
this module takes care of log configuration
"""
import configparser
import json
import logging
from logging.config import dictConfig

CUSTOM = configparser.RawConfigParser()
CUSTOM.optionxform = lambda option: option
CUSTOM.read('config.ini')

LOGGING_CONFIG = list(CUSTOM['log_conf'].values())
LOGGING_CONFIG = LOGGING_CONFIG[0]

dictConfig(json.loads(LOGGING_CONFIG))
logger = logging.getLogger()
