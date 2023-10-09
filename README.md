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

## Add Label
We have predefined labels at my work, so we use this script to create the same issue throughout the organization:
```zsh
poetry run add_label
```


## Create Issue
To create the same issue in multiple or just one repo, then you need to modify `create_issue/__main__.py` with the repos you want to create for and then run:
```zsh
poetry run create_issue
```
