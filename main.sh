#!/bin/bash

# Number of terminals to open
num_terminals=25

# Get the directory where this script is located
script_dir=$(dirname "$(readlink -f "$0")")

# Function to run the Python script in each terminal
run_script_in_terminal() {
    x-terminal-emulator -e "bash -c \"cd '$script_dir'; while :; do python3 test.py; done\""
}

# Loop to open multiple terminals and run the script in each
for ((i=0; i<num_terminals; i++)); do
    run_script_in_terminal
done


#pkill -e terminal
