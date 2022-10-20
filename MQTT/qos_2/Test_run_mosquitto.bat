::CHCP 65001
:: Documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start 

:: Echo turned off to see the only relevant outputs.
@echo off

Title Mosquitto shell 

:: Under the Assumption that the conda enviorment"qs4pl"  is installed already
:: ECHO Activating conda enviorment qs4pl......
:: call activate qs4pl

:: Assuming the python is added to the PATH variable
:: Opening in background using /B
:: uncomment if you want to run sub together in this script

:: start "subscriber" python "sub.py"

:: Assume the Mosquitto version 1.6.9 (not the latest), is installed under the folder "C:\Program Files\mosquitto"
:: The config file has been modified to accept anonymous connections with, "allow_anonymous true"

call cd "C:\Program Files\mosquitto"

ECHO Running Mosquitto with the given config file at %cd%
ECHO To stop the running, \n press "Ctrl+C" and press "J"

call mosquitto -v -c mosquitto.conf



:: pause