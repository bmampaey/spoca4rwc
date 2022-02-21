#! /bin/bash
# This script will run the script AIA_CH_pipeline.py 1 day at a time

if [ $# -ne 2 ]; then
	echo You must specify the start date and the end date
	exit 2
fi

FIRST_DATE=`date -d "$1" +\%F`
LAST_DATE=`date -d "$2" +\%F`

START_DATE=$FIRST_DATE
while [ "$START_DATE" \< "$LAST_DATE" ]; do
	END_DATE=`date -d "$START_DATE + 1 day" +\%F`
	echo Running AIA_CH_PIPELINE.py from $START_DATE to $END_DATE
	/opt/spoca4rwc/scripts/AIA_CH_pipeline.py --debug --log_file ./AIA_CH_pipeline.log --start_date $START_DATE --end_date $END_DATE
	START_DATE=$END_DATE
done
