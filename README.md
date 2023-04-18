# Overview
I needed a quick script that I can run once a month to check the latest version of the open-source projects that I am currently reverse-engineering to make sure I am aware of a new release.

## Setup

Inside of `__main__.py`, fill in the `TOKEN` variable with a PAT token. 
You will also have to update the entries in `PROJECT_VERSIONS` to the projects you're working on at the moment.

## Running script
After you have it more personalized towards you, then just run the following two commands:

```
poetry install
poetry run main
```
