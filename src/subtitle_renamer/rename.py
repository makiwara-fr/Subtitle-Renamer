import os


class Renamer:
    def __init__(self, regexps):
        self.regexps = regexps

    def rename(self, videos, srts):
        print("Matching videos and subtitles : ")
        print("--------------------------------")
        i = 0
        for k, v in srts.items():
            try:
                # find matching video
                # print(os.path.join(os.path.dirname(v.path), self.regexps.check_video.split(videos[k].name)[0]+".srt"))
                os.rename(
                    v.path,
                    os.path.join(
                        os.path.dirname(v.path),
                        self.regexps.check_video.split(videos[k].name)[0] + ".srt",
                    ),
                )
                i = i + 1
            except:
                print("No videos found for subtitle : " + str(v.name))

        print(str(i) + " subtitles renamed")
