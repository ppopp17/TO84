#!/usr/bin/bash
set -e
# This runs the python consumer
# Usage: pythonConsumer.sh [ env ]
#   env - the environment the script is being executed in, defaults to ALTAMIRA_L
#         Must be one of the following values:
#         ALTAMIRA_U: altamira uncalssified environment

BINPATH=`dirname $0`
AL="ALTAMIRA_L"
AU="ALTAMIRA_U"
AS="ALTAMIRA_S"
# other environments? inside NASIC?

# determine environment
ENVIRONMENT=${1:-$AL}

# source the correct environment variables file
if [ "$ENVIRONMENT" = "$AL" ]; then
  echo source altamira_unclass.properties
  #source $BINPATH/altamira_local.properties
else
  echo Usage: pythonConsumer.sh ENV
  echo
  echo   where ENV indicates the environment to run in
  echo   ENV is one of the following values:
  echo     ALTAMIRA_U - unclass DC/OS at Altamira
  echo     ALTAMIRA_S - secret DC/OS at Altamira
  echo
  exit
fi

# start up python consumer
#ping 10.0.2.15
#python --version
python "$BINPATH/../pythonConsumer/main.py" $@
