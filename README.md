# ThreadAsync

Web API using FastAPI in Python.

## Install

```bash
uv sync
cp .env.example .env
# Edit .env with your database config
# Run the database with docker
docker compose up -d
uv run alembic upgrade head
```

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

Install Prek:
```
uv run prek install
# Then run:
prek run --all-files
```



## Troubleshooting install

```
uv sync --reinstall
```
