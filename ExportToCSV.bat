@echo off
call .venv/scripts/activate

python YarnTxt2CSV(DumpFile).py
python conbineCSV(DumpFile).py

pause