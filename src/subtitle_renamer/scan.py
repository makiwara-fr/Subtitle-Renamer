import os
from subtitle_renamer import settings as CONFIG
import re


class Scanner():

	

	def __init__(self, regexps):
		self.regexps = regexps

	def recognize_season_episode(self, file_name):
		""" Recognize season and episode in the file name and give it back as S[0-9]E[0-9] format. Returns an empty string if unrecognized"""
	
	
		tmp = self.regexps.get_season_episode.search(file_name)
		if (tmp != None):
			split = self.regexps.get_odd_episode_splitter.split(self.regexps.get_odd_season_splitter.split(tmp[0])[1])
			return "S"+split[0].strip().lstrip("0")+"E"+split[1].strip().lstrip("0")
		else:
			tmp = self.regexps.get_odd_season_episode1.search(file_name)
			if tmp != None:
				split = self.regexps.get_odd_season_episode_splitter.split(tmp[0])
				return "S"+split[0].strip().lstrip("0")+"E"+split[1].strip().lstrip("0")
			else:
				tmp = self.regexps.get_odd_season_episode2.search(file_name)
				if tmp != None:
					split = self.regexps.get_odd_episode_splitter2.split(self.regexps.get_odd_season_splitter2.split(tmp[0])[1])
					return "S"+split[0].strip().lstrip("0")+"E"+split[1].strip().lstrip("0")
				
				else:
					# do no recognize season or episode, 
					return ""
	
		
			



	def scan_folder(self, wd):
	
		videos = {}
		srt = {}
	
		# Scanning folder
		print("-------------------------")
		print("Scanning folder :")
		print(wd)
		print("-------------------------")
	
		# scanning all the files
		for entry in os.scandir(wd):
			if entry.is_file():
				# recursive directories should be tackled
				#if CONFIG.debug:
					#print(entry.name)
				# recognize if videos
				if self.regexps.check_video.search(entry.name):
					tmp = self.recognize_season_episode(entry.name)
					if tmp != "":
						#print(tmp)
						videos[tmp] = entry
				elif self.regexps.check_srt.search(entry.name):
					tmp = self.recognize_season_episode(entry.name)
					if tmp != "":
						#print(tmp)
						srt[tmp] = entry
						#srt.append({tmp: entry.name})

		
		
		# feedbacks
		print("Found %s videos" % len(videos))
		print("Found %s subtitles files" % len(srt))
		print("-------------------------")
	
		return videos, srt
	
