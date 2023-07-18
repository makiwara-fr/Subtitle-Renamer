# -*- coding: utf-8 -*-
# ###################################################################################
#
# 			Your text
#
# 	License:
# 	Author:
#
# 	                __   .__
# 	  _____ _____  |  | _|__|_  _  _______ ____________
# 	 /     \\__  \ |  |/ /  \ \/ \/ /\__  \\_  __ \__  \
# 	|  Y Y  \/ __ \|    <|  |\     /  / __ \|  | \// __ \_
# 	|__|_|  (____  /__|_ \__| \/\_/  (____  /__|  (____  /
# 	      \/     \/     \/                \/           \/
#
# ###################################################################################


import sys
from datetime import datetime
import getopt

from subtitle_renamer import settings as CONFIG
from subtitle_renamer.settings import log as log
from subtitle_renamer import scan
from subtitle_renamer import rename
from subtitle_renamer import regexps


def usage():
    print("Recognised options")
    print("-d, --debug set debug mode to ON")
    print("-h, --help show this help")


def main(arg_list):
    # get params if needed
    # set all parameters according to command line
    # --------------------------------------------
    try:
        opts, args = getopt.getopt(arg_list, "hd", ["help", "debug"])
    except getopt.GetoptError as err:
        log(err, "error")
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--debug"):
            CONFIG.debug = True
            log("Debug mode ON")
    # 		elif opt in ("-o, --output"):
    # 			exported_file = arg

    # Welcome
    print("")
    print("")
    print("")
    print(
        "".join(
            (
                "                 __   .__                              \n",
                "   _____ _____  |  | _|__|_  _  _______ ____________   \n",
                "  /     \\\\__  \ |  |/ /  \ \/ \/ /\__  \\\\_  __ \\__  \\  \n",
                " |  Y Y  \/ __ \|    <|  |\     /  / __ \|  | \// __ \_\n",
                " |__|_|  (____  /__|_ \__| \/\_/  (____  /__|  (____  /\n",
                "      \/     \/     \/                \/           \/ \n",
            )
        )
    )
    print("")
    print("")
    print("")

    print("#######################################")
    print("")
    print("	" + CONFIG.NAME)
    print("")
    print("#######################################")
    print("")

    # checking parameters
    if args == []:
        print("No working folder given exiting.")
        usage()
        sys.exit(0)
    else:
        for a in args:
            print(a)
        # to be done checking beforehand if args contains only folders
        folders = args

    # preparing the scanner for the different folders
    regexps_gen = regexps.Regexps()
    scanner = scan.Scanner(regexps_gen)
    renamer = rename.Renamer(regexps_gen)

    # print("Scanning folders for video files")

    for folder in folders:
        # scanning the folders
        videos, srts = scanner.scan_folder(folder)

        # matching subtitles and videos
        renamer.rename(videos, srts)

    # All done
    print("")
    print("#######################################")
    print("	Thanks for using us")
    print("	See you soon")
    print("#######################################")
    print("")


if __name__ == "__main__":
    main(sys.argv[1:])


def launch():
    main(sys.argv[1:])
