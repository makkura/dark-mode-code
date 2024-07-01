# Maps and Markers with Folium

## Running the Notebook
This can be run natively on your machine using the Running Locally details or via Docker container via the Running with Docker details.

### Running Locally
#### Python and Jupyter Labs requirements
**Note**: It is recommended to segregate your python and package installation for each project via your preferred tool such as pyenv, anaconda, or miniconda

python3 (3.10.11 or current) [Download](https://www.python.org/downloads/) \
pip - May be installed with Python but may need installed seperately [PIP check & install](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) \
jupyter lab [Jupyter Install](https://jupyter.org/install) \

#### Requirements installation
The requirements file sets the Folium version. \
It can be installed via:
```
pip install -r requirements.txt
```

#### Running
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
This will run the container by:
* pull an official Jupyter Notebook image
* apply some configuration to it to open Notebook (instead of Lab) and set it to Dark Mode (my preference)
* bind the current directory to the working folder in the container so changes and output can persist

```
docker compose run -d
```

The container will be accessible when the container shows a Status of healthy. \
You can check this via checking the Status column when running:
```
docker ps
```

Visit [http://localhost:8888](http://localhost:8888) \
Double click on map.ipynb to open it in the main window. \
Click the double arrow >> icon to run each formula on the page. \

### Running the independent map.py script
#### Python requirements
**Note**: It is recommended to segregate your python and package installation for each project via your preferred tool such as pyenv, anaconda, or miniconda

python3 (3.10.11 or current) [Download](https://www.python.org/downloads/) \
pip - May be installed with Python but may need installed seperately [PIP check & install](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) \

#### Requirements installation
The requirements file sets the Folium version. \
It can be installed via:
```
pip install -r requirements.txt
```

#### Running
Replace the data.csv with your own file, if desired.
```
python map.py
```
A map.html will be generated in the output directory

### Running with Docker
Docker and Docker Compose (or equivalent) must be installed.
[Docker Desktop](https://docs.docker.com/get-docker/)

#### Running
Replace the data.csv with your own file, if desired.

This will run the container by:
* pull an official python image
* bind the current directory to the working folder in the container so the data.csv file and mapy.py file are accessible in the container and output can persist

```
docker compose -f docker-compose-map.yaml run
```
A map.html file will be generated in the output directory.

### A Note on Docker Usage
Normally a docker image will be built to encapsulate a single application and run it as a container.
The focus in the docker usage for this project is less about encapsulating the running application for running in the long term and more about allowing for an easy, clean environment that won't muddy up the rest of the system.

