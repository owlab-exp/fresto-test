call .\setGrinderEnv.cmd

echo %CLASSPATH%

java -classpath %CLASSPATH% -DHTTPPlugin.additionalHeaders=fresto-uuid net.grinder.TCPProxy -console -http > grinder_proxy.py
