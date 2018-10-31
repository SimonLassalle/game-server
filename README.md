# Server for the API of the game database

This project includes the python3.6 server that requests the MySQL Database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project has been made to be Dockerized, i.e. it runs inside a Docker container. That means you need to download and install Docker on your machine first:

```
https://store.docker.com/editions/community/docker-ce-desktop-windows
```

If you are on Windows Home (not Pro edition), you will not be able to install Docker, so you will want to use Docker Toolbox instead. You can download it on this page:

```
https://docs.docker.com/toolbox/toolbox_install_windows/
```

You also need docker-compose, because the project is a multi-container Docker application. By default, docker-compose is included in Docker Toolbox.

### Installing

You need to clone this git repository on your local machine. This can be done by using this command:

```
git clone https://github.com/SimonLassalle/game.git
```

Then, go to the root directory of the project and open your favorite terminal. You just need to run this command to install all python dependencies, create the SQL database and run the API server:

```
docker-compose up --build
```

#Isn't thas too easy ? :D