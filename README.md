Six-Four [![PyPI version](https://badge.fury.io/py/sixfour.png)](http://badge.fury.io/py/sixfour)
========

A base64 encoder for images that optionally embeds encoded image data in HTML, Markdown, CSS, LESS, or SASS files at the site of a {{64}} tag.

## Documentation Site
[Six-Four documentation](http://chrissimpkins.github.io/six-four)

## Dependencies
Requires Python 2 or 3

Tested in versions 2.7.5 and 3.3.2

## Install

If you use pip for Python package management, you can install Six-Four with the following command:
```
pip install sixfour
```
Otherwise, obtain the source code with one of the following methods:

**Method 1**: Clone the sixfour repository with the following command:
```
git clone https://github.com/chrissimpkins/six-four.git
```
**Method 2**: Download a compressed archive with one of the following links:

[gzipped tar archive](https://github.com/chrissimpkins/six-four/tarball/master)

[zip archive](https://github.com/chrissimpkins/six-four/zipball/master)

Then, navigate to the top level of the source directory and run the following command:
``` python
python setup.py install
```

## Usage
### base64 Encoding --> Standard Output Stream
Include the `-i` flag with the input image file path and the raw base64 encoded image data will be printed to the standard output stream:
``` bash
sixfour -i 'path/to/image.png'
```
You can use this method to pipe the raw base64 encoded image data to any other application on *nix platforms:
``` bash
sixfour -i 'path/to/image.png' | coolimageapp --process-it
```

### base64 Encoding --> &lt;img&gt; Tag in HTML or Markdown file
Insert the tag `{{64}}` at the site in your Markdown or HTML file where you want to embed the base64 encoded image tag:

``` html
<!DOCTYPE html>
    ...snip...
    <body>
        <div class="main-container">
            <div class="main wrapper clearfix">
			{{64}}
            </div> <!-- #main -->
        </div> <!-- #main-container -->
    ...snip...
    </body>
</html>
```

Include both the `-i` flag with an image file path and the `-o` flag with a HTML or Markdown file path in your command:
``` bash
sixfour -i 'path/to/coolimage.png' -o 'path/to/index.html'
```
The `{{64}}` tag in the HTML above will be replaced with a &lt;img&gt; tag that looks like this:
``` html
<!DOCTYPE html>
    ...snip...
    <body>
        <div class="main-container">
            <div class="main wrapper clearfix">
			<img src="data:image/png;base64, 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
			YII=" alt='coolimage' />
            </div> <!-- #main -->
        </div> <!-- #main-container -->
    ...snip...
    </body>
</html>
```
The image filename is used as the `<alt>` attribute in the tag.  The image MIME type is automatically inserted in the data URI based upon your image file extension.

### base64 Encoding --> Embedded Data URI in CSS File
Insert the tag `{{64}}` at the site in your CSS file where you want to embed the base64 encoded image data URI:
``` css
.base64test {
	background: #fff {{64}} repeat-x;
}
```
Include both the `-i` flag with an image file path and the `-c` (or --css=) flag with a CSS file path in your command:
``` bash
sixfour -i 'path/to/coolimage.png' -c 'path/to/main.css'
```
And your CSS file will look like this:
``` css
.base64test {
	background: #fff url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAIAAABLixI0AAAAOElEQVQ4y2N4Qz3AAMSfP73DJCEIPxuNZBh112Bz14cPEISPjdVdg9Ws0fAaDa8hHF6j5dcQcxcA3DHODs/IAR8AAAAASUVORK5CYII=') repeat-x;
}
```

### base64 Encoding --> Embedded Data URI in LESS File
Use the -l or --less flag with a path to the LESS file.  Insert the LESS variable @sixfour at the site where you would like to embed your base64 encoded image.  This variable does not need to be defined in your LESS file.

``` sass
.funky {
  background: #fff @sixfour repeat-x;
  font: 2px/3px {
    family: fantasy;
    size: 30em;
    weight: bold;
  }
}
```

Run Six-Four on your LESS file (before you compile it with LESS) with the following syntax:
``` bash
sixfour -i 'path/to/coolimage.png' --less='less/main.less'
```

### base64 Encoding --> Embedded Data URI in SASS File
If you use the -s or --sass flag with the file path to a SASS file, you can use the SASS variable $sixfour at the replacement site for your data URI.  You do not need to define this variable in your SASS file, simply insert it where you would like the data URI to be embedded.
``` sass
.funky {
  background: #fff $sixfour repeat-x;
  font: 2px/3px {
    family: fantasy;
    size: 30em;
    weight: bold;
  }
}
```

Then run Six-Four on your SASS file (before your compile it with SASS or Compass) using the following syntax:
``` bash
sixfour -i 'path/to/coolimage.png' --sass='sass/main.scss'
```

and compile the file normally with sass:
``` bash
sass --update 'sass/main.scss'
```


## Help
Help documentation is accessed with either of the following commands:
``` bash
sixfour -h
```
or
``` bash
sixfour --help
```

## License
MIT license

## Changelog

**v1.3.0** - added LESS file embed support

**v1.2.0** - added SASS file embed support + bug fixes for CSS embed + automatic MIME type detection for jpg, gif, png, and svg file types

**v1.1.3** - modified Python 3 vs 2 interpreter check

**v1.1.2** - updated -h flag help documentation

**v1.1.0** - added Python 3 support with Python 2 + 3 tests

**v1.0.1** - added alt attribute completion with image filename

**v1.0.0** - initial release

✪ Chris
