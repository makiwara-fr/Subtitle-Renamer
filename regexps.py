import re
import settings as CONFIG

class Regexps:
	
	def __init__(self):
		# regexp to understand season and episode coding
		self.get_season_episode = re.compile("S[0-9]+E[0-9]+", flags=re.IGNORECASE)
		self.get_odd_season_episode1 = re.compile("[0-9]+x[0-9]+|[0-9]+E[0-9]", flags=re.IGNORECASE)
		self.get_odd_season_episode2 = re.compile("[Season *[0-9]+ +Episode *[0-9]", flags=re.IGNORECASE)
		self.get_odd_season_episode_splitter = re.compile("x|E", flags=re.IGNORECASE)
		self.get_odd_season_splitter = re.compile("S", flags=re.IGNORECASE)
		self.get_odd_episode_splitter = re.compile("E", flags=re.IGNORECASE)
		self.get_odd_season_splitter2 = re.compile("Season +", flags=re.IGNORECASE)
		self.get_odd_episode_splitter2 = re.compile("Episode +", flags=re.IGNORECASE)

		regexp_videos = ""
		regexp_srt = ""

		# regexp to find videos files
		for ext in CONFIG.VIDEOS_EXTENSIONS:
			if regexp_videos == "":
				regexp_videos = "\." + ext + "$"
			else:
				regexp_videos = regexp_videos + "|\." + ext + "$"
		# regexp to find videos files
		for ext in CONFIG.SRT_EXTENSIONS:
			if regexp_srt == "":
				regexp_srt = "\." + ext + "$"
			else:
				regexp_srt = regexp_srt + "|\." + ext + "$"
				
		# Regexp to find videos and subitiles files
		self.check_video = re.compile(regexp_videos, flags=re.IGNORECASE)
		self.check_srt = re.compile(regexp_srt, flags=re.IGNORECASE)