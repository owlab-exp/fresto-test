call .\setGrinderEnv_131112.cmd

echo %CLASSPATH%

java -classpath %CLASSPATH% net.grinder.Grinder %GRINDERPROPERTIES%
