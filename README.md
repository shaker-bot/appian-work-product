# Appian Work Product

## Dependencies
* Python 3.12

## Optional (Just some venv options if that's the desired workflow)
* Pipenv (Pipfile provided if desired)
* (uv)[https://docs.astral.sh/uv/] (uv.lock provided if desired)

## Two Ways to "Simulate"
### Automatic Card Dealing and Output
Lines 9-19 in `main.py` are by default uncommented. This will run the full simulation with the deck being fully dealt out after a single shuffle and then attempting to get another card which will output the fact that the deck has no more cards.

### Interactive Deck Usage
Lines 23-46 in `main.py` are commented out. Uncomment these lines and comment out 9-19 to have an interactive "experience" with the deck. This usage allows you to shuffle multiple times, reset the deck, check the remaining number of cards, and simply quit out of the program.

## How to Run
### Basic
```
python main.py
```

### Pipenv
```
# If you have pipenv installed you can skip this first step
pip install pipenv

# Create the venv
pipenv install --dev

# Run the program
pipenv run python main.py
```

### uv
```
# uv Installation (via either Homebrew or curl)
brew install uv
# or
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create the venv
uv venv --python 3.11

# Run the program
uv run main.py
```

## To Note
* There are multiple ways to handle the environment for running this code (i.e. Pipfile, uv, local). Eventually when new dependencies are needed, we can limit these options to one, to give a consistent development experience.
* For this project, I've really only committed to main for the initial code changes. However usually I would open an branch and then create a PR against the main branch, this was just for ease at the moment.