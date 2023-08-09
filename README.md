# Python FastAPI, htmx, DaisyUI, nginx boilerplate

A stack for a fast, async and beautiful web app that you can deploy in 3 minutes.
- No ridiculus javascript framework, just hypermedia [htmx](https://htmx.org) 🚀
- Fast, snappy user experience ⚡
- Production grade async Python backend 🐍 ([FastAPI](https://fastapi.tiangolo.com/), [gunicorn](https://gunicorn.org/) and [nginx](https://www.nginx.com/))
- Fully working web app example with Stripe payment integration for getting domain name ideas via ChatGPT

## Features

- Easy usage with Makefile (`make run`, `make deploy`)
- Environment variables collected in `.env`
- `make deploy` builds tailwind and DaisyUI into a slim css file
- Poetry for Python dependency management
- Sqlalchemy ORM makes it simple to start with something small like Sqlite and then change to Postgres when needed
- https via `certbot` that autoinstalls in nginx

## Prerequisites

- Python 3.8+
- Node.js
- Python Poetry
- SSH access to the deployment server

## Installation & Setup

1) Copy the `.env.example` to `.env` and fill in the required values.
2) `poetry install`
3) Follow instructions in [`scripts/bootstrap_server.md`](https://github.com/maxberggren/unstoppable/blob/main/scripts/bootstrap_server.md) for setting up everything on a Hetzner Ubuntu 22 machine (works great on the cheapest €4.51 / mo CAX11 e.g.).
4) `make run` to run locally
5) `make deploy` to deploy to prod

## Contact
- [@maxberggren](https://www.twitter.com/maxberggren)