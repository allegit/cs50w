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

# target    prerequisite           command
# ------------------------------------------------
coat:		shoes mobile sweater;  @echo put on $@
shoes:		socks trousers;        @echo put on $@
mobile:		trousers;              @echo put on $@
sweater:	shirt;                 @echo put on $@
socks:		;                      @echo put on $@
trousers:	pants shirt;           @echo put on $@
shirt:		undershirt;            @echo put on $@
pants:		;                      @echo put on $@
undershirt:	;                      @echo put on $@