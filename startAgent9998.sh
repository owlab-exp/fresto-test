#!/bin/sh

source ./setGrinderEnv9998.sh
echo $CLASSPATH

java -classpath $CLASSPATH net.grinder.Grinder $GRINDERPROPERTIES
