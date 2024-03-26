build:
	docker build -t jop-sql .

run:
	docker run -d -p 3306:3306 jop-sql

stop:
	docker stop $(docker ps | grep 'jop-sql' | awk ' { print $1 } ')
