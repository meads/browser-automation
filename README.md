# RPA Browser

Automated browser steps.
****
### Setup:
This repo uses python3.8 and venv for virtual environments.
1. Clone the repo and install python3.8 if you need it along with relevant system packages.
2. Change directory to the project and create your virtual environment.

```bash
# from in the project directory
$ python3.8 -m venv .
$ pip3 install -r requirements.txt
```
### Run Example:
```bash
# from in the project directory
source venv/bin/activate
(venv)$ python3 main.py
```
```
TODO:
- Setup better package structure.
- Testing existing inspect element tools.
- Record steps and leverage image recognition.
- Basic DSL to drive the browser steps.
```