postgres:
	docker run --name planner -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:latest

stop_container:
	docker stop planner

remove_container:
	docker rm planner

logs:
	docker logs planner

createdb:
	docker exec -it planner createdb --username=root --owner=root simple_planner

dropdb:
	docker exec -it planner dropdb simple_planner


.PHONY: postgres stop_container remove_container logs createdb dropdb