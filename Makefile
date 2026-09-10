.PHONY: update radar papers check
PYTHON ?= python3

update:
	$(PYTHON) scripts/update.py

radar:
	$(PYTHON) scripts/weekly.py

papers:
	$(PYTHON) scripts/build_papers.py

check:
	$(PYTHON) -m py_compile scripts/update.py scripts/weekly.py scripts/build_papers.py scripts/check_repo.py
	$(PYTHON) scripts/check_repo.py
	$(PYTHON) -m unittest discover -s tests
