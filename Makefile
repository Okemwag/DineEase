.PHONY: help

help:
	@echo "Available targets:"
	@echo "  run           : Start the Dockerized application"
	@echo "  stop          : Stop the Docker containers"
	@echo "  clean         : Stop and remove Docker containers, networks, and volumes"
	@echo "  logs-backend  : View logs for the Django backend"
	@echo "  logs-frontend : View logs for the Next.js frontend"

run:
	docker-compose up -d --build

stop:
	docker-compose down

clean: stop
	docker-compose down -v --remove-orphans

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend
backend:
	docker-compose exec backend bash
frontend:
	docker-compose exec frontend bash