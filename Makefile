.PHONY: up down logs ps

DOCKER_TAG := latest
up: ## do docker compose up with hot release
	docker compose --env-file ./backend/.env up

down: ## do docker compose down
	docker compose --env-file ./backend/.env down

logs: ## tail docker compose logs
	docker compose logs -f

ps: ## check container status
	docker compose ps

# test: ## execute tests
# 	go test -v ./...
