#!/bin/sh

./setGrinderEnv.sh

echo $CLASSPATH

java -classpath $CLASSPATH net.grinder.Grinder $GRINDERPROPERTIES
