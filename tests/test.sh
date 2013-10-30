#!/bin/sh

# Function defs
cleanup_files(){
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.html
	cp imagecss_bu.css imagecss_test.css
	cp md-test_bu.md md-test.md
	cp imagesass_bu.scss imagesass_test.scss
}

# Cleanup previous tests
if [ "$1" = "cleanup" ]; then
	cleanup_files
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

	# TEST: Python 2.7 SASS tag replacement
	TEST_SASS="Python 2.7 SASS Image Embed"
	echo "$TEST_SASS test started..."
	python ../sixfour.py -i sos.png --sass=imagesass_test.scss
	if (( $? )); then
		echo "$TEST_SASS failed"
		echo "#### STOP"
		exit 1
	fi
	echo "--DIFF START--"
	diff imagesass_test.scss imagesass_standard.scss
	echo "--DIFF END--"
	echo "Test sass compile after Python 2.7 image embed..."
	sass ./imagesass_test.scss >&-
	if (( $? )); then
		echo "$TEST_SASS failed @ sass compile step"
		echo "#### STOP"
		exit 1
	else
		echo "---> sass compile completed successfully"
	fi
	echo " "

	# Cleanup for Python 3 tests
	cleanup_files

	# PYTHON 3.3 TESTS
	# TEST: Python 3.3 Single tag replacement
	TEST_SINGLE_THREE="Python 3 Image Embed x 1"
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
	TEST_DOUBLE_THREE="Python 3 Image Embed x 2"
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
	TEST_MD_THREE="Python 3 Markdown Image Embed"
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
	TEST_CSS_THREE="Python 3 CSS Image Embed"
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

	# TEST: Python 3.3 SASS tag replacement
	TEST_SASS_THREE="Python 3 SASS Image Embed"
	echo "$TEST_SASS_THREE test started..."
	python3 ../sixfour.py -i sos.png --sass=imagesass_test.scss
	if (( $? )); then
		echo "$TEST_SASS_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "--DIFF START--"
	diff imagesass_test.scss imagesass3_standard.scss
	echo "--DIFF END--"
	echo "Test sass compile after Python 3 image embed..."
	sass ./imagesass_test.scss >&-
	if (( $? )); then
		echo "$TEST_SASS_THREE failed @ sass compile step"
		echo "#### STOP"
		exit 1
	else
		echo "---> sass compile completed successfully"
	fi
	echo " "

	# Cleanup for Image MIME type test
	cleanup_files

	# TEST: GIF MIME TYPE TEST (Python 2.7)
	TEST_GIF="GIF MIME type"
	echo "$TEST_GIF test started..."
	python ../sixfour.py -i nana.gif -c imagecss_test.css
	grep 'data:image/gif' imagecss_test.css >&-
	if (( $? )); then
		echo "$TEST_GIF test failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---> $TEST_GIF test completed successfully\n"

	# TEST: JPG MIME TYPE TEST (Python 2.7)
	TEST_JPG="JPG MIME type"
	echo "$TEST_JPG test started..."
	python ../sixfour.py -i nana.jpg -o image_test.html
	grep 'data:image/jpg' image_test.html >&-
	if (( $? )); then
		echo "$TEST_JPG test failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---> $TEST_JPG test completed successfully\n"

	# TEST : PNG MIME TYPE TEST (Python 2.7)
	TEST_PNG="PNG MIME type"
	echo "$TEST_PNG test started..."
	python ../sixfour.py -i sos.png -o md-test.md
	grep 'data:image/png' md-test.md >&-
	if (( $? )); then
		echo "$TEST_PNG test failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---> $TEST_PNG test completed successfully\n"

	# TEST : SVG MIME TYPE TEST (Python 2.7)
	TEST_SVG="SVG Mime type"
	echo "$TEST_SVG test started..."
	python ../sixfour.py -i commonslogo.svg -s imagesass_test.scss
	grep 'data:image/svg+xml' imagesass_test.scss >&-
	if (( $? )); then
		echo "$TEST_SVG test failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---> $TEST_SVG test completed successfully\n"

fi

