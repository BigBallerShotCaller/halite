#!/bin/bash

if hash python3 2>/dev/null; then
    ./halite -d "10 10" "python3 MyBot.py" "python3 RandomBot.py"
else
    ./halite -d "10 10" "python MyBot.py" "python RandomBot.py"
fi
