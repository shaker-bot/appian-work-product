# Appian Work Product

## Dependencies
* Python 3.12

## Optional (Just some venv options if that's the desired workflow)
* Pipenv (Pipfile provided if desired)
* (uv)[https://docs.astral.sh/uv/] (uv.lock provided if desired)

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