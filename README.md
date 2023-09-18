# Match API

## Interviewee details (to fill out)

#### Note

The details you provide here are purely to help us improve our process, and will have no bearing on your candidacy.

### Name

- 


### Estimated time to complete

- 

### Notes/Feedback

- 




## Requirements

- Python 3.11 **EXACTLY** (other versions will fail to compile match_lib)
- Docker (not required for running the project, but recommended to build/test your finished API)


## Development Setup

- Ensure you have the correct python version with `python --version` (if not, `pyenv` is a good tool for swapping python versions)
- Create a Python virtual environment (feel free to name it whatever you'd like): `python -m venv venv`
- Activate your virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate.bat` (Windows)
- Install dependencies: `pip install -r requirements.txt`


## Running in development

`python app.py`


## Running in production

- Build the docker image: `docker build -t matchapi:latest .`
- View your built images: `docker images`
- Run a built image: `docker run matchapi:latest` or `docker run -p <PORT>:<PORT> matchapi:latest` if exposing a server port


## Running load tests

[Locust](https://docs.locust.io/en/stable/index.html) is included in this template, and the included `locustfile.py` can by used to inspect the performance of your API. Feel free to modify it as needed to better suit your needs.

### Run Locust

- After setting up your virtual environment and installing dependencies, you can run this command to start locust: `locust`
- To view the Locust UI, go to `http://localhost:8089`
- From here you can select a number of users, how many are created per-second, and the URL of your server. A good starting point is `100 users` with a `spawn rate 10`. The `host` option is whatever the URL of your locally running server is
- Press `Start Swarming` to begin the test. You can then tap on the `Charts` tab at the top to view your requests/sec, user count, and error rates.


## Adding dependencies

- Install the dependency (Flask, for example): `pip install flask`
- Save it to your requirements: `pip freeze -l > requirements.txt` (`-l` prevents adding any globally-installed packages)