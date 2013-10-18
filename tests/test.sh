#!/bin/sh

# Cleanup previous tests
if [ "$1" = "cleanup" ]; then
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.html
	cp imagecss_bu.css imagecss_test.css
	cp md-test_bu.md md-test.md
	if [ -f "dirty" ]; then
		rm dirty
	fi
elif [ -f dirty ]; then
	echo "The test directory is dirty. Please run the cleanup command."
else
	# Create Dirty Test Directory Indicator File
	touch dirty

	# PYTHON 2.7 TESTS
	# TEST: Python 2.7 Single image embed
	TEST_SINGLE="Python 2.7 HTML Image Embed x 1"
	echo "$TEST_SINGLE test started..."
	python ../sixfour.py -i sm-logo.png -o image_test.html
	if (( $? )); then
		echo "$TEST_SINGLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image_test.html image_standard.html
	echo "---DIFF END---"
	echo " "

	# TEST: Python 2.7 two image embed
	TEST_DOUBLE="Python 2.7 HTML Image Embed x 2"
	echo "$TEST_DOUBLE test started..."
	python ../sixfour.py -i sm-logo.png -o image2_test.html
	if (( $? )); then
		echo "$TEST_DOUBLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image2_test.html image2_standard.html
	echo "---DIFF END---"
	echo " "

	#TEST: Python 2.7 Markdown file image embed
	TEST_MD="Python 2.7 Markdown Image Embed"
	echo "$TEST_MD test started..."
	python ../sixfour.py -i sm-logo.png -o md-test.md
	if (( $? )); then
		echo "$TEST_MD failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff md-test.md md-test_standard.md
	echo "---DIFF END---"
	echo " "

	# TEST: Python 2.7 CSS tag replacement
	TEST_CSS="Python 2.7 CSS Image Embed"
	echo "$TEST_CSS test started..."
	python ../sixfour.py -i sos.png --css=imagecss_test.css
		if (( $? )); then
		echo "$TEST_CSS failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff imagecss_test.css imagecss_standard.css
	echo "---DIFF END---"
	echo " "

	# Cleanup for Python 3 tests
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.html
	cp imagecss_bu.css imagecss_test.css
	cp md-test_bu.md md-test.md

	# PYTHON 3.3 TESTS
	# TEST: Python 3.3 Single tag replacement
	TEST_SINGLE_THREE="Python 3.3 Image Embed x 1"
	echo "$TEST_SINGLE_THREE test started..."
	python3 ../sixfour.py -i sm-logo.png -o image_test.html
	if (( $? )); then
		echo "$TEST_SINGLE_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image_test.html image_standard3.html
	echo "---DIFF END---"
	echo " "

	# TEST: Python 3 Two tag replacement
	TEST_DOUBLE_THREE="Python 3.3 Image Embed x 2"
	echo "$TEST_DOUBLE_THREE test started..."
	python3 ../sixfour.py -i sm-logo.png -o image2_test.html
	if (( $? )); then
		echo "$TEST_DOUBLE_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image2_test.html image2_standard3.html
	echo "---DIFF END---"
	echo " "

	#TEST: Python 3.3 Markdown file image embed
	TEST_MD_THREE="Python 3.3 Markdown Image Embed"
	echo "$TEST_MD_THREE test started..."
	python3 ../sixfour.py -i sm-logo.png -o md-test.md
	if (( $? )); then
		echo "$TEST_MD_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff md-test.md md-test_standard3.md
	echo "---DIFF END---"
	echo " "

	# TEST: Python 3.3 CSS tag replacement
	TEST_CSS_THREE="Python 3.3 CSS Image Embed"
	echo "$TEST_CSS_THREE test started..."
	python3 ../sixfour.py -i sos.png --css=imagecss_test.css
		if (( $? )); then
		echo "$TEST_CSS_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff imagecss_test.css imagecss_standard3.css
	echo "---DIFF END---"
	echo " "

fi

