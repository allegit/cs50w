.DEFAULT_GOAL := build

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