#!/usr/bin/env bash
# set -e
install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt

format:	
	black myapp/*.py 

lint:
	pylint --disable=R,C myapp/*.py

#  container-lint:
#  	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python myapp/test_main.py

deploy:
	python myapp/main.py
		
all: install lint test format deploy
