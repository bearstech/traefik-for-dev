export UID:=$(shell id -u)
COMPOSE=docker-compose -f docker-compose.yml -f tools.yml

build:
	docker build -t myapp -f Dockerfile.app --build-arg=uid=$(UID) .
	docker build -t mycdn -f Dockerfile.cdn --build-arg=uid=$(UID) .

traefik_hosts:
	echo "127.0.0.1 localhost" > traefik_hosts

up: traefik_hosts
	$(COMPOSE) up

tests: traefik_hosts
	$(COMPOSE) up -d
	$(COMPOSE) exec -T traefik wait_for_services --timeout 20
	$(COMPOSE) exec -T traefik traefik_hosts > traefik_hosts
	$(COMPOSE) exec -T app python3 test_selenium.py
