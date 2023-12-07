#!/bin/bash
python -m isort src
python -m black src
python -m flake8 src
python -m mypy src/inverter_com
