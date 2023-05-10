[![Sphinx](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://choosealicense.com/licenses/mit/)
![Pytest Cov](https://img.shields.io/badge/coverage-100%25-green)
[![Beerware License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/rafalploszanski/url_shortener/blob/master/LICENSE)

# URL Shortener

A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.


## Demo

[URL Shortener Heroku](https://protected-brushlands-01714.herokuapp.com/api/schema/swagger-ui//)


## Tech Stack

**Server:** Python, Django, Django Rest Framework, Docker, Postgres


## Run Locally

Clone the project

```bash
  git clone git@github.com:rafalploszanski/url_shortener.git
```

Go to the project directory

```bash
  cd url_shortener
```

Set environment variables

```bash
cp ./envs/api.default.env ./envs/api.env
cp ./envs/postgres.default.env ./envs/postgres.env
# set variable values
```

Start the docker containers

```bash
  docker compose up
```

Go to your client and type:

```bash
  http://0.0.0.0:8000/api/schema/swagger-ui/
```

## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

`DJ_SECRET_KEY` - Django secret key for CSRF [gist](https://gist.github.com/rafalploszanski/6899e23d1ee98e93fc930182dfa6da62)

`DJ_DEBUG` - Production development mode

`DJ_ALLOWED_HOSTS` - Allowed hosts for Django

`LOGGING_LVL` - Python logging package levels

`DJ_SU_NAME` - Default superuser name

`DJ_SU_EMAIL` - Default superuser email

`DJ_SU_PASSWORD` - Default superuser password



Also variables to your ./envs/postgres.env file

`POSTGRES_USER` - Postgres root user

`POSTGRES_PASSWORD` - Postgres root password

`POSTGRES_DB` - Database name 

`POSTGRES_HOST` - Database host (Need to add docker service name)

`POSTGRES_PORT` - Database ports




## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/rafalploszanski/url_shortener/master/screenshots/coverage.png?token=GHSAT0AAAAAAB2732R7WTCBOA3GGHBTHVBEZC3YBMA)




## Authors

- [@rafalploszanski](https://github.com/rafalploszanski)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/rafalploszanski?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafał-płoszański-78391513a/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/RafalPloszanski)



