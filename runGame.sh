#!/bin/bash

if hash python3 2>/dev/null; then
    ./halite -d "20 20" "python3 MyBot.py" "python3 MyBot4.py"
else
    ./halite -d "20 20" "python MyBot.py" "python MyBot4.py"
fi
