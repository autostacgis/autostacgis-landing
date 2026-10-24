.PHONY: dev build check release
dev:
	python3 -m http.server 4174 --bind 127.0.0.1 --directory public
build: check
	@echo "Static site ready in public/"
check:
	python3 scripts/check.py
release: check
	gh workflow run pages.yml
