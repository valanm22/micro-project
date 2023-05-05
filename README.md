# micro-project

## Getting Started 

### Prerequisites

* Python 3.3 or higher

### Project setup

```diff 
# cloning the repo
$ git clone https://github.com/valanm22/micro-project.git
# move to the project folder
$ cd micro-project
```

### Activating virtual environment

```diff
# creating venv
$ python3 -m venv your_env_name
# activating the venv
$ your_env_name\Scripts\activate
# installing the required packages
$ pip install -r requirements.txt
```
    
### Running app

```diff
# exporting app to environment variable
$ set FLASK_APP=run.py
# mentioning environment type
$ set FLASK_ENV=development
# running app
$ flask run
```
