.PHONY: install VD-games build package-install

install:
	uv sync

VD-games:
	PYTHONPATH=src python3 -m games_project.VD_games.scripts.VD_main

build:
	uv build

package-install:
	uv tool install dist/*.whl
