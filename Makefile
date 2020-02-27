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

.PHONY: coat shoes mobile sweater socks trousers shirt pants undershirt

# Declare a local variable
# An example of explicit and implicit rules
# An explicit rule assigns the commands for several targets 

dress_articles = coat shoes mobile sweater socks trousers shirt pants undershirt

$(dress_articles) :;	@echo put on $@

# Implicit rule to state the pre-requisites only

# target    prerequisite           
# --------------------------------
coat:		shoes mobile sweater
shoes:		socks trousers
mobile:		trousers
sweater:	shirt
trousers:	pants shirt
shirt:		undershirt
