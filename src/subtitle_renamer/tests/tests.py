from src.subtitle_renamer import regexps

def test_regexp():
    regexp = regexps.Regexps()
    assert regexp is not None


from src.subtitle_renamer import scan
import os

def test_scan():

    scanner = scan.Scanner(regexps.Regexps())
    
    # recognize_season_episode function
    test_scenarios = {"file-S15E25.avi":"S15E25", "file 3E12.mp4":"S3E12", "file Season 4 Episode 124.mpg":"S4E124", "file.Season.50.Episode.124.mpg":"S50E124","file.season.630.episode.1.mpg":"S630E1", "test_5x20.mov":"S5E20"}

    for filename, result in test_scenarios.items():
        assert scanner.recognize_season_episode(filename) == result

    # test scanning folder
    vids, srts = scanner.scan_folder(os.path.dirname("src/subtitle_renamer/tests"))
    assert type(vids) == dict
    assert type(srts) == dict
   

from src.subtitle_renamer import rename


def test_rename():
    pass