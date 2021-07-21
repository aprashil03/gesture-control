# gesture-control
Use hand gestures to manipulate your computer!

## Features
- Advanced vector based finger tracking, this increases the gesture activation accuracy when the hand is far from the camera.
- Script support. (refer the usage section for more information)

## Installation

- Although I would recommend using venv for running this project, some issues with evdev persist, and the fix for it can vary based on operating system. Since venv's are risk-free, I have still included the initialization commands. Yet, if you're uncertain of fixing the bug during pyenv's installation inside venv, feel free to use global python and pip to run your project. 
- You might have to use the alias pip3 / python3 instead of the regular pip / python.
```bash
# with global pip and python
git clone https://github.com/aprashil/gesture-control.git
cd gesture-control
pip install -r requirements.txt
```

```bash
# with venv
git clone https://github.com/aprashil/gesture-control.git
cd gesture-control
python3 -m venv env
source ./env/bin/activate
python -m pip install -r requirements.txt
```
## Usage
- Once inside the project folder, just run:
```py
python main.py
```
- Note: if you get an error stating something along the lines of "can't open camera by index", then change "video_source_index" to "1".
```json
{
    "video_source_index":"0",
    "scripts":"True",
    "draw_points":"True",
    "min_det_conf":"0.5",
    "min_track_conf":"0.5"
}
```
- Press [Escape] to exit.
### Setting up scripts:
1) Set scripts to True in config.json.
2) Make your script's driver definition "run" (see scripts/example_script.py)
3) put your script.py file in the scripts directory.
4) assign your script to a gesture configuration by editing register.json
5) in register.json, the keys are a combination of finger/thumb indices as follows:
- 0 > thumb
- 1 > index finger
- 2 > middle finger
- 3 > ring finger
- 4 > pinky finger
```json
{
    "0":"example_script",
    "1":"",
    "2":"",
    "3":"",
    "4":"",
    "01":"",
    "12":"",
    "23":"",
    "34":"",
    "40":"",
    "012":"",
    "123":"",
    "234":""
}
```

## Contributing
Pull requests are welcome!