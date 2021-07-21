# gesture-control
Use hand gestures to manipulate your computer!

## Features
- Advanced vector based finger tracking, this increases the gesture activation accuracy when the hand is far from the camera.
- Script support. (refer the usage section for more information)

## Installation

- You might have to use the alias pip3 / python3 instead of the regular pip / python.
```bash
# with global pip and python
git clone https://github.com/aprashil/gesture-control.git
cd gesture-control
pip install -r requirements.txt
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
- Just bend a finger to activate it's gesture!
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
## Known Bugs
1) The application crashes after displaying "Segmentation fault (core dumped)" when using virtual environments, this is the primary reason that venv setup instructions have not been given in the installation section. The issue does not persist when using global opencv packages.

## Contributing
Pull requests are welcome!