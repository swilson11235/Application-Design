PROGRAM = usewebimages
BASE = webImages
TEST = test_$(BASE)
MODULE = $(BASE)_pkg

program:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE)
	python $(PROGRAM).py
	mv images/montage.jpg .
	rm -r images

test:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE)
	python $(MODULE)/$(TEST).py

doc:
	pydoc -w ./ 
	mv $(MODULE).html documentation
	mv $(MODULE).$(TEST).html documentation
	mv $(MODULE).$(BASE).html documentation
	mv $(PROGRAM).html documentation

