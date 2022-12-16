#!/bin/bash

rm -rf output
mkdir output

python3 scripts/1_vodafone.py
python3 scripts/2_airtel_tigo.py
python3 scripts/3_mtn.py
