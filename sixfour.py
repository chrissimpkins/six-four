#!/usr/bin/env python

import sys
import os
import getopt

# Constants
VERSION = "1.1.3"
REPLACE_TAG = "{{64}}"

def main(argv):
    basesixfour = ""
    inpath = ""
    htmlpath = ""
    csspath = ""
    css = 0
    i = 0

    try:
        opts, args = getopt.getopt(argv, "chi:o:v", ["css=", "image=", "html=", "help", "version"])
    except getopt.GetoptError:
        print("Usage: sixfour.py [-chiov][--css=,--image=,--html=,--help,--version] <arg>")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-c', '--css'):
            css = 1
            csspath = arg
            i += 1
        elif opt in ('-i', '--image'):
            inpath = arg
            i += 1
        elif opt in ('-o', '--html'):
            htmlpath = arg
            i += 1
        elif opt in ('-v', '--version'):
            version()
            sys.exit(0)

    if i < 1:
        print("The image file path is missing.")
        sys.exit(1)
    elif i == 1:
        basesixfour = sixfourit(inpath)
        basesixfour_stripped = basesixfour.rstrip()
        sys.stdout.write(basesixfour_stripped)
    elif i == 2:
        basesixfour = sixfourit(inpath)
        basesixfour_stripped = basesixfour.rstrip()
        if css:
            insertimg_css(csspath, basesixfour_stripped, inpath)
        else:
            insertimg(htmlpath, basesixfour_stripped, inpath)




def help():
    helpstring = """
-----------------------------------
sixfour
Copyright 2013 Christopher Simpkins
MIT License
-----------------------------------

DESCRIPTION
A base64 encoder for images that optionally embeds encoded image data in HTML, Markdown, or CSS files at the site of a {{64}} tag.

USAGE
  sixfour [-chiov] [--css=,--image=,--html=,--help,--version] <arg>

OPTIONS
  -c --css=     - embed in CSS file <filepath>
  -h --help     - view this help documentation
  -i --image=   - image <filepath>
  -o --html=    - embed in HTML or MD file <filepath>
  -v --version  - show application version

EXAMPLES
  sixfour -i "img/image.png" -o "index.html"
  sixfour -i "img/image.png" --css="css/main.css"

NOTES
## Access the data through the standard output stream:
To push the base64 encoded image data to the standard output stream, use the image filepath only (-i or --image).

## Embed a base64 encoded image in a HTML or Markdown file:
Use the replacement tag {{64}} in your HTML or Markdown file at the location where you would like to embed a base64 data URI in an HTML <img> tag.  Include the recipient file path with the -o or --html flag in your command.  Include the image path with the -i or --image flag.

## Embed a base64 encoded image in a CSS element:
Use the replacement tag {{64}} in your CSS file at the location where you would like to embed your base64 data URI.  Include the recipient CSS file path with the -c or --css flag in your command.  Include the image path with the -i or --image flag.

SOURCE REPOSITORY
http://github.com/chrissimpkins/six-four

DOCUMENTATION
http://chrissimpkins.github.io/six-four/

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
    except Exception as e:
        print("Unable to embed your base64 encoded image tag.")
        print((str(e)))
        sys.exit(1)

def insertimg_css(csspath, base64string, imgpath):
    cssstring = ""
    try:
        with open(csspath, "r+") as f:
            cssstring = f.read()
            f.seek(0)
            the_b64 = makecsstag(base64string)
            new_cssstring = cssstring.replace(REPLACE_TAG, the_b64)
            f.write(new_cssstring)
            f.close()
            print("Insertion completed successfully")
    except Exception as e:
        print("Unable to embed your base64 encoded image in the CSS file")
        print((str(e)))
        sys.exit(1)

def makeimgtag(base64string, imgfile):
    pretag = """<img src="data:image/png;base64, """
    basefile = os.path.basename(imgfile)
    basename = os.path.splitext(basefile)[0]
    posttag = '" ' + "alt='" + basename + "' />"
    the_string = pretag + base64string + posttag
    return the_string

def makecsstag(base64string):
    pretag = """url(data:image/gif;base64,"""
    posttag = ")"
    the_string = pretag + base64string + posttag
    return the_string

def sixfourit(inpath):
    try:
        with open(inpath, "rb") as f:
            data = f.read()
            f.close()
        # test the sys.version_info tuple for major version number
        py3 = sys.version_info[0] > 2
        if py3:
            # Python 3
            import base64
            return base64.b64encode(data).decode()
        else:
            # Python 2
            return data.encode("base64")
    except Exception as e:
        print((str(e)))
        sys.exit(1)


def version():
    print(("sixfour version " + VERSION))

if __name__ == "__main__":
	main(sys.argv[1:])
