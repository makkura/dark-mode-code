# Maps and Markers with Folium

## Running
This can be run natively on your machine using the Running Locally details or via Docker container via the Running with Docker details.

### Running Locally
#### Python and Jupyter Labs requirements
**Note**: It is recommended to segregate your python and package installation for each project via pyenv, anaconda, or miniconda

python3 (3.10.11 or current) [Download](https://www.python.org/downloads/) \
pip - May be installed with Python but may need installed seperately [PIP check & install](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) \
jupyter lab [Jupyter Install](https://jupyter.org/install) \

#### Folium installation
From the directory this repo is in:
```
pip install -r requirements.txt
```

#### Running
From the directory this repo is in:
```
jupyter lab
```
This should open your browser to: [http://localhost:8888/lab](http://localhost:8888) \
Double click on map.ipynb to open it in the main window. \
Click the doube arrow >> icon to run each formula on the page. \ 

### Running with Docker
Docker and Docker Compose (or equivalent) must be installed.
[Docker Desktop](https://docs.docker.com/get-docker/)

#### Running
From the diretory this repo is in:
```
docker compose run -d
```
Visit [http://localhost:8888](http://localhost:8888) \
Double click on map.ipynb to open it in the main window. \
Click the double arrow >> icon to run each formula on the page. \

