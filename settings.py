

import logging

debug = True



DEFAULT_EXPORT_PATH = "./output/"
DEFAULT_INPUT_PATH ="./input/"
NAME = "Auto subtitle renamers"
VERSION = "0"
VIDEOS_EXTENSIONS = ["mkv", "avi", "mp4"]
SRT_EXTENSIONS = ["srt"]


def log(str, level="info"):
	
	if level == "info":
		print(str)
		logging.info(str)
	else:
		if debug: 
			print(str)
		if level == "debug":
			logging.debug(str)
		elif level == "error":
			logging.error(str)
		else:
			logging.info(str)
	