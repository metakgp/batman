#! /usr/bin/bash

cd ~/batman  && source venv/bin/activate
nohup python batman.py > batman.log &

