#!/bin/sh

# Cleanup tests
if [ "$1" = "cleanup" ]; then
	cp image_bu.html image_test.html
	cp image2_bu.html image2_test.html
else
	# TEST: Single tag replacement
	TEST_SINGLE="Tag Replacement x 1"
	echo "$TEST_SINGLE test started..."
	../sixfour.py -i sm-logo.png -o image_test.html
	if (( $? )); then
		echo "$TEST_SINGLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image_test.html image_master.html
	echo "---DIFF END---"
	echo "\n"
	# TEST: Two tag replacement
	TEST_DOUBLE="Tag Replacement x 2"
	echo "$TEST_DOUBLE test started..."
	../sixfour.py -i sm-logo.png -o image2_test.html
	if (( $? )); then
		echo "$TEST_SINGLE failed"
		echo "#### STOP"
		exit 1
	fi
	echo "---DIFF START---"
	diff image2_test.html image2_master.html
	echo "---DIFF END---"
fi

