# --- User Parameters

# Django directory
PROJECT_NAME=bkcore

# Testing parameters
NPROCS=auto

# --- Internal Parameters

# Testing parameters
PYTEST_SEARCH_PATHS=${PROJECT_NAME}
PYTEST_OPTIONS=-n ${NPROCS} --cov=${PROJECT_NAME}
PYTEST_PYLINT_OPTIONS=

# Documentation
DOC_DIR=docs

# --- Targets

# Default target
all: fast-test

# Testing
fast-test fast-check:
	make test PYTEST_OPTIONS="-x ${PYTEST_OPTIONS}"

full-test full-check:
	make test PYTEST_PYLINT_OPTIONS="--pylint --pylint-error-types=EF";

test check:
	pep8 setup.py
	py.test ${PYTEST_SEARCH_PATHS} ${PYTEST_OPTIONS} ${PYTEST_PYLINT_OPTIONS}

.coverage:
	-make test

coverage-report: .coverage
	coverage report -m

# Documentation generation

# Package distribution
dist: clean
	python setup.py sdist --formats=gztar,zip

# Maintenance
clean:
	find . -name "__pycache__" -delete
	find . -name "*.pyc" -exec rm -f {} \;
	rm -rf .cache
	rm -rf .coverage .coverage.* coverage
	rm -rf dist *.egg-info

# Phony Targets
.PHONY: all clean dist \
        test fast-test full-test \
        check fast-check full-check \
        coverage-report
