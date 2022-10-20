::CHCP 65001
:: Documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start 

:: Echo turned off to see the only relevant outputs.
@echo off

Title Qs4pl Conda Env

:: Under the Assumption that the conda enviorment"qs4pl"  is installed already
ECHO Activating conda enviorment qs4pl......
call activate qs4pl


cmd

:: pause