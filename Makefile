PACKAGE_NAME:=peinan-utils

.PHONY: all
all: help

.PHONY: install-dev ## install the pip package in the develop environment
install-dev:
	pip install -e .

.PHONY: uninstall-dev ## uninstall the pip package in the develop environment
uninstall-dev:
	pip uninstall $(PACKAGE_NAME) -y

.PHONY: reinstall-dev ## uninstall and install the pip package in the develop environment
reinstall-dev: uninstall-dev install-dev

.PHONY: help ## View help
help:
	@grep -E '^.PHONY: [a-zA-Z_-]+.*?## .*$$' $(MAKEFILE_LIST) | sed 's/^.PHONY: //g' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
