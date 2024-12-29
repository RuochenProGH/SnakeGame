ECHO Running coverage report...
coverage run .\UnitTest.py
ECHO Generating HTML report...
coverage html
ECHO Report Summary:
coverage report -m
ECHO Done.
PAUSE