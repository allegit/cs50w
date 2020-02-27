.DEFAULT_GOAL := build

all: target

target: help dep build test clean

help:
	@echo "Help unavailable now...."
dep:
	@echo "No dependencies found...."
build:
	@echo "Creating empty files...."
	touch file1.txt
	ls
test:
	@echo `pwd`

clean:
	@echo "Cleaning up some files..."
	rm -v file1.txt

#SHELL := $(shell which bash)