all:
	@echo 'make re-env – Destroy virtual environment and setup new one for development'
	@echo 'make install – Install libraries using pip'
	@echo 'make makemigrations – Create migrations'
	@echo 'make migrate – Apply migrations'
	@echo 'make build – Build a docker image'
	@echo 'make run – Run server inside container'
	@echo 'make test – Run tests'
	@echo 'make stop – Stop container'
	@echo 'make destroy – Destroy container'
	@echo 'make python – Run python inside container'
	@exit 0

re-venv:
	rm -rf venv
	python -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt

build:
	docker-compose build

run:
	docker-compose up --build -d

install:
	docker-compose exec web pip install -r requirements.txt

makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate --noinput

test:
	docker-compose exec web python tests/baseline.py

stop:
	docker-compose stop

destroy:
	docker-compose down

shell:
	docker-compose run web bash

python:
	docker-compose run web ipython
