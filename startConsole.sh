#!/bin/sh
source ./setGrinderEnv.sh
echo $CLASSPATH

java -classpath $CLASSPATH  net.grinder.Console
