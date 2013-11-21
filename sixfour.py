#!/usr/bin/env python

import sys
import os
import getopt

# Constants
VERSION = "1.3.3"
REPLACE_TAG = "{{64}}"
SASS_REPLACE_TAG = "$sixfour"
LESS_REPLACE_TAG = "@sixfour"

def main(argv):
    basesixfour = ""
    inpath = ""
    htmlpath = ""
    csspath = ""
    css = 0
    sass = 0
    less = 0
    i = 0

    try:
        opts, args = getopt.getopt(argv, "c:hi:l:o:s:v", ["css=", "image=", "html=", "help", "less=", "sass=", "version"])
    except getopt.GetoptError:
        print("Usage: sixfour [-cilos][--css=,--image=,--html=,--less=,--sass=] <arg>")
        print("Help: sixfour -h | --help")
        print("Version: sixfour -v | --version")
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
        elif opt in ('-l', '--less'):
            less = 1
            csspath = arg
            i += 1
        elif opt in ('-s', '--sass'):
            sass = 1
            csspath = arg
            i += 1
        elif opt in ('-v', '--version'):
            version()
            sys.exit(0)

    if i < 1:
        print("The image file path is missing.")
        sys.exit(1)
    elif i == 1:  #print to std out
        basesixfour = sixfourit(inpath)
        basesixfour_stripped = basesixfour.rstrip()
        sys.stdout.write(basesixfour_stripped)
    elif i == 2:  #in file and out file specified
        basesixfour = sixfourit(inpath)
        basesixfour_stripped = basesixfour.rstrip()
        if css:
            insertimg_css(csspath, basesixfour_stripped, inpath)
        elif sass:
            insertimg_sass(csspath, basesixfour_stripped, inpath)
        elif less:
            insertimg_less(csspath, basesixfour_stripped, inpath)
        else:
            insertimg(htmlpath, basesixfour_stripped, inpath)
    elif i > 2:  #too many options used on the CL
        print("sixfour Error: You entered too many options.")
        print("Type sixfour --help to view the help documentation")
        sys.exit(1)




def help():
    helpstring = """
-----------------------------------
sixfour
Copyright 2013 Christopher Simpkins
MIT License
-----------------------------------

DESCRIPTION
A base64 encoder for images that optionally embeds encoded image data in HTML, Markdown, CSS, LESS, or SASS files.

USAGE
  sixfour [-cilos] [--css=,--image=,--html=,--less=,--sass=] <arg>

SOURCE FILE EMBED TAG
  CSS, HTML, and Markdown: {{64}}
  LESS: @sixfour
  SASS: $sixfour

OPTIONS
  -c --css=     - embed in CSS file <filepath>
  -h --help     - view this help documentation
  -i --image=   - image <filepath>
  -l --less=    - embed in LESS file <filepath>
  -o --html=    - embed in HTML or MD file <filepath>
  -s --sass=    - embed in SASS file <filepath>
  -v --version  - show application version

EXAMPLES
  sixfour -i "img/image.png" -o "index.html"
  sixfour -i "img/image.png" --css="css/main.css"
  sixfour -i "img/image.png" --less="less/main.less"
  sixfour -i "img/image.png" --sass="sass/main.scss"

NOTES
-->> Access the data through the standard output stream <<--
To push the base64 encoded image data to the standard output stream, use the image filepath only (-i or --image).

-->> Embed a base64 encoded image in a HTML or Markdown file <<--
Use the embed tag {{64}} in your HTML or Markdown file at the location where you would like to embed a base64 data URI in an HTML <img> tag.  Include the recipient file path with the -o or --html flag in your command.  Include the image path with the -i or --image flag.

-->> Embed a base64 encoded image in a CSS element <<--
Use the embed tag {{64}} in your CSS file at the location where you would like to embed your base64 data URI.  Include the recipient CSS file path with the -c or --css flag in your command.  Include the image path with the -i or --image flag. The image MIME type is automatically detected from the filename extension.

-->> Embed a base64 encoded image in a LESS or SASS element <<--
For LESS files, use the -l or --less flag with the filepath to the LESS file.  For SASS files, use the -s or --sass flag with the filepath to the SASS file.  sixfour will embed the base64 data URI at the site of the less variable, @sixfour, or SASS variable, $sixfour, respectively.   It is not necessary to define the variable in your LESS or SASS files.  Simply insert it at the location(s) where you intend to embed the data URI and run the appropriate sixfour command.  Use the -c or --css flags if you would prefer to use the {{64}} tag is SASS or LESS files.

SOURCE REPOSITORY
http://github.com/chrissimpkins/six-four

DOCUMENTATION
http://chrissimpkins.github.io/six-four/

    """
    print(helpstring)

