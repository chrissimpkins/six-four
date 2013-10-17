#!/bin/sh

# Cleanup tests
if [ "$1" = "cleanup" ]; then
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.
	rm dirty
elif [ -f dirty ]; then
	echo "The test directory is dirty. Please run the cleanup command."
else
	# Create Dirty Test Directory Indicator File
	touch dirty

	# PYTHON 2.7 TESTS
	# TEST: Python 2.7 Single tag replacement
	TEST_SINGLE="Python 2.7 Tag Replacement x 1"
	echo "$TEST_SINGLE test started..."
	python ../sixfour.py -i sm-logo.png -o image_test.html
	if (( $? )); then
		echo "$TEST_SINGLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image_test.html image_master.html
	echo "---DIFF END---"
	echo "\n"
	# TEST: Python 2.7 Two tag replacement
	TEST_DOUBLE="Python 2.7 Tag Replacement x 2"
	echo "$TEST_DOUBLE test started..."
	python ../sixfour.py -i sm-logo.png -o image2_test.html
	if (( $? )); then
		echo "$TEST_DOUBLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image2_test.html image2_master.html
	echo "---DIFF END---"
	echo " "

	# Cleanup for Python 3 tests
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.html

	# PYTHON 3.3 TESTS
	# TEST: Python 3.3 Single tag replacement
	TEST_SINGLE_THREE="Python 3.3 Tag Replacement x 1"
	echo "$TEST_SINGLE_THREE test started..."
	python3 ../sixfour.py -i sm-logo.png -o image_test.html
	if (( $? )); then
		echo "$TEST_SINGLE_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image_test.html image_master.html
	echo "---DIFF END---"
	echo "\n"
	# TEST: Python 3 Two tag replacement
	TEST_DOUBLE_THREE="Python 3.3 Tag Replacement x 2"
	echo "$TEST_DOUBLE_THREE test started..."
	python3 ../sixfour.py -i sm-logo.png -o image2_test.html
	if (( $? )); then
		echo "$TEST_DOUBLE_THREE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image2_test.html image2_master.html
	echo "---DIFF END---"

fi

