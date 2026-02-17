.PHONY: install VD-games build package-install run game

install:
	uv sync

VD-games:
	uv run python3 -m games_project.VD_games.scripts.VD_main

game:
	uv run python3 src/games_project/VD_games/scripts/VD_games.py

run: game

build:
	uv build

package-install:
	uv tool install --force dist/*.whl
lint:
	uv run ruff check src/
