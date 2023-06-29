# FastAPI/Python Service
This project has been created using the [DOME 4.0 Reference Connector Plugin Template](https://github.com/DOME-4-0/reference-connector),
and is based on on SINTEF's [Fastapi Template](https://github.com/SINTEF/fastapi-template).

## Run in Docker
### Development target
The development target will allow for automatic reloading when source code changes. This requires that the local directory is bind-mounted using the -v or --volume argument. To Build and run the development target from the command line:


	docker build --rm -q -f Dockerfile \
	  --label "dome.{{cookiecutter.project_slug}}-target=development" \
	  --target development \
	  -t "dome/{{cookiecutter.project_slug}}-development:latest" .
	  
	docker run --rm -i --user="$(id -u):$(id -g)" -p 8080:8080 -v "$PWD:/app" dome/{{cookiecutter.project_slug}}-development:latest

Open http://localhost:8080 on your browser to test the application.

### Production target
The production target will not reload itself on code change and will run a predictable version of the code on port 80. Also you might want to use a named container with the --restart=always option to ensure that the container is restarted indefinitely regardless of the exit status. To build and run the production target from the command line:


	docker build --rm -q -f Dockerfile \
	  --label "dome.{{cookiecutter.project_slug}}-target=production" \
	  --target production \
	  -t "dome/{{cookiecutter.project_slug}}-production:latest" .
	  
	docker run -d -p 80:80 --user="$(id -u):$(id -g)" --name {{cookiecutter.project_slug}} --restart=always dome/{{cookiecutter.project_slug}}-production:latest
