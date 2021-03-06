#!/usr/bin/env python

from setuptools import setup

setup(name='sixfour',
      version='1.3.3',
      description='base64 Image Encoder and Embedder',
      author='Christopher Simpkins',
      author_email='chris@zerolabs.net',
      maintainer='Christopher Simpkins',
      maintainer_email='chris@zerolabs.net',
      url='https://github.com/chrissimpkins/six-four',
      platforms=['any'],
      py_modules=['sixfour'],
      scripts=['sixfour'],
      license='MIT License',
      keywords='image,base64,web,internet,CSS,HTML,Markdown,sass,scss,less,embed,tag,64',
      long_description="""Six-Four is a base64 encoder for images that embeds an appropriately formatted, encoded image in HTML, Markdown, CSS, LESS, or SASS files, or streams the raw image data through the standard output stream.

        `Six-Four Documentation <http://chrissimpkins.github.io/six-four/>`_

        Tested in Python v2.7.6 & v3.3.2""",
      classifiers= [
      	'Development Status :: 5 - Production/Stable',
		'Environment :: MacOS X',
		'Environment :: Other Environment',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: MacOS',
		'Operating System :: Microsoft',
		'Operating System :: Microsoft :: MS-DOS',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: Other OS',
		'Operating System :: POSIX',
		'Operating System :: POSIX :: BSD',
		'Operating System :: POSIX :: BSD :: BSD/OS',
		'Operating System :: POSIX :: BSD :: FreeBSD',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX :: Other',
		'Operating System :: Unix',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Programming Language :: Unix Shell',
		'Topic :: Internet',
		'Topic :: Multimedia',
		'Topic :: Multimedia :: Graphics',
		'Topic :: Multimedia :: Graphics :: Editors',
		'Topic :: Multimedia :: Graphics :: Graphics Conversion'
      ],
      )
