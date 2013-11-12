#!/bin/sh

source ./setGrinderEnv_131112.sh
echo $CLASSPATH

java -classpath $CLASSPATH net.grinder.Grinder $GRINDERPROPERTIES
