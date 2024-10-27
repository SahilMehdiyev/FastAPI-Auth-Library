# Makefile

.PHONY: install
install:
	poetry install

.PHONY: run
run:
	poetry run uvicorn app.main:app --reload

.PHONY: test
test:
	poetry run pytest

.PHONY: update
update:
	poetry update
