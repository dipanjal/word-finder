#!/bin/bash

rm -rf .venv
python -m venv .venv
source .venv/Scripts/activate
pip install -r ./requirements.txt