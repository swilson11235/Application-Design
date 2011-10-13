PROGRAM = usewave
BASE = Wave
TEST = test_Wave
MODULE = Wave_pkg

program:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE)
	python $(PROGRAM).py

test:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE)
	python $(MODULE)/$(TEST).py

doc:
	pydoc -w ./ 
	mv $(MODULE).html documentation
	mv $(MODULE).$(TEST).html documentation
	mv $(MODULE).$(BASE).html documentation
	mv $(MODULE).$(PROGRAM).html documentation

