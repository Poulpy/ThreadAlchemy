# ThreadAsync

Web API using FastAPI in Python.

## Run

```
uv run fastapi dev
```

## Lint

```
uv run ruff check --fix .   # lint + corrections automatiques
uv run ruff format .        # formatage (remplace black)
```

## Prek

Add .pre-commit-config.yaml to the root of the project.

```YAML
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.17
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format
```

And then run:
```
prek run --all-files
```



## Troubleshooting install

```
uv sync --reinstall
```
