call .\setGrinderEnv.cmd

echo %CLASSPATH%

java -classpath %CLASSPATH% net.grinder.Grinder %GRINDERPROPERTIES%
