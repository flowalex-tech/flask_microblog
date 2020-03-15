# Flask Microblog

This is a microblog that I created off of the folowing guide: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Each commit will be one chapter

> Chapters 10 and 11 are off by one, they should be chapters 11 and 12. I skipped the email support since it will be in a docker container that will be deployed to k8s and I don't want to configure smtp

## Building the site locally

This site is built with python3 and flask

To get started building the site run the following commands for Linux and OSx

```bash

python3 -m venv venv

python3 -m pip install --user virtualenv

virtualenv venv

source venv/bin/activate

```