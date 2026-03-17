# System-Input-Output
Designing a system which accepts various inputs and validates with various usecases mentioned here and get outputs either to feedback to same process or response back in various formats.
**Tools Used**
1. Flask
2. MQTT
3. Postgresql
4. Vuejs

_Usecases_
**Case-1**
start Date: 17thMarch2026
End Date: 
Description:
Approach:
1.With help of MQTT setup locally both logging and credentials enablement create a static input from publisher and receiver receives
Adding logs to view the case is running file.
2. Convert to secure way of Publishing and Subscribing
3. Add proper traceback of logs flow for this case.
4. Automate the existing flow
4. Add necessary TDD to handle setup, configure, process.
5. Send various data types values that will be accepted by Mosquitto MQTT.
6. Add Web-Socket Frontend for the same

_Current state:_
Completed: Currently, I am in approach step1 where the Mosquito MQTT have been installed and setup with default configuration and were able to publish and subscribe locally in windows 11 machine using python and added python logging to traceback the approach.
Setup Versions:
windows 11
MQTT version 20.2
python 3.12

_Inprogress:_
configuration of logs and user credentials in progress.

_ToDo:_
Complete: MQTT tool logging and user credentials enablement and key and secret enablement.
