#!/usr/bin/env python

import sys
import os
import getopt

VERSION = "1.0.1"
REPLACE_TAG = "{{64}}"

def main(argv):
    basesixfour = ""
    inpath = ""
    outpath = ""
    i = 0

    try:
        opts, args = getopt.getopt(argv, "hi:o:v", ["image=","html=","help","version"])
    except getopt.GetoptError:
        print "Usage: sixfour.py [-hiov][--image=,--html=,--help,--version] <arg(s)>"
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-i', '--image'):
            inpath = arg
            i += 1
        elif opt in ('-o', '--html'):
            outpath = arg
            i += 1
        elif opt in ('-v', '--version'):
            version()
            sys.exit(0)

    if i < 1:
        print("Failed to enter image file path.")
    elif i == 1:
        basesixfour = sixfourit(inpath)
        print(basesixfour)
    elif i == 2:
        basesixfour = sixfourit(inpath)
        basesixfour_stripped = basesixfour.rstrip()
        insertimg(outpath, basesixfour_stripped, inpath)




def help():
    helpstring = """
-----------------------------------
sixfour
Copyright 2013 Christopher Simpkins
MIT License
-----------------------------------

DESCRIPTION
sixfour is a base64 encoder for images that will optionally insert an appropriately tagged base64 encoded image in a HTML or Markdown document.

USAGE
  sixfour [-hio] [--image=,--html=,--help] <arg(s)>

OPTIONS
  -h --help     - view this help documentation
  -i --image    - image file path
  -o --html     - HTML file path (for <img> tag insertion)
  -v --version  - show application version

EXAMPLE
  sixfour.py -i "img/image.png" -o "index.html"

NOTES
## To access the data through the standard output stream:
To push the base64 encoded image data through the standard output stream, use the image filepath only (-i or --image).

## To insert a base64 encoded image in a HTML or Markdown file
Use the replacement tag {{64}} in your HTML or Markdown file at the location where you would like to insert a base64 data URI in an HTML <img> tag.
    """
    print(helpstring)

def insertimg(htmlpath, base64string, imgpath):
    htmlstring = ""
    try:
        with open(htmlpath, "r+") as f:
            htmlstring = f.read()
            f.seek(0)
            the_b64 = makeimgtag(base64string, imgpath)
            new_htmlstring = htmlstring.replace(REPLACE_TAG, the_b64)
            f.write(new_htmlstring)
            f.close()
            print("Insertion completed successfully")
    except Exception, e:
        print("Unable to insert your base64 encoded image tag.")
        print(str(e))
        sys.exit(1)

def makeimgtag(base64string, imgfile):
    pretag = """<img src="data:image/png;base64, """
    basefile = os.path.basename(imgfile)
    basename = os.path.splitext(basefile)[0]
    posttag = '" ' + "alt='" + basename + "' />"
    the_string = pretag + base64string + posttag
    return the_string

def sixfourit(inpath):
    try:
        with open(inpath, "rb") as f:
            data = f.read()
            f.close()
        return data.encode("base64")
    except Exception, e:
        print (str(e))
        sys.exit(1)


def version():
    print("sixfour version " + VERSION)

if __name__ == "__main__":
	main(sys.argv[1:])
