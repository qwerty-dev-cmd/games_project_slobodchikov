.PHONY: install lint build package-install even calc gcd

install:
	uv sync

lint:
	uv run ruff check src/

even:
	uv run python3 -m games_project.VD_games.scripts.VD_even

calc:
	uv run python3 -m games_project.VD_games.scripts.VD_calc

gcd:
	uv run python3 -m games_project.VD_games.scripts.VD_gcd

build:
	uv build

package-install:
	uv tool install --force dist/*.whl
