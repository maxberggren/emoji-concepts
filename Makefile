
include .env
export

run:
	# Run the dev server locally
	npx tailwindcss -i ./static/src/input.css -o ./static/tailwind.css
	poetry run uvicorn main:app --reload

attach:
	# SSH into the server machine
	ssh root@$$SERVER_ADDR

deploy:
	# Compile tailwind, if needed install latest dependencies on the server
	# and gracefully tell the webserver to reload with the new code without
	# dropping any existing connections.
	npx tailwindcss -i ./static/src/input.css -o ./static/tailwind.css
	bash scripts/deploy_app.sh
	ssh root@$$SERVER_ADDR "source .env"
	ssh root@$$SERVER_ADDR "/root/.local/bin/poetry install"
	ssh root@$$SERVER_ADDR "kill -HUP \`ps -C gunicorn fch -o pid | head -n 1\`"