# HTML + Markdown replacements
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

# CSS replacements
def insertimg_css(csspath, base64string, imgpath):
    cssstring = ""
    try:
        with open(csspath, "r+") as f:
            cssstring = f.read()
            f.seek(0)
            the_b64 = makecsstag(base64string, imgpath)
            new_cssstring = cssstring.replace(REPLACE_TAG, the_b64)
            f.write(new_cssstring)
            f.close()
            print("Insertion completed successfully")
    except Exception as e:
        print("Unable to embed your base64 encoded image in the CSS file")
        print((str(e)))
        sys.exit(1)

# SASS replacements
def insertimg_sass(sasspath, base64string, imgpath):
    sassstring = ""
    try:
        with open(sasspath, "r+") as f:
            sassstring = f.read()
            f.seek(0)
            the_b64 = makecsstag(base64string, imgpath)
            new_sassstring = sassstring.replace(SASS_REPLACE_TAG, the_b64)
            f.write(new_sassstring)
            f.close()
            print("Insertion completed successfully")
    except Exception as e:
        print("Unable to embed your base64 encoded image in the SASS file")
        print((str(e)))
        sys.exit(1)

# LESS replacements
def insertimg_less(lesspath, base64string, imgpath):
    lessstring = ""
    try:
        with open(lesspath, "r+") as f:
            lessstring = f.read()
            f.seek(0)
            the_b64 = makecsstag(base64string, imgpath)
            new_lessstring = lessstring.replace(LESS_REPLACE_TAG, the_b64)
            f.write(new_lessstring)
            f.close()
            print("Insertion completed successfully")
    except Exception as e:
        print("Unable to embed your base64 encoded image in the LESS file")
        print(str(e))
        sys.exit(1)

def makeimgtag(base64string, imagepath):
    themime = ""
    gifmime = "image/gif"
    jpgmime = "image/jpg"
    pngmime = "image/png"
    svgmime = "image/svg+xml"
    # define the correct image MIME type
    if (imagepath.endswith(".png") or imagepath.endswith(".PNG")):
        themime = pngmime
    elif (imagepath.endswith(".jpg") or imagepath.endswith(".jpeg") or imagepath.endswith(".JPG") or imagepath.endswith(".JPEG")):
        themime = jpgmime
    elif (imagepath.endswith(".gif") or imagepath.endswith(".GIF")):
        themime = gifmime
    elif (imagepath.endswith(".svg") or imagepath.endswith(".SVG")):
        themime = svgmime
    else: #default to a png if cannot find the suffix
        themime = pngmime
    pretag = """<img src="data:""" + themime + """;base64, """
    basefile = os.path.basename(imagepath)
    basename = os.path.splitext(basefile)[0]
    posttag = '" ' + "alt='" + basename + "' />"
    the_string = pretag + base64string + posttag
    return the_string

def makecsstag(base64string, imagepath):
    themime = ""
    gifmime = "image/gif"
    jpgmime = "image/jpg"
    pngmime = "image/png"
    svgmime = "image/svg+xml"
    # define the correct image MIME type
    if (imagepath.endswith(".png") or imagepath.endswith(".PNG")):
        themime = pngmime
    elif (imagepath.endswith(".jpg") or imagepath.endswith(".jpeg") or imagepath.endswith(".JPG") or imagepath.endswith(".JPEG")):
        themime = jpgmime
    elif (imagepath.endswith(".gif") or imagepath.endswith(".GIF")):
        themime = gifmime
    elif (imagepath.endswith(".svg") or imagepath.endswith(".SVG")):
        themime = svgmime
    else: #default to a png if cannot find the suffix
        themime = pngmime
    pretag = """url('data:""" + themime + """;base64,"""
    posttag = "')"
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
