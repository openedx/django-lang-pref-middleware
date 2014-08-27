COVERAGE = $(ROOT)/build/coverage
PACKAGE = lang_pref_middleware

validate: test.requirements test quality

test.requirements:
	pip install -q -r requirements.txt

test:
	./manage.py test --with-coverage --cover-inclusive --cover-branches --cover-html --cover-html-dir=$(COVERAGE)/html/ --cover-xml --cover-xml-file=$(COVERAGE)/coverage.xml --cover-package=$(PACKAGE)

quality:
	pep8 --config=.pep8 $(PACKAGE)
	pylint --rcfile=.pylintrc $(PACKAGE)

	# Ignore module level docstrings and all test files
	pep257 --ignore=D100,D203 --match='(?!test).*py' $(PACKAGE)
