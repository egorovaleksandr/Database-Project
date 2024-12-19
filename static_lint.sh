#!/bin/bash

if ! command -v pylint &> /dev/null
then
    echo "Pylint не установлен. Установите pylint с помощью 'pip install pylint'."
    exit 1
fi

pylint dealershipDB/