@echo off
call .venv/scripts/activate

python conbineCSV(DumpFile).py
python CSV2YarnTxt(DumpFile).py

pause