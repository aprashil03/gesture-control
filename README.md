# gesture-control
Use hand gestures to manipulate your computer!


## Installation

- Although I would recommend using venv for running this project, some issues with evdev persist, and the fix for it can vary based on operating system. Since venv's are risk-free, I have still included the initialization commands. Yet, if you're uncertain of fixing the bug during pyenv's installation inside venv, feel free to use global python and pip to run your project. 
- You might have to use the alias pip3 / python3 instead of the regular pip / python.
```bash
# with global pip and python
git clone https://github.com/aprashil/gesture-control.git
cd gesture-control
pip install -r requirements.txt
python main.py
```

```bash
# with venv
git clone https://github.com/aprashil/gesture-control.git
cd gesture-control
python3 -m venv env
source ./env/bin/activate
python -m pip install -r requirements.txt
python main.py
```