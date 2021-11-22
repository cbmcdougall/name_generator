# Python Name Generator

A simple name generator made in python, where you can generate a dragon name or a penguin name!

## Installation

- Clone or download this repo and navigate to this folder
- Run `pipenv shell` to enter the virtual environment
- Run `pipenv install` within the virtual environment to install dependencies

## Usage

NB: Currently the only dependencies are for testing so just `python app.py` will also run the app without needing pipenv / the virtual environment

Within the virual environment:

- Start the program with `pipenv run app`
  - Case/capitalisation on user inputs doesn't matter
  - It will ask you to input a name
  - It will then ask for a birth month
    - This must be the full month name e.g. January
  - Then it will ask for what name to generate
    - Only options are "dragon" and "penguin"
  - It will then tell you the generated name before asking for your name again
  - type "exit" when asked for any input to exit the program
- Run the testing suite with `pipenv run test`
- Run test coverage with `pipenv run coverage`
- Exit the virtual environment with `exit`
