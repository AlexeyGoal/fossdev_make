


create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif 
	mkdir -p $(PRACTICE)
	touch demo-practice/README.md


remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif 
	rm -rf $(PRACTICE)