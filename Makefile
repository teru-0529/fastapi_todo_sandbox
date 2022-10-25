.PHONY: up down logs ps shell migrate_head migrate_base

DOCKER_TAG := latest
up: ## do docker compose up with hot release
	docker compose --env-file ./backend/.env up

down: ## do docker compose down
	docker compose --env-file ./backend/.env down

logs: ## tail docker compose logs
	docker compose logs -f

ps: ## check container status
	docker compose ps

shell: ## login api shell
	docker exec -it api /bin/sh

migrate_head:
	docker compose --env-file ./backend/.env run --rm api alembic upgrade head

migrate_base:
	docker compose --env-file ./backend/.env run --rm api alembic downgrade base

# test: ## execute tests
# 	go test -v ./...
