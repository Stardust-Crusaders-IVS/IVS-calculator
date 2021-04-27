
# targets:

all: 

pack:
	# TODO

clean:
	rm -r ./__pycache__

test:
	python ./src/math_library_tests.py

doc:
	# TODO

run:
	@cd ./src; python ./gui.py 2>/dev/null

profile:
	# TODO

