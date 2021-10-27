[![Python application](https://github.com/foureyesapps/timebooker/actions/workflows/python-app.yml/badge.svg)](https://github.com/foureyesapps/timebooker/actions/workflows/python-app.yml)
# Time Booker

Heroku Deployment: https://timebooker-prod.herokuapp.com
### Install

1. Create a virtualenv
```
$ virtualenv -p python3.8 venv
```
2. Install all dependencies
```
pip install -r requirements.txt requirements-dev.txt
```
3. Activate the virutalenv
```
source venv/bin/activate
```
4. Run fast API server
```
uvicorn timebooker.main:app --reload --port 8043
```