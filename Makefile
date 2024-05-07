.PHONY: help

help:
	@echo "Available targets:"
	@echo "  run           : Start the Dockerized application"
	@echo "  stop          : Stop the Docker containers"
	@echo "  clean         : Stop and remove Docker containers, networks, and volumes"
	@echo "  logs-backend  : View logs for the Django backend"
	@echo "  logs-frontend : View logs for the Next.js frontend"

build:
	docker build -t dinease .

run:
	docker compose up -d --force-recreate

stop:
	docker-compose down

clean: stop
	docker-compose down -v --remove-orphans

logs:
	docker-compose logs -f backend


backend:
	docker-compose exec backend sh

migrate:
	docker compose run --rm backend sh -c "python manage.py makemigrations && python manage.py migrate"

createsuperuser:
	docker compose run --rm backend sh -c "python manage.py createsuperuser"

install:
	python3 -m venv env &&
	source env/bin/activate &&
	pip install -r requirements.txt


	