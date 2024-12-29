import subprocess

# Run the unit tests with coverage
subprocess.run(['coverage', 'run', 'UnitTest.py'])

# Generate the HTML report
subprocess.run(['coverage', 'html'])

# Show the report summary in the terminal
subprocess.run(['coverage', 'report', '-m'])
